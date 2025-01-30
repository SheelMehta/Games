function makeGuess() {
    let guess = document.getElementById("guessInput").value;

    fetch('/guess', {
        method: 'POST',
        body: JSON.stringify({ guess: guess }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log("Response:", data);  // Debugging: Check server response

        if (data.error) {
            document.getElementById("result").innerText = data.error;
        } else {
            document.getElementById("result").innerText = data.message;

            if (data.win) {
                document.getElementById("guessInput").value = "";
                document.getElementById("guessList").innerHTML = ""; // Clear previous list
            }

            // Ensure guesses are displayed
            updateGuessList(data.guesses);
        }
    })
    .catch(error => console.error("Error:", error));
}

function updateGuessList(guesses) {
    console.log("Updating guess list:", guesses);  // Debugging: Log guesses
    let guessList = document.getElementById("guessList");
    guessList.innerHTML = ""; // Clear current list

    if (guesses.length === 0) {
        let li = document.createElement("li");
        li.textContent = "No guesses yet.";
        guessList.appendChild(li);
        return;
    }

    guesses.forEach(guessObj => {
        let li = document.createElement("li");
        li.textContent = `Guess: ${guessObj.guess} - Feedback: ${guessObj.feedback}`;
        guessList.appendChild(li);
    });
}

// Toggle number colors between light and dark
function toggleNumber(element) {
    element.classList.toggle("active");
}