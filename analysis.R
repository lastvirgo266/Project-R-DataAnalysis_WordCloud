getwd()


#import
library(wordcloud)
library(RColorBrewer)
library(KoNLP)

#add Dictionary
useSejongDic()
data <- readLines("data.txt")
data <- sapply(data, extractNoun, USE.NAMES = F) #return List
data_unlist <- unlist(data) # change list to vector


#Apply option
data_unlist <- Filter(function(x){nchar(x)>=2}, data_unlist)


#Sub Unused word
sub_words <- readLines("sub_text.txt")

for(i in 1:length(sub_words)){
  data_unlist <- gsub(sub_words[i],"",data_unlist)
}


#print frequency
wordcount <- table(data_unlist)
#wordcount_top <- wordcount[wordcount>200]
wordcount_top <-head(sort(wordcount, decreasing = T),50)
#wordcount_top[199]



#Make word Cloud
color <- brewer.pal(12, "Set3")
windowsFonts(font=windowsFont("a한글사랑L"))
wordcloud(names(wordcount_top), wordcount_top, scale=c(5,0.5),random.order = FALSE, random.color = TRUE, colors = color, family = "font")
