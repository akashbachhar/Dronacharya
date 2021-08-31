const url = window.location.href
console.log(url)
const quizBox = document.getElementById('quiz-box')
const scoreBox = document.getElementById('score-box')
const resultBox = document.getElementById('result-box')
const timeBox = document.getElementById('time-box')
const activateTimer = (time) => {
    if(time.toString().length < 2){
        timeBox.innerHTML = `<b>0${time}:00</b>`
    } else {
        timeBox.innerHTML = `<b>${time}:00</b>`
    }
    {
        let minutes = time - 1
        let seconds = 60
        let displaySeconds
        let displayMinutes

        const timer = setInterval(()=>{
            seconds--;
            if(seconds<0){
                seconds = 59;
                minutes--;
            }
            if(minutes.toString().length<2){
                displayMinutes = '0'+minutes
            } else {
                displayMinutes = minutes
            }
            if(seconds.toString().length<2){
                displaySeconds = '0'+seconds
            } else {
                displaySeconds = seconds
            }
            if(minutes===0 && seconds===0){
                timeBox.innerHTML = "<b>00:00</b>"
                setTimeout(()=>{
                    clearInterval(timer)
                    alert('Time Over')
                    sendData()
                },500)
            }
            timeBox.innerHTML = `<b>${displayMinutes}:${displaySeconds}</b>`
        },1000)
    }

}
$.ajax({
    type: 'GET',
    url:`${url}data`,
    success: function(res){
        // console.log(res)
        const data = res.data
        data.forEach(el => {
            for( const [question, answers] of Object.entries(el)){
                quizBox.innerHTML += `
                    <hr>
                    <div class="mb-2">
                        <b>Q: ${question}</b>
                    </div>
                `
                answers.forEach(answer=>{
                    quizBox.innerHTML += `
                        <div>
                            <input type="radio" class="ans" id="${question}-${answer}" name="${question}" value="${answer}">
                            <label for="${question}">${answer}</label> 
                        </div>
                    `
                })
            }
        })
        activateTimer(res.time)
    },
    error: function(err){
        console.log(err)
    }
})

const QuizForm = document.getElementById('quiz-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')
const sendData = () => {
    const elements = [...document.getElementsByClassName('ans')]
    const data= {}
    data['csrfmiddlewaretoken'] = csrf[0].value
    elements.forEach(el=>{
        if(el.checked){
            data[el.name] = el.value
        } else {
            if(!data[el.name]){
                data[el.name] = null
            }
        }
    })
    $.ajax({
        type: 'POST',
        url: `${url}save/`,
        data: data,
        success: function(res){
            const results = res.results
            console.log(results)

            QuizForm.style.visibility = "hidden"
            scoreBox.innerHTML = `${res.passed?'Congrats! ':'Oops!'} Your result is : ${res.score.toFixed(2)}%`
            results.forEach(res=>{
                const resDiv = document.createElement("div")
                for(const [question, resp] of Object.entries(res)){
                    /* console.log(question)
                    console.log(resp)
                    console.log('---------------') */
                    resDiv.innerHTML += question
                    const cls = ['container','p-3','text-light','h3']
                    resDiv.classList.add(...cls)
                    if(resp=='not answered'){
                        resDiv.innerHTML += '-not answered'
                        resDiv.classList.add('bg-danger')
                    } else {
                        const answer = resp['answered']
                        const correct = resp['correct_answer']
                        if(answer==correct){
                            resDiv.classList.add('bg-success')
                            resDiv.innerHTML += `answered: ${answer}`
                        } else {
                            resDiv.classList.add('bg-danger')
                            resDiv.innerHTML += ` correct answer: ${correct} | `
                            resDiv.innerHTML += ` answered: ${answer }`
                        }
                    }

                }
                //const body = document.getElementById('result-pg')
                resultBox.append(resDiv)
            })
        },
        error: function(err){
            console.log(err)
        }
    })

}
QuizForm.addEventListener('submit',e=>{
    e.preventDefault()
    sendData()
})