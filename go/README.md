## Command
```
bazel build //:hello
./bazel-bin/hello_/hello
```
or
```
bazel run //:hello
```

### Dependency graph
```
bazel query --notool_deps --noimplicit_deps "deps(//:hello)" \
  --output graph
```
Outputs all but host and implicit dependencies for the target