QT += network

HEADERS += \
# Models
    $${PWD}/OAIExecAPI.h \
    $${PWD}/OAIForQuery.h \
    $${PWD}/OAIMarketStatXML_inner.h \
    $${PWD}/OAIType.h \
    $${PWD}/OAITypeStat.h \
    $${PWD}/OAITypeStatXML.h \
# APIs
    $${PWD}/OAIMarketstatApi.h \
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
    $${PWD}/OAIExecAPI.cpp \
    $${PWD}/OAIForQuery.cpp \
    $${PWD}/OAIMarketStatXML_inner.cpp \
    $${PWD}/OAIType.cpp \
    $${PWD}/OAITypeStat.cpp \
    $${PWD}/OAITypeStatXML.cpp \
# APIs
    $${PWD}/OAIMarketstatApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
