import inspect
import sys
import yaml

from fabric.tasks import Task
from fabric.state import env


#class CustomTask(Task):
    #def __init__(self, func, myarg, *args, **kwargs):
        #super(CustomTask, self).__init__(*args, **kwargs)
        #self.func = func
        #self.myarg = myarg

    #def run(self, *args, **kwargs):
        #print("RUN!")
        #return self.func(*args, **kwargs)


def _create_stage(stage_config):
    def function_template(*args, **kwargs):
        for key, value in stage_config.iteritems():
            setattr(env, key, value)

    return function_template


def _create_stages_from_config():
    stages = None

    with open("./skeppa.yml", 'r') as stream:
        stages = yaml.load(stream)

    for name in stages:
        stage = stages[name]
        module_obj = sys.modules[__name__]
        setattr(module_obj, name, _create_stage(stage))


# setup
# build
# deploy


_create_stages_from_config()