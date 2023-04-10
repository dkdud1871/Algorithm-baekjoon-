def solution(answers):
    num1=[1,2,3,4,5]
    num2=[2,1,2,3,2,4,2,5]
    num3=[3,3,1,1,2,2,4,4,5,5]
    answer = []
    score=[0]*3
    
    for i in range(len(answers)):
        if answers[i]== num1[i%5]:
            score[0]+=1
        if answers[i]== num2[i%8]:
            score[1]+=1
        if answers[i]== num3[i%10]:
            score[2]+=1
            
    for j in range(len(score)):
        if score[j]== max(score):
            answer.append(j+1)
    return answer