

    
def pontuação():
    return r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

def stopwords():
    lista = ['a', 'à', 'ao', 'aos', 'aquela', 'aquelas', 'aquele', 'aqueles', 'aquilo', 'as', 'às', 'até', 'com', 'como', 'da', 'das', 'de', 'dela', 'delas', 'dele', 'deles', 'depois', 'do', 'dos', 'e', 'é', 'ela', 'elas', 'ele', 'eles', 'em', 'entre', 'era', 'eram', 'éramos', 'essa', 'essas', 'esse', 'esses', 'esta', 'está', 'estamos', 'estão', 'estar', 'estas', 'estava', 'estavam', 'estávamos', 'este', 'esteja', 'estejam', 'estejamos', 'estes', 'esteve', 'estive', 'estivemos', 'estiver', 'estivera', 'estiveram', 'estivéramos', 'estiverem', 'estivermos', 'estivesse', 'estivessem', 'estivéssemos', 'estou', 'eu', 'foi', 'fomos', 'for', 'fora', 'foram', 'fôramos', 'forem', 'formos', 'fosse', 'fossem', 'fôssemos', 'fui', 'há', 'haja', 'hajam', 'hajamos', 'hão', 'havemos', 'haver', 'hei', 'houve', 'houvemos', 'houver', 'houvera', 'houverá', 'houveram', 'houvéramos', 'houverão', 'houverei', 'houverem', 'houveremos', 'houveria', 'houveriam', 'houveríamos', 'houvermos', 'houvesse', 'houvessem', 'houvéssemos', 'isso', 'isto', 'já', 'lhe', 'lhes', 'mais', 'mas', 'me', 'mesmo', 'meu', 'meus', 'minha', 'minhas', 'muito', 'na', 'não', 'nas', 'nem', 'no', 'nos', 'nós', 'nossa', 'nossas', 'nosso', 'nossos', 'num', 'numa', 'o', 'os', 'ou', 'para', 'pela', 'pelas', 'pelo', 'pelos', 'por', 'qual', 'quando', 'que', 'quem', 'são', 'se', 'seja', 'sejam', 'sejamos', 'sem', 'ser', 'será', 'serão', 'serei', 'seremos', 'seria', 'seriam', 'seríamos', 'seu', 'seus', 'só', 'somos', 'sou', 'sua', 'suas', 'também', 'te', 'tem', 'tém', 'temos', 'tenha', 'tenham', 'tenhamos', 'tenho', 'terá', 'terão', 'terei', 'teremos', 'teria', 'teriam', 'teríamos', 'teu', 'teus', 'teve', 'tinha', 'tinham', 'tínhamos', 'tive', 'tivemos', 'tiver', 'tivera', 'tiveram', 'tivéramos', 'tiverem', 'tivermos', 'tivesse', 'tivessem', 'tivéssemos', 'tu', 'tua', 'tuas', 'um', 'uma', 'você', 'vocês', 'vos']
    return lista

def separar_frases(texto):
    frases = []
    frase_atual = ""
    for char in texto:
        frase_atual += char
        if char in ".!?":  # Verifica se o caractere é um ponto final, exclamação ou interrogação
            frases.append(frase_atual.strip())
            frase_atual = ""
    if frase_atual:  # Adiciona a última frase caso não tenha terminado em um dos sinais
        frases.append(frase_atual.strip())
    return frases


