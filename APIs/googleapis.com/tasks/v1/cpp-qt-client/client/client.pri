QT += network

HEADERS += \
# Models
    $${PWD}/OAITask.h \
    $${PWD}/OAITaskList.h \
    $${PWD}/OAITaskLists.h \
    $${PWD}/OAITask_links_inner.h \
    $${PWD}/OAITasks.h \
# APIs
    $${PWD}/OAITasklistsApi.h \
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
    $${PWD}/OAITask.cpp \
    $${PWD}/OAITaskList.cpp \
    $${PWD}/OAITaskLists.cpp \
    $${PWD}/OAITask_links_inner.cpp \
    $${PWD}/OAITasks.cpp \
# APIs
    $${PWD}/OAITasklistsApi.cpp \
    $${PWD}/OAITasksApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
