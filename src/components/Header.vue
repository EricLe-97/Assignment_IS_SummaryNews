<template>
    <div id="header">
        <img src="../assets/ai.jpeg">
        <h3 class ="center"> News Summary </h3>
    </div>
</template>

<script>
export default {
    name:'Header',
    mounted(){
    //     this.$nextTick(function(){
    //     window.addEventListener("scroll", function(){
    //       var navbar = document.getElementById("nav");
    //       var nav_classes = navbar.classList;
    //       if(document.documentElement.scrollTop >= 150) {
    //         if (nav_classes.contains("shrink") === false) {
    //           nav_classes.toggle("shrink");
    //         }
    //       }
    //       else {
    //         if (nav_classes.contains("shrink") === true) {
    //           nav_classes.toggle("shrink");
    //         }
    //       }
    //     })
    //   })

        window.onscroll = function() {scrollFunction()};

        function scrollFunction() {
        if (document.body.scrollTop > 10 || document.documentElement.scrollTop > 10) {
            document.getElementById("header").style.height = "5%";
            // document.getElementById("logo").style.fontSize = "25px";
        } else if (document.body.scrollTop < 100 || document.documentElement.scrollTop < 100) {
            document.getElementById("header").style.height = "100%";
            // document.getElementById("logo").style.fontSize = "35px";
        }
        }
                
    }
}
</script>

<style scoped>
    #header{
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        animation-direction: alternate;
        animation:fadein 2s linear;
        /* margin-bottom: 100px; */
        align-items: center;
        position: relative;
        margin-bottom: 50px;
        height: 100%;
        transition: 0.15s all ease-in-out;
        
    }
    @keyframes fadein {
        from{opacity: 0;direction: ltr;top: -1000px;}
        to{opacity: 1;direction: ltr;top:0;}
    }
    #header img{
        box-sizing: border-box;
        height: 100%;
        width: 90%;
        margin: auto;
        display: block;
        margin-left: auto;
        margin-right:auto;
    }
    .center{
        position: absolute;
        top:0%;
        left: 45%;
        color: antiquewhite;
    }

</style>