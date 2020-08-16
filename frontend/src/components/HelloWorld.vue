<template>
  <div class="container-fluid">
      <div class="row no-gutter">
        <div class="d-none d-md-flex justify-content-center col-md-6 col-lg-6 bg-image">
          <div class="card2" style="top: 29vh;"></div>
          <div class="card2">
            <div class="image-skeleton"></div>
          </div>
          <div class="card">
            <div class="image-skeleton"></div>
            <div class="avatar-skeleton"></div>
            <div class="text-skeleton"></div>
            <div class="text-skeleton" style="width: 85%"></div>
            <div class="text-skeleton" style="height: 3%; width: 70%; border-radius: 10em; top: 3em"></div>
          </div>  
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
export default {
  name: 'HelloWorld',
  props: {
    msg: String
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
  

  .card {
    position: relative;
    display: flex;
    height: 500px;
    width: 400px;
    top: 25vh;
    box-shadow: -10px 5px 10px rgba(0, 0, 0, 0.75);
    border-radius: 1.55em;
    border: 0;
    background: linear-gradient(-45deg, #ee0979, #fc4a1a, #2c3e50, #23d5ab);
    background-size: 500% 500%;
    /* transform: rotate(45deg); */
    /* transform-origin: 50% ; */
    animation: swipe 3s ease-in-out forwards infinite;
  }
  .card2 {
    position: fixed;
    display: flex;
    height: 500px;
    width: 400px;
    box-shadow: -10px 5px 10px rgba(0, 0, 0, 0.75);
    border-radius: 1.55em;
    border: 0;
    background:linear-gradient(90deg, #42275a 0%,#734b6d 100% );
    background-size: 500% 500%;
    /* transform: rotate(45deg); */
    /* transform-origin: 50% ; */
    /* animation: swipe 3s ease-in-out forwards infinite; */
    top: 27vh;
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

  

 .image-skeleton {
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

  .avatar-skeleton {
    position: relative;
    display: inline-block!important;
    height: 6.5%;
    width: 8%;
    border-radius: 5em;
    top: 2em;
    left: 2.5%;
    margin-top: 0.5em;
    background-color: rgba(255, 255, 255, 0.5);
    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.75);
  }

  .text-skeleton {
    position: relative;
    display: inline-block!important;
    height: 5%;
    width: 94%;
    border-radius: 1.2em;
    top: 2em;
    left: 2.5%;
    margin-top: 0.5em;
    background-color: rgba(255, 255, 255, 0.5);
    box-shadow: -0px 2px 5px rgba(0, 0, 0, 0.75); 
  }


  .cover{
    display: inline-block;
    height: 1em;
    width: 8ch;
    /* background-color: black; */
    /* z-index: 1; */
  }

  /* .card-heading {
    height: 1rem;
    width: 50%;
    margin: 5px;
    border-radius: 3px;
    color: black;
  } */

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
