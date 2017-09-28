CREATE TABLE IF NOT EXISTS MagTable (Name varchar(10),
			 ra varchar(10),
			 Dec varchar(10),
		   	 B FLOAT, 
			 R FLOAT);
			 

.separator ,
.import MagTable.dat MagTable
