#!/usr/bin/env ruby
# Regularexpression that accept one agrument and pass matching method
puts ARGV[0].scan(/hbt{1,5}n/).join
