def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celcius fahrenheit 
    ##################################################
    """

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """

    celcius = float(input("Celsius:"))
    fahrenheit = 9 / 5 * celcius + 32
    print(f'fahrenheit:\t{fahrenheit:.2f}')

    return celcius, fahrenheit
    
if __name__ == '__main__':
    main()
