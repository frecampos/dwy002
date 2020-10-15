function valida_rut_formu(){
    var valida_el_rut= validarut();
    if(valida_el_rut){
        true; 
    }else{
        false;
    }
}




function validarut(){
    var rut=document.getElementById("txtrut").value;
    if (rut.length!=10) {
      alert("Rut incompleto")
      return false;
    }
    //Validacion del rut
    var suma=0;
    var num=3;
    for (let index = 0; index < 8; index++) {
      var car = rut.slice(index,index+1);
      suma = suma + (car * num);
      num = num - 1;
      if (num == 1){
          num = 7;
      }
    }
    var resto = suma % 11;
    var dv = 11 - resto;

    if (dv < 10) {

          } else {
     if (dv==10) {
        dv='K';
      }else{
        dv = 0;
      }
      
    }

    var dv_usuario=rut.slice(-1).toUpperCase();

    if (dv != dv_usuario) {
      alert("RUT INCORRECTO")
      return false;
    }else{
      return true;
    }
  }

  function validarCorreo (){
    re=/^([\da-z_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/
    if(!re.exec(document.getElementById("txtemail").value)){
      alert('CORREO NO VALIDO');
      false;
    }
    else true;
    }

    function validarfecha(){
      var date = new date(document.getElementById("fecha").value);
      date.setMonth(date.getMonth()-12);
      
    }