library(rvest)

cars_url <- "https://en.wikipedia.org/wiki/Comma-separated_values"
cars_html <- read_html(cars_url)

table <- html_node(cars_html, ".wikitable")%>%
          html_table()

csv <- write.csv(table, 
          file = "Cars")

