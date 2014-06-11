<?php

function convert_binary( $number )
{
	if ($number > 0) {
		echo $number % 2;
		
		if ($number % 2 == 1) {
			$number -= 1;		
		}		
		$number = $number / 2;	
		convert_binary( $number );
	}	
}

print_r(convert_binary( 35 ));

