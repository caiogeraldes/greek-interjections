require(tidyverse)

df <- read_csv("../data/data.csv")
df

counts <- df %>%
  group_by(author) %>%
  count() %>%
  arrange(desc(n))

df <- df %>%
  dplyr::filter(interjection != "ὦ")

df %>% ggplot(aes(y=interjection)) + geom_bar()


df %>% ggplot(aes(x= author, fill=author)) + geom_bar()


