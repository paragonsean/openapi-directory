QT += network

HEADERS += \
# Models
    $${PWD}/OAIBackupLongTermRetentionPolicy.h \
    $${PWD}/OAIBackupLongTermRetentionPolicyListResult.h \
    $${PWD}/OAIBackupLongTermRetentionPolicyProperties.h \
# APIs
    $${PWD}/OAIBackupLongTermRetentionPoliciesApi.h \
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
    $${PWD}/OAIBackupLongTermRetentionPolicy.cpp \
    $${PWD}/OAIBackupLongTermRetentionPolicyListResult.cpp \
    $${PWD}/OAIBackupLongTermRetentionPolicyProperties.cpp \
# APIs
    $${PWD}/OAIBackupLongTermRetentionPoliciesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
