QT += network

HEADERS += \
# Models
    $${PWD}/OAIManagementLockListResult.h \
    $${PWD}/OAIManagementLockObject.h \
    $${PWD}/OAIManagementLockProperties.h \
# APIs
    $${PWD}/OAIManagementLocksApi.h \
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
    $${PWD}/OAIManagementLockListResult.cpp \
    $${PWD}/OAIManagementLockObject.cpp \
    $${PWD}/OAIManagementLockProperties.cpp \
# APIs
    $${PWD}/OAIManagementLocksApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
