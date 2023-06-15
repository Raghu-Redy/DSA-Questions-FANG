class Solution:
    def printSquare(self, N):
        for i in range(N):
            for j in range(N):
                print("*", end=" ")
            print()

# Example usage
solution = Solution()
N = int(input("Enter the value of N: "))  # Assuming user inputs 5
solution.printSquare(N)
