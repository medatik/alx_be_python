#marks = [15,16,17,14,11,16,14]
#marks = [15,2,9,14,11,6,4,12,13,3,15,2,3,6,15]
marks = [15,2,19,14,11,6,14,15,17,9]

def output (marks) :
    x = 0
    i = 0
    som = 0
    avg = 0
    good = 0


    for mark in marks :
        som += mark
        i += 1

    avg = som / i
    
    match avg :
        case _ if avg < 10 :
            print(f"ach had no9ta? wakha tkoun 7mar matjibch {avg}")
            print("ach had no9at dyal walou")
        case _ :
            print(f"tbarkllah 3lik istamir! {avg} rah no9ta mzyana")
            print("no9at mzyanin")

    for mark in marks :
        if mark >= 10 :
            if x == 0 :
                print(f"lwla mzyana, {mark} nadya")
            elif x == 1 :
                print(f"mazal {mark} rah mzyana")
            else :
                print(f"lli wraha, {mark} 7ta hiya mzyana")
            x = 2
            good += 1
            
        else :
            if x == 0 :
                print(f"ghir lbdya katbyn lik, {mark} 7ta hiya no9ta? allah y3tina wjhek")
            elif x == 1 :
                print(f"{mark} 7ta hiya nfs chay2, sir 7fad lik chwiya")
            else :
                print(f"wlakin hadi: {mark}, chnahiya hadi wach mn niytek?")
            x = 1
            good -= 1
            

    if avg < 10 :
        print("iwa ach ghadi ngoulik sir khdem 3la rasek")
    elif avg >= 10 and good == i :
        print("rak nadi istamir")
    elif avg >= 10 and good != i :
        print("3al l3oumoum mzyan, wlakin khassek tkhdem 3la rasek")

output(marks)
        