texto = """Claro! Vou formatar o texto para você, destacando as principais seções e melhorando a legibilidade. Aqui está a versão formatada:

---

**Prefácio**

Um de nossos doces favoritos aqui na Dinamarca é o Ga-Jol, cujos fortes vapores de licorice são um complemento perfeito para nosso clima úmido e, geralmente, frio. Parte do charme do Ga-Jol, para nós dinamarqueses, são os dizeres sábios impressos em cada caixa. Comprei dois pacotes dessa iguaria essa manhã e nela veio este antigo ditado dinamarquês:

**Ærlighed i små ting er ikke nogen lille ting.**

*"Honestidade em pequenas coisas não é uma coisa pequena."* 

Era um bom presságio para com o que eu já desejava dizer aqui. Pequenas coisas são importantes. Este é um livro sobre preocupações modestas cujos valores estão longe de ser pequenos.

Deus está nos detalhes, disse o arquiteto Ludwig Mies van der Rohe. Essa citação retoma argumentos com contemporâneos sobre o papel da arquitetura no desenvolvimento de software, especialmente no mundo Agile. Bob e eu, às vezes, acabávamos engajados entusiasmadamente debatendo sobre este assunto. E sim, Mies van der Rohe atentava para os utilitários e as formas imemoriais de construção que fundamentam uma ótima arquitetura. Por outro lado, ele também selecionava pessoalmente cada maçaneta para cada casa que ele projetava. Por quê? Porque pequenas coisas são importantes.

Em nosso “debate” sobre Desenvolvimento Dirigido a Testes (TDD, sigla em inglês), Bob e eu descobrimos que concordamos que a arquitetura do software possui um lugar importante no desenvolvimento, embora provavelmente tenhamos perspectivas diferentes do significado exato disso. Essas diferenças são relativamente irrelevantes, contudo, pois podemos admitir que profissionais responsáveis dedicam algum tempo para pensar e planejar o início de um projeto. As noções de desenvolvimento dirigido apenas por testes e por códigos do final da década de 1990 já não existem mais. Mesmo assim, a atenção aos detalhes é um fundamento de profissionalismo ainda mais crítico do que qualquer visão maior. Primeiro, é por meio da prática em pequenos trabalhos que profissionais adquirem proficiência e confiança para se aventurar nos maiores. Segundo, a menor parte de uma construção desleixada, a porta que não fecha direito ou o azulejo levemente torto do chão, ou mesmo uma mesa desarrumada, retira completamente o charme do todo. É sobre isso que se trata o código limpo.

Ainda assim, a arquitetura é apenas uma metáfora para o desenvolvimento de software, especialmente para a parte que entrega o produto inicial no mesmo sentido que um arquiteto entrega uma construção imaculada. Nessa época do Scrum e do Agile, o foco está em colocar o produto rapidamente no mercado. Desejamos que a indústria funcione em velocidade máxima na produção de software. Essas fábricas humanas: programadores que pensam e sentem, que trabalham a partir das pendências de um produto ou do user story para criar o produto. A metáfora da fabricação está mais forte do que nunca no pensamento. Os aspectos da produção da manufatura japonesa de automóveis, de um mundo voltado para a linha de montagem, inspiraram grande parte do Scrum.

Ainda assim, mesmo na indústria automobilística, a maior parte do trabalho não está na fabricação, mas na manutenção – ou na prevenção. Em software, 80% ou mais do que fazemos é chamado de “manutenção”: o ato de reparar. Em vez de abraçar o típico foco ocidental sobre a produção de bons softwares, deveríamos pensar mais como um pedreiro que conserta casas na indústria de construção, ou um mecânico de automóveis na área automotiva. O que o gerenciamento japonês tem a dizer sobre isso?

Por volta de 1951, uma abordagem qualitativa chamada Manutenção Produtiva Total (Total Productive Maintenance - TPM em inglês) surgiu no cenário japonês. Seu foco era na manutenção em vez da produção. Um dos maiores fundamentos da TPM é o conjunto dos chamados princípios 5S, uma série de disciplinas – uso aqui o termo “disciplina” para fins educativos. Os princípios 5S, na verdade, são os fundamentos do Lean – outro jargão no cenário ocidental, e cada vez mais conhecida no mundo dos softwares. Esses princípios não são uma opção. Assim como Tio Bob diz em suas preliminares, a prática de um bom software requer tal disciplina: foco, presença de espírito e pensamento. Nem sempre é sobre fazer, sobre pressionar os equipamentos da fábrica para produzir em velocidade máxima. A filosofia dos 5S inclui os seguintes conceitos:

- **Seiri**: organização (pense em “ordenar”). Saber onde estão as coisas – usar abordagens como nomes adequados – é crucial. Acha que dar nome a identificadores não é importante? Leia próximos capítulos.

- **Seiton**: arrumação (pense em “sistematizar”). Há um antigo ditado americano que diz: “Um lugar para tudo, e tudo em seu lugar”. Um pedaço de código deve estar onde você espera encontrá-lo – caso não esteja, refatore e o coloque lá.

- **Seiso**: limpeza (pense em “polir”): manter o local de trabalho livre de fossa pendurados, gordura, migalhas e lixo. O que os autores falam aqui sobre encher seu código com comentários e linhas de códigos como comentários que informam o passado ou os desejos para o futuro? Livre-se deles.

- **Seiketsu**: padronização. A equipe concorda em manter o local de trabalho limpo. Você acha que este livro fala algo sobre ter um estilo de programação consistente e uma série de práticas dentro da equipe? De onde vêm tais padrões? Continue a leitura.

- **Shutsuke**: disciplina (autodisciplina). Isso significa ter disciplina para seguir as práticas e refletir frequentemente isso no trabalho e estar disposto a mudar.

Se aceitar o desafio – isso, o desafio – de ler e aplicar o que é aconselhado neste livro, você entenderá e apreciará o último item. Aqui estamos finalmente indo em direção às raízes do profissionalismo responsável numa profissão que deve se preocupar com o ciclo de vida de um produto. Conforme façamos a manutenção de automóveis e outras máquinas na TPM, a manutenção corretiva – esperar que bugs apareçam – é a exceção. Em vez disso, subimos um nível: inspecionamos as máquinas todos os dias e consertamos as partes desgastadas antes de quebrarem, ou percorremos o equivalente aos famosos 16.000 km antes da primeira troca de óleo para testar o desgaste. No código, a refatoração é impiedosa. Você ainda pode melhorar um nível a mais com o advento do movimento da TPM há 50 anos; construa máquinas que sejam passíveis de manutenção. Tornar seu código legível é tão importante quanto torná-lo executável. A última prática, adicionada à TPM em torno de 1960, é focar na inclusão de máquinas inteiramente novas ou substituir as antigas. Como nos adverte Fred Brooks, provavelmente devemos refazer partes principais do software a partir do zero a cada sete anos ou então se livrar dos entulhos. Talvez devêssemos atualizar a constante de tempo de Fred para semanas, dias ou horas, em vez de anos. É aí onde ficam os detalhes.

Há um grande poder nos detalhes, mesmo assim existe algo simples e profundo sobre essa abordagem para a vida, como talvez esperemos de qualquer abordagem que afirme ter origem japonesa. Mas essa não é apenas uma visão ocidental de mundo sobre a vida; a sabedoria de ingleses e americanos também está cheia dessas advertências. A citação de Seiton mais acima veio da ponta da caneta de um ministro em Ohio que visualizou literalmente a organização “como um remédio para todos os níveis de mal”. E Seiso? Deus ama a limpeza. Por mais bonita que uma casa seja, uma mesa desarrumada retira seu esplendor. E Shutsuke nessas pequenas questões? Quem é fiel no pouco também é no muito. E que tal ficar ansioso para refatorar na hora certa, fortalecendo sua posição para as “grandes” decisões subsequentes, em vez de descartá-las? Um homem prevenido vale por dois. Deus ajuda a quem cedo madruga. Não deixe para amanhã o que se pode fazer hoje. (Esse era o sentido original da frase “o último momento de responsabilidade”, em Lean, até cair nas mãos dos consultores de software). E que tal “calibrar” o local de esforços pequenos e individuais num grande todo? De grão em grão a galinha enche o papo. Ou que tal integrar um trabalho de prevenção no dia a dia? Antes prevenir do que remediar.

O código limpo honra as profundas raízes do conhecimento sob nossa cultura mais ampla, ou como ela fora um dia, ou deve ser, e poderá vir a ser com a atenção correta aos detalhes. Mesmo na grande literatura na área de arquitetura encontramos visões que remetem a esses supostos detalhes. Pense nas maçanetas de Mies van der Rohe. Aquilo é seiri. É ficar atento a cada nome de variável. Deve-se escolher o nome de uma variável com cuidado, como se fosse seu primeiro filho.

Como todo proprietário de uma casa sabe, tal cuidado e constante refinamento jamais acaba. O arquiteto Christopher Alexander – pai dos padrões e das linguagens de padrões – enxerga cada ato do próprio projeto como um conserto pequeno e local. E ele enxerga a habilidade de uma boa estrutura como o único objetivo do arquiteto; pode-se deixar as formas maiores para os padrões e seus aplicativos para os moradores. O

"""

