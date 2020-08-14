#! /usr/bin/env bash

for f in `ls docs/*.raml`; do 
    # echo "${f%.*}.raml"
    raml2html "${f%.*}.raml" > "${f%.*}.html"
    raml2md  "${f%.*}.raml" > "${f%.*}.md"
    markdown-pdf "${f%.*}.md"
done