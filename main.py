# import module
import streamlit as st

# Title
st.title("Hello Title comes here!!!")
# Header
st.header("This is a header") 

# Subheader
st.subheader("This is a subheader")
# Text
st.text("Hello This is text!!!")
# Markdown
st.markdown("### This is a markdown")
# success
st.success("Success")

# success
st.info("Information")

# success
st.warning("Warning")

# success
st.error("Error")

# Exception - This has been added later
exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)
# Write text
st.write("Text with write")

# Writing python inbuilt function range()
st.write(range(10))
# Display Images

# import Image from pillow to open images
from PIL import Image
img = Image.open("E:/Nilima/data science/images/meenakshi_temple.jpg")

# display image using streamlit
# width is used to set the width of an image
st.image(img, width=200)
# checkbox
# check if the checkbox is checked
# title of the checkbox is 'Show/Hide'
if st.checkbox("Show/Hide"):

    # display the text if the checkbox returns True value
    st.text("Showing the widget")
########################## more checkboxes
lang_cbox1 = st.checkbox("English")
lang_cbox2 = st.checkbox("Hindi")
lang_cbox3 = st.checkbox("Marathi")
if(lang_cbox1):
    st.success("English")
if(lang_cbox2):
    st.success("Hindi")
if(lang_cbox3):
    st.success("Marathi")


########################## Radio button
# radio button
# first argument is the title of the radio button
# second argument is the options for the radio button
status = st.radio("Select Gender: ", ('Male', 'Female'))

# conditional statement to print 
# Male if male is selected else print female
# show the result using the success function
if (status == 'Male'):
    st.success("Male")
else:
    st.success("Female")

###################### more than 2 options
Highest_degree = st.radio("Select Degree: ", ('Bachelor', 'Masters','Phd'))

# conditional statement to print 
# Male if male is selected else print female
# show the result using the success function
if (Highest_degree == 'Bachelor'):
    st.success("Bachelor")
elif Highest_degree=='Masters':
    st.success("Masters")
else:
    st.success("Phd")


############################################# Selection Box
# Selection box

# first argument takes the titleof the selectionbox
# second argument takes options
hobby = st.selectbox("Hobbies: ",
                     ['Dancing', 'Reading', 'Sports'])

# print the selected hobby
st.write("Your hobby is: ", hobby)
############################################## Multi Select Box
# multi select box

# first argument takes the box title
# second argument takes the options to show
hobbies = st.multiselect("Degree: ",
                         ['B.Tech', 'M.Tech', 'Phd'])

# write the selected options
st.write("You selected", len(hobbies), 'hobbies')

############################################## Button
# Create a simple button that does nothing
st.button("Click me")

# Create a button, that when clicked, shows a text
if(st.button("About")):
    st.text("Welcome To Streamlit!!!")

############################################### Text Input
# Text Input

# save the input text in the variable 'name'
# first argument shows the title of the text input box
# second argument displays a default text inside the text input area
name = st.text_input("Enter Your name", "Type Here ...")

# display the name when the submit button is clicked
# .title() is used to get the input text string
if(st.button('Submit')):
    result = name.title()
    st.success(result)
############################################# # slider

# first argument takes the title of the slider
# second argument takes the starting of the slider
# last argument takes the end number
level = st.slider("Select the level", 1, 5)

# print the level
# format() is used to print value 
# of a variable at a specific position
st.text('Selected: {}'.format(level))
##############################################