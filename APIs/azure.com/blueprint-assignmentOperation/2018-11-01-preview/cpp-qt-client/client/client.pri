QT += network

HEADERS += \
# Models
    $${PWD}/OAIAssignmentDeploymentJob.h \
    $${PWD}/OAIAssignmentDeploymentJobResult.h \
    $${PWD}/OAIAssignmentJobCreatedResource.h \
    $${PWD}/OAIAssignmentOperation.h \
    $${PWD}/OAIAssignmentOperationList.h \
    $${PWD}/OAIAssignmentOperationProperties.h \
    $${PWD}/OAIAzureResourceBase.h \
    $${PWD}/OAIAzureResourceManagerError.h \
# APIs
    $${PWD}/OAIAssignmentOperationsApi.h \
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
    $${PWD}/OAIAssignmentDeploymentJob.cpp \
    $${PWD}/OAIAssignmentDeploymentJobResult.cpp \
    $${PWD}/OAIAssignmentJobCreatedResource.cpp \
    $${PWD}/OAIAssignmentOperation.cpp \
    $${PWD}/OAIAssignmentOperationList.cpp \
    $${PWD}/OAIAssignmentOperationProperties.cpp \
    $${PWD}/OAIAzureResourceBase.cpp \
    $${PWD}/OAIAzureResourceManagerError.cpp \
# APIs
    $${PWD}/OAIAssignmentOperationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
