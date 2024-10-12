QT += network

HEADERS += \
# Models
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationListResult.h \
    $${PWD}/OAIOperation_display.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAIWorkspace.h \
    $${PWD}/OAIWorkspaceKeysResponse.h \
    $${PWD}/OAIWorkspaceListResult.h \
    $${PWD}/OAIWorkspaceProperties.h \
    $${PWD}/OAIWorkspacePropertiesUpdateParameters.h \
    $${PWD}/OAIWorkspaceUpdateParameters.h \
# APIs
    $${PWD}/OAIOperationApi.h \
    $${PWD}/OAIWorkspacesApi.h \
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
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationListResult.cpp \
    $${PWD}/OAIOperation_display.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAIWorkspace.cpp \
    $${PWD}/OAIWorkspaceKeysResponse.cpp \
    $${PWD}/OAIWorkspaceListResult.cpp \
    $${PWD}/OAIWorkspaceProperties.cpp \
    $${PWD}/OAIWorkspacePropertiesUpdateParameters.cpp \
    $${PWD}/OAIWorkspaceUpdateParameters.cpp \
# APIs
    $${PWD}/OAIOperationApi.cpp \
    $${PWD}/OAIWorkspacesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
