$(document).ready(function () {
   $.get("localhost:8000/api/proveedor", data,
       function (data, textStatus, jqXHR) {
        console.log(respuesta) 
       },
       "json"
   );
});

