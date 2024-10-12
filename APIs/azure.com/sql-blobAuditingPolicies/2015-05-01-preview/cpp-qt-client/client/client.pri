QT += network

HEADERS += \
# Models
    $${PWD}/OAIDatabaseBlobAuditingPolicy.h \
    $${PWD}/OAIDatabaseBlobAuditingPolicyProperties.h \
# APIs
    $${PWD}/OAIBlobAuditingApi.h \
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
    $${PWD}/OAIDatabaseBlobAuditingPolicy.cpp \
    $${PWD}/OAIDatabaseBlobAuditingPolicyProperties.cpp \
# APIs
    $${PWD}/OAIBlobAuditingApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
