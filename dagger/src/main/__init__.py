"""A generated module for Dagger functions

This module has been generated via dagger init and serves as a reference to
basic module structure as you get started with Dagger.

Two functions have been pre-created. You can modify, delete, or add to them,
as needed. They demonstrate usage of arguments and return types using simple
echo and grep commands. The functions can be called from the dagger CLI or
from one of the SDKs.

The first line in this comment block is a short description line and the
rest is a long description with more detail on the module's purpose or usage,
if appropriate. All modules should have a short description.
"""

import dagger
from dagger import dag, function, object_type


@object_type
class Dagger:
    @function
    def plone(self, src: dagger.Directory) -> dagger.Directory:
        """Returns a plone container from local buildout"""
        python = (
            dag.container()
            .from_("python:3.8-buster")
            .with_directory("/src", src, include=["buildout.cfg", "dagger-cache"])
            .with_env_variable("XDG_CACHE_HOME", "/src/dagger-cache/python")
            .with_exec(["python", "--version"])
            .with_exec(["pip", "install", "virtualenv"])
            .with_exec(["virtualenv", "--version"])
            .with_exec(["virtualenv", "/src"])
            .with_exec(["/src/bin/pip", "install", "--upgrade", "pip"])
            .with_exec(["/src/bin/pip", "install", "zc.buildout"])
            .with_exec(["/src/bin/buildout", "-Nvv",
                        "buildout:download-cache=/src/dagger-cache/buildout/download",
                        "buildout:eggs-directory=/src/dagger-cache/buildout/eggs",
                        "-c", "/src/buildout.cfg", "install", "instance", "test"])
            .with_exec(["/src/bin/test", "-s", "plone.autoform"])
            .directory("/src/dagger-cache")

        )

        return python
