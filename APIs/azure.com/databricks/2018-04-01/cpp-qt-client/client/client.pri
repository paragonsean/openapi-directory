QT += network

HEADERS += \
# Models
    $${PWD}/OAIErrorDetail.h \
    $${PWD}/OAIErrorInfo.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationListResult.h \
    $${PWD}/OAIOperation_display.h \
    $${PWD}/OAIProvisioningState.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAISku.h \
    $${PWD}/OAITrackedResource.h \
    $${PWD}/OAIWorkspace.h \
    $${PWD}/OAIWorkspaceCustomBooleanParameter.h \
    $${PWD}/OAIWorkspaceCustomObjectParameter.h \
    $${PWD}/OAIWorkspaceCustomParameterType.h \
    $${PWD}/OAIWorkspaceCustomParameters.h \
    $${PWD}/OAIWorkspaceCustomStringParameter.h \
    $${PWD}/OAIWorkspaceListResult.h \
    $${PWD}/OAIWorkspaceProperties.h \
    $${PWD}/OAIWorkspaceProviderAuthorization.h \
    $${PWD}/OAIWorkspaceUpdate.h \
# APIs
    $${PWD}/OAIOperationsApi.h \
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
    $${PWD}/OAIErrorDetail.cpp \
    $${PWD}/OAIErrorInfo.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationListResult.cpp \
    $${PWD}/OAIOperation_display.cpp \
    $${PWD}/OAIProvisioningState.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAISku.cpp \
    $${PWD}/OAITrackedResource.cpp \
    $${PWD}/OAIWorkspace.cpp \
    $${PWD}/OAIWorkspaceCustomBooleanParameter.cpp \
    $${PWD}/OAIWorkspaceCustomObjectParameter.cpp \
    $${PWD}/OAIWorkspaceCustomParameterType.cpp \
    $${PWD}/OAIWorkspaceCustomParameters.cpp \
    $${PWD}/OAIWorkspaceCustomStringParameter.cpp \
    $${PWD}/OAIWorkspaceListResult.cpp \
    $${PWD}/OAIWorkspaceProperties.cpp \
    $${PWD}/OAIWorkspaceProviderAuthorization.cpp \
    $${PWD}/OAIWorkspaceUpdate.cpp \
# APIs
    $${PWD}/OAIOperationsApi.cpp \
    $${PWD}/OAIWorkspacesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
