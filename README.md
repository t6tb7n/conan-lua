# conan-lua

Conan package for [lua](https://www.lua.org)

The packages generated with this **conanfile** can be found on [bintray](https://bintray.com/conan-community).

## Package Status

| Bintray | Travis | Appveyor |
|---------|--------|----------|
|[ ![Download](https://api.bintray.com/packages/zimmerk/conan/lua%3Azimmerk/images/download.svg) ](https://bintray.com/zimmerk/conan/lua%3Azimmerk/_latestVersion)|[![Build Status](https://travis-ci.org/AtaLuZiK/conan-lua.svg?branch=release%2F5.3.4)](https://travis-ci.org/AtaLuZiK/conan-lua)|[![Build status](https://ci.appveyor.com/api/projects/status/0s9w9tb38kvj4o8r/branch/release/5.3.4?svg=true)](https://ci.appveyor.com/project/AtaLuZiK/conan-lua/branch/release/5.3.4)|

## Reuse the packages

### Basic setup

```
conan install lua/5.3.4@zimmerk/stable
```

### Project setup

```
[requires]
lua/5.3.4@zimmerk/stable

[options]
# Take a look for all avaliable options in conanfile.py

[generators]
cmake
```

Complete the installitation of requirements for your project running:

```
conan install .
```

Project setup installs the library (and all his dependencies) and generates the files conanbuildinfo.txt and conanbuildinfo.cmake with all the paths and variables that you need to link with your dependencies.

Follow the Conan getting started: http://docs.conan.io
