# Each extracted wheel repo contains a py_library target 
# representing the wheel's contents. Rather than depend 
# on this target's label directly -- which would require 
# hardcoding the wheel repo's mangled name into your 
# BUILD files -- you should instead use the requirement() 
# function defined in the central repo's //:requirements.bzl 
# file. This function maps a pip package name to a label.
load("@depends//:requirements.bzl", "requirement")

# load("@rules_python//python/pip_install:requirements.bzl", "compile_pip_requirements")

load("@rules_python//python:defs.bzl", "py_binary")

py_library(
    name = "hello_world_deps",
    deps = [
        requirement("flask"),
    ],
)

py_binary(
  name = "hello-world",
  srcs = ["hello-world.py"],
  # deps = [ requirement("flask") ],
)

# Check that our compiled requirements are up-to-date
# compile_pip_requirements(
#     name = "requirements",
# )