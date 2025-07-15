import pandas as pd
import matplotlib.pyplot as plt


tabela = pd.DataFrame({
    'idade' : [20, 23, 45, 31, 32],
    'nome' : ['joão', 'maria', 'josé', 'sofia', 'helena']
})

plt.hist(tabela['idade'])
