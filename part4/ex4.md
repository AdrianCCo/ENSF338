1. Go left and look at the number of each room. Then stop until I find the room I want to find.

2. It would take 15 steps and each steps means to check each room to see if it is EY128

3. This is an average case scenario  

4. The worst case would be if the desired room was the first room on the right (EY 138) and the best case scenario would be the first room on the left (EY100).

5. Since we know the rooms are sorted and rooms are sorted out in a loop. I would first check for the edge 
cases by either going right first or left first depending on if number of the room is near 100 or 138, then go near 
the midpoint of the middle room (EY118) and the first rooms (EY100 | EY138) since I know the rooms are sorted. Then
continue to find midpoint depending on if the value of the midpoint room is less than, equal to, or greater than the
room we are looking for. 

