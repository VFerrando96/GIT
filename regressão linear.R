#INTERVALO DE CONFIANÇA para b0 e b1
setwd("/home/ime/Downloads")
getwd()
library(readxl) # importação de arquivos .XLSX
# Importação:
bd <- as.data.frame(read_xlsx("Cimento_Regressão.xlsx",
                                 sheet = "BD_Cimento",
                                 col_names = TRUE,
                                 range = "A1:E14"))
mod1<-lm(heat ~ x1,data=bd)
summary(mod1)
sqe = sqrt(anova(mod1)[2,2])
confint(mod1,level=0.95)

######################
# 
# Analise de residuos
#
#############
# 1 os erros apresentam meda e variancia constante
#H0 os residuos seguem distribuição normal
# H1 C.C
"""
alpha=
n=
estatistica do teste=
valor critico =
par(mfrow)=c(1,2),pin=c(5,5)
boxplot(Ei)
hist(ei,prob=TRUE)
lines(density(ei))
                              valor-p < alpha (bom senso)
    

"""
resid(mod1)
shapiro.test(resid(mod1))
""" ao nivel de significancia alpha de 0.05 e tamanho amostral n=13, não há evidencia para rejeitar a hipotese nula; ou seja, 
os residuos segue a distribuição normal.


Homocedasticidade == variancia dos residuos= constante

heterocedasticidade == variancia não constantes

teste de breusch-pagan cedasticidade dos residuos

"""

library(lmtest)
bptest(mod1)