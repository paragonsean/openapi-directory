QT += network

HEADERS += \
# Models
    $${PWD}/OAIResource.h \
    $${PWD}/OAIRestorableDroppedManagedDatabase.h \
    $${PWD}/OAIRestorableDroppedManagedDatabaseListResult.h \
    $${PWD}/OAIRestorableDroppedManagedDatabaseProperties.h \
    $${PWD}/OAITrackedResource.h \
# APIs
    $${PWD}/OAIRestorableDroppedManagedDatabasesApi.h \
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
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAIRestorableDroppedManagedDatabase.cpp \
    $${PWD}/OAIRestorableDroppedManagedDatabaseListResult.cpp \
    $${PWD}/OAIRestorableDroppedManagedDatabaseProperties.cpp \
    $${PWD}/OAITrackedResource.cpp \
# APIs
    $${PWD}/OAIRestorableDroppedManagedDatabasesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
