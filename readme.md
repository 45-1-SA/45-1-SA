# 45-1-SA
"Коллективная разработка приложений"

Корневая директория

main_tasks.py - этот файл запускает процесс преобразования XDB -> RAM -> DBD 

main_prjadm.py - это файл запускает процесс преобразования DBD -> RAM - > XDB2

main_mssql.py - это файл запускает процессы: 

1) генерация описателя по исходной демонстрационной БД в RAM представлении
2) преобразования RAM -> XDB и RAM -> DDL с выводом в консоль ram-представления3)        
3) перенос данных из исходной в целевую БД

Директория modules

xdb_ram - модуль преобразования xml таблиц из xdb файлов в ram-представление.

ram_xdb - модуль преобразования ram представления в xml таблицы в xdb файл.

ram_dbd - модуль преобразования ram представления в sql таблицы в db файл.

dbd_ram - модуль преобразования sql таблиц из db файла в ram представление.

mssql_ram - модуль генерации описателя по исходной демонстрационной БД в RAM представлении.

mssql_postgres - модуль переноса данных из исходной в целевую БД.
