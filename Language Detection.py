#Hackerrank Language Detection challenge
#Author: Luciano Andrade

#Given a snippet of text in English, French, German, or Spanish, detect the snippet's language and print the language name. You may build an offline model for this. The snippet may contain one or more lines.

#You may make no more than 15 submissions for this problem, during the contest.

#Input Format

#One or more lines of text.

#Constraints

#. The snippet will not exceed 3 kilobytes in size.
#. The snippet will be onw of the following languages: English, French, German, or Spanish.

#Output Format

#Print the snippet's language (in Title Case, as written above) on a new line.

eng_set = ["and", "the", "to", "that", "for", "not", "with", "you", "this", "but", "have", "he", "him", "from", "they", "she", "her", "there", "their", "would", "what", "of", "in", "of"]

deu_set = ["der", "und", "sein", "ein", "zu", "haben", "ich", "werden", "sie", "nicht"]
 
fr_set = ["le", "et", "pour", "dans", "ce", "qui", "sur", "pas", "plus", "avec", "tout", "faire", "autre", "mais", "nous", "vous", "comme", "leur", "elle", "avant", "aussi", "même", "bien", "très"]

sp_set = ["que", "te", "el", "y", "ser", "se", "por", "con", "su", "para", "como", "todo", "pero", "mas", "este", "otro", "ese", "porque", "cuando", "muy", "sin", "mucho", "sobre", "mi"]

snippet = input();

eng_count = 0
deu_count = 0
fr_count = 0
sp_count = 0

for word in eng_set:
    if word in snippet:
        eng_count += 1
for word in deu_set:
    if word in snippet:
        deu_count += 1
for word in fr_set:
    if word in snippet:
        fr_count += 1
for word in sp_set:
    if word in snippet:
        sp_count += 1

feq=[["English",eng_count],["Spanish",sp_count],["German",deu_count],["French",fr_count]]

feq.sort(key=lambda x: x[1])

print(feq[-1][0])
