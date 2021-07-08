import csv
import random
import difflib

row_count = 0
passed = 0
used = []
randoms = False
end = False
wrong = 0
correct = 0
xbad = [448,549,666,936,937,943,1008] #produces errors for Xhosa Column 1, don't know why

##english_1 = 0
##english_2 = 1
##xhosa_1 = 2
##xhosa_2 = 3

path = 'C:\\Users\\User\\Desktop\\py work\\Old\\Xhosa quiz\\Vocab.csv'
econding_ = 'Windows-1252'

def reference(rand,language):
    with open(path, encoding=econding_) as read:
                reader = csv.reader(read)
                row_x = [row for idx, row in enumerate(reader) if idx in (rand,)][0][0].split(';')[language]
    return row_x

def language(rand,language):
    if rand in xbad:
        if language == 2:
            row_x = "!ERROR!"*5
        else:
            row_x = reference(rand,language)            
    else:
        row_x = reference(rand,language)
    return row_x

def cont():
    cont = input().lower()
    if cont == 'e':
        end = True
    else:
        end = False
    return end

def answer(correct, wrong, answer):
    result = ''
    provided = input()
    
    provided_seq = list(str(provided))
    answer_seq = list(str(answer))
    score = int(difflib.SequenceMatcher(None, provided_seq, answer_seq).ratio()*100)
    
    # print(provided_seq, answer_seq, '.....Score', score)
    if score >= 80:
        correct += 1
        result = 'Correct!'
    else:
        wrong += 1
        result = 'INCORRECT!'
        
        
    return correct, wrong, result

input('Welcome to isiXhosa Quiz! (Press any key to begin):')

while True:
    try:
        select = int(input("Select language of the questions- (1)English (2)Xhosa (3)Switch it up!: "))
    
        if select == 1:
            lang_Q, lang_A = 1,2
            break
        elif select == 2:
            lang_Q, lang_A = 2,1
            break
        elif select == 3:
            randoms = True
            break
        else:
            pass
    except ValueError:
        print('-_-')
            

for i in open(path, encoding=econding_):
    row_count +=1

while True:
    if passed == row_count:
        break
    elif end is True:
        break
    else:
        rand = random.randint(0,row_count-1)
        if rand in used:
            pass
        else:
            used.append(rand)
            
            if randoms is True:
                lang_Q = random.randint(1,2)
                if lang_Q == 1:
                    lang_A = 2
                else:
                    lang_A = 1
            else:
                pass
                    
            row_x1, row_x2 = language(rand,lang_Q), language(rand,lang_A)

            if row_x1 == '':
                pass
            else:
                passed +=1
                print('Question:',row_x1, end='\r')
                print()
                correct, wrong, result = answer(correct, wrong, row_x2)
                
                print('\nYou are '+ result +' The answer is: \''+ row_x2 +'\'.\nPress enter for next the question.')
                end = cont()

                #print('\n')


print('\nYou have completed the quiz!')
fin_per = (correct/passed)*100
print('Score: '+str(correct)+'/'+str(passed),str(fin_per)+'%')
print('Hit enter to exit')
        
input()


    

    



        
