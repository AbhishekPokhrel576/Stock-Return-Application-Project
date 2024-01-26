from app.utils.reader import convert_stock_returns
from app.domain.StockReturn import StockReturn
from app.domain.Industry import Industry
from app.utils.reader import convert_industry
import app.utils.stockutils as StockUtils




# This is the Starting Point File.
def main():
    ind_file_path = 'Resources\Stocks_Industry.txt'
    ret_file_path = 'Resources\Stocks_Returns.txt'
    with open(ret_file_path, 'r') as f:
        content = f.readlines()
        # We want to start from the second line because we don't want to take the header into account
        stock_returns: list[StockReturn] = convert_stock_returns(content[1:])
    
    with open(ind_file_path, 'r') as s:
        content = s.readlines()
        industries: list[Industry] = convert_industry(content[1:])
    
    while True:
        print_Main_Menu()
        user_selection = int(input('Option: '))
        if user_selection == 0:
            break
        elif user_selection == 1:
            # \n has been used everywhere for aesthetics and spacing purposes
            print('\n A List of Unique Stocks: ')
            print(StockUtils.get_distinct_stocks(stock_returns))
            print('------------------------\n')
            continue
        elif user_selection == 2:
            stock_name = input('Please enter the name of a particular Stock: ').upper() # added the upper() function to take the user entry and capitalize it.
            
            try:
                print('\n Min, max, and average return for the Stock ' + stock_name)
                print(StockUtils.get_stock_stats(stock_returns, stock_name))
                print('------------------------\n')
            except:
                print(f'You have entered an Invalid Stock name here. Please enter again! Here is the list you can choose from below: \n{StockUtils.get_distinct_stocks(stock_returns)}\n')

        elif user_selection == 3:
            indus_name = input('Please enter the name of a particular Industry: ')
            try:
                print('\n Min, max and average return for the ' + indus_name + ' Industry: ')
                print(StockUtils.get_industry_stats(stock_returns, industries, indus_name))
                print('------------------------\n')
            except:
                print(f'You have entered an Invalid Industry name here. Please enter again! Here is the list you can choose from below: \n{StockUtils.get_unique_industries(industries)}\n')

        else:
            print("OPTION YOU SELECTED IS INVALID. ")

def print_Main_Menu():
    print('Hello. Welcome to the Stock Return Calculator Application')
    print('Please choose an option from the menu given: ')
    print('1. Receive a list of all unique stocks')
    print('2. Receive min, max and average return of a particular Stock')
    print('3. REceive min, max and average return of a particular Industry')
    print('0. Exit Application!')
main()
        
