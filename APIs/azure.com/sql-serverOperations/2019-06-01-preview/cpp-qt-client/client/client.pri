QT += network

HEADERS += \
# Models
    $${PWD}/OAIProxyResource.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAIServerOperation.h \
    $${PWD}/OAIServerOperationListResult.h \
    $${PWD}/OAIServerOperationProperties.h \
# APIs
    $${PWD}/OAIServerOperationsApi.h \
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
    $${PWD}/OAIProxyResource.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAIServerOperation.cpp \
    $${PWD}/OAIServerOperationListResult.cpp \
    $${PWD}/OAIServerOperationProperties.cpp \
# APIs
    $${PWD}/OAIServerOperationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
