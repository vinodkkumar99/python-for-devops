import re
text = "My name is Vinod Kumar and age is 25 years"

pattern = r"Vinod Kumar"
replace = "Vinod Kumar K"

new_text = re.sub(pattern, replace, text)
print("mofified text:",new_text)