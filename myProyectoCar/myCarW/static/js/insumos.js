class insumos {

    nombreinsumo;
    precio;
    descripcion;
    //set
    setNombreinsumo(nombreinsumo){ this.nombreinsumo=nombreinsumo; }
    setPrecio(precio){ this.precio=precio; }
    setDescripcion(descripcion){ this.descripcion=descripcion; }
    //get
    getRut(){ return this.nombreinsumo; }
    getPrecio(){ return this.precio; }
    getDescripcion(){ return this.descripcion; }

    imprimir() {
        return "Nombre insumo:" + this.nombreinsumo + "precio:" +this.precio + "Descripcion:"+this.descripcion;
    }
}

var arreglo=new Array();
var x=0;
function Grabar(){
    if (typeof(Storage)=='undefinied') {
      alert("no soportado");
      return false;  
    }
    var nombreinsumo = document.getElementById("txtnombreinsumo").value;
    var precio = document.getElementById("txtprecio").value;
    var descripcion = document.getElementById("txtdes").value;
    ins = new insumos();
    ins.setNombreinsumo(nombreinsumo);
    ins.setPrecio(precio);
    ins.setDescripcion(descripcion);

    alert(ins.imprimir());
    arreglo[x]=ins;
    x++;
    localStorage.setItem("Registro Insumo",arreglo);
    alert("Insumo en localStorage")

   }

  function listarinsu(){

    var todo ="";
    for (let index = 0; index < arreglo.length; index++) {
        var datos = arreglo[index];
        todo=todo+ datos.imprimir()+"<br>";
        }
        document.getElementById("section").innerHTML = todo;

  }