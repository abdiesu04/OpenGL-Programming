from collections import deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    
    results = []
    
    for _ in range(t):
        present = set()
        rec_act = deque()
        seq = {}
        
        n = int(data[index])
        m = int(data[index + 1])
        index += 2
        
        for i in range(n, 0, -1):
            rec_act.append(i)
            present.add(i)
            seq[i] = -1
        
        remove_time = 0
        
        for i in range(m):
            post = int(data[index])
            index += 1
            remove_time += 1
            
            if post not in present:
                front_post = rec_act.popleft()
                seq[front_post] = remove_time
                present.remove(front_post)
                
                present.add(post)
                rec_act.append(post)
        
        result = ' '.join(str(seq[i]) for i in range(1, n + 1))
        results.append(result)
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()
