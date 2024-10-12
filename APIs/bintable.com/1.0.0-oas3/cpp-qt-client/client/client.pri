QT += network

HEADERS += \
# Models
    $${PWD}/OAIResponseItem.h \
# APIs
    $${PWD}/OAIBalanceApi.h \
    $${PWD}/OAILookupApi.h \
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
    $${PWD}/OAIResponseItem.cpp \
# APIs
    $${PWD}/OAIBalanceApi.cpp \
    $${PWD}/OAILookupApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
