QT += network

HEADERS += \
# Models
    $${PWD}/OAIServerConnectionPolicy.h \
    $${PWD}/OAIServerConnectionPolicyProperties.h \
# APIs
    $${PWD}/OAIConnectionPoliciesApi.h \
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
    $${PWD}/OAIServerConnectionPolicy.cpp \
    $${PWD}/OAIServerConnectionPolicyProperties.cpp \
# APIs
    $${PWD}/OAIConnectionPoliciesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
