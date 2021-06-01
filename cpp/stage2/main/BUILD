# cc_library: built-in build rule, which tells Bazel to build a
# library from hello-greet.cc, also adding any required headers
load("@rules_cc//cc:defs.bzl", "cc_binary", "cc_library")

cc_library(
    name = "hello-greet",
    srcs = ["hello-greet.cc"],
    hdrs = ["hello-greet.h"],
)

cc_binary(
    name = "hello-world",
    srcs = ["hello-world.cc"],
    deps = [
        ":hello-greet", # requires target hello-greet to build
    ],
)