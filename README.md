Count the number of islands on a two dimensional grid. 1 is land: 0 is water.
Any land connected horizontally or vertically belongs to the same Island.

![alt text](image.png)

https://www.youtube.com/shorts/M657SIxKJj8

The main idea of my solution is to mark any Island that you have visited with a sign. If you visit it again, the sign will tell you that you have been here before. Therefore, you will not count the island twice. As soon as you find a patch of land without a sign, you can raise the count for the number of islands. I chose as a sign a negative numbers, such that it is not confused with an unknown Island or water. The first encountered island gets -1, the second -2 ,...

A separate recursive function detects all patches of land connected to a patch that you have discovered and thus constitute an Island. 

I know that the recursion depth is limited in python and I can probably find an equivalent solution with a while loop, but this was my first grasp of the problem. It's really nice that the array is altered while looping through it's elements such that the islands counts are visible after completing the algorithm.