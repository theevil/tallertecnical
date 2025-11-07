from ..entities.project import Project



def create_project(db_session, project_data):
    project = Project(**project_data)
    db_session.add(project)
    db_session.commit()
    db_session.refresh(project)
    return project

def get_project_by_id(db_session, project_id):
    return db_session.get(Project, project_id)

def get_all_projects(db_session):
    return db_session.query(Project).all()

def delete_project(db_session, project_id):
    project = db_session.get(Project, project_id)
    if project:
        db_session.delete(project)
        db_session.commit()
        return True
    return False