QT += network

HEADERS += \
# Models
    $${PWD}/OAIManagedInstance.h \
    $${PWD}/OAIManagedInstanceListResult.h \
    $${PWD}/OAIManagedInstanceProperties.h \
    $${PWD}/OAIManagedInstanceUpdate.h \
    $${PWD}/OAIManagedInstanceUpdate_sku.h \
# APIs
    $${PWD}/OAIManagedInstancesApi.h \
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
    $${PWD}/OAIManagedInstance.cpp \
    $${PWD}/OAIManagedInstanceListResult.cpp \
    $${PWD}/OAIManagedInstanceProperties.cpp \
    $${PWD}/OAIManagedInstanceUpdate.cpp \
    $${PWD}/OAIManagedInstanceUpdate_sku.cpp \
# APIs
    $${PWD}/OAIManagedInstancesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
