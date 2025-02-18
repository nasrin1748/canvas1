from pyscript import when,document
from pyscript import display
from js import document
def fun():
    from js import document
    from pyscript import display,HTML,when
    # Get the canvas and context
    canvas = document.getElementById("myCanvas")
    context = canvas.getContext("2d")
    context.clearRect(0, 0, canvas.width, canvas.height)
    context.stroke()

    context.font = "30px Arial"
    context.fillStyle = "WHITE"
    display(HTML("""
        <input type="text" id="input1" placeholder="Enter first input">
        <input type="text" id="input2" placeholder="Enter second input">
        <button id="inpButton">Submit</button>"""))
    @when("click", "#inpButton")
    def on_canvas_click():
            context.clearRect(0, 0, canvas.width, canvas.height)
            context.stroke()
            input1 = document.getElementById('input1').value
            input2 = document.getElementById('input2').value
            #context.clearRect(0, 0, canvas.width, canvas.height)
            context.font = "15px Arial"
            context.fillStyle = "WHITE"
            context.fillText("first number  "+input1, 400, 380)
            #context.clearRect(0, 0, canvas.width, canvas.height)
            context.fillText("Second number  "+input2, 400, 400)
            #context.clearRect(0, 0, canvas.width, canvas.height)
            context.fillText("Answer  " +str(int(input1)+int(input2)),400,430)
    canvas.addEventListener("click", on_canvas_click)
