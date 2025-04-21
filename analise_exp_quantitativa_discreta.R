# LucasArcanjoNoquelliDaSilva_RM563353_fase2_cap7

# Medidas de Tendência Central

quantitativa_discreta <- c(4045, 3808, 9000000, 238636442, 1557570401, 4595, 9200, 46, 77223, 35375235, 49, 54000, 933600, 38, 4, 30, 30, 70, 275000000, 80, 43, 8, 2000000, 10, 1325, 65000, 2700, 5200000000, 2000000, 85)

#calculando média
media_quantitativa_discreta <- mean(quantitativa_discreta)

#calculando mediana
mediana_quantitativa_discreta <- median(quantitativa_discreta)

# calculando moda
library(DescTools)

moda_quantitativa_discreta <- Mode(quantitativa_discreta)

#Medida de Dispersão

minimo_quantitativa_discreta <- min(quantitativa_discreta)

maximo_quantitativa_discreta <- max(quantitativa_discreta)

amplitude_quantitativa_discreta <- diff(range(quantitativa_discreta))

variancia_quantitatuva_discreta <- var(quantitativa_discreta)

desvio_padrao_quantitativa_discreta <- sd(quantitativa_discreta)

coef_variacao_quantitativa_discreta <- (sd(quantitativa_discreta)/mean(quantitativa_discreta))*100

#Medidas Separatrizes

quartis_quantitativa_discreta <- quantile(quantitativa_discreta, probs=c(0.25, 0.50, 0.75))

decis_quantitativa_discreta <- quantile(quantitativa_discreta, probs = seq(0.1, 0.9, by = 0.1))

centis_quantitativa_discreta <- quantile(quantitativa_discreta, probs = seq(0.01, 0.99, by = 0.01))


# Análise Gráfica

library(ggplot2)

df <- data.frame(valor = quantitativa_discreta)

# Histograma com ggplot2

ggplot(df, aes(x = valor))+
  geom_histogram(bins = 30, fill = "steelblue", color = "white")+
  ggtitle("Histograma com ggplot2")+
  xlab("Valores")+
  ylab("Frequência")

# Boxplot com ggplot2

ggplot(df, aes(y = valor))+
  geom_boxplot(fill = "tomato")+
  ggtitle("Boxplot com ggplot2")+
  ylab("Valores")