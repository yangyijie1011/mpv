def __cp_to_variant__(ctx, variant, basename):
    src = ctx.bldnode.search(basename).read()
    node = ctx.bldnode.make_node("{0}/{1}".format(variant, basename))
    node.parent.mkdir()
    node.write(src)

def __get_version__(ctx):
    import subprocess
    process = subprocess.Popen(["sh", "./version.sh", "--print"],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               cwd=ctx.srcnode.abspath())
    (version, err) = process.communicate()
    version = version.strip()
    if not isinstance(version, str):
        version = version.decode('utf-8')
    return version

def __get_build_date__():
    import time
    return time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime())

def __write_config_h__(ctx):
    ctx.start_msg("Writing configuration header:")
    ctx.write_config_header('config.h')
    __cp_to_variant__(ctx, ctx.options.variant, 'config.h')
    ctx.end_msg("config.h", "PINK")

def __write_version_h__(ctx):
    ctx.start_msg("Writing header:")
    ctx.env.VERSION = __get_version__(ctx)
    ctx.define("VERSION",   ctx.env.VERSION)
    ctx.define("BUILDDATE", __get_build_date__())
    ctx.write_config_header("version.h")
    __cp_to_variant__(ctx, ctx.options.variant, 'version.h')
    ctx.end_msg("version.h", "PINK")

def __add_mplayer_defines__(ctx):
    from sys import argv
    ctx.define("CONFIGURATION", " ".join(argv))
    ctx.define("MPLAYER_CONFDIR", ctx.env.CONFDIR)

def configure(ctx):
    __add_mplayer_defines__(ctx)
    __write_config_h__(ctx)
    __write_version_h__(ctx)
