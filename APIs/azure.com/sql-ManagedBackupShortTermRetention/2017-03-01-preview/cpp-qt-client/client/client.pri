QT += network

HEADERS += \
# Models
    $${PWD}/OAIManagedBackupShortTermRetentionPolicy.h \
    $${PWD}/OAIManagedBackupShortTermRetentionPolicyListResult.h \
    $${PWD}/OAIManagedBackupShortTermRetentionPolicyProperties.h \
    $${PWD}/OAIProxyResource.h \
    $${PWD}/OAIResource.h \
# APIs
    $${PWD}/OAIManagedBackupShortTermRetentionPoliciesApi.h \
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
    $${PWD}/OAIManagedBackupShortTermRetentionPolicy.cpp \
    $${PWD}/OAIManagedBackupShortTermRetentionPolicyListResult.cpp \
    $${PWD}/OAIManagedBackupShortTermRetentionPolicyProperties.cpp \
    $${PWD}/OAIProxyResource.cpp \
    $${PWD}/OAIResource.cpp \
# APIs
    $${PWD}/OAIManagedBackupShortTermRetentionPoliciesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
