from pybuilder.core import init,use_plugin

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin('python.integrationtest')
use_plugin("python.coverage")
use_plugin("python.install_dependencies")
use_plugin("python.distutils")

default_task = "publish"


@init
def initialize(project):
    project.include_file('src/unittest/python', 'twitter_data.txt')
    project.set_property("coverage_break_build", False)
    project.build_depends_on('mockito')
    project.build_depends_on('boddle')
