$(document).ready(function(){

//避免gif沒從頭播放
  $('.loadimg').attr('src','');
  $('.loadimg').attr('src',"../static/Image/loading.gif");//Path使用 "../" 是為了避免下層目錄無法讀取GIF

//gif結束
  setTimeout(function() {
    $('.loading').fadeOut(1000);
  }, 1000);

//判斷是否為首頁 True-> slogan
  if(window.location.pathname === "/home"){
    //slogan顯示
    setTimeout(function() {
      $('.slogan_load').fadeIn(1000);
    },2000)
    //Loading結束
    setTimeout(function() {
      //solgan上滑
        $('.slogan_load').slideUp("slow");
      //顯示內容
        $('.content').fadeIn(1000)
        document.getElementById("nav").setAttribute('id', '')
       
      },3500)

    
  }else{
    //Loading結束
    setTimeout(function() {
      $('.loading').fadeOut(1000);
      //顯示內容
      $('.content').fadeIn(1000)
      document.getElementById("nav").setAttribute('id', '')
    }, 1000);
  }



  

});
