#!/usr/bin/env ruby
require "cgi"
require "open-uri"
require "json"
cgi = CGI.new
print cgi.header("text/html;charset=utf-8")
io = open("http://localhost:8983/solr/wikipedia/select?q=#{URI.escape cgi["q"]}&wt=json")
json = io.read
data = JSON.load(json)
result = data["response"]["docs"]

print "<html>\n"
print "<head><title>result</title><link href=\"search.css\" rel=\"stylesheet\" type=\"text/css\" /></head>\n"
print "<body>\n"
print "<div class=\"square\">"
print "<h1>Result</h1>\n"

result.each.with_index(1) do |e,i|
	puts i," : ",e["title"]
	puts "<br>"
end

print "<br>"
print "<p><a href=\"http://localhost/solr/search.html\">戻る</a></p>"
print "<br>"
print "</div>"
print "</body>\n"
print "</html>\n"