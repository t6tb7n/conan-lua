cmake_minimum_required(VERSION 3.2)
project(lua LANGUAGES C)

include(${CONANBUILDINFO_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

option(BUILD_INTERPRETER "Build interpreter" OFF)
option(BUILD_COMPILER "Build compiler" OFF)

set(LUA_LIB_SOURCES
  src/lapi.c
  src/lcode.c
  src/lctype.c
  src/ldebug.c
  src/ldo.c
  src/ldump.c
  src/lfunc.c
  src/lgc.c
  src/llex.c
  src/lmem.c
  src/lobject.c
  src/lopcodes.c
  src/lparser.c
  src/lstate.c
  src/lstring.c
  src/ltable.c
  src/ltm.c
  src/lundump.c
  src/lvm.c
  src/lzio.c
  src/lauxlib.c
  src/lbaselib.c
  src/lbitlib.c
  src/lcorolib.c
  src/ldblib.c
  src/liolib.c
  src/lmathlib.c
  src/loslib.c
  src/lstrlib.c
  src/ltablib.c
  src/lutf8lib.c
  src/loadlib.c
  src/linit.c
)

if(WIN32)
  list(APPEND LUA_LIB_SOURCES
    windows/resource.h
    windows/lua.rc
  )
  set_source_files_properties(windows/lua.rc PROPERTIES LANGUAGE RC)
endif(WIN32)

add_definitions(-DLUA_COMPAT_5_2)

if(UNIX)
  link_libraries(m)
endif(UNIX)

add_library(lua SHARED ${LUA_LIB_SOURCES})
target_compile_definitions(lua
  PUBLIC LUA_COMPAT_5_2
)
if(UNIX)
  target_compile_definitions(lua
    PUBLIC LUA_USE_LINUX
  )
elseif(MINGW OR WIN32)
  target_compile_definitions(lua
    PUBLIC LUA_BUILD_AS_DLL
  )
endif()

if(${BUILD_INTERPRETER})
  add_executable(lua_interpreter src/lua.c)
  target_link_libraries(lua_interpreter lua)
  set_target_properties(lua_interpreter PROPERTIES
    OUTPUT_NAME lua
  )
  if(NOT WIN32)
    target_include_directories(lua_interpreter
      PRIVATE ${CONAN_INCLUDE_DIRS_READLINE})
    target_link_libraries(lua_interpreter dl ${CONAN_LIBS_READLINE})
  endif(NOT WIN32)
endif(${BUILD_INTERPRETER})

if(${BUILD_COMPILER})
  add_executable(lua_compiler src/luac.c ${LUA_LIB_SOURCES})
  set_target_properties(lua_compiler PROPERTIES
    OUTPUT_NAME luac
  )
endif(${BUILD_INTERPRETER})
