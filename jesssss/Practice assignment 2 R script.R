#st2195 assignment 2, scraping from web

install.packages("rvest")
library(rvest)
library(dplyr)

cars_link <- "https://en.wikipedia.org/wiki/Comma-separated_values"
cars_html <- read_html(cars_link)

table <- html_node(cars_html, ".wikitable") %>%
  html_table()

write.csv(table, file = "Cars")

read.csv("Cars")

