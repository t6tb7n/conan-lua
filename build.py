import copy

from conan.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add_common_builds()

    extend_settings = []
    for settings in builder.items:
        settings = copy.deepcopy(settings)
        settings.options["lua:build_interpreter"] = True
        extend_settings.append(settings)
    builder.items.extend(extend_settings)

    extend_settings = []
    for settings in builder.items:
        settings = copy.deepcopy(settings)
        settings.options["lua:build_compiler"] = True
        extend_settings.append(settings)
    builder.items.extend(extend_settings)

    builder.run()
