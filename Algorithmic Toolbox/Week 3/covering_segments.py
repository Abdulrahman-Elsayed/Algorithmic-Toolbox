# Uses python3
import sys

def segment_covered(segments):
    points = []
    segments = sorted(segments, key=lambda item:item[1])    
    
    while len(segments):
        b = segments[0][1]
        points.append(b)
        
        while len(segments):
            segment = segments[0]
            
            if b in range(segment[0], segment[1] + 1):
                segments.remove(segment)
            else:
                break
                     
    return points 
    
    
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = []
    for i in range(n):
        segments.append([data[2 *i], data[2 * i + 1]])
        
    points = segment_covered(segments)
    
    print(len(points))
    print(*points)