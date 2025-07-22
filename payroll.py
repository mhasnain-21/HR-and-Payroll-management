def calculate_payroll(hours, rate, tax_rate = 0.1):
    gross = hours * rate
    tax = gross * tax_rate
    net = gross - tax
    return gross, tax, net