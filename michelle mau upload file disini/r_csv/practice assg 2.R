install.packages("rvest")
library(rvest)

car_link <- "https://en.wikipedia.org/wiki/Comma-separated_values"
car_html <- read_html(car_link)

table <- html_nodes(car_html, ".wikitable") %>%
          html_table()

csv <- write.csv(table, file = "Cars")
read.csv("Cars")