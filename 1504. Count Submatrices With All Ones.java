class Solution {
    public int numSubmat(int[][] mat) {
        int m = mat.length, n = mat[0].length;
        int[][] heights = new int[m][n];
        
        // Step 1: Build histogram heights
        for (int j = 0; j < n; j++) {
            for (int i = 0; i < m; i++) {
                if (mat[i][j] == 0) {
                    heights[i][j] = 0;
                } else {
                    heights[i][j] = (i == 0 ? 1 : heights[i - 1][j] + 1);
                }
            }
        }

        int res = 0;
        
        // Step 2: For each row, count submatrices
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (heights[i][j] > 0) {
                    int minHeight = heights[i][j];
                    // extend leftwards
                    for (int k = j; k >= 0; k--) {
                        if (heights[i][k] == 0) break;
                        minHeight = Math.min(minHeight, heights[i][k]);
                        res += minHeight;
                    }
                }
            }
        }
        
        return res;
    }
}
