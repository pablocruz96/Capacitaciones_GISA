/*
 * Esta clase funciona para realizar todos los métodos
 * que tengan que ver con el módulo de Proyectos.
 *
 * Ultima Actualización: 20/12/2019
 */
j(document).ready(function() {
	var dir = window.location.href;
	console.log(dir);

	 if (dir.indexOf('pruebas_Practicas/vista_Pruebas.cgi?cmd=formulario1')>-1) {
	 	console.log("Formulario");
	 	
	 	j("#boton").click(function(){
	 		var nombre = j("#nombre").val();
	 		console.log(nombre);
	 	});
	 }
});// fin document ready
