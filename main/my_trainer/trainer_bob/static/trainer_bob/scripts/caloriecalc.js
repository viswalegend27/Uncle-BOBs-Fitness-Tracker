console.log(`Hello the script is running`)
const tabs = document.querySelectorAll('.tab-btn');
const metricHeight = document.getElementById('metric-height-group')
const imperialHeight = document.getElementById('imperial-height-group')
const unitInput = document.getElementById('unit_system_input'); // the hidden input
const weight = document.getElementById('weight-input')
const rSec = document.getElementById("r-sec");
const form = document.querySelector(".form");
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
const resultDiv = document.querySelector('.result');
const rightContainer = document.querySelector('.right-container');

// function to make the calculation dynamic. Not static
form.addEventListener("submit", async function(e) {
    // prevent the code from reverting back to its original functionality.
    e.preventDefault();
    console.log("Form submission prevented");

    try {
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        
        // referencing for our document.
        const formData = new FormData(form);
        // fetching our backend data.
        const response = await fetch(form.action, {
            method: "POST",
            body: formData,
            headers: {
                "X-Requested-With": "XMLHttpRequest",
                "X-CSRFToken": csrftoken
            }
        });

        if (!response.ok) throw new Error('Network response was not ok');

        const data = await response.json();
        // to check the data that is been posted.
        // console.log("Data received:", data);
        
        // Check for goals, and check the length of the BMR array.
        if (data.m_goals && data.m_goals.length > 0) {
            rSec.style.display = "flex";
            resultDiv.innerHTML = 
            `
                <h3>Maintenance Calories: ${data.m_goals[0]}</h3>
                <h3>Minimum Weight Loss: ${data.m_goals[1]}</h3>
                <h3>Moderate Weight Loss: ${data.m_goals[2]}</h3>
            `;
        } // check if only bmr asked. 
        else if (data.bmr && (Array.isArray(data.bmr) ? data.bmr.length > 0 : data.bmr)) {
            rSec.style.display = "flex";
            document.querySelector('.result').innerHTML = `<h3>Basal Metabolic Rate (BMR): ${data.bmr}</h3>`;
        } else {
            console.log("No data returned for BMR or Goals");
        }

        rightContainer.classList.remove('empty-state');
    } catch (error) {
        console.error("There was an error:", error);
    }
});

tabs.forEach(tab => {
  tab.addEventListener('click', function () {
    // remove active from all
    tabs.forEach(t => t.classList.remove('active'));
    // add active to clicked tab
    this.classList.add('active');
    const selectedUnit = this.dataset.unit;

    if (selectedUnit === "imperial"){
      imperialHeight.style.display = 'block';
      metricHeight.style.display = 'none';
      weight.placeholder = 'LBs'
      unitInput.value = 'imperial';
    } else {
      metricHeight.style.display = 'block';
      imperialHeight.style.display = 'none';
      weight.placeholder = 'Kg'
      unitInput.value = 'metric';
    }

  console.log(`Current unit: ${unitInput.value}`);
  });
});
