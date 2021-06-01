# Each extracted wheel repo contains a py_library target 
# representing the wheel's contents. Rather than depend 
# on this target's label directly -- which would require 
# hardcoding the wheel repo's mangled name into your 
# BUILD files -- you should instead use the requirement() 
# function defined in the central repo's //:requirements.bzl 
# file. This function maps a pip package name to a label.
#load("@depends//:requirements.bzl", "requirement")

#py_library(
#    name = "hello-world-deps",
#    deps = [
#        requirement("flask"),
#    ]
#)


# built-in build rule, which tells Bazel to build a self-contained 
# executable binary from the source file without dependencies
load("@rules_python//python:defs.bzl", "py_binary")

py_binary(
  name = "hello-world",
  srcs = ["hello-world.py"],
  # deps = [ "depends" ],
)