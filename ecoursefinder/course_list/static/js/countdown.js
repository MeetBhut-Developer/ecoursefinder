// countdown.js

// Function to calculate the time difference between two dates
function getTimeDifference(targetDate) {
    const now = new Date().getTime();
    const distance = targetDate - now;
  
    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);
  
    return {
      days,
      hours,
      minutes,
      seconds,
    };
  }
  
  // Function to update the countdown display
  function updateCountdownDisplay(targetDate, countdownElementId) {
    const countdownElement = document.getElementById(countdownElementId);
    const timeDifference = getTimeDifference(targetDate);
  
    if (timeDifference.distance < 0) {
      clearInterval(intervalId);
      countdownElement.innerHTML = "EXPIRED";
      return;
    }
  
    countdownElement.innerHTML = `${timeDifference.days}d ${timeDifference.hours}h ${timeDifference.minutes}m ${timeDifference.seconds}s`;
  }
  
  // Set the target date and element ID
  const targetDate = new Date("2023-12-31T00:00:00").getTime();
  const countdownElementId = "countdown";
  
  // Initial update
  updateCountdownDisplay(targetDate, countdownElementId);
  
  // Update the countdown every second
  const intervalId = setInterval(() => {
    updateCountdownDisplay(targetDate, countdownElementId);
  }, 1000);
  