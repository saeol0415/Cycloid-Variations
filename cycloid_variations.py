import turtle
import tkinter as tk
import math

# Create turtles for the Epicycloid and Hypocycloid
epicycloid_turtle = turtle.Turtle()
hypocycloid_turtle = turtle.Turtle()

# Hide the turtles initially
epicycloid_turtle.hideturtle()
hypocycloid_turtle.hideturtle()

def draw_epicycloid():
    hypocycloid_turtle.hideturtle()  # Hide the Hypocycloid turtle
    turtle.clearscreen()  # Clear the main turtle screen

    # Retrieve the radius values from the entry fields
    R_epicycloid = float(entry_R_epicycloid.get())
    r_epicycloid = float(entry_r_epicycloid.get())
    d_epicycloid = float(entry_d_epicycloid.get())

    turtle.speed('fastest')  # Set the drawing speed to the fastest

    # Calculate the angle increment for one step
    theta_increment = 0.1

    # Move the turtle to the initial position
    turtle.penup()
    x = (R_epicycloid + r_epicycloid) * math.cos(0) - d_epicycloid * math.cos((R_epicycloid + r_epicycloid) * 0 / r_epicycloid)
    y = (R_epicycloid + r_epicycloid) * math.sin(0) - d_epicycloid * math.sin((R_epicycloid + r_epicycloid) * 0 / r_epicycloid)
    turtle.goto(x, y)
    turtle.pendown()

    # Draw the epicycloid
    t = 0
    max_iterations = 10000  # Set a maximum number of iterations to avoid infinite loops
    while t < max_iterations:
        theta = t * theta_increment
        x = (R_epicycloid + r_epicycloid) * math.cos(theta) - d_epicycloid * math.cos((R_epicycloid + r_epicycloid) * theta / r_epicycloid)
        y = (R_epicycloid + r_epicycloid) * math.sin(theta) - d_epicycloid * math.sin((R_epicycloid + r_epicycloid) * theta / r_epicycloid)
        turtle.goto(x, y)
        t += 1

    turtle.penup()
    
def draw_hypocycloid():
    epicycloid_turtle.hideturtle()  # Hide the Epicycloid turtle
    turtle.clearscreen()  # Clear the main turtle screen

    # Retrieve the radius values from the entry fields
    R_hypocycloid = float(entry_R_hypocycloid.get())
    r_hypocycloid = float(entry_r_hypocycloid.get())

    turtle.speed('fastest')  # Set the drawing speed to the fastest

    # Calculate the angle increment for one step
    theta_increment = 0.1

    # Move the turtle to the initial position
    turtle.penup()
    x = (R_hypocycloid - r_hypocycloid) * math.cos(0) + r_hypocycloid * math.cos((R_hypocycloid - r_hypocycloid) * 0 / r_hypocycloid)
    y = (R_hypocycloid - r_hypocycloid) * math.sin(0) - r_hypocycloid * math.sin((R_hypocycloid - r_hypocycloid) * 0 / r_hypocycloid)
    turtle.goto(x, y)
    turtle.pendown()

    # Draw the hypocycloid
    t = 0
    max_iterations = 10000  # Set a maximum number of iterations to avoid infinite loops
    while t < max_iterations:
        theta = t * theta_increment
        x = (R_hypocycloid - r_hypocycloid) * math.cos(theta) + r_hypocycloid * math.cos((R_hypocycloid - r_hypocycloid) * theta / r_hypocycloid)
        y = (R_hypocycloid - r_hypocycloid) * math.sin(theta) - r_hypocycloid * math.sin((R_hypocycloid - r_hypocycloid) * theta / r_hypocycloid)
        turtle.goto(x, y)
        t += 1

    turtle.penup()

def set_radius_epicycloid():
    # Retrieve the radius values from the entry fields
    R_epicycloid = float(entry_R_epicycloid.get())
    r_epicycloid = float(entry_r_epicycloid.get())
    d_epicycloid = float(entry_d_epicycloid.get())

    # Update the radius labels
    label_R_epicycloid.config(text=f"R: {R_epicycloid}")
    label_r_epicycloid.config(text=f"r: {r_epicycloid}")
    label_d_epicycloid.config(text=f"d: {d_epicycloid}")

