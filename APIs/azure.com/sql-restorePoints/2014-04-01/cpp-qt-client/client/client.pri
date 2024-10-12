QT += network

HEADERS += \
# Models
    $${PWD}/OAIRestorePoint.h \
    $${PWD}/OAIRestorePointListResult.h \
    $${PWD}/OAIRestorePointProperties.h \
# APIs
    $${PWD}/OAIDatabaseBackupApi.h \
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
    $${PWD}/OAIRestorePoint.cpp \
    $${PWD}/OAIRestorePointListResult.cpp \
    $${PWD}/OAIRestorePointProperties.cpp \
# APIs
    $${PWD}/OAIDatabaseBackupApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
