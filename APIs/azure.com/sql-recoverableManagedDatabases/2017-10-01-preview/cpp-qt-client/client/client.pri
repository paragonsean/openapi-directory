QT += network

HEADERS += \
# Models
    $${PWD}/OAIProxyResource.h \
    $${PWD}/OAIRecoverableManagedDatabase.h \
    $${PWD}/OAIRecoverableManagedDatabaseListResult.h \
    $${PWD}/OAIRecoverableManagedDatabaseProperties.h \
    $${PWD}/OAIResource.h \
# APIs
    $${PWD}/OAIRecoverableManagedDatabasesApi.h \
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
    $${PWD}/OAIProxyResource.cpp \
    $${PWD}/OAIRecoverableManagedDatabase.cpp \
    $${PWD}/OAIRecoverableManagedDatabaseListResult.cpp \
    $${PWD}/OAIRecoverableManagedDatabaseProperties.cpp \
    $${PWD}/OAIResource.cpp \
# APIs
    $${PWD}/OAIRecoverableManagedDatabasesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
