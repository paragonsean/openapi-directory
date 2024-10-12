QT += network

HEADERS += \
# Models
    $${PWD}/OAIAccount.h \
    $${PWD}/OAIAccountListResult.h \
    $${PWD}/OAIAccountProperties.h \
    $${PWD}/OAIAccountPropertiesUpdateParameters.h \
    $${PWD}/OAIAccountUpdateParameters.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationListResult.h \
    $${PWD}/OAIOperation_display.h \
    $${PWD}/OAIProject.h \
    $${PWD}/OAIProjectListResult.h \
    $${PWD}/OAIProjectProperties.h \
    $${PWD}/OAIProjectPropertiesUpdateParameters.h \
    $${PWD}/OAIProjectUpdateParameters.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAIStorageAccountProperties.h \
    $${PWD}/OAIWorkspace.h \
    $${PWD}/OAIWorkspaceListResult.h \
    $${PWD}/OAIWorkspaceProperties.h \
    $${PWD}/OAIWorkspacePropertiesUpdateParameters.h \
    $${PWD}/OAIWorkspaceUpdateParameters.h \
# APIs
    $${PWD}/OAIAccountsApi.h \
    $${PWD}/OAIOperationApi.h \
    $${PWD}/OAIProjectsApi.h \
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
    $${PWD}/OAIAccount.cpp \
    $${PWD}/OAIAccountListResult.cpp \
    $${PWD}/OAIAccountProperties.cpp \
    $${PWD}/OAIAccountPropertiesUpdateParameters.cpp \
    $${PWD}/OAIAccountUpdateParameters.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationListResult.cpp \
    $${PWD}/OAIOperation_display.cpp \
    $${PWD}/OAIProject.cpp \
    $${PWD}/OAIProjectListResult.cpp \
    $${PWD}/OAIProjectProperties.cpp \
    $${PWD}/OAIProjectPropertiesUpdateParameters.cpp \
    $${PWD}/OAIProjectUpdateParameters.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAIStorageAccountProperties.cpp \
    $${PWD}/OAIWorkspace.cpp \
    $${PWD}/OAIWorkspaceListResult.cpp \
    $${PWD}/OAIWorkspaceProperties.cpp \
    $${PWD}/OAIWorkspacePropertiesUpdateParameters.cpp \
    $${PWD}/OAIWorkspaceUpdateParameters.cpp \
# APIs
    $${PWD}/OAIAccountsApi.cpp \
    $${PWD}/OAIOperationApi.cpp \
    $${PWD}/OAIProjectsApi.cpp \
    $${PWD}/OAIWorkspacesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
