#!/usr/bin/perl

use Date::Calc qw(:all);
require 'cgi-lib.pl';
use Eflow::user_check;
use Eflow::Libs;
use MSQL_VB;
use CGI;
use Encode;
use MIME::Lite;
use Eflow::GH;
use Eflow::jstl;
use utf8;
binmode STDOUT,':utf8';
use CGI::Carp qw(fatalsToBrowser);#error
use Switch;

use Time::Local;
use POSIX qw/strftime/;

print PrintHeader();

my ($s, $min, $h, $d, $m, $y) = localtime();

$|=1;
$qt = new CGI;
%in = $qt->Vars;
conectadb();
$lib->hash_decode(\%in);

SetSystemTime();
$user = user_check(1);

require 'menu.pl';
$CMD=$in{'cmd'};
my $gh=Eflow::GH->new();
my @js =();
my @js_post =();
my @css=();
my @links=();
@log=();
my $title = qq||;
$title = "";
$subTitle=qq||;
my $body = "";
my $ocem=0;

eval {
    $CMD = $in{'cmd'};
    #   print qq|CDM ---> $CMD...|;
    if (!$CMD) {
        $body = inicio();
    } elsif (exists &$CMD) {
        $body = &$CMD;
    }else{
        die;
    }
    1;
} or do {
    my $e = $@;
    push @log ,{'log' => 'e' , 'mensaje' => "Algo paso mal no se encontro el metodo: $e\n"};
    $ocem = 1;
};

# creacion de scrips JS y Css 
#NOTA **** procurar usar menos archivos requeridos
# versiones /produccion/testeo/cambios/desarrollo

$version="1.0.0.2";
my @js =("/js/proyectos/SUtil/functionGral.js?v=$version");
my @js_post =("/js/proyectos/SUtil/libreria.js?v=$version","/js/proyectos/proy_Practicas/main.js?v=$version"); 
my @css = ("/css/proy_Proyectos/Proyectos.css?v=$version");


# fin de archivos 

print $gh->runHTML(\@js,\@css,$title,$subTitle,$body,"","",\@log,$ocem,\@js_post,$MainPo,$user);


#################################  INICIO SIN CMD  #####################################
########################################################################################
# Esta función se ejecuta cuando el parametro 'cmd' no es encontrado.
########################################################################################
sub inicio {
    $html = qq|Practicantes.
    texto prueba
    |;
    return $html;
}

