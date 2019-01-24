import pymssql
import time
#链接数据库
global sqlIP
global cx
global sVal
sVal=[]
global czk
global cus

sqlIP={}
sqlIP["xgygyy"]="192.168.1.136"
sqlIP["wjbserver"]="192.168.5.110"
sqlIP["zgjhser"]="192.168.6.67"
sqlIP["gqserver"]="192.168.8.251"
sqlIP["zyyserver"]="192.168.186.228"
sqlIP["cnjhser"]="192.168.186.236"


class cxsalm():
    def __init__(self,addIP,servername,misdb,posdb,startDate,endDate):
        self.addIP = addIP
        self.servername = servername
        self.misdb = misdb
        self.posdb = posdb
        self.startDate = startDate
        self.endDate = endDate

        print(self.servername)
    def cxsql(self):
        conn =pymssql.connect(host=self.addIP,user="sa",password='',database=self.misdb)
        cur = conn.cursor()
        cxval =0
        sql=[]
        #设置sql执行语句

        for i in range(23):
            sql.append(i)
        sql[0] = "select * from tSysFunc c where FuncCode='U00095' and (C.Funckind='0' or C.Funckind='1'  or C.Funckind='2' or C.Funckind='5' or C.Funckind='6' )  and ( IsNull(c.AppType,'')='' or IsNull(c.AppType,'')='0')"
        sql[1] = "select QryName from UserReport where qryNo=95"
        sql[2] = "select Sum(IsEnter) as IsEnter from tUserGrp a,tGrpRight b where a.Grpcode=b.GrpCode and UserCode='1002' and b.FuncCode='U00095'"
        sql[3] = "select sum(IsEnter) as IsEnter,sum(IsAdd) as IsAdd,sum(IsEdit) as IsEdit,sum(IsDel) as IsDel, sum(IsQuery) as IsQuery,sum(IsPrint) as IsPrint,sum(IsPrnSet) as IsPrnSet,sum(IsExport) as IsExport, sum(IsCheck) as IsCheck,sum(IsWrite) as IsWrite,sum(IsSpec) as IsSpec from tUserGrp a,tGrpRight b where  a.grpCode=b.GrpCode and a.UserCode='1002' and b.FuncCode='U00095'"
        sql[4] = "select * from tUserDep where DepCode='0' and UserCode='1002'"
        sql[5] = "select QryName,iFrozen,XTitle from UserReport where qryNo=95"
        sql[6] = "select * from  RelativeRpt where qryNo=95"
        sql[7] = "Select * from userReport where QryNo=95"
        sql[8] = "Select QryNo,ParamName,Caption,ParamType,cast(TName as text) as tName, ResultField,ShowField,IsMust,iOrder from UserRptParam where QryNo=95 order by iOrder"
        sql[9] = "select *  from sysobjects where name='up_UserDefine95' and xType='P'"
        sql[10] = "select * from tGridSet where FuncCode='U00095'"
        sql[11] = "select * from tGridSet where FuncCode='U00095'"
        sql[12] = "select * from tColumnSet where FuncCode='U00095' Order by ItemNO"
        sql[13] = "Select * from tLoginInfo where Name='IT02'"
        sql[14] = "select * from ExportScheme where ExPortCode='U00095' order by SerialNo"
        sql[15] = "select c.* from tLinkFunc a,tSysFunc c ,(select d.FuncCode,Sum(IsEnter) as IsEnter from tUserGrp c,tGrpRight d where c.Grpcode=d.GrpCode and UserCode='1002' group by d.FuncCode ) e where  e.IsEnter>0 and c.FuncCode=e.FuncCode and a.FuncCode='U00095' and  a.LinkCode=c.FuncCode and (iNodeCode<>'')   and (iNodeCode<>'YY') and (iNodeCode<>'ZZ') and (iNodeCode<>'XX') and (C.Funckind='0' or C.Funckind='1'  or C.Funckind='2' or C.Funckind='5' or C.Funckind='6' )  and ( IsNull(c.AppType,'')='' or IsNull(c.AppType,'')='0') order by  a.iOrder"
        #sql[16] = "set ansi_nulls on  set ansi_warnings on"
        sql[16] = """if object_id('tempdb..#U000951002') is not null Begin drop table #tempTable  End
                    create table #U000951002(iResult int ) declare @i int exec @i=up_UserDefine95 '1002-A' ,
                    '"""+ self.addIP +"' ,'["+ self.posdb +"]' ,'0' ,'" + self.startDate + "' ,'" + self.endDate + "' ,'' insert into #U000951002 Values(@i)"
        sql[17] =  "select iResult from #U000951002"
        #sql[19] = "set ansi_nulls off set ansi_warnings off"
        sql[18] = "select OptValue from tSysOpt where OptName='EXABEdition'"
        sql[19] = "Select * from tColumnSet where  FuncCode='U00095'"

        for i in range(20):
            if i ==16:
                cur.execute(sql[i])
                run=cur.fetchall()
            else:
                cur.execute(sql[i])

        for i in run:
            cxval = cxval+i[29]
        print("促销收入：{:.2f}".format(cxval))
        cur.close()
        conn.close()
        return cxval
    def czksql(self):
        conn =pymssql.connect(host=self.addIP,user="sa",password='',database=self.misdb)
        cur = conn.cursor()
        czkval =0
        #设置sql执行语句
        sql=[]
        for i in range(23):
            sql.append(i)
        sql[0]="select * from tSysFunc c where FuncCode='U00058' and (C.Funckind='0' or C.Funckind='1'  or C.Funckind='2' or C.Funckind='5' or C.Funckind='6' )  and ( IsNull(c.AppType,'')='' or IsNull(c.AppType,'')='0')"
        sql[1]="select QryName from UserReport where qryNo=58"
        sql[2]="select Sum(IsEnter) as IsEnter from tUserGrp a,tGrpRight b where a.Grpcode=b.GrpCode and UserCode='1002' and b.FuncCode='U00058'"
        sql[3]="select sum(IsEnter) as IsEnter,sum(IsAdd) as IsAdd,sum(IsEdit) as IsEdit,sum(IsDel) as IsDel, sum(IsQuery) as IsQuery,sum(IsPrint) as IsPrint,sum(IsPrnSet) as IsPrnSet,sum(IsExport) as IsExport, sum(IsCheck) as IsCheck,sum(IsWrite) as IsWrite,sum(IsSpec) as IsSpec from tUserGrp a,tGrpRight b where  a.grpCode=b.GrpCode and a.UserCode='1002' and b.FuncCode='U00058'"
        sql[4]="select * from tUserDep where DepCode='0' and UserCode='1002'"
        sql[5]="select QryName,iFrozen,XTitle from UserReport where qryNo=58"
        sql[6]="select * from  RelativeRpt where qryNo=58"
        sql[7]="select * from userReport where QryNo=58"
        sql[8]="select QryNo,ParamName,Caption,ParamType,cast(TName as text) as tName, ResultField,ShowField,IsMust,iOrder from UserRptParam where QryNo=58 order by iOrder"
        sql[9]="select *  from sysobjects where name='up_UserDefine58' and xType='P'"
        sql[10]="select * from tGridSet where FuncCode='U00058'"
        sql[11]="select * from tGridSet where FuncCode='U00058'"
        sql[12]="select * from tColumnSet where FuncCode='U00058' Order by ItemNO"
        sql[13]="select * from tLoginInfo where Name='IT02'"
        sql[14]="select * from ExportScheme where ExPortCode='U00058' order by SerialNo"
        sql[15]="select c.* from tLinkFunc a,tSysFunc c ,(select d.FuncCode,Sum(IsEnter) as IsEnter from tUserGrp c,tGrpRight d where c.Grpcode=d.GrpCode and UserCode='1002' group by d.FuncCode ) e where  e.IsEnter>0 and c.FuncCode=e.FuncCode and a.FuncCode='U00058' and  a.LinkCode=c.FuncCode and (iNodeCode<>'')   and (iNodeCode<>'YY') and (iNodeCode<>'ZZ') and (iNodeCode<>'XX') and (C.Funckind='0' or C.Funckind='1'  or C.Funckind='2' or C.Funckind='5' or C.Funckind='6' )  and ( IsNull(c.AppType,'')='' or IsNull(c.AppType,'')='0') order by  a.iOrder"
        sql[16]="if object_id('tempdb..#U000581002') is not null Begin drop table #tempTable  End"
        sql[17]="""create table #U000581002(iResult int ) declare @k int exec @k=up_UserDefine58 '1002-A'
                    ,'"""+self.addIP+"' ,'["+ self.posdb +"' , '"+self.startDate+"' , '"+self.endDate+"' insert into #U000581002 Values(@k)"
        sql[18]="select iResult from #U000581002"
        sql[19]="select OptValue from tSysOpt where OptName='EXABEdition'"
        sql[20]="select * from tColumnSet where  FuncCode='U00058'"
        for i in range(20):
            if i==17:
                cur.execute(sql[i])
                runs = cur.fetchall()
            else:
                cur.execute(sql[i])

        for i in runs:
            czkval = czkval+i[20]
        print("储值卡消费：{:.2f}".format(czkval))
        cur.close()
        conn.close()
        return czkval

    def possql(self):
        conn =pymssql.connect(host=self.addIP,user="sa",password='',database=self.misdb)
        cur = conn.cursor()
        cusval =0
        sumcount =0
        kll = 0
        #设置sql执行语句
        sql=[]
        for i in range(23):
            sql.append(i)
        sql[0] = "select * from tSysFunc c where FuncCode='U00020'  and (C.Funckind='0' or C.Funckind='1'  or C.Funckind='2' or C.Funckind='5' or C.Funckind='6' )  and ( IsNull(c.AppType,'')='' or IsNull(c.AppType,'')='0')"
        sql[1] = "select QryName from UserReport where qryNo=20"
        sql[2] = " select Sum(IsEnter) as IsEnter from tUserGrp a,tGrpRight b where a.Grpcode=b.GrpCode and UserCode='1002' and b.FuncCode='U00020'"
        sql[3] = "select sum(IsEnter) as IsEnter,sum(IsAdd) as IsAdd,sum(IsEdit) as IsEdit,sum(IsDel) as IsDel,sum(IsQuery) as IsQuery,sum(IsPrint) as IsPrint,sum(IsPrnSet) as IsPrnSet,sum(IsExport) as IsExport,sum(IsCheck) as IsCheck,sum(IsWrite) as IsWrite,sum(IsSpec) as IsSpec from tUserGrp a,tGrpRight b where  a.grpCode=b.GrpCode and a.UserCode='1002' and b.FuncCode='U00020'"
        sql[4] = "select * from tUserDep where DepCode='0' and UserCode='1002'"
        sql[5] = "select QryName,iFrozen,XTitle from UserReport where qryNo=20"
        sql[6] = "select * from  RelativeRpt where qryNo=20"
        sql[7] = "select * from userReport where QryNo=20"
        sql[8] = "Select QryNo,ParamName,Caption,ParamType,cast(TName as text) as tName, ResultField,ShowField,IsMust,iOrder from UserRptParam where QryNo=20 order by iOrder"
        sql[9] = "select *  from sysobjects where name='up_UserDefine20' and xType='P'"
        sql[10] = "select * from tGridSet where FuncCode='U00020'"
        sql[11] = "select * from tColumnSet where FuncCode='U00020' Order by ItemNO"
        sql[12] = "select * from tLoginInfo where Name='"+self.servername+"'"
        sql[13] = "select * from ExportScheme where ExPortCode='U00020' order by SerialNo"
        sql[14] = "select c.* from tLinkFunc a,tSysFunc c ,(select d.FuncCode,Sum(IsEnter) as IsEnter from tUserGrp c,tGrpRight d where c.Grpcode=d.GrpCode and UserCode='1002' group by d.FuncCode ) e where  e.IsEnter>0 and c.FuncCode=e.FuncCode and a.FuncCode='U00020' and  a.LinkCode=c.FuncCode and (iNodeCode<>'')   and (iNodeCode<>'YY') and (iNodeCode<>'ZZ') and (iNodeCode<>'XX') and (C.Funckind='0' or C.Funckind='1'  or C.Funckind='2' or C.Funckind='5' or C.Funckind='6' )  and ( IsNull(c.AppType,'')='' or IsNull(c.AppType,'')='0') order by  a.iOrder"
        sql[15] = "if object_id('tempdb..#U000201002') is not null Begin drop table #tempTable  End"
        sql[16] = """create table #U000201002(iResult int )    declare @i int       exec @i=up_UserDefine20 '1002-A'
                    ,'["""+ self.servername +"]'     ,'["+ self.posdb +"]'     , '历史时段'     , '' , '"+  self.startDate +"'  , '"+ self.endDate +"'    insert into #U000201002 Values(@i) "
        sql[17] = "select iResult from #U000201002"
        sql[18] = "select OptValue from tSysOpt where OptName='EXABEdition'"
        sql[19] = "select * from tColumnSet where FuncCode='U00020'"
        for i in range(20):
            if i==16:
                cur.execute(sql[i])
                r = cur.fetchall()
            else:
                cur.execute(sql[i])

        for k in r:
            cusval +=k[1]
            sumcount+=k[2]
        if cusval != 0:
            kll = round(sumcount/cusval,2)
        else:
            kll = 0
        print("交易次数:{:.2f}".format(cusval))
        print("客单价：{:.2f}".format(kll))
        ck = [cusval] + [kll]
        cur.close()
        conn.close()
        return ck

def run(ip,serverName,startDate,endDate):

    if ip=="gqserver":
        wjb = cxsalm(ip,serverName,"newfdbmis5000","newFDbPos5000",startDate,endDate)
    else:
        wjb = cxsalm(ip,serverName,"fdbmis5000","FDbPos5000",startDate,endDate)

    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    cx = wjb.cxsql()
    czk = wjb.czksql()
    cus = wjb.possql()
    sVal=[cx]+[czk]+cus
    return sVal

