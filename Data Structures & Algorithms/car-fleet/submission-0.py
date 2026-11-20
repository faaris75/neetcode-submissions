class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # If the car reaches the target at the same time as the car infront than that is one fleet if the remaining cars can't finish at the same time then they are different fleets
        # To find if they reach the target at the same time we need to see the remaining distance left for car[i] and car[i+1] and find the time needed to reach the target using (Distance remaining)/(speed) = Time

        # Pair (position, speed) and sort from closest to target to farthest
        cars = sorted(zip(position, speed), reverse=True)
        stack = []  # Stores arrival times of each distinct fleet

        for pos, spd in cars:
            time = (target - pos) / spd
            # Only push a new fleet if this car takes longer than the fleet ahead
            if not stack or time > stack[-1]:
                stack.append(time)

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