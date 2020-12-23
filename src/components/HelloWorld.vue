<template>
  <div class ="link-input">
    <input class ="input-holder" v-on:keyup="test" placeholder="Type your link for me to process . . . . ." v-model="link">
    <button type="button" v-on:click="send_link"  > K-mean process </button>
    <modal name="kmean">
      <h1> K-mean model process </h1>
      {{this.kmean}}</modal>
  </div>
  <!-- <div class="hello">
    <h1>{{ msg }}</h1>
    <p>
      For a guide and recipes on how to configure / customize this project,<br>
      check out the
      <a href="https://cli.vuejs.org" target="_blank" rel="noopener">vue-cli documentation</a>.
    </p>
    <h3>Installed CLI Plugins</h3>
    <ul>
      <li><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-babel" target="_blank" rel="noopener">babel</a></li>
      <li><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-eslint" target="_blank" rel="noopener">eslint</a></li>
    </ul>
    <h3>Essential Links</h3>
    <ul>
      <li><a href="https://vuejs.org" target="_blank" rel="noopener">Core Docs</a></li>
      <li><a href="https://forum.vuejs.org" target="_blank" rel="noopener">Forum</a></li>
      <li><a href="https://chat.vuejs.org" target="_blank" rel="noopener">Community Chat</a></li>
      <li><a href="https://twitter.com/vuejs" target="_blank" rel="noopener">Twitter</a></li>
      <li><a href="https://news.vuejs.org" target="_blank" rel="noopener">News</a></li>
    </ul>
    <h3>Ecosystem</h3>
    <ul>
      <li><a href="https://router.vuejs.org" target="_blank" rel="noopener">vue-router</a></li>
      <li><a href="https://vuex.vuejs.org" target="_blank" rel="noopener">vuex</a></li>
      <li><a href="https://github.com/vuejs/vue-devtools#vue-devtools" target="_blank" rel="noopener">vue-devtools</a></li>
      <li><a href="https://vue-loader.vuejs.org" target="_blank" rel="noopener">vue-loader</a></li>
      <li><a href="https://github.com/vuejs/awesome-vue" target="_blank" rel="noopener">awesome-vue</a></li>
    </ul>
  </div> -->
</template>

<script>
import Vue from 'vue'
import VModal from 'vue-js-modal'
Vue.use(VModal,{})
import axios from 'axios'
export default {
  name: 'HelloWorld',
  data(){
    return{
      link:'',
      kmean:'',
    }
  },
  // mounted(){
  //   if (this.link){
  //     this.$modal.show('example')
      
  //   }
  // },
  methods:{
    test  (e)  {
      if (e.keyCode === 13) {
        this.log += e.key;
        axios.post('http://127.0.0.1:5000/api',{
          url:this.link
        })
        .then((res)=>{
          this.kmean = res.data.kmean;
          this.$modal.show('kmean')
          console.log(this.$modal);
        })
        .catch((err)=>console.log(err));
      }
      // } else if (e.keyCode === 50) {
      //   alert('@ was pressed');
      // }      
      
    },
    send_link(){
      axios.post('http://127.0.0.1:5000/api',{
          url:this.link
        })
        .then((res)=>{
          this.kmean = res.data.kmean;
          this.$modal.show('kmean')
        })
        .catch((err)=>console.log(err));
    }
  },
  
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.link-input{
  display:flex;
  box-sizing: border-box;
  width:100%;
  height: 100px;
  border: 2px solid black;
}
input {
  display: block;
  margin-left: auto;
  margin-right:auto;
  width:80%;
  height:30%;
  
  padding: 4px 12px;
  color: rgba(0,0,0,.70);
  border: 1px solid rgba(0,0,0,.12);
  transition: 1s all linear;
  background: white;

}
button{
  height:40%;
  width: 10%;
  float:right;

}
</style>
