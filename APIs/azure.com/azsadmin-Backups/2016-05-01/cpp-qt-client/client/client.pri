QT += network

HEADERS += \
# Models
    $${PWD}/OAIBackup.h \
    $${PWD}/OAIBackupInfo.h \
    $${PWD}/OAIBackupList.h \
    $${PWD}/OAIBackupModel.h \
    $${PWD}/OAIOperationStatus.h \
    $${PWD}/OAIRoleOperationStatus.h \
# APIs
    $${PWD}/OAIBackupsApi.h \
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
    $${PWD}/OAIBackup.cpp \
    $${PWD}/OAIBackupInfo.cpp \
    $${PWD}/OAIBackupList.cpp \
    $${PWD}/OAIBackupModel.cpp \
    $${PWD}/OAIOperationStatus.cpp \
    $${PWD}/OAIRoleOperationStatus.cpp \
# APIs
    $${PWD}/OAIBackupsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
