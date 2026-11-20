class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # If the car reaches the target at the same time as the car infront than that is one fleet if the remaining cars can't finish at the same time then they are different fleets
        # Pair (position, speed) and sort from closest to target to farthest

        pair = [[p,s] for p,s in zip(position,speed)]
        stack = []

        for p,s in sorted(pair)[::-1]: #This just reverses sorting
            stack.append((target-p)/s)
            if len(stack)>= 2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)
        

        '''stack = [0] * len(position)
        for i, pos in enumerate(position):
            d_remaining = target - pos
            time = d_remaining / speed[i]
            stack[i] = time
            if stack[i] == stack[-1]:
                stack.pop()
            else:
                continue
        return len(position)
        '''