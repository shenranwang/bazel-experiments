# Stage 2

Builds multiple targets in a single package.

## Command
```
bazel build //main:hello-world
```

* //main: --- location of the BUILD file relative to the root of the workspace
* hello-world --- target name in the BUILD file, automatically build library rule as it is a dependency

## Observed outputs

* bazel-bin: contains the built binary/executable --- `./bazel-bin/main/hello-world`
* bazel-out: ???
* bazel-stage1: ???
* bazel-testlogs: ???

### Dependency graph
```
bazel query --notool_deps --noimplicit_deps "deps(//main:hello-world)" \
  --output graph
```
Outputs all but host and implicit dependencies for the target