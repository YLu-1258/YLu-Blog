import getpass

class Colors:
    '''
    Colors class to print colored text to terminal, Does not work in fastpages :/
    '''
    # Man I love ANSI
    PINK = '\033[95m'
    LILAC = '\033[94m'
    BLUE = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Quiz():
    # Main class for the quiz
    def __init__(self):
        # Quiz "constructor", initiates list of questions and answers and other settings.
        self.ques = []
        self.ans = []
        self.colors = Colors()
        self.showans = False     # Show correct answers after a wrong input
        self.total = 0           # Total questions
        self.correct = 0         # Total right
        self.skipped = 0         # Total skipped

    def addQues(self, question, answer):
        '''
        Adding Questions and answers to the quiz
        '''
        self.ques.append(question)
        self.ans.append(answer)
        self.total += 1          # increment total by 1 
    
    def askQues(self, idx):
        '''
        Helper function to ask one question, check answer, increment student data
        '''
        print(self.colors.PINK + "QUESTION: " + self.colors.ENDC + self.colors.BOLD + self.ques[idx] + self.colors.ENDC) # Print Question
        rsp = input(self.colors.YELLOW + "What is your response? " + self.colors.ENDC)                                    # Get Response
        if rsp.lower() == self.ans[idx].lower():                                                                         # Check answer
            print(self.colors.GREEN + "YOU ARE CORRECT!" + self.colors.ENDC + " Response " + self.colors.BLUE + rsp + self.colors.ENDC + " is correct!")
            self.correct += 1
        elif rsp.lower() == "/s":
            print(self.colors.YELLOW + "Skipping...." + self.colors.ENDC)
            self.skipped += 1
        else:
            if self.showans:
                print(self.colors.RED + "Response '" + rsp + "' is incorrect." + self.colors.ENDC + " The right answer was " + self.colors.BLUE + self.ans[idx] + self.colors.ENDC)
            else:
                print(self.colors.RED + "Response '" + rsp + "' is incorrect." + self.colors.ENDC)

    def percentage(self, x, y):
        '''
        Function to calculate percentage correct
        '''
        return 100 * float(x)/float(y)

    def playQuiz(self):
        '''
        Main Quiz loop, set settings and ask questions
        '''
        show_ans = input(self.colors.UNDERLINE + "Would you like to show correct answers after incorrect responses? [y/n]" + self.colors.ENDC + " ")
        print(self.colors.YELLOW + "GOOD LUCK {0}!".format(getpass.getuser().upper()) + " Type '" + self.colors.BLUE + "/s" + self.colors.YELLOW + "' to skip!")
        if show_ans in ["y", "yes", "Y", "YES"]: # Multiple cases of user inputs, assume any other input / no input == False.
            self.showans = True
        for i in range(0,self.total):            # Iterate over all questions, no repetitive code here
            self.askQues(i)
        # Print a little congratulations message
        print(self.colors.LILAC + "Congratulations! you got " + self.colors.GREEN + '{0:.2f}'.format(self.percentage(self.correct, self.total)) + "%" + self.colors.LILAC + " and {0} questions skipped on this quiz!".format(self.colors.YELLOW + str(self.skipped) + self.colors.LILAC)) 


# Creating our quiz
q1 = Quiz()

# AYO CHEATER STOP LOOKIN HERE
q1.addQues("Name the Python output command mentioned in this lesson?", "print")
q1.addQues("If you see many lines of code in order, what would College Board call it?", "sequence")
q1.addQues("What keyword in python is used to describe a function?", "def")
q1.addQues("What command is used to include other functions that were previously developed?", "import")
q1.addQues("What command is used to evaluate correct or incorrect response in this quiz?", "if")
q1.addQues("Each 'if' command contains an '_________' to determine a true or false condition?", "expression")
q1.addQues("What is an input to a function or method called?", "parameter")
q1.addQues("If Input is data the computer receives, what is the data that the computer sends back?", "output")
q1.addQues("What is a reusable block of code called?", "function")
q1.addQues("What operator is used for string concatenation in Python?", "+")

q1.playQuiz()


