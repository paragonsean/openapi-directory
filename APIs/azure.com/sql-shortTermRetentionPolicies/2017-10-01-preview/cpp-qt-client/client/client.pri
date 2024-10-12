QT += network

HEADERS += \
# Models
    $${PWD}/OAIBackupShortTermRetentionPolicy.h \
    $${PWD}/OAIBackupShortTermRetentionPolicyListResult.h \
    $${PWD}/OAIBackupShortTermRetentionPolicyProperties.h \
# APIs
    $${PWD}/OAIBackupShortTermRetentionPoliciesApi.h \
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
    $${PWD}/OAIBackupShortTermRetentionPolicy.cpp \
    $${PWD}/OAIBackupShortTermRetentionPolicyListResult.cpp \
    $${PWD}/OAIBackupShortTermRetentionPolicyProperties.cpp \
# APIs
    $${PWD}/OAIBackupShortTermRetentionPoliciesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
