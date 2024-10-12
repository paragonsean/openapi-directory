QT += network

HEADERS += \
# Models
    $${PWD}/OAIAddCommentRequest.h \
    $${PWD}/OAIAssignee.h \
    $${PWD}/OAIEditTaskRequest.h \
    $${PWD}/OAIFollower.h \
    $${PWD}/OAINewNoteRequest.h \
    $${PWD}/OAINewNoteRequest_target.h \
    $${PWD}/OAINewNote_request.h \
    $${PWD}/OAINewNote_request_target.h \
    $${PWD}/OAINewTaskRequest.h \
    $${PWD}/OAITarget.h \
# APIs
    $${PWD}/OAINoteApi.h \
    $${PWD}/OAITaskApi.h \
# Others
    $${PWD}/OAIHelpers.h \
    $${PWD}/OAIHttpRequest.h \
    $${PWD}/OAIObject.h \
    $${PWD}/OAIEnum.h \
    $${PWD}/OAIHttpFileElement.h \
    $${PWD}/OAIServerConfiguration.h \
    $${PWD}/OAIServerVariable.h \
    $${PWD}/OAIOauth.h

SOURCES += \
# Models
    $${PWD}/OAIAddCommentRequest.cpp \
    $${PWD}/OAIAssignee.cpp \
    $${PWD}/OAIEditTaskRequest.cpp \
    $${PWD}/OAIFollower.cpp \
    $${PWD}/OAINewNoteRequest.cpp \
    $${PWD}/OAINewNoteRequest_target.cpp \
    $${PWD}/OAINewNote_request.cpp \
    $${PWD}/OAINewNote_request_target.cpp \
    $${PWD}/OAINewTaskRequest.cpp \
    $${PWD}/OAITarget.cpp \
# APIs
    $${PWD}/OAINoteApi.cpp \
    $${PWD}/OAITaskApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
