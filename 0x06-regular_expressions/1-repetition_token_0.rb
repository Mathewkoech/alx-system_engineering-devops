#!/usr/bin/env ruby
# Takes the first command-line argument (ARGV[0]),
# Scans for the pattern /hbt{2,5}n/ which matches 'hbtn', 'hbttn',
# The matches are then joined and printed to the standard output.
puts ARGV[0].scan(/hbt{2,5}n/).join
