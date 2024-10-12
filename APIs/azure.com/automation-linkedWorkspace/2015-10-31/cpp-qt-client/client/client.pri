QT += network

HEADERS += \
# Models
    $${PWD}/OAILinkedWorkspace.h \
    $${PWD}/OAILinkedWorkspace_Get_default_response.h \
# APIs
    $${PWD}/OAILinkedWorkspaceApi.h \
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
    $${PWD}/OAILinkedWorkspace.cpp \
    $${PWD}/OAILinkedWorkspace_Get_default_response.cpp \
# APIs
    $${PWD}/OAILinkedWorkspaceApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
