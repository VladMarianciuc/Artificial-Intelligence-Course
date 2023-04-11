joc = {'a1': ' ', 'b1': ' ', 'c1': ' ',        # inițializarea gridului de joc intr-o variabila de tip dictionar
       'a2': ' ', 'b2': ' ', 'c2': ' ',
       'a3': ' ', 'b3': ' ', 'c3': ' '}


def afisare(joc):                              # functie ce afiseaza gridul in diferite momente ale jocului
  print('-----------------------')
  print('   A|B|C\n')
  print(f"1  {joc['a1']}|{joc['b1']}|{joc['c1']}")
  print('-  -+-+-')
  print(f"2  {joc['a2']}|{joc['b2']}|{joc['c2']}")
  print('-  -+-+-')
  print(f"3  {joc['a3']}|{joc['b3']}|{joc['c3']}")
  print('\n')

afisare(joc)
om = input('Alege X sau 0: ').upper()          # alegerea semnului de joc
bot = '0'if(om=='X') else 'X'
print('\n')

def casutaLibera(mutare):                      # functie care verifica daca o mutare este valida (i.e. sa nu puna peste alt semn)
  if joc[mutare] == ' ':
    return True 
  return False 

def puneMutare(semn, mutare):                  # functie ce pune semnul corespunzator in grid 
  if casutaLibera(mutare):                     # si verifica daca este intrunita conditia de victorie sau remiza
    joc[mutare] = semn 
    afisare(joc)
    if remiza():
      print('Egalitate!')
      quit()
    if victorie():
        print('Ai pierdut!')

  else:                                        # in cazul unei mutari ilegale, se cere alegerea unei alte mutari
    mutare = input('Nu merge. Pune în altă parte: ').lower()
    puneMutare(semn, mutare)
    return    
    
def remiza():                                  # conditie de remiza
  for k in joc.keys():
    if joc[k] == ' ':
      return False 
  return True 
  
def victorie():                                # conditie de victorie
  if (joc['a1'] == joc['b1'] and joc['a1'] == joc['c1'] and joc['a1'] != ' '):
      return True
  elif (joc['a2'] == joc['b2'] and joc['a2'] == joc['c2'] and joc['a2'] != ' '):
      return True
  elif (joc['a3'] == joc['b3'] and joc['a3'] == joc['c3'] and joc['a3'] != ' '):
      return True
  elif (joc['a1'] == joc['a2'] and joc['a1'] == joc['a3'] and joc['a1'] != ' '):
      return True
  elif (joc['b1'] == joc['b2'] and joc['b1'] == joc['b3'] and joc['b1'] != ' '):
      return True
  elif (joc['c1'] == joc['c2'] and joc['c1'] == joc['c3'] and joc['c1'] != ' '):
      return True
  elif (joc['a1'] == joc['b2'] and joc['a1'] == joc['c3'] and joc['a1'] != ' '):
      return True
  elif (joc['a3'] == joc['b2'] and joc['a3'] == joc['c1'] and joc['a3'] != ' '):
      return True
  else:
      return False

def mutareOm():   
  print('OM\n--')
  mutare = input(f'Pune un {om}: ').lower()
  puneMutare(om, mutare)
  return 

def mutareBot():
  scor_optim = -1000
  mutare_optima = ''
  for k in joc.keys():
    if joc[k] == ' ':
      joc[k] = bot
      scor = minimax(joc, False)
      joc[k] = ' '
      if scor > scor_optim:
        scor_optim = scor 
        mutare_optima = k
  print('BOT\n---')
  print(f'Scor: {scor_optim}. Mutare optima: {mutare_optima}')
  if(scor_optim):
    print('Predicție: Victorie')
  else:
    print('Predicție: Egalitate')
  puneMutare(bot, mutare_optima)
  return 
  
def cineCastiga(semn):
  if (joc['a1'] == joc['b1'] and joc['a1'] == joc['c1'] and joc['a1'] == semn):
      return True
  elif (joc['a2'] == joc['b2'] and joc['a2'] == joc['c2'] and joc['a2'] == semn):
      return True
  elif (joc['a3'] == joc['b3'] and joc['a3'] == joc['c3'] and joc['a3'] == semn):
      return True
  elif (joc['a1'] == joc['a2'] and joc['a1'] == joc['a3'] and joc['a1'] == semn):
      return True
  elif (joc['b1'] == joc['b2'] and joc['b1'] == joc['b3'] and joc['b1'] == semn):
      return True
  elif (joc['c1'] == joc['c2'] and joc['c1'] == joc['c3'] and joc['c1'] == semn):
      return True
  elif (joc['a1'] == joc['b2'] and joc['a1'] == joc['c3'] and joc['a1'] == semn):
      return True
  elif (joc['a3'] == joc['b2'] and joc['a3'] == joc['c1'] and joc['a3'] == semn):
      return True
  else:
      return False


def minimax(joc, maxim): # parametrul maxim este de tip Boolean si are rolul de a oscila intre maximizare si minimizare (in functie de jucatorul care este la mutare)
  if cineCastiga(bot):   # scorul diferitelor pozitii
      return 1 
  elif cineCastiga(om):
      return -1 
  elif remiza():
      return 0
      
  if maxim:                  # aici muta bot-ul, deci vrem sa maximizam scorul
      scor_optim = -1000 
      for k in joc.keys():
          if joc[k] == ' ':
              joc[k] = bot 
              scor = minimax(joc, False)
              joc[k] = ' '
              if scor > scor_optim:
                  
                scor_optim = scor
      return scor_optim 
  else:                      # aici muta omul, deci vrem sa maximizam scorul omului (altfel spus sa minimizam scorul botului)
      scor_optim = 1000 
      for k in joc.keys():
          if joc[k] == ' ':
              joc[k] = om 
              scor = minimax(joc, True)
              joc[k] = ' '
              if scor < scor_optim:
                  scor_optim = scor 
      return scor_optim


while not victorie():                
  if(om=='X'):
    mutareOm()
    mutareBot()
  else:
    mutareBot()
    mutareOm()
