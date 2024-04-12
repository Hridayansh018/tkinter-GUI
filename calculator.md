CREATING A CALCULATOR USING PYTHON...!

Importing Libraries: The import statement imports the necessary modules from the Tkinter library to create GUI elements.

Function Definitions:

button_press(num): This function appends the pressed button's value to the equation text displayed on the calculator screen.
backspace(): This function removes the last character from the equation text.
clear(): This function clears the equation text, resetting it to an empty string.
equals(): This function evaluates the equation and displays the result on the calculator screen. If an error occurs during evaluation, it displays "ERROR".
Initializing GUI Window: The Tk() function creates a new window for the calculator application.

Creating Labels and Buttons:

Label: This creates a label widget to display the equation text.
Button: These create various buttons for digits, arithmetic operations, and special functions like clear and backspace. Each button is associated with a specific command to execute when clicked.
Layout Management:

pack(): This is used to organize and display the widgets within the window. The pack() method is called on the Label widget to display the equation text.
grid(): This is used to arrange buttons in a grid layout within the frame widget.
Main Loop:

mainloop(): This method enters the Tkinter event loop, where the program remains until the user closes the window. During this loop, Tkinter continuously listens for events such as button clicks and updates the GUI accordingly.
Overall, the program creates a simple calculator GUI with buttons for digits, arithmetic operations, and special functions. Users can input equations and evaluate them using the "=" button.
