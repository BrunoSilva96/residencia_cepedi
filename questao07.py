import random

timeA = 'Bahia'
timeB = 'Vitória'
timeC = 'Vasco'
timeD = 'Flamengo'

def resultado_partidas(time1, time2):
    gols_time1 = int(input(f"Digite os gols marcados pelo {time1}: "))
    gols_time2 = int(input(f"Digite os gols marcados pelo {time2}: "))
    
    if gols_time1 > gols_time2:
      return time1
    elif gols_time2 > gols_time1:
      return time2
    else:
      print("Jogo empatado, penalidade maxíma!!!")

      def penaltis():
        penaltis_time1 = random.randint(0, 5)
        penaltis_time2 = random.randint(0, 5)

        if penaltis_time1 > penaltis_time2:
          return time1
        elif penaltis_time2 > penaltis_time1:
          return time2
        else:
          penaltis()
    
      return penaltis()

finalista1 = resultado_partidas(timeA, timeB)
finalista2 = resultado_partidas(timeC, timeD)

print(f"Os times {finalista1} e {finalista2} estão na grande final!")
            