def set_radius_hypocycloid():
    # Retrieve the radius values from the entry fields
    R_hypocycloid = float(entry_R_hypocycloid.get())
    r_hypocycloid = float(entry_r_hypocycloid.get())

    # Update the radius labels
    label_R_hypocycloid.config(text=f"R: {R_hypocycloid}")
    label_r_hypocycloid.config(text=f"r: {r_hypocycloid}")

def reset_radius_epicycloid():
    epicycloid_turtle.clear()  # Clear the Epicycloid turtle drawing
    hypocycloid_turtle.clear()  # Clear the Hypocycloid turtle drawing
    entry_R_epicycloid.delete(0, tk.END)
    entry_R_epicycloid.insert(0, "100")
    entry_r_epicycloid.delete(0, tk.END)
    entry_r_epicycloid.insert(0, "50")
    entry_d_epicycloid.delete(0, tk.END)
    entry_d_epicycloid.insert(0, "75")
    set_radius_epicycloid()

def reset_radius_hypocycloid():
    epicycloid_turtle.clear()  # Clear the Epicycloid turtle drawing
    hypocycloid_turtle.clear()  # Clear the Hypocycloid turtle drawing
    entry_R_hypocycloid.delete(0, tk.END)
    entry_R_hypocycloid.insert(0, "150")
    entry_r_hypocycloid.delete(0, tk.END)
    entry_r_hypocycloid.insert(0, "50")
    set_radius_hypocycloid()

# Create the main window
window = tk.Tk()
window.title("Epicycloid and Hypocycloid Drawer")

# Create the Epicycloid section
epicycloid_frame = tk.Frame(window)
epicycloid_frame.pack(side=tk.LEFT, padx=10)

label_R_epicycloid = tk.Label(epicycloid_frame, text="R:")
label_R_epicycloid.pack()
entry_R_epicycloid = tk.Entry(epicycloid_frame)
entry_R_epicycloid.insert(0, "100")
entry_R_epicycloid.pack()

label_r_epicycloid = tk.Label(epicycloid_frame, text="r:")
label_r_epicycloid.pack()
entry_r_epicycloid = tk.Entry(epicycloid_frame)
entry_r_epicycloid.insert(0, "50")
entry_r_epicycloid.pack()

label_d_epicycloid = tk.Label(epicycloid_frame, text="d:")
label_d_epicycloid.pack()
entry_d_epicycloid = tk.Entry(epicycloid_frame)
entry_d_epicycloid.insert(0, "75")
entry_d_epicycloid.pack()

button_set_epicycloid = tk.Button(epicycloid_frame, text="Set Radius", command=set_radius_epicycloid)
button_set_epicycloid.pack()

button_draw_epicycloid = tk.Button(epicycloid_frame, text="Draw Epicycloid", command=draw_epicycloid)
button_draw_epicycloid.pack()

button_reset_epicycloid = tk.Button(epicycloid_frame, text="Reset Radius", command=reset_radius_epicycloid)
button_reset_epicycloid.pack()

# Create the Hypocycloid section
hypocycloid_frame = tk.Frame(window)
hypocycloid_frame.pack(side=tk.RIGHT, padx=10)

label_R_hypocycloid = tk.Label(hypocycloid_frame, text="R:")
label_R_hypocycloid.pack()
entry_R_hypocycloid = tk.Entry(hypocycloid_frame)
entry_R_hypocycloid.insert(0, "150")
entry_R_hypocycloid.pack()

label_r_hypocycloid = tk.Label(hypocycloid_frame, text="r:")
label_r_hypocycloid.pack()
entry_r_hypocycloid = tk.Entry(hypocycloid_frame)
entry_r_hypocycloid.insert(0, "50")
entry_r_hypocycloid.pack()

button_set_hypocycloid = tk.Button(hypocycloid_frame, text="Set Radius", command=set_radius_hypocycloid)
button_set_hypocycloid.pack()

button_draw_hypocycloid = tk.Button(hypocycloid_frame, text="Draw Hypocycloid", command=draw_hypocycloid)
button_draw_hypocycloid.pack()

button_reset_hypocycloid = tk.Button(hypocycloid_frame, text="Reset Radius", command=reset_radius_hypocycloid)
button_reset_hypocycloid.pack()

# Initialize the turtle graphics
turtle.setup(800, 600)
turtle.hideturtle()
turtle.penup()

# Start the Tkinter event loop
window.mainloop()
