import module3 as ManOfTheMatch
p1={"name":"virat kohli" , "role":"bat" , "runs":112 , "4":10 , "6":0 , "balls":119 , "field":0}
p2={"name":"du plessis" , "role":"bat" , "runs":120 , "4":11 , "6":2 , "balls":112 , "field":0}
p3={"name":"bhuvneshwar kumar" , "role":"bowl" , "wkts":1, "overs":10 , "runs":71 , "field":1}
p4={"name":"yezvendra chahal" , "role":"bowl" , "wkts":2, "overs":10 , "runs":45 , "field":0}
p5={"name":"kuldip yadav" , "role":"bowl" , "wkts":3, "overs":10 , "runs":34 , "field":0}
top1={}
top2={}
nextp1={}
nextp2={}
top1=ManOfTheMatch.batting_point(p1)
top2=ManOfTheMatch.bowling_point(p3)
list=[p1,p2,p3,p4,p5]
for i in list:
    if (i["role"]=="bat"):
        nextp1=ManOfTheMatch.batting_point(i)
        print(nextp1)
        if top1["batscore"]<nextp1["batscore"]:
            top1=nextp1
    elif (i["role"]=="bowl"):
        nextp2=ManOfTheMatch.bowling_point(i)
        print(nextp2)
        if top2["bowlscore"]<nextp2["bowlscore"]:
            top2=nextp2

if top1["batscore"]>top2["bowlscore"]:
    print("top palyer amongst the 5 given player is {} and his total points are {}".format(top1["name"],top1["batscore"]))
