"""''

%A = Nome do dia,
%d = Numero do dia do mes com 2 casas decimais
de
%B = Nome do mes
de
%Y = Ano em quatro casas

'%A, %d de %B de %Y'

#########################

%d/ = Numero do dia
%m/ = Numero do mes
%Y  = Numero do ano

%d/%m/%Y 

###################

%H: = Hora
%M: = Minuto 
%S  = Segundo

"""''

from datetime import datetime
from locale import setlocale, LC_ALL  # muda idioma
from calendar import mdays  # ve o mes e qts dias tem tal mes

setlocale(LC_ALL, 'pt_BR.utf-8')  # muda idioma

dt = datetime.now()
mes_atual = int(dt.strftime('%m'))
formatacao = dt.strftime('%A, %d de %B de %Y')
formatacao2 = dt.strftime('%d/%m/%Y %H:%M:%S')

print(formatacao)
print(formatacao2)
print(f'Mês atual: {mes_atual} \nMês atual tem: {mdays[mes_atual]} dias')
