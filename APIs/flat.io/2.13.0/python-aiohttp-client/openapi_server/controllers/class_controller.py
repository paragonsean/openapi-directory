from typing import List, Dict
from aiohttp import web

from openapi_server.models.assignment import Assignment
from openapi_server.models.assignment_copy import AssignmentCopy
from openapi_server.models.assignment_creation import AssignmentCreation
from openapi_server.models.assignment_submission import AssignmentSubmission
from openapi_server.models.assignment_submission_comment import AssignmentSubmissionComment
from openapi_server.models.assignment_submission_comment_creation import AssignmentSubmissionCommentCreation
from openapi_server.models.assignment_submission_history import AssignmentSubmissionHistory
from openapi_server.models.assignment_submission_update import AssignmentSubmissionUpdate
from openapi_server.models.class_creation import ClassCreation
from openapi_server.models.class_details import ClassDetails
from openapi_server.models.class_update import ClassUpdate
from openapi_server.models.flat_error_response import FlatErrorResponse
from openapi_server.models.score_details import ScoreDetails
from openapi_server.models.score_fork import ScoreFork
from openapi_server import util


async def activate_class(request: web.Request, _class) -> web.Response:
    """Activate the class

    Mark the class as &#x60;active&#x60;. This is mainly used for classes synchronized from Clever that are initially with an &#x60;inactive&#x60; state and hidden in the UI. 

    :param _class: Unique identifier of the class
    :type _class: str

    """
    return web.Response(status=200)


async def add_class_user(request: web.Request, _class, user) -> web.Response:
    """Add a user to the class

    This method can be used by a teacher of the class to enroll another Flat user into the class.  Only users that are part of your Organization can be enrolled in a class of this same Organization.  When enrolling a user in the class, Flat will automatically add this user to the corresponding Class group, based on this role in the Organization. 

    :param _class: Unique identifier of the class
    :type _class: str
    :param user: Unique identifier of the user
    :type user: str

    """
    return web.Response(status=200)


async def archive_assignment(request: web.Request, _class, assignment) -> web.Response:
    """Archive the assignment

    Archive the assignment 

    :param _class: Unique identifier of the class
    :type _class: str
    :param assignment: Unique identifier of the assignment
    :type assignment: str

    """
    return web.Response(status=200)


async def archive_class(request: web.Request, _class) -> web.Response:
    """Archive the class

    Mark the class as &#x60;archived&#x60;. When this course is synchronized with another app, like Google Classroom, this state will be automatically be updated. 

    :param _class: Unique identifier of the class
    :type _class: str

    """
    return web.Response(status=200)


async def copy_assignment(request: web.Request, _class, assignment, body) -> web.Response:
    """Copy an assignment

    Copy an assignment to a specified class.  If the original assignment has a due date in the past, this new assingment will be created without a due date.  If the new class is synchronized with an external app (e.g. Google Classroom), the copied assignment will also be posted on the external app. 

    :param _class: Unique identifier of the class
    :type _class: str
    :param assignment: Unique identifier of the assignment
    :type assignment: str
    :param body: 
    :type body: dict | bytes

    """
    body = AssignmentCopy.from_dict(body)
    return web.Response(status=200)


async def create_assignment(request: web.Request, _class, body=None) -> web.Response:
    """Assignment creation

    Use this method as a teacher to create and post a new assignment to a class.  If the class is synchronized with Google Classroom, the assignment will be automatically posted to your Classroom course. 

    :param _class: Unique identifier of the class
    :type _class: str
    :param body: 
    :type body: dict | bytes

    """
    body = AssignmentCreation.from_dict(body)
    return web.Response(status=200)


async def create_class(request: web.Request, body) -> web.Response:
    """Create a new class

    Classrooms on Flat allow you to create activities with assignments and post content to a specific group.  When creating a class, Flat automatically creates two groups: one for the teachers of the course, one for the students. The creator of this class is automatically added to the teachers group.  If the classsroom is synchronized with another application like Google Classroom, some of the meta information will automatically be updated.  You can add users to this class using &#x60;PUT /classes/{class}/users/{user}&#x60;, they will automatically added to the group based on their role on Flat. Users can also enroll themselves to this class using &#x60;POST /classes/enroll/{enrollmentCode}&#x60; and the &#x60;enrollmentCode&#x60; returned in the &#x60;ClassDetails&#x60; response. 

    :param body: 
    :type body: dict | bytes

    """
    body = ClassCreation.from_dict(body)
    return web.Response(status=200)


