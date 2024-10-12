QT += network

HEADERS += \
# Models
    $${PWD}/OAIListOperationsResponse.h \
    $${PWD}/OAILogicalInterface.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationMetadata.h \
    $${PWD}/OAIReconciliationOperationMetadata.h \
    $${PWD}/OAIServerNetworkTemplate.h \
    $${PWD}/OAIStatus.h \
# APIs
    $${PWD}/OAIOperationsApi.h \
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
    $${PWD}/OAIListOperationsResponse.cpp \
    $${PWD}/OAILogicalInterface.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationMetadata.cpp \
    $${PWD}/OAIReconciliationOperationMetadata.cpp \
    $${PWD}/OAIServerNetworkTemplate.cpp \
    $${PWD}/OAIStatus.cpp \
# APIs
    $${PWD}/OAIOperationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
