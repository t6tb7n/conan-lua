import os
import shutil

from conans import CMake, ConanFile, tools


class LuaConan(ConanFile):
    name = "lua"
    version = "5.3.4"
    license = "https://www.lua.org/license.html"
    url = "https://www.lua.org/ftp/"
    description = "Lua is a powerful, efficient, lightweight, embeddable scripting language."
    settings = "os", "compiler", "build_type", "arch"
    options = {"build_interpreter": [True, False], "build_compiler": [True, False]}
    default_options = "build_interpreter=False", "build_compiler=False"
    exports = ["CMakeLists.txt"]
    generators = "cmake"

    @property
    def zip_folder_name(self):
        return "lua-%s" % self.version

    def config(self):
        del self.settings.compiler.libcxx

    def source(self):
        zip_name = "lua-%s.tar.gz" % self.version
        tools.download("https://www.lua.org/ftp/%s" % zip_name, zip_name)
        tools.check_md5(zip_name, "53a9c68bcc0eda58bdc2095ad5cdfc63")
        tools.unzip(zip_name)
        os.unlink(zip_name)

    def build(self):
        shutil.move("CMakeLists.txt", "%s/CMakeLists.txt" % self.zip_folder_name)
        with tools.chdir(self.zip_folder_name):
            os.mkdir("_build")
            with tools.chdir("_build"):
                cmake = CMake(self)
                if self.options.build_interpreter:
                    cmake.definitions["BUILD_INTERPRETER"] = "ON"
                if self.options.build_compiler:
                    cmake.definitions["BUILD_COMPILER"] = "ON"
                cmake.configure(build_dir=".", source_dir="..")
                cmake.build(build_dir=".")

    def package(self):
        src_dir = "%s/src" % self.zip_folder_name
        build_dir = "%s/_build" % self.zip_folder_name

        export_includes = [
            "lua.h",
            "lua.hpp",
            "lualib.h",
            "lauxlib.h",
            "luaconf.h",
        ]

        for name in export_includes:
            self.copy(name, dst="include", src=src_dir)
        self.copy("*/lua.exe", dst="bin", src=build_dir, keep_path=False)
        self.copy("*/luac.exe", dst="bin", src=build_dir, keep_path=False)
        self.copy("*/lua", dst="bin", src=build_dir, keep_path=False)
        self.copy("*/luac", dst="bin", src=build_dir, keep_path=False)
        self.copy("*.lib", dst="lib", src=build_dir, keep_path=False)
        self.copy("*.dll", dst="bin", src=build_dir, keep_path=False)
        self.copy("*.a", dst="lib", src=build_dir, keep_path=False)
        self.copy("*.so*", dst="lib", src=build_dir, keep_path=False)
        self.copy("*.dylib*", dst="lib", src=build_dir, keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["lua"]
