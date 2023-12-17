from manim import *

class IsolateVariables(Scene):
    def construct(self):
        # Original equation
        equation = MathTex("3s", "=", "15", "+", "2s")

        # Move the equation to the top of the screen
        equation.move_to(2 * UP)

        # Show the original equation
        self.play(Write(equation))

        # Subtract 2s from both sides
        minus_2s = MathTex("3s", "-", "2s", "=", "15", "+", "2s", "-", "2s")
        minus_2s.next_to(equation, DOWN, buff=0.5)

        self.play(Transform(equation.copy(), minus_2s))

        # Simplify both sides
        simplified_equation = MathTex("s", "=", "15")
        simplified_equation.next_to(minus_2s, DOWN, buff=0.5)

        self.play(Transform(minus_2s.copy(), simplified_equation))

        # Highlight the solution
        solution = simplified_equation[2].copy().set_color(GREEN)
        self.play(Transform(simplified_equation[2].copy(), solution))

        # Wait for a moment
        self.wait(2)