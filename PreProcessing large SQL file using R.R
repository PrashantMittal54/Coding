library(RSQLite)
library(DBI)
getwd()
setwd('C:/Prashant/UTD Semesters/First/Database/Project')
con <- dbConnect(SQLite(),'FPA_FOD_20170508.sqlite')

dbListTables(con)

fires <- dbReadTable(con,'Fires')
fires <- data.table::setDT(fires)
nrow(fires)
nwcg <- dbReadTable(con, 'NWCG_UnitIDActive_20170109')
nwcg <- data.table::setDT(nwcg)


#library(R)
library(RMySQL)
#library(pool)
dbDisconnect(con)
nrow(fires)
class(fires)
con2 <- dbConnect(RMySQL::MySQL(), user = "root", password = "root", host = "127.0.0.1",
                  dbname = 'temp', port = 3306)
dbListTables(con2)
head(fires)
write.table(Identi2,file="tmp1.txt", fileEncoding ="utf8")
idf3 <- read.table(file="tmp1.txt",encoding="utf8", na.strings = "NA", fill = TRUE)
idf3 <- data.table::setDT(idf3)
fires1$Shape <- NA
head(idf3)
str(idf3)
idf3$FPA_ID <- as.character(idf3$FPA_ID)
idf3$Source_Reporting_Unit <- as.character(idf3$Source_Reporting_Unit)
idf3$NWCG_Unit_ID <- as.character(idf3$NWCG_Unit_ID)
unique(Identi2$Source_Reporting_Unit)
dbWriteTable(con2, 'idf', idf3, append = TRUE, row.names = FALSE)
dbWriteTable(con2, 'NWCG_UnitIDActive_20170109', nwcg, append = TRUE, row.names = FALSE)

poolClose(con2)
