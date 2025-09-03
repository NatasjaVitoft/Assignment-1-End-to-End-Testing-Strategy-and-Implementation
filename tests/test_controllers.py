import pytest
from src.db.db_connection import get_connection, init_db
from src.controllers.list_controller import ListTaskController
from src.controllers.task_controller import TaskController

# Fixtures
# All fixture sets up some kind of ressource the tests needs
# This PyTest fixture sets up an in-memory database that we need for our tests 
@pytest.fixture
def db_conn():
    conn = get_connection()
    init_db(conn)
    return conn

# This fixture creates a TaskController object that we need for all our test for tasks
@pytest.fixture
def task_controller(db_conn):
    return TaskController(db_conn)

# This fixture creates a TaskController object that we need for all our test for tasks
@pytest.fixture
def list_controller(db_conn):
    return ListTaskController(db_conn)


# UNITTESTS

def test_add_task(task_controller):

    task = task_controller.add_task(
        title="Test",
        description="Test",
        deadline="2025-09-10",
    )

    assert isinstance(task, int)
    assert task > 0
    
def test_get_task(task_controller):
    # Create a task
    task_id = task_controller.add_task(
        title="Whatever",
        description="Whatever",
        deadline="2024-10-10"
    )

    assert task_id > 0

    # Retrieve the task
    retrieved_task = task_controller.get_task(task_id)

    # Correct assertions
    assert retrieved_task is not None
    assert retrieved_task.id == task_id
    assert retrieved_task.title == "Whatever"
    assert retrieved_task.list_id is None

def test_delete_task(task_controller):

    # Need to create a task first
    task_id = task_controller.add_task(
        title="To be deleted",
        description="To be deleted",
        deadline="2024-11-11"
    )

    # Check if its created
    assert task_id > 0

    # Lets delete it
    task_controller.delete_task(task_id)

    # Try and recieve it and hopefully its None
    deleted_task = task_controller.get_task(task_id)
    assert deleted_task is None

def test_add_list(list_controller):

    list_id = list_controller.add_list(name="Best list ever")

    assert isinstance(list_id, int)
    assert list_id > 0

def test_get_list(list_controller):

    # Create a list
    list_id = list_controller.add_list(name="My List")
    assert list_id > 0

    # Retrieve the list
    retrieved_list = list_controller.get_list(list_id)

    # Correct assertions
    assert retrieved_list is not None
    assert retrieved_list.id == list_id
    assert retrieved_list.name == "My List"

def test_delete_list(list_controller):

    # Need to create a list first
    list_id = list_controller.add_list(name="To be deleted")

    # Check if its created
    assert list_id > 0

    # Lets delete it
    list_controller.delete_list(list_id)

    # Try and recieve it and hopefully its None

    deleted_list = list_controller.get_list(list_id)
    assert deleted_list is None


# NARROW INTEGRATION TESTS (MAYBE)

def test_add_task_to_list(task_controller, list_controller):

    # List first
    list_id = list_controller.add_list(name="TEST LIST")
    # Control if its created
    assert list_id > 0
    # We create a task
    task_id = task_controller.add_task(
        title="Task for a list",
        description="Task for a listt",
        deadline="2025-03-09"
    )
    # Control if its created
    assert task_id > 0
    # Now we add the task to the list
    task_controller.add_task_to_list(task_id, list_id)
    # Now we retrieve the task and check if the list_id is correct (which should be the one we created)
    task = task_controller.get_task(task_id)
    assert task is not None
    assert task.list_id == list_id
    print(task.list_id)