sub formulario1 {

    $html = qq|
        <!--
            <div class="card">
                <div class="card-header">
                    FORMARIO DATOS
                </div>
                <div class="card-body">
                   <label for="nombre">Nombre del usuario:</label>
                   <input id="nombre" class="form-control" placeholder="escriba el nombre del usuario">
                    <hr>
                    <button id="boton" class="btn btn-success">Formulario</button>
                </div>
            </div> 
        --> 

            <div>
            <h1 style="text-align:center;">Formulario vacantes</h1><hr>
            <form>
            <input type="Date" >
            <input list="gerencias" value = "gerencias">
            <datalist id="gerencias">
                <option value="Internet Explorer">
                <option value="Firefox">
                <option value="Chrome">
                <option value="Opera">
                <option value="Safari">
            </datalist>
            <input list="gerencias" value = "areas">
            <input list="gerencias" value = "Puesto requerido"><br><br>
            <p>Numero de personas requeridas: <input type="number"> 
            <p>
                <table style="center">
                    <tr>
                        <td><b>Genero:</b></td>
                        <td><input type="radio" id="male" name="gender" value="Mausculino">
                            <label for="">Masculino</label><br>
                            <input type="radio" id="female" name="gender" value="Femenino">
                            <label for="female">Femenino</label><br>
                            <input type="radio" id="other" name="gender" value="Otro">
                            <label for="other">Otro</label>
                        </td>
                        <td><b>Escolaridad:</b></td>
                        <td>
                            <input type="radio" id="nones" name="Escolaridad" value="no necesaria">
                            <label for="">No necesaria</label><br>
                            <input type="radio" id="primaria" name="Escolaridad" value="Primaria">
                            <label for="female">Primaria</label><br>
                            <input type="radio" id="secundaria" name="Escolaridad" value="secundaria">
                            <label for="other">Secundaria</label><br>
                            <input type="radio" id="bachillerato" name="Escolaridad" value="bachillerato">
                            <label for="other">Bachillerato</label><br>
                            <input type="radio" id="Univercidad" name="Escolaridad" value="Univercidad">
                            <label for="other">Univercidadun</label>
                        </td>
                        <td><b>Estado civil:</b></td>
                        <td>
                            <input type="radio" id="Soltero" name="estatus" value="Soltero">
                            <label for="">Masculino</label><br>
                            <input type="radio" id="Casado" name="estatus" value="Casado">
                            <label for="female">Femenino</label><br>
                            <input type="radio" id="union" name="estatus" value="union libre">
                            <label for="other">Union libre</label>
                        </td>
                    </tr>
                </table>
            </p>
            <p>
                <table style="center">
                    <tr>
                        <td><b>Experiencía minima:</b></td>
                        <td>
                            <input type="radio" id="nonese" name="Experiencia" value="no necesaria">
                            <label for="">No necesaria</label><br>
                            <input type="radio" id="seism" name="Experiencia" value="seis meses">
                            <label for="female">Seis Meses</label><br>
                            <input type="radio" id="unanio" name="Experiencia" value="un anio">
                            <label for="other">Un año</label><br>
                            <input type="radio" id="dosanio" name="Experiencia" value="dos anio">
                            <label for="other">dos años</label><br>
                            <input type="radio" id="tresanio" name="Experiencia" value="tres anio">
                            <label for="other">Tres años</label><br>
                            <input type="radio" id="mastresanio" name="Experiencia" value="mas de tres anio">
                            <label for="other">Mas de Tres Años</label>
                        </td>
                        <td><b>Edad:</b></td>
                        <td>
                            <input type="radio" id="diesiocho" name="Edad" value="18 a 20">
                            <label for="">18 a 20</label><br>
                            <input type="radio" id="veinte" name="Edad" value="20 a 30">
                            <label for="">20 a 30</label><br>
                            <input type="radio" id="treinta" name="Edad" value="30 a 40">
                            <label for="">30 a 40</label><br>
                            <input type="radio" id="cuarenta" name="Edad" value="40 a 50">
                            <label for="">40 a 50</label><br>
                            <input type="radio" id="cincuenta" name="Edad" value="mas de 50">
                            <label for="">Mas de 50</label>
                        </td>
                    </tr>
                </table>
            </p>
            <p>conocimientos especiales: <input type="text" id="conesp">habilidades especiales: <input type="text" id="habesp"></p>
            <hr><h3>Justificación para la vacante</h3><hr>
            <p><input type="checkbox" id="disp">Puesto vacante </p> 
            <p>Para sustituir a:<input type="text" id="anterior"></p>
            <table>
                <tr>
                    <td><b>Motivo:</b></td>
                    <td>
                        <input type="radio" id="Renuncio" name="Motivo" value="Renuncio">
                        <label for="">Renuncio</label><br>
                        <input type="radio" id="baja" name="Motivo" value="baja">
                        <label for="female">Fue dado de baja</label><br>
                        <input type="radio" id="Promovido" name="Motivo" value="Promovido">
                        <label for="other">Fue Promovido</label><br>
                        <input type="radio" id="transferido" name="Motivo" value="transferido">
                        <label for="other">Fue transferido</label>                    
                    </td>
                </tr>
            </table>
            <input type="submit" value="Mandar">
            </form>
            </div>
    |;
    return $html;
}


sub conectadb {
    if (!$lib) {
        $lib = Libs->new();
    }
    if (!$visesiv) {
        $visesiv = MSQL_VB->new();
        $visesiv->connectdb('proyecto_indicadores','VISE-SIV');
    }
    
}

sub clearDescriptionJson{
    my $varString=shift;
    $varString=~ s/\n//g;
    $varString=~s/\n/ /g;
    $varString=~s/"/ /g;
    $varString=~s/'/ /g;
    $varString=~s/\r//g;
    $varString=~s/\t/ /g;
    $varString=~s/\s/ /g;
    return $varString
}
