<h2><a href="https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion">Maximum Unique Subarray Sum After Deletion</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>You are given an integer array <code>nums</code>.</p>

<p>You are allowed to delete any number of elements from <code>nums</code> without making it <strong>empty</strong>. After performing the deletions, select a <span data-keyword="subarray-nonempty">subarray</span> of <code>nums</code> such that:</p>

<ol>
	<li>All elements in the subarray are <strong>unique</strong>.</li>
	<li>The sum of the elements in the subarray is <strong>maximized</strong>.</li>
</ol>

<p>Return the <strong>maximum sum</strong> of such a subarray.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,4,5]</span></p>

<p><strong>Output:</strong> <span class="example-io">15</span></p>

<p><strong>Explanation:</strong></p>

<p>Select the entire array without deleting any element to obtain the maximum sum.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,0,1,1]</span></p>

<p><strong>Output:</strong> 1</p>

<p><strong>Explanation:</strong></p>

<p>Delete the element <code>nums[0] == 1</code>, <code>nums[1] == 1</code>, <code>nums[2] == 0</code>, and <code>nums[3] == 1</code>. Select the entire array <code>[1]</code> to obtain the maximum sum.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,-1,-2,1,0,-1]</span></p>

<p><strong>Output:</strong> 3</p>

<p><strong>Explanation:</strong></p>

<p>Delete the elements <code>nums[2] == -1</code> and <code>nums[3] == -2</code>, and select the subarray <code>[2, 1]</code> from <code>[1, 2, 1, 0, -1]</code> to obtain the maximum sum.</p>
</div>



*how to solve*
<p> Sum all unique positive numbers in the array.

If no positive numbers exist, pick the maximum number in the array (could be zero or negative).

This sum is the maximum achievable sum of a unique subarray after any allowed deletions.</p>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
</ul>
