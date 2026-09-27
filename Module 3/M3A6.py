# Name: Aaron Madero
# Student ID: 862105814
# Section: 07
# Assignment: Module 3 Assignment 6

name = input("What is the student name? ")
score = int(input("What is their score? "))

grade_a = range(90,101)
grade_b = range(80,91)
grade_c = range(70,81)
grade_d = range(60,71)
grade_f = range(0,60)

letter_grade = ""
a_or_an = ""

if score in grade_a:
    letter_grade = "A"
    a_or_an = "an"
if score in grade_b:
    letter_grade = "B"
    a_or_an = "a"
if score in grade_c:
    letter_grade = "C"
    a_or_an = "a"
if score in grade_d:
    letter_grade = "D"
    a_or_an = "a"
if score in grade_f:
    letter_grade = "F"
    a_or_an = "an"

print(f"{name} earned {a_or_an} {letter_grade}")