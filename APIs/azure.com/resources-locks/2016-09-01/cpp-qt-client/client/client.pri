QT += network

HEADERS += \
# Models
    $${PWD}/OAIManagementLockListResult.h \
    $${PWD}/OAIManagementLockObject.h \
    $${PWD}/OAIManagementLockOwner.h \
    $${PWD}/OAIManagementLockProperties.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationListResult.h \
    $${PWD}/OAIOperation_display.h \
# APIs
    $${PWD}/OAIManagementLocksApi.h \
    $${PWD}/OAIOperationsApi.h \
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
    $${PWD}/OAIManagementLockOwner.cpp \
    $${PWD}/OAIManagementLockProperties.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationListResult.cpp \
    $${PWD}/OAIOperation_display.cpp \
# APIs
    $${PWD}/OAIManagementLocksApi.cpp \
    $${PWD}/OAIOperationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
