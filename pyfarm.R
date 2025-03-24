# Dados estatísticos sobre o consumo histórico de calcário na Fazenda Esperança.
# ------------------------------------------------------------------------------

# Os dados em [consumo_calcario] foram trazidos da aplicação em Python (pyfarm.py).
# Por favor, veja o arquivo README.md para outras informações relacionadas.

# Dados históricos
# Mostram o consumo total anual de calcário, em kg/ha, entre 2009 e 2024.
consumo_calcario <- data.frame(ano=c("2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024"), consumo=c(5920, 5300, 6156, 6027, 5564, 5897, 5857, 6003, 5808, 4970, 6345, 5689, 5900, 5857, 5897, 6017))

# Média
# Consumo anual médio de calcário, em kg/ha, entre 2009 e 2024.
media_calcario <- mean(consumo_calcario$consumo)
print(media_calcario)

# Desvio padrão
# Variabilidade do consumo de calcário ao longo dos anos, em torno da média.
desvio_calcario <- sd(consumo_calcario$consumo)
print(desvio_calcario)

# Os dados de média e desvio padrão foram copiados de volta par a aplicação em Python, para exibição.

