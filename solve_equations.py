from solve_equations import *

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

class Equation_1(Scene):
    def construct(self):
        # Display the original equation
        equation = MathTex("2x + 5 = 11")
        equation.to_edge(UP, buff=1.5)
        self.play(Write(equation))
        self.wait(1)

        # Subtract 5 from both sides
        minus_five = MathTex("-5", color=RED).next_to(equation, DOWN)
        equation_minus_five = MathTex("2x + 5 - 5 = 11 - 5")
        equation_minus_five.next_to(minus_five, DOWN)

        self.play(Transform(equation.copy(), equation_minus_five), Write(minus_five))
        self.wait(1)

        # Simplify and display the result
        result_equation = MathTex("2x = 6").next_to(equation_minus_five, DOWN)
        self.play(Transform(equation_minus_five.copy(), result_equation))
        self.wait(1)

        # Divide both sides by 2
        divide_by_two = MathTex("\\div 2", color=RED).next_to(result_equation, DOWN)
        equation_divide_by_two = MathTex("\\frac{2x}{2} = \\frac{6}{2}")
        equation_divide_by_two.next_to(divide_by_two, DOWN)

        self.play(Transform(result_equation.copy(), equation_divide_by_two), Write(divide_by_two))
        self.wait(1)

        # Simplify and display the final result
        final_result = MathTex("x = 3", color=GREEN).next_to(equation_divide_by_two, DOWN)
        self.play(Transform(equation_divide_by_two.copy(), final_result))
        self.wait(1)

class Equation_2(Scene):
    def construct(self):
        # Display the original equation
        equation = MathTex("\\sqrt{x} + 3 = 7")
        equation.to_edge(UP, buff=1.5)
        self.play(Write(equation))
        self.wait(1)

        # Subtract 3 from both sides
        minus_three = MathTex("-3", color=RED).next_to(equation, DOWN)
        equation_minus_three = MathTex("\\sqrt{x} + 3 - 3 = 7 - 3")
        equation_minus_three.next_to(minus_three, DOWN)

        self.play(Transform(equation.copy(), equation_minus_three), Write(minus_three))
        self.wait(1)

        # Simplify and display the result
        result_equation = MathTex("\\sqrt{x} = 4").next_to(equation_minus_three, DOWN)
        self.play(Transform(equation_minus_three.copy(), result_equation))
        self.wait(1)

        # Square both sides
        square_both_sides = MathTex("({\\sqrt{x}})^2 = 4^2", color=RED).next_to(result_equation, DOWN)
        equation_square = MathTex("x = 16", color=GREEN).next_to(square_both_sides, DOWN)

        self.play(Transform(result_equation.copy(), square_both_sides), Write(equation_square))
        self.wait(1)

class Equation_3(Scene):
    def construct(self):
        # Display the original equation
        equation = MathTex("x^2 - 13 = 12")
        equation.to_edge(UP, buff=1.5)
        self.play(Write(equation))
        self.wait(1)

        # Add 13 to both sides
        plus_thirteen = MathTex("+13", color=RED).next_to(equation, DOWN)
        equation_plus_thirteen = MathTex("x^2 - 13 + 13 = 12 + 13")
        equation_plus_thirteen.next_to(plus_thirteen, DOWN)

        self.play(Transform(equation.copy(), equation_plus_thirteen), Write(plus_thirteen))
        self.wait(1)

        # Simplify and display the result
        result_equation = MathTex("x^2 = 25").next_to(equation_plus_thirteen, DOWN)
        self.play(Transform(equation_plus_thirteen.copy(), result_equation))
        self.wait(1)

        # Square root both sides
        sqrt_both_sides = MathTex("\\sqrt{x^2} = \\sqrt{25}", color=RED).next_to(result_equation, DOWN)
        equation_sqrt = MathTex("x = 5", color=GREEN).next_to(sqrt_both_sides, DOWN)

        self.play(Transform(result_equation.copy(), sqrt_both_sides), Write(equation_sqrt))
        self.wait(1)

class Equation_4(Scene):
    def construct(self):
        # Display the original equation
        equation = MathTex("\\frac{x + 3}{4} = 2")
        equation.to_edge(UP, buff=0.5)
        self.play(Write(equation))
        self.wait(1)

        # Multiply both sides by 4
        times_four = MathTex("\\cdot 4", color=RED).next_to(equation, DOWN)
        equation_times_four = MathTex("\\frac{x + 3}{4} \\cdot 4 = 2 \\cdot 4")
        equation_times_four.next_to(times_four, DOWN)

        self.play(Transform(equation.copy(), equation_times_four), Write(times_four))
        self.wait(1)

        # Simplify and display the result
        result_equation = MathTex("x + 3 = 8").next_to(equation_times_four, DOWN)
        self.play(Transform(equation_times_four.copy(), result_equation))
        self.wait(1)

        # Subtract 3 from both sides
        minus_three = MathTex("-3", color=RED).next_to(result_equation, DOWN)
        equation_minus_three = MathTex("x + 3 - 3 = 8 - 3")
        equation_minus_three.next_to(minus_three, DOWN)

        self.play(Transform(result_equation.copy(), equation_minus_three), Write(minus_three))
        self.wait(1)

        # Simplify and display the final result
        final_result = MathTex("x = 5", color=GREEN).next_to(equation_minus_three, DOWN)
        self.play(Transform(equation_minus_three.copy(), final_result))
        self.wait(1)

class Equation_5(Scene):
    def construct(self):
        # Display the original equation
        equation = MathTex("5(x-1) = 10")
        equation.to_edge(UP, buff=1)
        self.play(Write(equation))
        self.wait(1)

        # Divide both sides by 5
        divide_by_five = MathTex("\\div 5", color=RED).next_to(equation, DOWN)
        equation_divide_by_five = MathTex("\\frac{5(x-1)}{5} = \\frac{10}{5}")
        equation_divide_by_five.next_to(divide_by_five, DOWN)

        self.play(Transform(equation.copy(), equation_divide_by_five), Write(divide_by_five))
        self.wait(1)

        # Simplify and display the result
        result_equation = MathTex("x - 1 = 2").next_to(equation_divide_by_five, DOWN)
        self.play(Transform(equation_divide_by_five.copy(), result_equation))
        self.wait(1)

        # Add 1 to both sides
        plus_one = MathTex("+1", color=RED).next_to(result_equation, DOWN)
        equation_plus_one = MathTex("x - 1 + 1 = 2 + 1")
        equation_plus_one.next_to(plus_one, DOWN)

        self.play(Transform(result_equation.copy(), equation_plus_one), Write(plus_one))
        self.wait(1)

        # Simplify and display the final result
        final_result = MathTex("x = 3", color=GREEN).next_to(equation_plus_one, DOWN)
        self.play(Transform(equation_plus_one.copy(), final_result))
        self.wait(1)
