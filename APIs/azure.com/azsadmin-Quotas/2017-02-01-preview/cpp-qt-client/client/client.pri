QT += network

HEADERS += \
# Models
    $${PWD}/OAIQuota.h \
    $${PWD}/OAIQuotaList.h \
# APIs
    $${PWD}/OAIKeyVaultApi.h \
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
# APIs
    $${PWD}/OAIKeyVaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
