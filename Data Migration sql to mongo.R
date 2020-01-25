library(RSQLite)
library(DBI)
library(mongolite)
library(jsonlite)

# set the directory where your .sqlite file is present.

setwd('C:/Prashant/UTD Semesters/First/Database/Project')
con <- dbConnect(SQLite(),'FPA_FOD_20170508.sqlite')

dbListTables(con)

fires <- dbReadTable(con,'Fires')
fires <- data.table::setDT(fires)
nrow(fires)

#Create a db named Project & collection named fires in mongo db manually before executing
#below commands.

my_collection = mongo(collection = "fires", db = "Project")
fires$Shape <- NULL
my_collection$insert(fires)
my_collection$count()
