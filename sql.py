import pymssql
import re
#链接数据库
conn =pymssql.connect(host="192.168.186.236",user="sa",password='',database='fdbmis5000')
cur = conn.cursor()
#设置sql执行语句
sql =[]
for i in range(21):
    sql.append(i)
sql[0] = """select * from tSysFunc c
            where FuncCode='U00085'
            and (C.Funckind='0' or C.Funckind='1'  or C.Funckind='2' or C.Funckind='5' or C.Funckind='6' )  and ( IsNull(c.AppType,'')='' or IsNull(c.AppType,'')='0')"""
sql[1] = "select QryName from UserReport where qryNo=85 "
sql[2] = "select Sum(IsEnter) as IsEnter from tUserGrp a,tGrpRight b where a.Grpcode=b.GrpCode and UserCode='1002' and b.FuncCode='U00085'"
sql[3] = """select sum(IsEnter) as IsEnter,sum(IsAdd) as IsAdd,sum(IsEdit) as IsEdit,sum(IsDel) as IsDel,
            sum(IsQuery) as IsQuery,sum(IsPrint) as IsPrint,sum(IsPrnSet) as IsPrnSet,sum(IsExport) as IsExport,
            sum(IsCheck) as IsCheck,sum(IsWrite) as IsWrite,sum(IsSpec) as IsSpec
            from tUserGrp a,tGrpRight b
            where  a.grpCode=b.GrpCode
            and a.UserCode='1002' and b.FuncCode='U00085' """
sql[4] = "select * from tUserDep where DepCode='0' and UserCode='1002'"
sql[5] = "select QryName,iFrozen,XTitle from UserReport where qryNo=85"
sql[6] = "select * from  RelativeRpt where qryNo=85"
sql[7] = "Select * from userReport where QryNo=85"
sql[8] = """Select QryNo,ParamName,Caption,ParamType,cast(TName as text) as tName,
            ResultField,ShowField,IsMust,iOrder from UserRptParam
            where QryNo=85
            order by iOrder """
sql[9] = "select *  from sysobjects  where name='up_UserDefine85' and xType='P' "
sql[10] = "select * from tGridSet where FuncCode='U00085' "
sql[11] = "select * from tColumnSet where FuncCode='U00085' Order by ItemNO "
sql[12] = "Select * from tLoginInfo where Name='IT02' "
sql[13] = "select * from ExportScheme where ExPortCode='U00085'order by SerialNo "
sql[14] = """select c.* from tLinkFunc a,tSysFunc c
            ,(select d.FuncCode,Sum(IsEnter) as IsEnter from tUserGrp c,tGrpRight d
            where c.Grpcode=d.GrpCode and UserCode='1002'
            group by d.FuncCode ) e
            where  e.IsEnter>0 and c.FuncCode=e.FuncCode
            and a.FuncCode='U00085' and  a.LinkCode=c.FuncCode
            and (iNodeCode<>'')   and (iNodeCode<>'YY')
            and (iNodeCode<>'ZZ') and (iNodeCode<>'XX')
            and (C.Funckind='0' or C.Funckind='1'  or C.Funckind='2' or C.Funckind='5' or C.Funckind='6' )  and ( IsNull(c.AppType,'')='' or IsNull(c.AppType,'')='0')
            order by  a.iOrder """
sql[15] = "set ansi_nulls on  set ansi_warnings on "
sql[16] = """create table #U000851002(iResult int )
             declare @i int
             exec @i=up_UserDefine85 '1002-A'
            ,'[192.168.186.236]'
            ,'[fdbpos5000]'
            , '-1'
            , '0'
            , '2018-12-01'
            , '2018-12-18'
             insert into #U000851002 Values(@i)
            """
sql[17] = "select iResult from #U000851002"
sql[18] = "set ansi_nulls off  set ansi_warnings off "
sql[19] = "select OptValue from tSysOpt where OptName='EXABEdition'"
sql[20] = "Select * from tColumnSet where FuncCode='U00085'"
sql.insert(0,"if object_id('tempdb..#U000851002') is not null Begin drop table #tempTable  End  ;")
#去除sql列表中的换行符‘\n’
lis = []
for i in range(22):
    print(i)
    s = re.sub('[\n]','',sql[i])
    lis.append(s)
print(lis[16:22])
for i in range(22):

    cur.execute(sql[i])

    print("正在执行第"+str(i)+"条语句")
    if i == 22:
        print("sql语句执行完成")

#cur.execute("select * from [FDbMis5000].[dbo].[DepItem]")
#print(cur.fetchmany(19))
print(cur.fetchall())
cur.close()
conn.close()
