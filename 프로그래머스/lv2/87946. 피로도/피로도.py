# permutations= 순열, 서로 다른 n개의 원소에서 r개를 중복없이 순서에 상관있게 선택
from itertools import permutations 

def solution(k, dungeons):
    # 최대 던전 수
    max_count=0
    
    for p in list(permutations(dungeons, len(dungeons))):
        hp= k
        count=0
        
        for minimum, consume  in p:
            if hp < minimum:
                break
            else:
                hp-=consume
                count+=1
        if count > max_count:
            max_count= count
    return max_count
            
            
