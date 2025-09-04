from fpdf import FPDF
import webbrowser


class Bill:
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, other_flatmate):
        weight = self.days_in_house / (self.days_in_house + other_flatmate.days_in_house)
        return round(bill.amount * weight, 2)


class PdfReport:
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        pdf.set_font("Arial", "B", 24)
        pdf.cell(0, 40, "Flatmates Bill", border=0, align="C", ln=1)

        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 20, f"Period: {bill.period}", ln=1)

        pdf.set_font("Arial", size=12)
        pdf.cell(0, 20, f"{flatmate1.name} pays: ${flatmate1.pays(bill, flatmate2)}", ln=1)
        pdf.cell(0, 20, f"{flatmate2.name} pays: ${flatmate2.pays(bill, flatmate1)}", ln=1)

        pdf.output(self.filename)
        webbrowser.open(self.filename)


# ============================
# Program starts here
# ============================

# Take user input
period = input("Enter the bill period (e.g. March 2025): ")
amount = float(input("Enter the bill amount: "))

name1 = input("Enter the name of flatmate 1: ")
days1 = int(input(f"How many days did {name1} stay in the house? "))

name2 = input("Enter the name of flatmate 2: ")
days2 = int(input(f"How many days did {name2} stay in the house? "))

# Create objects
bill = Bill(amount, period)
flatmate1 = Flatmate(name1, days1)
flatmate2 = Flatmate(name2, days2)

# Generate report
report = PdfReport("flatmates_bill.pdf")
report.generate(flatmate1, flatmate2, bill)

print(f"\n{flatmate1.name} pays: ${flatmate1.pays(bill, flatmate2)}")
print(f"{flatmate2.name} pays: ${flatmate2.pays(bill, flatmate1)}")
print("PDF report generated: flatmates_bill.pdf")
