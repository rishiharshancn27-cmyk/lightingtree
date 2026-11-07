"""Draw a simple branching tree with Python's built-in turtle graphics."""

import turtle


def draw_tree(t: turtle.Turtle, length: float) -> None:
    """Recursively draw two branches from each segment."""
    if length < 10:
        return

    t.forward(length)
    t.color("orange")
    t.circle(2)
    t.color("brown")

    t.left(30)
    draw_tree(t, length * 3 / 4)
    t.right(60)
    draw_tree(t, length * 3 / 4)
    t.left(30)
    t.backward(length)


def main() -> None:
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Recursive Turtle Tree")

    pen = turtle.Turtle()
    pen.pensize(2)
    pen.color("green")
    pen.left(90)
    pen.backward(100)
    pen.speed(0)
    pen.shape("turtle")

    draw_tree(pen, 100)
    screen.mainloop()


if __name__ == "__main__":
    main()
