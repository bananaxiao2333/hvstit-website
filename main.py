from datetime import datetime

now = datetime.now()

def define_env(env):
    """
    This is the hook for the variables, macros and filters.
    """

    @env.macro
    def get_time():
        "generate compile time"
        return now.strftime("%Y-%m-%d %H:%M:%S")

