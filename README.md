
<!DOCTYPE html>
<html lang="en">
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Silent Library </title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
  <style>
    /* Remove the navbar's default margin-bottom and rounded borders */ 
    .navbar {
      margin-bottom: 0;
      border-radius: 0;
      /* text-align: center;
      position: fixed !important;
     */
    }

  
    /* Set height of the grid so .sidenav can be 100% (adjust as needed) */
    .row.content {height: 450px}
    
    /* Set gray background color and 100% height */
    .sidenav {
      padding-top: 20px;
      background-color: #f1f1f1cb;
      height: 100%;
     
    }
    
    /* Set black background color, white text and some padding */
    footer {
      background-color: #555;
      color: white;
      padding: 15px;
    }
    
    /* On small screens, set height to 'auto' for sidenav and grid */
    @media screen and (max-width: 767px) {
      .sidenav {
        height: auto;
        padding: 15px;
       
      }
      .row.content {height:auto;} 
    }
     .carousel-inner img {
      width:100%;
      /* Set width to 100%  */
       margin: auto;
       
       min-height: 200px;
   } 

  /* Hide the carousel text when the screen is less than 600 pixels wide */
    @media (max-width: 600px) {
    .carousel-caption {
      display: none; 
    }
      } 
   
  .blink {
                animation: blinker 5s linear infinite;
                /* color: rgba(233, 218, 6, 0.788); */
                font-family: sans-serif;
            }

            @keyframes blinker {
                50% {
                    opacity: 0;
                }
            }
  </style>
</head>

<body>
  <script>
    var text = document.getElementById("demo");
    //text.innerHT Pradhusha";
   
  </script>
<nav class="navbar navbar-inverse navbar-fixed-top">
  <div class="container-fluid">
    <div class="navbar-header">
      
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>          
      </button>
      
    </div>
    <div class="collapse navbar-collapse" id="myNavbar" >
       
            <ul class="nav navbar-nav">
            <li class="blink"> 
              <a href="Home.html">
              <img src="images/si5.jpg" height="50px" width="80px">
              
            </a>
            </li> 
       
          </ul>
           
       
     <ul></ul>
           <ul class="nav navbar-nav">
             
        <li ><a href="Home.html"><H5>Home </H5></a></li>
        
        <li><a href="Booklist.html"><H5> Books List </H5></a></li>
        <li><a href="Eventsandpro.html"><H5> Events And Promotions </H5></a></li>
        <li><a href="Sitemap.html"><H5> Sitemap </H5></a></li>

        <li><a href="Contact.html"><H5> Contact </H5></a></li>
        <li><a href="Privacy.html"><H5> Privacy Policy </H5></a></li>
        
      </ul>
      <ul></ul>
      <ul class="nav navbar-nav navbar-right">
        <li><a href="login.html"><span class="glyphicon glyphicon-log-in" ></span> Login</a></li>
      </ul>
      
      <form class="navbar-form navbar-right" role="search" id="myInput" action="/Booklist.html">
       
        <div class="form-group input-group">
         <ul><li >
          <input type="search" class="form-control" placeholder="Search Books.." id="sls" name="sls">
          <span class="input-group-btn">
            <button class="btn btn-default" type="button" onclick = "document.getElementById('demo').innerHTML = '<---------------Oops! Sorry @ This book is not available right now !Click me to close this popup----------->'">
              
              <span class="glyphicon glyphicon-search"></span>
              
            </button>
            
          </span>        
        </div>
      </form>
      
    </div>
    
  </div>
  <a href="Home.html">
    <p style="color: turquoise; background-color: tomato; font-size:medium"  align="center" id="demo" >
  </p></a>
  
</nav>

 <div id="myCarousel" class="carousel slide" data-ride="carousel">
    <!-- Indicators  -->
    <ol class="carousel-indicators">
      <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
      <li data-target="#myCarousel" data-slide-to="1"></li>
      <li data-target="#myCarousel" data-slide-to="2"></li>
      <li data-target="#myCarousel" data-slide-to="3"></li>
      <li data-target="#myCarousel" data-slide-to="4"></li>
    </ol> 

    <!-- Wrapper for slides -->
     <div class="carousel-inner" role="listbox">
      <div class="item active" >
      <A HREF="booksdetails.html"><img src="images/image-1250x380 (2).jpg" ></A>
        <div class="carousel-caption">
                  
         <h3>Main Hall</h3>
          <p>Read in peace, learn with focus</p>
          
        </div>      
      </div> 

      <div class="item">
        <A HREF="booksdetails.html">
          <!-- <font color="red" size="4">Book Shelf</font> -->
          <img src="images/image-1250x380 (1).jpg"  ></a>
        <div class="carousel-caption"  >
         
          
          <h3>BookShelf</h3>
          <p>Read in peace, learn with focus</p>
          
        </div>      
      </div>
      <div class="item">
        <A HREF="booksdetails.html"><img src="images/image-1250x380 (4).jpg"  ></A>
        <div class="carousel-caption"  >
          <h3>Book Park</h3>
          <p>Read in peace, learn with focus</p>
        </div>      
      </div>
      <div class="item">
        <A HREF="booksdetails.html"><img src="images/image-1250x380 (3).jpg" ></A>
        <div class="carousel-caption"  >
          <h3>Peace Reading </h3>
          <p>Read in peace, learn with focus</p>
        </div>      
      </div>
      <div class="item">
        <A HREF="booksdetails.html"><img src="images/image-1250x380.jpg"></A>
        <div class="carousel-caption"  >
          <h3>New Collection</h3>
          <p>Read in peace, learn with focus</p>
        </div>      
      </div>
  
