<h2><a href="https://leetcode.com/problems/permutation-in-string">567. Permutation in String</a></h2><h3>🟡 Medium</h3><p><strong>Topics:</strong> <code>Hash Table</code> <code>Two Pointers</code> <code>String</code> <code>Sliding Window</code></p><p><strong>Runtime:</strong> 13 ms (beats 84.79%) &nbsp;·&nbsp; <strong>Memory:</strong> 19.5 MB (beats 18.12%)</p><p><em>Solved on 2026-08-01</em></p><hr><p>Given two strings <code>s1</code> and <code>s2</code>, return <code>true</code> if <code>s2</code> contains a <span data-keyword="permutation-string">permutation</span> of <code>s1</code>, or <code>false</code> otherwise.</p>

<p>In other words, return <code>true</code> if one of <code>s1</code>&#39;s permutations is the substring of <code>s2</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;ab&quot;, s2 = &quot;eidbaooo&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> s2 contains one permutation of s1 (&quot;ba&quot;).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;ab&quot;, s2 = &quot;eidboaoo&quot;
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s1.length, s2.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s1</code> and <code>s2</code> consist of lowercase English letters.</li>
</ul>
<hr><h3>Similar Problems</h3><ul><li><a href="https://leetcode.com/problems/minimum-window-substring/">Minimum Window Substring <em>(Hard)</em></a></li><li><a href="https://leetcode.com/problems/find-all-anagrams-in-a-string/">Find All Anagrams in a String <em>(Medium)</em></a></li></ul>