QT += network

HEADERS += \
# Models
    $${PWD}/OAIManagedInstanceOperation.h \
    $${PWD}/OAIManagedInstanceOperationListResult.h \
    $${PWD}/OAIManagedInstanceOperationProperties.h \
    $${PWD}/OAIProxyResource.h \
    $${PWD}/OAIResource.h \
# APIs
    $${PWD}/OAIManagedInstanceOperationsApi.h \
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
    $${PWD}/OAIManagedInstanceOperation.cpp \
    $${PWD}/OAIManagedInstanceOperationListResult.cpp \
    $${PWD}/OAIManagedInstanceOperationProperties.cpp \
    $${PWD}/OAIProxyResource.cpp \
    $${PWD}/OAIResource.cpp \
# APIs
    $${PWD}/OAIManagedInstanceOperationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
