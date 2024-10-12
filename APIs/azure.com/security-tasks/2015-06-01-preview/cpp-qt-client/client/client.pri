QT += network

HEADERS += \
# Models
    $${PWD}/OAISecurityTask.h \
    $${PWD}/OAISecurityTaskList.h \
    $${PWD}/OAISecurityTaskParameters.h \
    $${PWD}/OAISecurityTaskProperties.h \
    $${PWD}/OAITasks_ListByHomeRegion_default_response.h \
    $${PWD}/OAITasks_ListByHomeRegion_default_response_error.h \
# APIs
    $${PWD}/OAITasksApi.h \
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
    $${PWD}/OAISecurityTask.cpp \
    $${PWD}/OAISecurityTaskList.cpp \
    $${PWD}/OAISecurityTaskParameters.cpp \
    $${PWD}/OAISecurityTaskProperties.cpp \
    $${PWD}/OAITasks_ListByHomeRegion_default_response.cpp \
    $${PWD}/OAITasks_ListByHomeRegion_default_response_error.cpp \
# APIs
    $${PWD}/OAITasksApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
