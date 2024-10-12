QT += network

HEADERS += \
# Models
    $${PWD}/OAIBackupLongTermRetentionPolicy.h \
    $${PWD}/OAILongTermRetentionBackup.h \
    $${PWD}/OAILongTermRetentionBackupListResult.h \
    $${PWD}/OAILongTermRetentionBackupProperties.h \
    $${PWD}/OAILongTermRetentionPolicyProperties.h \
# APIs
    $${PWD}/OAIBackupLongTermRetentionPoliciesApi.h \
    $${PWD}/OAILongTermRetentionBackupsApi.h \
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
    $${PWD}/OAILongTermRetentionBackup.cpp \
    $${PWD}/OAILongTermRetentionBackupListResult.cpp \
    $${PWD}/OAILongTermRetentionBackupProperties.cpp \
    $${PWD}/OAILongTermRetentionPolicyProperties.cpp \
# APIs
    $${PWD}/OAIBackupLongTermRetentionPoliciesApi.cpp \
    $${PWD}/OAILongTermRetentionBackupsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
