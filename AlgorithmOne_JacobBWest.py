# Jacob B. West
# November 3, 2021
# CENG-325 Algorithm 1
# Dr. Karlsson

# See bottom of file for main- all four algorithms will execute their associated examples provided

def MultiplicationOne(multiplier, multiplicand):
    originMultiplier = multiplier
    originMultiplicand = multiplicand
    product = 0b00000000
    print("Multiplication Algorithm One")
    print("Iter. %-12s %-17s %-17s" % ("Multiplier", "Multiplicand", "Product"))
    outputFormat = "{:^6}{:08b}     {:016b}  {:016b}"
    answerFormat = "Answer: {:08b} * {:08b} = {:08b} ({} * {} = {})\n"
    print(outputFormat.format(0, multiplier, multiplicand, product))

    # Algorithm One Start
    for rep in range(16):
        if multiplier & (1 << 0):
            product = multiplicand + product

        multiplicand = (multiplicand << 1) & 0b111111111111  # Shift left one bit
        multiplier = (multiplier >> 1) & 0b1111111111111111
        print(outputFormat.format(rep + 1, multiplier, multiplicand, product))
    # Algorithm One End

    print(answerFormat.format(originMultiplier, originMultiplicand, product, originMultiplier, originMultiplicand,
                              product))


def MultiplicationTwo(multiplier, multiplicand):
    originMultiplier = multiplier
    originMultiplicand = multiplicand
    product = 0b00000000000000000
    print("Multiplication Algorithm Two")
    print("Iter. %-12s %-17s" % ("Multiplicand", "Product"))
    outputFormat = "{:^6}{:08b}     {:017b}"
    answerFormat = "Answer: {:08b} * {:08b} = {:08b} ({} * {} = {})\n"

    product = product + multiplier  # Place multiplicand into bottom 8 bits of product
    print(outputFormat.format(0, multiplicand, product))

    # Algorithm Two Start
    for rep in range(8):
        if product & (1 << 0):
            result = (product >> 8) + multiplicand
            product = product & 0b00000000011111111  # Mask top 9 bits
            product = (result << 8) | product
        product = (product >> 1) & 0b1111111111111111  # Shift right one bit
        print(outputFormat.format(rep + 1, multiplicand, product))
    # Algorithm Two End

    print(answerFormat.format(originMultiplier, originMultiplicand, product, originMultiplier, originMultiplicand,
                              product))


def DivisionOne(dividend, divisor):
    originDividend = dividend
    originDivisor = divisor
    quotient = 0b0000
    print("Division Algorithm One")
    print("Iter. Quotient Divisor Remainder")
    outputFormat = "{:^6}{:04b}     {:08b}  {:08b}"
    answerFormat = "Answer: {:04b} / {:04b} = {:04b} R{:04b} ({} / {} = {} R{})\n"

    divisor = (divisor << 4) & 0b11111111
    remainder = dividend
    print(outputFormat.format(0, quotient, divisor, remainder))
    # Algorithm One Start
    for rep in range(5):
        remainder = remainder - divisor
        if remainder >= 0:
            quotient = (quotient << 1) & 0b1111
            quotient = quotient | (1 << 0)
        else:
            remainder = remainder + divisor
            quotient = (quotient << 1) & 0b0000
            quotient = quotient & (0 << 0)

        divisor = (divisor >> 1) & 0b11111111
        print(outputFormat.format(rep + 1, quotient, divisor, remainder))
    # Algorithm One End

    print(answerFormat.format(originDividend, originDivisor, quotient, remainder, originDividend, originDivisor, quotient, remainder))


def DivisionTwo(dividend, divisor):
    originDividend = dividend
    originDivisor = divisor
    remainder = 0b00000000000000000
    print("Division Algorithm Two")
    print("Iter. Divisor   Remainder")
    outputFormat = "{:^6}{:08b}  {:017b}"
    answerFormat = "Answer: {:08b} / {:08b} = {:08b} R{:08b} ({} / {} = {} R{})\n"

    remainder = remainder + dividend
    print(outputFormat.format(0, divisor, remainder))
    # Algorithm Two Start
    for rep in range(8):
        remainder = (remainder << 1) & 0b11111111111111111
        result = (remainder >> 8) - divisor
        if result >= 0:
            remainder = remainder & 0b00000000011111111 # Mask Top 9
            remainder = (result << 8) | remainder
            remainder = remainder | (1 << 0)
        else:
            remainder = remainder | (0 << 0)
        print(outputFormat.format(rep + 1, divisor, remainder))
    # Algorithm Two End

    quotient = remainder & 0b11111111
    remainder = (remainder >> 8) & 0b111111111
    print(
        answerFormat.format(originDividend, originDivisor, quotient, remainder, originDividend, originDivisor, quotient,
                            remainder))


def main():
    MultiplicationOne(0b00000011, 0b0000000000000110) # Algorithm 3.3
    MultiplicationTwo(0b00000011, 0b0000000000000110) # Algorithm 3.5
    DivisionOne(0b1111, 0b0100) # Algorithm 3.8
    DivisionTwo(0b00111100, 0b00010001) # Algorithm 3.11


if __name__ == '__main__':
    main()