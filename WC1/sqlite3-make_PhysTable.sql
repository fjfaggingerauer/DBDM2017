CREATE TABLE IF NOT EXISTS PhysTable (Name varchar(10),
			 T_eff INT,
			 FeH FLOAT );
			 

.separator ,
.import PhysTable.dat PhysTable
