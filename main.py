# Import PyScript modules
from pyodide.ffi import create_proxy  # Needed to connect JS events to Python functions
from js import document  # Allows access to HTML document elements

# ------------------------------
# TEAM DATA: Mapping grade-section combinations to Intramurals teams
# ------------------------------
# The key is "Grade-SECTION" in uppercase to match the dropdown input.
# The value is the team assigned to that combination.
team_data = {
    "7-RUBY": "Yellow Tigers",
    "8-EMERALD": "Yellow Tigers",
    "9-SAPPHIRE": "Yellow Tigers",
    "10-SAPPHIRE": "Yellow Tigers",
    "11-LUNA": "Yellow Tigers",

    "7-SAPPHIRE": "Green Hornets",
    "8-RUBY": "Green Hornets",
    "9-TOPAZ": "Green Hornets",
    "10-EMERALD": "Green Hornets",
    "12-TINIO": "Green Hornets",

    "7-EMERALD": "Blue Bears",
    "8-TOPAZ": "Blue Bears",
    "8-JADE": "Blue Bears",
    "9-RUBY": "Blue Bears",
    "10-TOPAZ": "Blue Bears",
    "12-JOSE": "Blue Bears",

    "7-TOPAZ": "Green Hornets",
    "8-SAPPHIRE": "Green Hornets",
    "9-JADE": "Green Hornets",
    "9-EMERALD": "Green Hornets",
    "10-RUBY": "Green Hornets",
    "11-AMORSOLO": "Green Hornets",
}

# ------------------------------
# TEAM BANNERS: Mapping team names to their banner images
# ------------------------------
# The key is the team name, the value is the URL of the banner image
team_banners = {
    "Yellow Tigers": "https://drive.google.com/uc?export=view&id=1sHsy79_nyRlRYZR59XtAc7qSvqNEiGSc",
    "Green Hornets": "https://drive.google.com/uc?export=view&id=1UBitykTV7XRrzLxMdfrYmDLl3ynaSfZ9",
    "Red Bulldogs": "https://drive.google.com/uc?export=view&id=18mOuUZ47YX_xy0cdApui-UKEH3DNTA8q",
    "Blue Bears": "https://drive.google.com/uc?export=view&id=1hvp8JLy20GwqFSWolqFZKnX0LK82PPEc",
}

# ------------------------------
# FUNCTION: check_eligibility
# This function is called when the user clicks the "Check Eligibility" button
# ------------------------------
def check_eligibility(event):
    """
    Determines if a student is eligible for Intramurals based on registration,
    medical clearance, grade, and section. Uses nested if/elif/else statements.
    """

    # Grab the div where results will be displayed
    result_div = document.getElementById("result")
    result_div.innerHTML = ""  # Clear previous messages to avoid stacking results

    # ------------------------------
    # Check registration
    # ------------------------------
    reg = document.querySelector('input[name="registration"]:checked')  # Grab selected radio
    if not reg:  # If nothing selected
        result_div.innerHTML = "<p style='color:#d4a373;'>Please select registration.</p>"
    else:
        if reg.value != "Yes":  # If registration is "No"
            result_div.innerHTML = "<p style='color:#d4a373;'>You need to register online.</p>"
        else:
            # ------------------------------
            # Check medical clearance
            # ------------------------------
            med = document.querySelector('input[name="medical"]:checked')
            if not med:  # If nothing selected
                result_div.innerHTML = "<p style='color:#d4a373;'>Please select medical clearance.</p>"
            else:
                if med.value != "Yes":  # If medical clearance is "No"
                    result_div.innerHTML = "<p style='color:#d4a373;'>You need to secure a medical clearance.</p>"
                else:
                    # ------------------------------
                    # Check grade and section
                    # ------------------------------
                    grade = document.getElementById("grade").value.strip()  # Remove spaces
                    section = document.getElementById("section").value.strip()

                    if grade == "" or section == "":  # If user left either empty
                        result_div.innerHTML = "<p style='color:#d4a373;'>Please select grade and section.</p>"
                    else:
                        key = f"{grade}-{section}".upper()  # Format key to match dictionary

                        # ------------------------------
                        # Nested conditional: eligible or not
                        # ------------------------------
                        if key in team_data:  # If combination exists
                            team = team_data[key]  # Get team name
                            banner_url = team_banners.get(team, "")  # Get banner URL

                            # Display eligibility message with team and banner
                            result_div.innerHTML = f"""
                                <h2 style='color:#f5f0e1;'>Congratulations! You are eligible!</h2>
                                <h2 class='mt-3'>{team}</h2>
                                <img src='{banner_url}' class='team-banner' alt='{team} Banner'>
                            """
                        else:  # Not eligible
                            result_div.innerHTML = "<p style='color:#d4a373;'>Sorry, you’re not eligible.</p>"

# ------------------------------
# BUTTON EVENT BINDING
# ------------------------------
btn = document.getElementById("checkBtn")  # Grab button element
btn_proxy = create_proxy(check_eligibility)  # Create JS proxy for Python function
btn.addEventListener("click", btn_proxy)  # Bind click event to function