async def create_submission(request: web.Request, _class, assignment, body) -> web.Response:
    """Create or edit a submission

    Use this method as a student to create, update and submit a submission related to an assignment. Students can only set &#x60;attachments&#x60; and &#x60;submit&#x60;. Teachers can use &#x60;PUT /classes/{class}/assignments/{assignment}/submissions/{submission}&#x60; to update a submission by id. 

    :param _class: Unique identifier of the class
    :type _class: str
    :param assignment: Unique identifier of the assignment
    :type assignment: str
    :param body: 
    :type body: dict | bytes

    """
    body = AssignmentSubmissionUpdate.from_dict(body)
    return web.Response(status=200)


async def delete_class_user(request: web.Request, _class, user) -> web.Response:
    """Remove a user from the class

    This method can be used by a teacher to remove a user from the class, or by a student to leave the classroom.  Warning: Removing a user from the class will remove the associated resources, including the submissions and feedback related to these submissions. 

    :param _class: Unique identifier of the class
    :type _class: str
    :param user: Unique identifier of the user
    :type user: str

    """
    return web.Response(status=200)


async def delete_submission(request: web.Request, _class, assignment, submission) -> web.Response:
    """Delete a submission

    Use this method as a teacher to delete a submission and allow student to start over the assignment 

    :param _class: Unique identifier of the class
    :type _class: str
    :param assignment: Unique identifier of the assignment
    :type assignment: str
    :param submission: Unique identifier of the submission
    :type submission: str

    """
    return web.Response(status=200)


async def delete_submission_comment(request: web.Request, _class, assignment, submission, comment) -> web.Response:
    """Delete a feedback comment to a submission

    

    :param _class: Unique identifier of the class
    :type _class: str
    :param assignment: Unique identifier of the assignment
    :type assignment: str
    :param submission: Unique identifier of the submission
    :type submission: str
    :param comment: Unique identifier of the comment
    :type comment: str

    """
    return web.Response(status=200)


async def edit_submission(request: web.Request, _class, assignment, submission, body) -> web.Response:
    """Edit a submission

    Use this method as a teacher to update the different submission and give feedback. Teachers can only set &#x60;return&#x60;, &#x60;draftGrade&#x60; and &#x60;grade&#x60; 

    :param _class: Unique identifier of the class
    :type _class: str
    :param assignment: Unique identifier of the assignment
    :type assignment: str
    :param submission: Unique identifier of the submission
    :type submission: str
    :param body: 
    :type body: dict | bytes

    """
    body = AssignmentSubmissionUpdate.from_dict(body)
    return web.Response(status=200)


async def enroll_class(request: web.Request, enrollment_code) -> web.Response:
    """Join a class

    Use this method to join a class using an enrollment code given one of the teacher of this class. This code is also available in the &#x60;ClassDetails&#x60; returned to the teachers when creating the class or listing / fetching a specific class.  Flat will automatically add the user to the corresponding class group based on this role in the organization. 

    :param enrollment_code: The enrollment code, available to the teacher in &#x60;ClassDetails&#x60; 
    :type enrollment_code: str

    """
    return web.Response(status=200)


async def export_submissions_reviews_as_csv(request: web.Request, _class, assignment) -> web.Response:
    """CSV Grades exports

    Export list of submissions grades to a CSV file

    :param _class: Unique identifier of the class
    :type _class: str
    :param assignment: Unique identifier of the assignment
    :type assignment: str

    """
    return web.Response(status=200)


async def export_submissions_reviews_as_excel(request: web.Request, _class, assignment) -> web.Response:
    """Excel Grades exports

    Export list of submissions grades to an Excel file

    :param _class: Unique identifier of the class
    :type _class: str
    :param assignment: Unique identifier of the assignment
    :type assignment: str

    """
    return web.Response(status=200)


async def fork_score_0(request: web.Request, score, body, sharing_key=None) -> web.Response:
    """Fork a score

    This API call will make a copy of the last revision of the specified score and create a new score. The copy of the score will have a privacy set to &#x60;private&#x60;.  When using a [Flat for Education](https://flat.io/edu) account, the inline and contextualized comments will be accessible in the child document. 

    :param score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;). 
    :type score: str
    :param body: 
    :type body: dict | bytes
    :param sharing_key: This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document. 
    :type sharing_key: str

    """
    body = ScoreFork.from_dict(body)
    return web.Response(status=200)


async def get_class(request: web.Request, _class) -> web.Response:
    """Get the details of a single class

    

    :param _class: Unique identifier of the class
    :type _class: str

    """
    return web.Response(status=200)


