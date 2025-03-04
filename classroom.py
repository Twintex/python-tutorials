import pandas as pd

#Dictionary of a classroom 

data = {
      "Classrooms" : ["Jss_3", "Ss_1", "Ss_2", "Ss_3"],
      "Height"  : [0.8, 1.2, 1.4, 1.6],
      "Average_Score" : [56, 63, 72, 90],
      "Students_Residence" : ["Uyo", "P.H", "Calabar", "Abak"],
}

df = pd.DataFrame(data)

print(df)