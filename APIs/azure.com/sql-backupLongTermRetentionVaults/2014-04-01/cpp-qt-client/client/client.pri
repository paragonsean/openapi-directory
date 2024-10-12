QT += network

HEADERS += \
# Models
    $${PWD}/OAIBackupLongTermRetentionVault.h \
    $${PWD}/OAIBackupLongTermRetentionVaultListResult.h \
    $${PWD}/OAIBackupLongTermRetentionVaultProperties.h \
# APIs
    $${PWD}/OAIBackupLongTermRetentionVaultsApi.h \
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
    $${PWD}/OAIBackupLongTermRetentionVault.cpp \
    $${PWD}/OAIBackupLongTermRetentionVaultListResult.cpp \
    $${PWD}/OAIBackupLongTermRetentionVaultProperties.cpp \
# APIs
    $${PWD}/OAIBackupLongTermRetentionVaultsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
