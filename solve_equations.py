from manim import *

class Equation(Scene):
    def construct(self):
        # Display the original equation
        equation = MathTex("4 + x = 10")
        equation.shift(UP)
        self.play(Write(equation))
        self.wait(1)

        # Subtract 4 from both sides
        minus_four = MathTex("-4", color=RED).next_to(equation, DOWN)
        equation_minus_four = MathTex("4 + x - 4 = 10 - 4")
        equation_minus_four.next_to(minus_four, DOWN)

        self.play(Transform(equation.copy(), equation_minus_four), Write(minus_four))
        self.wait(1)

        # Simplify and display the result
        result_equation = MathTex("x = 6", color=GREEN).next_to(equation_minus_four, DOWN)
        self.play(Transform(equation_minus_four.copy(), result_equation))
        self.wait(1)

class Addition(Scene):
    def construct(self):
        # Display the original equation
        equation = MathTex("x - 8 = 14")
        equation.shift(UP)
        self.play(Write(equation))
        self.wait(1)

        # Add 8 to both sides
        plus_eight = MathTex("+8", color=RED).next_to(equation, DOWN)
        equation_plus_eight = MathTex("x - 8 + 8 = 14 + 8")
        equation_plus_eight.next_to(plus_eight, DOWN)

        self.play(Transform(equation.copy(), equation_plus_eight), Write(plus_eight))
        self.wait(1)

        # Simplify and display the result
        result_equation = MathTex("x = 22", color=GREEN).next_to(equation_plus_eight, DOWN)
        self.play(Transform(equation_plus_eight.copy(), result_equation))
        self.wait(1)

class Mulitplication(Scene):
    def construct(self):
        # Display the original equation
        equation = MathTex("\\frac{x}{3} = 6")
        equation.shift(UP)
        self.play(Write(equation))
        self.wait(1)

        # Multiply both sides by 3
        times_three = MathTex("\\times 3", color=RED).next_to(equation, DOWN)
        equation_times_three = MathTex("\\frac{x}{3} \\times 3 = 6 \\times 3")
        equation_times_three.next_to(times_three, DOWN)

        self.play(Transform(equation.copy(), equation_times_three), Write(times_three))
        self.wait(1)

        # Simplify and display the result
        result_equation = MathTex("x = 18", color=GREEN).next_to(equation_times_three, DOWN)
        self.play(Transform(equation_times_three.copy(), result_equation))
        self.wait(1)

class Division(Scene):
    def construct(self):
        # Display the original equation
        equation = MathTex("4x = 20")
        equation.shift(UP)
        self.play(Write(equation))
        self.wait(1)

        # Divide both sides by 4
        divide_by_four = MathTex("\\div 4", color=RED).next_to(equation, DOWN)
        equation_divide_by_four = MathTex("\\frac{4x}{4} = \\frac{20}{4}")
        equation_divide_by_four.next_to(divide_by_four, DOWN)

        self.play(Transform(equation.copy(), equation_divide_by_four), Write(divide_by_four))
        self.wait(1)

        # Simplify and display the result
        result_equation = MathTex("x = 5", color=GREEN).next_to(equation_divide_by_four, DOWN)
        self.play(Transform(equation_divide_by_four.copy(), result_equation))
        self.wait(1)

class SquareRoot(Scene):
    def construct(self):
        # Display the original equation
        equation = MathTex("x^2 = 9")
        equation.shift(UP)
        self.play(Write(equation))
        self.wait(1)

        # Take the square root of both sides
        sqrt_both_sides = MathTex("\\sqrt{x^2} = \\sqrt{9}", color=RED).next_to(equation, DOWN)
        equation_sqrt = MathTex("x = 3", color=GREEN).next_to(sqrt_both_sides, DOWN)

        self.play(Transform(equation.copy(), sqrt_both_sides), Write(equation_sqrt))
        self.wait(1)

class Power(Scene):
    def construct(self):
        # Display the original equation
        equation = MathTex("\\sqrt{x} = 4")
        equation.shift(UP)
        self.wait(1)

        # Raise both sides to the power of 2
        power_of_2_both_sides = MathTex("({\\sqrt{x}})^2 = 4^2", color=RED).next_to(equation, DOWN)
        equation_power_of_2 = MathTex("x = 16", color=GREEN).next_to(power_of_2_both_sides, DOWN)

        self.play(Transform(equation.copy(), power_of_2_both_sides), Write(equation_power_of_2))
        self.wait(1)