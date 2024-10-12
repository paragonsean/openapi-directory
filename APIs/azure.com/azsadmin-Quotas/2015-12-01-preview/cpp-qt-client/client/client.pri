QT += network

HEADERS += \
# Models
    $${PWD}/OAIQuota.h \
    $${PWD}/OAIQuotaList.h \
    $${PWD}/OAIQuotaProperties.h \
# APIs
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
    $${PWD}/OAIQuota.cpp \
    $${PWD}/OAIQuotaList.cpp \
    $${PWD}/OAIQuotaProperties.cpp \
# APIs
    $${PWD}/OAIQuotasApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
