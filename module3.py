
def batting_point(x):
    ans={}
    points=0
    strike_rate=0
    ans["name"]=x["name"]
    cent=0
    if (x["runs"]>=100):
        cent=cent+10
    if (x["runs"]>=50):
        cent=cent+5
    if ((100*x["runs"]/x["balls"])>100):
        strike_rate=4
    elif ((100*x["runs"]/x["balls"])>=80 and (100*x["runs"]/x["balls"])<=100):
        strike_rate=2
    points=points+cent+strike_rate+x["4"]+x["6"]*2+10*x["field"]+x["runs"]/2
    ans["batscore"]=points
    return ans

def bowling_point(x):
    ans={}
    points=0
    wkt_point=0
    eco=0
    ans["name"]=x["name"]
    if(x["wkts"]>=5):
        wkt_point=10
    elif(x["wkts"]>=3):
        wkt_point=5
    if((x["runs"]/x["overs"])<=2):
        eco=10
    elif((x["runs"]/x["overs"])<=3.5 and (x["runs"]/x["overs"])>2):
        eco=7
    elif((x["runs"]/x["overs"])<=4.5 and (x["runs"]/x["overs"])>3.5):
        eco=4
    points=points+10*x["wkts"]+wkt_point+eco+10*x["field"]
    ans["bowlscore"]=points
    return ans



        
