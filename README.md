# removelines
A simple little Python3 script that removes lines from multiple files that include a matching string.

## Use case
This is particularly useful if you have many config files that each need many variables removing from them.

## How to use

1. Set `path`. Default is current working directory.
1. Add your removal strings to `to-remove`, one per line.
1. Run! removelines will remove lines from all the files in the `path` and below that include your removal strings.

This is not a reversible action, so consider testing before doing it for real. Lots of `print` statements have been left in; messy but allows you some idea on what it is doing.

##Caveats
Not designed to be user-friendly. 

Should run everywhere but tested on a Mac.

