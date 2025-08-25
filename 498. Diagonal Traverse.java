class Solution {
    public int[] findDiagonalOrder(int[][] mat) {
        if (mat == null || mat.length == 0) return new int[0];
        
        int m = mat.length, n = mat[0].length;
        int[] result = new int[m * n];
        int r = 0, c = 0;
        
        for (int i = 0; i < result.length; i++) {
            result[i] = mat[r][c];
            
            // If (r + c) is even → moving up
            if ((r + c) % 2 == 0) {
                if (c == n - 1) {  // last column → move down
                    r++;
                } else if (r == 0) { // top row → move right
                    c++;
                } else {  // move up-right
                    r--;
                    c++;
                }
            } 
            // If (r + c) is odd → moving down
            else {
                if (r == m - 1) {  // last row → move right
                    c++;
                } else if (c == 0) { // first column → move down
                    r++;
                } else {  // move down-left
                    r++;
                    c--;
                }
            }
        }
        return result;
    }
}
