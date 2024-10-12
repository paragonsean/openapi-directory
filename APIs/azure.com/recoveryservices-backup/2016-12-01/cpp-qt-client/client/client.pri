QT += network

HEADERS += \
# Models
    $${PWD}/OAIBackupStorageConfig.h \
    $${PWD}/OAIBackupStorageConfigProperties.h \
    $${PWD}/OAIBackupVaultConfig.h \
    $${PWD}/OAIBackupVaultConfigProperties.h \
# APIs
    $${PWD}/OAIBackupStorageConfigsApi.h \
    $${PWD}/OAIBackupVaultConfigsApi.h \
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
    $${PWD}/OAIBackupStorageConfig.cpp \
    $${PWD}/OAIBackupStorageConfigProperties.cpp \
    $${PWD}/OAIBackupVaultConfig.cpp \
    $${PWD}/OAIBackupVaultConfigProperties.cpp \
# APIs
    $${PWD}/OAIBackupStorageConfigsApi.cpp \
    $${PWD}/OAIBackupVaultConfigsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
