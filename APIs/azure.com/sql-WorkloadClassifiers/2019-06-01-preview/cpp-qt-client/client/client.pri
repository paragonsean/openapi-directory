QT += network

HEADERS += \
# Models
    $${PWD}/OAIProxyResource.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAIWorkloadClassifier.h \
    $${PWD}/OAIWorkloadClassifierListResult.h \
    $${PWD}/OAIWorkloadClassifierProperties.h \
# APIs
    $${PWD}/OAIWorkloadClassifiersApi.h \
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
    $${PWD}/OAIWorkloadClassifier.cpp \
    $${PWD}/OAIWorkloadClassifierListResult.cpp \
    $${PWD}/OAIWorkloadClassifierProperties.cpp \
# APIs
    $${PWD}/OAIWorkloadClassifiersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
