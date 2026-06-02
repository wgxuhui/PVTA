#!/usr/bin/python3

import os
import sys

if os.geteuid( ):
   args = [ 'sudo', 'python3' ] + sys.argv
   os.execvp( 'sudo', args )


if len( sys.argv ) == 1:
   print( 'down_bit <bit>' )
   exit( 0 )

bit_path = sys.argv[1]


print( 'Download ' + bit_path )

from pynq import xlnk
from pynq import Bitstream

xlnk.Xlnk().xlnk_reset()
bitstream = Bitstream( bit_path )
bitstream.download( )

