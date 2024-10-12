QT += network

HEADERS += \
# Models
    $${PWD}/OAICreateDatabaseRestorePointDefinition.h \
    $${PWD}/OAIRestorePoint.h \
    $${PWD}/OAIRestorePointListResult.h \
    $${PWD}/OAIRestorePointProperties.h \
# APIs
    $${PWD}/OAIRestorePointsApi.h \
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
    $${PWD}/OAICreateDatabaseRestorePointDefinition.cpp \
    $${PWD}/OAIRestorePoint.cpp \
    $${PWD}/OAIRestorePointListResult.cpp \
    $${PWD}/OAIRestorePointProperties.cpp \
# APIs
    $${PWD}/OAIRestorePointsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
