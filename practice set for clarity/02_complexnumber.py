# Create a class named Complex
class Complex:

    # This function runs automatically when object is created
    # It stores real part (r) and imaginary part (i) inside object
    def __init__(self, r, i):
        self.r = r      # store real part inside object
        self.i = i      # store imaginary part inside object

    # This function controls how object prints when we use print(object)
    def __str__(self):
        return f"{self.r} + {self.i}i"

    # This function runs when we use +
    # Example: c1 + c2  →  c1.__add__(c2)
    def __add__(self, other):

        # add real parts and imaginary parts separately
        return Complex(self.r + other.r,
                       self.i + other.i)

    # This function runs when we use *
    # Example: c1 * c2  →  c1.__mul__(c2)
    def __mul__(self, other):

        # formula:
        # (a+bi)(c+di) = (ac − bd) + (ad + bc)i

        real = self.r * other.r - self.i * other.i   # calculate real part
        imag = self.r * other.i + self.i * other.r   # calculate imaginary part

        # return new Complex object containing result
        return Complex(real, imag)


# create first complex number object
c1 = Complex(1, 2)   # represents 1 + 2i

# create second complex number object
c2 = Complex(3, 4)   # represents 3 + 4i


# add complex numbers using overloaded + operator
print(f"The addition is {c1 + c2}")

# multiply complex numbers using overloaded * operator
print(f"The multiplication is {c1 * c2}")