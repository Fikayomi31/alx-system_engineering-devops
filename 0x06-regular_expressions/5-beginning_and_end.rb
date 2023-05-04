#!/usr/bin/env ruby
# Regular expression matching a string that start wit
# h and end with n and can have any single character
puts ARGV[0].scan(/^h[a-z0-9]n$/).join
