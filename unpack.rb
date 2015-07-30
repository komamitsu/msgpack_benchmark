require 'msgpack'
require 'benchmark'

filename = ARGV.shift

File.open(filename) do |f|
  unpacker = MessagePack::Unpacker.new(f)
  Benchmark.bm do |x|
    x.report {
      unpacker.each do |obj|
      end
    }
  end
end

