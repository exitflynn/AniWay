var display = document.querySelector('#time');
    var breakDis = document.querySelector('#breakDis');
    var mes = document.querySelector('#mes');
    var gif = document.querySelector('#gif');
    var minutes;
    var seconds;
    var t;
    //Sets the initial display
    var startTime = 25;
    var breakTime = 5;
    var timer_is_on = 0;
    var chillout = 0;
    var timer = 60 * startTime;
    timeConverter();
    display.textContent = minutes + ":" + seconds;
    //Sets the break display
    timer = 60 * breakTime;
    timeConverter();
    breakDis.textContent = minutes + ":" + seconds;
    //Sets the main display back to work time
    timer = 60 * startTime;
    
    //Buttons
    var btn1 = document.querySelector('#btn1');
    var btn2 = document.querySelector('#btn2');
    var btn3 = document.querySelector('#btn3');
    var btn4 = document.querySelector('#btn4');
    var btn5 = document.querySelector('#btn5');
    var btn6 = document.querySelector('#btn6');
    var btn7 = document.querySelector('#btn7');
    
    
    btn1.addEventListener('click', () => {
      startCount();
    });
    
    btn2.addEventListener('click', () => {
      stopCount();
       mes.textContent = "Pause";
    });
    
    btn3.addEventListener('click', () => {
      reset();
      gif.style.backgroundImage = 'none';
      gif.style.border = 'none';
      mes.style.marginTop = "100px";
      mes.style.fontSize = "80px";
    });
    
    btn4.addEventListener('click', () => {
      timeUp();
    });
    
    btn5.addEventListener('click', () => {
      timeDown();
    });
    
    btn6.addEventListener('click', () => {
      breakTimeUp();
    });
    
    btn7.addEventListener('click', () => {
      breakTimeDown();
    });
    
    function timedCount() {
      timeConverter();
      display.textContent = minutes + ":" + seconds;
      timer--;
      if (timer === 0 && !chillout) {
        mes.textContent = "Break";
        chillout = 1;
        timer = 60 * breakTime;
        mes.style.marginTop = "20px";
        mes.style.fontSize = "50px";
        gif.style.backgroundImage = "url('https://media.giphy.com/media/11s7Ke7jcNxCHS/giphy.gif')";
      } else if (timer === 0 && chillout) {
        mes.textContent = "Work!";
        chillout = 0;
        timer = 60 * startTime;
        mes.style.marginTop = "20px";
        mes.style.fontSize = "50px";
        gif.style.backgroundImage = "url('https://media.giphy.com/media/E6jscXfv3AkWQ/giphy.gif')";
      }
      t = setTimeout(timedCount, 1000);
    }
    
    
    function startCount() {
      //Make shure doesn't count down from zero and doesn't stack the time function
      if (startTime && !timer_is_on) {
        if (!timer_is_on) {
          timer_is_on = 1;
        }
        if (!chillout) {
          mes.textContent = "Work!";
          mes.style.marginTop = "20px";
          mes.style.fontSize = "50px";
          gif.style.backgroundImage = "url('https://media.giphy.com/media/E6jscXfv3AkWQ/giphy.gif')";
          gif.style.border = "2px solid green";
        }
        timedCount();
      }
    }
    
    //Pause
    function stopCount() {
      clearTimeout(t);
      timer_is_on = 0;
      mes.style.marginTop = "20px";
      mes.style.fontSize = "50px";
      gif.style.backgroundImage = "url('https://media.giphy.com/media/3ornjXizVZDbngmjRK/giphy.gif')";
    }
    
    
    function reset() {
      timer_is_on = 0;
      startTime = 25;
      breakTime = 5;
      chillout = 0;
      timer = 60 * startTime;
      timeConverter();
      display.textContent = minutes + ":" + seconds;
      breakDis.textContent = "05:00";
      mes.textContent = "Ready?";
      
      stopCount();
       
    }
    
    function timeUp() {
      startTime++;
      timer_is_on = 0;
      timer = 60 * startTime;
      timeConverter();
      display.textContent = minutes + ":" + seconds;
    }
    
    function timeDown() {
      //Make sure doesn't go bellow zero
      if (startTime >= 1) {
        startTime--;
        timer_is_on = 0;
        timer = 60 * startTime;
        timeConverter();
        display.textContent = minutes + ":" + seconds;
      }
    }
    
    function breakTimeUp() {
      breakTime++;
      timer_is_on = 0;
      timer = 60 * breakTime;
      timeConverter();
      breakDis.textContent = minutes + ":" + seconds;
      //Puts the main display back on
      timer = 60 * startTime;
    }
    
    function breakTimeDown() {
      if (breakTime >= 1) {
        breakTime--;
        timer_is_on = 0;
        timer = 60 * breakTime;
        timeConverter();
        breakDis.textContent = minutes + ":" + seconds;
        timer = 60 * startTime;
      }
    }
    
    function timeConverter() {
      minutes = parseInt(timer / 60, 10);
      seconds = parseInt(timer % 60, 10);
      minutes = minutes < 10 ? "0" + minutes : minutes;
      seconds = seconds < 10 ? "0" + seconds : seconds;
    }