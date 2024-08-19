QT += network

HEADERS += \
# Models
    $${PWD}/OAIServerDnsAlias.h \
    $${PWD}/OAIServerDnsAliasAcquisition.h \
    $${PWD}/OAIServerDnsAliasListResult.h \
    $${PWD}/OAIServerDnsAliasProperties.h \
# APIs
    $${PWD}/OAIServerDnsAliasesApi.h \
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
    $${PWD}/OAIServerDnsAlias.cpp \
    $${PWD}/OAIServerDnsAliasAcquisition.cpp \
    $${PWD}/OAIServerDnsAliasListResult.cpp \
    $${PWD}/OAIServerDnsAliasProperties.cpp \
# APIs
    $${PWD}/OAIServerDnsAliasesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
