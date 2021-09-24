La instalacion de este script requiere la existencia de un DASD particular asignado para el trabajo: DINO01

Generé un PDS COVID19.SRC.COBOL y otro para COVID19.LINKLIB con el archivo ALLOPDS_covid19

Transferí como members de COVID19.SRC.COBOL TOTCNTRY y REPCNTRY a través del sistema de transferencia de archivos de c3270

Hice submit de ambos archivos anteriores, los que se compilaron y se transfirieron a COVID19.LINKLIB

Generé los PS siguientes con el archivo ALLOPS_covid19
COVID19.DATA.DAILY    
COVID19.DATA.TOTCNTRY 
COVID19.DATA.TOTCPREV 
