QT += network

HEADERS += \
# Models
    $${PWD}/OAIMigrationPhase.h \
    $${PWD}/OAIQuota.h \
    $${PWD}/OAIQuotaList.h \
    $${PWD}/OAIQuotaProperties.h \
# APIs
    $${PWD}/OAINetworkApi.h \
    $${PWD}/OAIQuotasApi.h \
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
    $${PWD}/OAIMigrationPhase.cpp \
    $${PWD}/OAIQuota.cpp \
    $${PWD}/OAIQuotaList.cpp \
    $${PWD}/OAIQuotaProperties.cpp \
# APIs
    $${PWD}/OAINetworkApi.cpp \
    $${PWD}/OAIQuotasApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
