import random as rand
import vim_list

def main():

	name = print_intro()	
	percentage = question_loop()
	print_results(percentage, name)	


def print_intro():

	print('Welcome to VIM tester!')
	print('What is your name?')

	usr_name=input()

	print('Hello, {}.'.format(usr_name))
	print('I am going to ask you a series of questions to test your VIM knowledge.')
	return usr_name


def question_loop():
	flag='1'
	right=0
	wrong=0

	the_list = vim_list.commands
	total_questions = len(the_list) - 1

	while flag == '1':
		n=rand.randint(0, total_questions)
		print('\nWhat command {} ?'.format(the_list[n][1]))
		answer=input()
		if answer==the_list[n][0]:
			print('Yes, you are correct! \n')
			right=right+1
		else:
			print('Not quite.  The answer is {}. \n'.format(the_list[n][0]))
			wrong=wrong+1
		print("Enter 1 to continue, or any other key to quit")
		flag=input()
		

	total=right+wrong
	percentage_correct=round(right/total*100,1)
	return percentage_correct


def print_results(perc, nm):
	print('{}, you got {}% correct.'.format(nm, str(perc)))
	if perc >= 80:
		print('You are a VIM master, {}!'.format(nm))
	else:
		print('Keep practicing VIM, {}!'.format(nm)) 


if __name__ == '__main__':
	main()
