require(tidyverse)

df <- read_csv("../data/data.csv")


df %>% group_by(interjection) %>% count() %>% arrange(desc(n))
# # A tibble: 93 × 2
# # Groups:   interjection [93]
#    interjection     n
#    <chr>        <int>
#  1 ὦ             2381
#  2 αὖ             281
#  3 οἴμοι          243
#  4 ἰὼ             233
#  5 φεῦ            165
#  6 αἰαῖ           114
#  7 ἰώ              88
#  8 ἔα              67
#  9 ὤμοι            63
# 10 ἰοὺ             51
# # … with 83 more rows

df %>% group_by(author) %>% count() %>% arrange(desc(n))
# # A tibble: 4 × 2
# # Groups:   author [4]
#   author           n
#   <chr>        <int>
# 1 Aristophanes  1550
# 2 Euripides     1429
# 3 Sophocles      918
# 4 Aeschylus      452


df <- df %>%
  dplyr::filter(interjection != "ὦ")

df %>% group_by(interjection) %>% count() %>% arrange(desc(n))
# # A tibble: 92 × 2
# # Groups:   interjection [92]
#    interjection     n
#    <chr>        <int>
#  1 αὖ             281
#  2 οἴμοι          243
#  3 ἰὼ             233
#  4 φεῦ            165
#  5 αἰαῖ           114
#  6 ἰώ              88
#  7 ἔα              67
#  8 ὤμοι            63
#  9 ἰοὺ             51
# 10 ἆ               50
# # … with 82 more rows

df %>% group_by(author) %>% count() %>% arrange(desc(n))
# # A tibble: 4 × 2
# # Groups:   author [4]
#   author           n
#   <chr>        <int>
# 1 Aristophanes   632
# 2 Euripides      627
# 3 Sophocles      377
# 4 Aeschylus      332


