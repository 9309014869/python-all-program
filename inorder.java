import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;

    public TreeNode(int val) {
        this.val = val;
        this.left = this.right = null;
    }
}

public class Main {

    public static TreeNode buildTreeInorderPreorder(int[] preorder, int preStart, int preEnd, int[] inorder, int inStart, int inEnd, Map<Integer, Integer> hm) {
        if (preStart > preEnd || inStart > inEnd) {
            return null;
        }

        TreeNode root = new TreeNode(preorder[preStart]);
        int inRoot = hm.get(preorder[preStart]);
        int numLeft = inRoot - inStart;

        root.left = buildTreeInorderPreorder(preorder, preStart + 1, preStart + numLeft, inorder, inStart, inRoot - 1, hm);
        root.right = buildTreeInorderPreorder(preorder, preStart + numLeft + 1, preEnd, inorder, inRoot + 1, inEnd, hm);

        return root;
    }

    public static TreeNode buildTree(int[] inorder, int[] preorder) {
        Map<Integer, Integer> hm = new HashMap<>();
        for (int i = 0; i < inorder.length; i++) {
            hm.put(inorder[i], i);
        }
        return buildTreeInorderPreorder(preorder, 0, preorder.length - 1, inorder, 0, inorder.length - 1, hm);
    }

    public static void main(String[] args) {
        int[] inorder = {40, 20, 50, 10, 60, 30};
        int[] preorder = {10, 20, 40, 50, 30, 60};

        TreeNode root = buildTree(inorder, preorder);

        // You can perform operations on the 'root' here
    }
}