async def get_score_submissions_0(request: web.Request, score) -> web.Response:
    """List submissions related to the score

    This API call will list the different assignments submissions where the score is attached. This method can be used by anyone that are part of the organization and have at least read access to the document. 

    :param score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;). 
    :type score: str

    """
    return web.Response(status=200)


async def get_submission(request: web.Request, _class, assignment, submission) -> web.Response:
    """Get a student submission

    

    :param _class: Unique identifier of the class
    :type _class: str
    :param assignment: Unique identifier of the assignment
    :type assignment: str
    :param submission: Unique identifier of the submission
    :type submission: str

    """
    return web.Response(status=200)


async def get_submission_comments(request: web.Request, _class, assignment, submission) -> web.Response:
    """List the feedback comments of a submission

    

    :param _class: Unique identifier of the class
    :type _class: str
    :param assignment: Unique identifier of the assignment
    :type assignment: str
    :param submission: Unique identifier of the submission
    :type submission: str

    """
    return web.Response(status=200)


async def get_submission_history(request: web.Request, _class, assignment, submission) -> web.Response:
    """Get the history of the submission

    For teachers only. Returns a detailed history of the submission. This currently includes state and grade histories. 

    :param _class: Unique identifier of the class
    :type _class: str
    :param assignment: Unique identifier of the assignment
    :type assignment: str
    :param submission: Unique identifier of the submission
    :type submission: str

    """
    return web.Response(status=200)


async def get_submissions(request: web.Request, _class, assignment) -> web.Response:
    """List the students&#39; submissions

    

    :param _class: Unique identifier of the class
    :type _class: str
    :param assignment: Unique identifier of the assignment
    :type assignment: str

    """
    return web.Response(status=200)


async def list_assignments(request: web.Request, _class) -> web.Response:
    """Assignments listing

    

    :param _class: Unique identifier of the class
    :type _class: str

    """
    return web.Response(status=200)


async def list_class_student_submissions(request: web.Request, _class, user) -> web.Response:
    """List the submissions for a student

    Use this method as a teacher to list all the assignment submissions sent by a student of the class 

    :param _class: Unique identifier of the class
    :type _class: str
    :param user: Unique identifier of the user
    :type user: str

    """
    return web.Response(status=200)


async def list_classes(request: web.Request, state=None) -> web.Response:
    """List the classes available for the current user

    

    :param state: Filter the classes by state
    :type state: str

    """
    return web.Response(status=200)


async def post_submission_comment(request: web.Request, _class, assignment, submission, body) -> web.Response:
    """Add a feedback comment to a submission

    

    :param _class: Unique identifier of the class
    :type _class: str
    :param assignment: Unique identifier of the assignment
    :type assignment: str
    :param submission: Unique identifier of the submission
    :type submission: str
    :param body: 
    :type body: dict | bytes

    """
    body = AssignmentSubmissionCommentCreation.from_dict(body)
    return web.Response(status=200)


async def unarchive_assignment(request: web.Request, _class, assignment) -> web.Response:
    """Unarchive the assignment.

    Mark the assignment as &#x60;active&#x60;. 

    :param _class: Unique identifier of the class
    :type _class: str
    :param assignment: Unique identifier of the assignment
    :type assignment: str

    """
    return web.Response(status=200)


async def unarchive_class(request: web.Request, _class) -> web.Response:
    """Unarchive the class

    Mark the class as &#x60;active&#x60;. When this course is synchronized with another app, like Google Classroom, this state will be automatically be updated. 

    :param _class: Unique identifier of the class
    :type _class: str

    """
    return web.Response(status=200)


async def update_class(request: web.Request, _class, body=None) -> web.Response:
    """Update the class

    Update the meta information of the class 

    :param _class: Unique identifier of the class
    :type _class: str
    :param body: Details of the Class
    :type body: dict | bytes

    """
    body = ClassUpdate.from_dict(body)
    return web.Response(status=200)


async def update_submission_comment(request: web.Request, _class, assignment, submission, comment, body) -> web.Response:
    """Update a feedback comment to a submission

    

    :param _class: Unique identifier of the class
    :type _class: str
    :param assignment: Unique identifier of the assignment
    :type assignment: str
    :param submission: Unique identifier of the submission
    :type submission: str
    :param comment: Unique identifier of the comment
    :type comment: str
    :param body: 
    :type body: dict | bytes

    """
    body = AssignmentSubmissionCommentCreation.from_dict(body)
    return web.Response(status=200)
