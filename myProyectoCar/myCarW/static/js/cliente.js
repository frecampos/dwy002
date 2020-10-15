class cliente {

    rut;
    nombre;
    apellido;
    email;
    fecha;
    nomusuario;
    contrasena;
    ;
    //set
    setRut(rut){ this.rut=rut; }
    setNombre(nombre){ this.nombre=nombre; }
    setApellido(apellido){ this.apellido=apellido; }
    setEmail(email){ this.email=email; }
    setFecha(fecha){ this.fecha=fecha; }
    setNomusuario(nomusuario){ this.nomusuario=nomusuario; }
    setContrasena(contrasena){ this.contrasena=contrasena; }
    //get
    getRut(){ return this.rut; }
    getNombre(){ return this.nombre; }
    getApellido(){ return this.apellido; }
    getEmail(){ return this.email; }
    getFecha(){ return this.fecha; }
    getNomusuario(){ return this.nomusuario; }
    getContrasena(){ return this.contrasena; }

    imprimir() {
        return "Rut:" + this.rut + "Nombre:" +this.nombre + "Apellido:" +this.apellido + "Email:" + this.email + "Fecha:" + this.fecha + "Nomusuario :" + this.nomusuario + "Contrasena :" + this.contrasena;
    }
}

var arreglocli=new Array();
var x=0;
function grabarcliente(){
    if (typeof(Storage)=='undefinied') {
      alert("no soportado");
      return false;  
    }
    var rut = document.getElementById("txtrut").value;
    var nombre = document.getElementById("txtnombre").value;
    var apellido = document.getElementById("txtapellido").value;
    var email = document.getElementById("txtemail").value;
    var fecha = document.getElementById("fecha").value;
    var nomusuario = document.getElementById("txtnomusuario").value;
    var contrasena = document.getElementById("txtcontrasena").value;
    cli = new cliente();
    cli.setRut(rut);
    cli.setNombre(nombre);
    cli.setApellido(apellido);
    cli.setEmail(email);
    cli.setFecha(fecha);
    cli.setNomusuario(nomusuario);
    cli.setContrasena(contrasena);

    alert(cli.imprimir());
    arreglocli[x]=cli;
    x++;
    localStorage.setItem("registro cliente",arreglocli);
    alert("Cliente en localStorage")
 
   }
  
   function listarcli(){

    var todo ="";
    for (let index = 0; index < arreglocli.length; index++) {
        var datos = arreglocli[index];
        todo=todo+ datos.imprimir()+"<br>";
        }
        document.getElementById("section").innerHTML = todo;

  }



