QT += network

HEADERS += \
# Models
    $${PWD}/OAIDatabaseBlobAuditingPolicy.h \
    $${PWD}/OAIDatabaseBlobAuditingPolicyListResult.h \
    $${PWD}/OAIDatabaseBlobAuditingPolicyProperties.h \
    $${PWD}/OAIExtendedDatabaseBlobAuditingPolicy.h \
    $${PWD}/OAIExtendedDatabaseBlobAuditingPolicyProperties.h \
    $${PWD}/OAIExtendedServerBlobAuditingPolicy.h \
    $${PWD}/OAIExtendedServerBlobAuditingPolicyProperties.h \
    $${PWD}/OAIServerBlobAuditingPolicy.h \
    $${PWD}/OAIServerBlobAuditingPolicyListResult.h \
    $${PWD}/OAIServerBlobAuditingPolicyProperties.h \
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
    $${PWD}/OAIDatabaseBlobAuditingPolicyListResult.cpp \
    $${PWD}/OAIDatabaseBlobAuditingPolicyProperties.cpp \
    $${PWD}/OAIExtendedDatabaseBlobAuditingPolicy.cpp \
    $${PWD}/OAIExtendedDatabaseBlobAuditingPolicyProperties.cpp \
    $${PWD}/OAIExtendedServerBlobAuditingPolicy.cpp \
    $${PWD}/OAIExtendedServerBlobAuditingPolicyProperties.cpp \
    $${PWD}/OAIServerBlobAuditingPolicy.cpp \
    $${PWD}/OAIServerBlobAuditingPolicyListResult.cpp \
    $${PWD}/OAIServerBlobAuditingPolicyProperties.cpp \
# APIs
    $${PWD}/OAIBlobAuditingApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
