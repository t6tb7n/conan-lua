cmake_minimum_required(VERSION 3.2)
project(lua LANGUAGES C)

option(BUILD_INTERPRETER "Build interpreter" OFF)
option(BUILD_COMPILER "Build compiler" OFF)

set(LUA_SOURCES_DIR ${CMAKE_CURRENT_SOURCE_DIR}/src)
set(LUA_LIB_SOURCES
  ${LUA_SOURCES_DIR}/lapi.c
  ${LUA_SOURCES_DIR}/lcode.c
  ${LUA_SOURCES_DIR}/lctype.c
  ${LUA_SOURCES_DIR}/ldebug.c
  ${LUA_SOURCES_DIR}/ldo.c
  ${LUA_SOURCES_DIR}/ldump.c
  ${LUA_SOURCES_DIR}/lfunc.c
  ${LUA_SOURCES_DIR}/lgc.c
  ${LUA_SOURCES_DIR}/llex.c
  ${LUA_SOURCES_DIR}/lmem.c
  ${LUA_SOURCES_DIR}/lobject.c
  ${LUA_SOURCES_DIR}/lopcodes.c
  ${LUA_SOURCES_DIR}/lparser.c
  ${LUA_SOURCES_DIR}/lstate.c
  ${LUA_SOURCES_DIR}/lstring.c
  ${LUA_SOURCES_DIR}/ltable.c
  ${LUA_SOURCES_DIR}/ltm.c
  ${LUA_SOURCES_DIR}/lundump.c
  ${LUA_SOURCES_DIR}/lvm.c
  ${LUA_SOURCES_DIR}/lzio.c
  ${LUA_SOURCES_DIR}/lauxlib.c
  ${LUA_SOURCES_DIR}/lbaselib.c
  ${LUA_SOURCES_DIR}/lbitlib.c
  ${LUA_SOURCES_DIR}/lcorolib.c
  ${LUA_SOURCES_DIR}/ldblib.c
  ${LUA_SOURCES_DIR}/liolib.c
  ${LUA_SOURCES_DIR}/lmathlib.c
  ${LUA_SOURCES_DIR}/loslib.c
  ${LUA_SOURCES_DIR}/lstrlib.c
  ${LUA_SOURCES_DIR}/ltablib.c
  ${LUA_SOURCES_DIR}/lutf8lib.c
  ${LUA_SOURCES_DIR}/loadlib.c
  ${LUA_SOURCES_DIR}/linit.c
)

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
  add_executable(lua_interpreter ${LUA_SOURCES_DIR}/lua.c ${LUA_LIB_SOURCES})
  set_target_properties(lua_interpreter PROPERTIES
    OUTPUT_NAME lua
  )
endif(${BUILD_INTERPRETER})

if(${BUILD_COMPILER})
  add_executable(lua_compiler ${LUA_SOURCES_DIR}/luac.c ${LUA_LIB_SOURCES})
  set_target_properties(lua_compiler PROPERTIES
    OUTPUT_NAME luac
  )
endif(${BUILD_INTERPRETER})