</div>
    <!-- Left and right controls -->
  <a class="left carousel-control" href="#myCarousel" role="button" data-slide="prev">
      <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
      <span class="sr-only">Previous</span>
    </a>
    <a class="right carousel-control" href="#myCarousel" role="button" data-slide="next">
      <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
      <span class="sr-only">Next</span>
    </a> 
</div>
 <!-- <div> 
 
   
  <img src="images/sl1.jpg" class="img-circle" alt="Cinque Terre" height="200px" width="230px" > 

   <Marquee>
    <img src="images/lib3.jpg" class="img-rounded" alt="Cinque Terre" height="300px" width="1085px" >
    <img src="images/lib7.jpg" class="img-rounded" alt="Cinque Terre" height="300px" width="1085px" >
    <img src="images/lib8.jpg" class="img-rounded" alt="Cinque Terre" height="300px" width="1085px" >
    <img src="images/lib9.jpg" class="img-rounded" alt="Cinque Terre" height="300px" width="1085px" >
    <img src="images/lib6.jpg" class="img-rounded" alt="Cinque Terre" height="300px" width="1085px" >
    <img src="images/lib5.jpg" class="img-rounded" alt="Cinque Terre" height="300px" width="1085px" >
       
  </Marquee> 
   
     <img src="images/sl2.jpg" class="img-circle" alt="Cinque Terre" height="200px" width="230px"> 

  
</div> -->
<div class="container-fluid text-center">    
  <div class="row content">
    <div class="col-sm-2 sidenav">
  <img src="images/render (5).png"   height="50px" width="170px"><br><br>
      <p><a href="#"> </a></p> 
      <p><a href="#"> </a></p>
      <p><a href="#"></a></p>
      <p><a href="#"><div class="well">
       <p><a href="booksdetails.html">New Arrivals</a></p>
      </div> </a></p>
    
      <p><a href="booksdetails.html"><div class="well">
        <p>Learning Resources</p>
      </div> </a></p>
      <p><a href="booksdetails.html"><div class="well">
        <p>Reading Initiatives</p>
      </div> </a></p>
      
      <p><a href="#"> </a></p>
      <p><a href="#"></a></p>
    </div>
    <div class="col-sm-8 text-left" > 
      <h1><marquee behavior="alternate" scrollamount="1" ><font color=gray size="6" >Welcome to Silent Library </font></marquee></h1>
      <div>
      
          <center> <table border="0" >
            <tr>
              <td ><a href="booksdetails.html"><img src="images/bk1.PNG" height="330" width="220"></a></td>
              <td><a href="booksdetails.html"><img src="images/bk2.PNG" height="330" width="220"></a></td>
           
              <td><a href="booksdetails.html"><img src="images/bk3.png" height="330" width="220"></a></td>
              
            </tr></a>
            
          </table></center>
        </p>
      </div>
      
  </div>
 
    <div class="col-sm-2 sidenav">
     <div><p> <img src="images/render (2).png"   height="50px" width="180px"> </p></div><br>
      <a href="Booklist.html"><div class="well">
        <p>Magazines</p></a>
      </div>
      
      <a href="booksdetails.html"><div class="well">
        <p>Newspapers</p></a>
      </div>
      <p><a href="Booklist.html"><div class="well">
        <p>Career Opportunities</p>
      </div> </a></p>
    </div>
  </div>
</div>

<footer class="container-fluid text-center">
  <p>
    <a href="feedback.html"> <font color="white">Feedback </font></a>| Email:silent@library.com.sg | Website : www.SilentLibrary.com<br>
   &copy; 2025 Silent Library. All Rights Reserved.</p>
</footer>

</body>
</html>