# define a quantidade de frazes do resumo.
if texto.count(". ") > 20: # se tiver tiver mais de 20 frases
    quant_frases_resumo = int(round(texto.count(". ") / 10, 0)) #divide a quantidade de frases por 10
else:
    quant_frases_resumo = 1 # 

# define Remove pontuações e retorna uma lista dos caracteres sem pontuações
caracteres_sem_pontuacao = []
for char in texto:
    if char not in pontuação():  # se o caracter não for uma pontuação
        caracteres_sem_pontuacao.append(char)        # então adicione a lista  
texto_sem_pontuacao = "".join(caracteres_sem_pontuacao)


# def  Remove as stopwords
stopwords = stopwords()
palavras_texto = texto_sem_pontuacao.split() # Divide o texto sem pontuação em palavras
testo_processado = []
for palavras in palavras_texto:
    if palavras.lower() not in stopwords:
        testo_processado.append(palavras)



# def  Coloca no dicionario a frequência de que cada palavra aparece.
frequencia_palavras = {}
for palavras in testo_processado:
    if palavras not in frequencia_palavras:
        frequencia_palavras[palavras] = 1
    else:
        frequencia_palavras[palavras] += 1


lista_frases = separar_frases(texto)


# def somar o ponto das palavras nas frazes e retorna um dicionario com o ponto da fraze na fraze
pontuacao_frases = {}
for frases in lista_frases:
    for palavras in frases.lower().split(): #divide as frases em palavras e converte para minusculo
        if palavras in frequencia_palavras.keys():
            if frases not in pontuacao_frases.keys():
                pontuacao_frases[frases] = frequencia_palavras[palavras]
            else:
                pontuacao_frases[frases] += frequencia_palavras[palavras]

pontuacao_frases = {
    chave: int(valor) for chave, valor in pontuacao_frases.items()
}


chaves = list(pontuacao_frases.values())
repetido = []
for i in range(quant_frases_resumo):
    repetido.append(max(chaves))
    del chaves[chaves.index(max(chaves))]



pontuacao_frases_lista = [(chave, valor) for chave, valor in pontuacao_frases.items()]

frases_resumo = []
for frase_pontuacao in pontuacao_frases_lista:
    if frase_pontuacao[1] in repetido:
        frases_resumo.append(frase_pontuacao[0])

resumo = ' '.join(frases_resumo)
print(resumo)

