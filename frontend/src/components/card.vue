<template>
  <div class="card" :class="{anim: isAnimated}" :style="{'top': top, 'background': gradient}">
    <div class="skeleton"></div>
    <div class="skeleton avatar"></div>
    <div class="skeleton text"></div>
    <div class="skeleton text" style="width: 85%"></div>
    <div class="skeleton text" style="height: 5%; width: 70%; top: 3em"></div>
  </div>
</template>

<script>


export default {
    name: 'Card',
    props: {
        isAnimated: Boolean,
        top: String,
        gradient: String,
    },
    components: {
    }
}
</script>

<style scoped>
.card {
    position: fixed;
    display: flex;
    height: 500px;
    width: 400px;
    top: 25vh;
    box-shadow: -10px 5px 10px rgba(0, 0, 0, 0.75);
    border-radius: 1.55em;
    border: 0;
    background: linear-gradient(-45deg, #ee0979, #fc4a1a, #2c3e50, #23d5ab);
    background-size: 500% 500%;  
}

.anim {
    position: relative;
    animation: swipe 3s ease-in-out forwards infinite;
}


@keyframes swipe {
    0% {
      transform: rotate(12deg);
      left: 6em;
      background-position: 0% 50%;
    }
    50% {
      transform: rotate(-6deg);
      left: -3em;
      background-position: 100% 50%;
    }
    100% {
      transform: rotate(12deg);
      left: 6em;
      background-position: 0% 50%;
    }
  }

  .skeleton {
        position: relative;
        display: inline-block!important;
        height: 50%;
        width: 95%;
        border-radius: 1.3em;
        left: 2.5%;
        top: 0.5em;
        background-color: rgba(255, 255, 255, 0.5);
        box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.75); 
  }

  .avatar {
    height: 6.5%;
    width: 8%;
    border-radius: 5em;
    top: 2em;
    margin-top: 0.5em;
  }

  .text {
    height: 5%;
    width: 94%;
    border-radius: 1.2em;
    top: 2em;
    margin-top: 0.5em;
  }

</style>