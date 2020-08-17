<template>
  <div class="container-fluid">
      <div class="row no-gutter">
        <div class="d-none d-md-flex justify-content-center col-md-6 col-lg-6 bg-image">
          <Card
            top="29vh"
            gradient="linear-gradient(90deg, #141e30 0%,#243b55 100% )" />
          <Card
            top="27vh"
            gradient="linear-gradient(90deg, #42275a 0%,#734b6d 100% )" />
          <Card isAnimated="true"></Card>

        </div>
        
        <div class="col-md-6 col-lg-6">
          <div class="login d-flex align-items-center py-5">
            <div class="container">
              <div class="row">
                <div class="col-md-9 col-lg-8 mx-auto">
                  <div class="jumbotron">
                      <h1 class="display-4">Unsaver</h1>
                      <p class="lead">Clear your Reddit saved posts with a swipe</p>
                      <hr class="my-4">
                      <p>Unsaver for Reddit uses Tinder-like swipe cards to help you browse through your saved posts easily</p>
                      <div class="btn-container">
                          <a class="btn btn-secondary btn-lg btn-white btn-block" href="" role="button">
                            <i class="fab fa-reddit fa-2x fa-fw" style="vertical-align: middle;"></i>
                              <span>Login to Reddit</span></a>
                      </div>
                    </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
import Card from './card.vue'
export default {
  name: 'Login',
  components: {
    Card,
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  
  .bg-image {
    background-image: url('../assets/reddit_snoo.jpg');
    background-size: cover;
    background-position: 20%;
    position: relative; 
    overflow: hidden;
  }
  

  .cover{
    display: inline-block;
    height: 1em;
    width: 8ch;
  }

  .jumbotron {
    background: none;
    text-overflow: ellipsis;
  }

  .login,
  .image {
    min-height: 100vh;
  }
  
  .btn-container {
    text-align: center;
    padding: 10%;
  }
  
  .btn-white {
    background-color: #fff;
    color: black;
    border-radius: 2em;
    font-size: medium;
    text-decoration: none;
  }

  @media (max-width: 1065px) {
    .login {
      font-size: small;
    }
    .btn-white {font-size: small;}
  }
  
  .btn-white:hover {
    background-color: #f83d19;
  }

  i {
    margin-right: 0.2em;
  }

</style>
