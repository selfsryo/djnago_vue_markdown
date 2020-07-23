<template>
  <section class="container">
    <article v-for="post of posts" :key="post.id">
      <h2 class="post-title">{{post.title}}</h2>
      <p class="post" v-html="post.main_text"></p>
			<hr>
    </article>
  </section>
</template>

<script>
import hljs from "highlight.js"

export default {
  name: "post",
  data() {
    return {
      posts: []
    };
  },
  mounted() {
    this.$http(this.$getPosts)
      .then(response => response.json())
      .then(data => (this.posts = data));
	},
	updated(){
		this.updateCodeSyntaxHighlighting()
	},
  methods: {
    updateCodeSyntaxHighlighting() {
      document.querySelectorAll("pre code").forEach(block => {
        hljs.highlightBlock(block);
      });
    }
  }
};
</script>
<style scoped>
	article {
		margin-bottom: 100px;
	}
</style>
