


class Project():
    """docstring for Project."""

    project = None
    project_name = None

    def __init__(self, _project, _project_name: str):
        self.project_name = _project_name
        self.project = _project

    def get_self_project(self):
        return self.project
