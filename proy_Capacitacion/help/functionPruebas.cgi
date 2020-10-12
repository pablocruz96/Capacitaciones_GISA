#!/usr/bin/perl

use Eflow::user_check;
use Eflow::Libs;
use MSQL_VB;
use CGI;
use Encode;
use Eflow::SAT;
use MIME::Lite;
use Eflow::GH;
use Eflow::jstl;
use Switch;
use JSON;

use utf8;
binmode STDOUT,':utf8';

print PrintHeader();
ReadParse();

$lib = Libs->new();
$lib->hash_decode(\%in);
use CGI::Carp qw(fatalsToBrowser);#error
$user = user_check(1);
$q = new CGI;
$qt=new CGI;

%ine = $q->Vars;
$lib->hash_decode(\%ine);

$CMD=$in{'cmd'};
require '../menu.pl';

conectadb();
SetSystemTime();


if($ine{'cmd'}){
	$CMD=$ine{'cmd'};
}

#print "$ine el cmd es -->$CMD<--- $ine{'cmd'} -->$id<--  ---->$courier<---- $firma";
eval {
	
    if (!$CMD) {
		$body = inicio();
	} elsif (exists &$CMD) {
		$body = &$CMD;
	}else{		
		die;
	}
	1;
} or do {
	print "No se localizo el metodo $CMD";
    #my $e = $\@;
    #push \@log ,{'log' => 'e' , 'mensaje' => "Algo paso mal no se encontro el metodo: $e\n"};
	#$ocem = 1;
};

################################# Codigo #################################33

sub clearDescriptionJson{
	my $varString=shift;
	$varString =~ s/\n//g;
	$varString=~s/\n/ /g;
	$varString=~s/"/ /g;
    $varString=~s/'/ /g;
	$varString=~s/\r//g;
	$varString=~s/\t/ /g;
	$varString=~s/\s/ /g;
	return $varString
}


sub getCleanFileName {
    $fn=shift;
    $fn =~ s/d/D/;
    $fn =~ s/ /_/g;
    $fn =~ s/\(//g;
    $fn =~ s/\)//g;
    $fn = "${STime}_$fn";
    return $fn;
}



sub notificar{
	my $email=shift;
	my $title=shift;
	my $msj=shift;		
	$lib->email_user_html_noFile($email, $title,$msj);	
}


sub conectadb {	
	
	if (!$lib) {
		$lib = Libs->new();
	}
	if(!$rsq){
		$rsq = Pg_VB->new();
	    $rsq->connectdb("dbname=workflow");
	}
	
	if (!$visesiv) {
		$visesiv = MSQL_VB->new();
		$visesiv->connectdb('proyecto_indicadores','VISE-SIV');

	}
}