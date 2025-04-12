def main():
    degrees_fahrenheit : float = float(input("input temprature in ferenheit: "))
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0

    print(f"temperature in celcius is: {degrees_celsius}")


if __name__ == '__main__':
    main()