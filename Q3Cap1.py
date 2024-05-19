#  Se você correr 10 quilômetros em 42 minutos e 42 segundos, qual é o seu passo médio (tempo por milha em minutos e segundos)? Qual é a sua velocidade média em milhas por hora?
quilometragem = 10;
milha = quilometragem/1.61; 

minutos = 42;
converte_Minutos_Segundos = minutos * 60;
segundos = 42; 
tempo_em_segundo =  minutos + segundos;
tempo_Em_Hora = tempo_em_segundo/3600;

converte_segundos_minutos = 42 / 60;
passo_medio_minutos = converte_segundos_minutos / milha;
passo_medio_segundos = tempo_em_segundo/milha; 
velocidade_media = milha/tempo_Em_Hora;

print(passo_medio_minutos,passo_medio_segundos,velocidade_media);