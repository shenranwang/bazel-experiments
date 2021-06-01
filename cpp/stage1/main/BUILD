# built-in build rule, which tells Bazel to build a self-contained 
# executable binary from the source file without dependencies
load("@rules_cc//cc:defs.bzl", "cc_binary") 

cc_binary(
    name = "hello-world", # target name
    srcs = ["hello-world.cc"], # source file(s)
)