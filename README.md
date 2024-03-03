# singularRdgQuery
Python script that queries a TEI compliant XML collation file and finds singular readings for a specified set and then prints the output to a csv, tab-delimited file.

The script can be run in the command line. It asks for two values:
  1) Please enter witnesses:
  2) Please enter the path of the XML file:
It returns the total instances in the command line and returns the results to a csv file in the same directory as the script.

The results that it returns are, in tab-delimited format, the following:
  1) The variation unit
  2) The variation unit address (from and to values), each in their own column
  3) The reading ID
  4) The witness(es)
  5) The reading type (if defined)
  6) The variant reading
  7) The reading of the A-text, if defined, for comparison
