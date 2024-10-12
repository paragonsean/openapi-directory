QT += network

HEADERS += \
# Models
# APIs
    $${PWD}/OAIFactOfTheDayApi.h \
    $${PWD}/OAINumberFactsApi.h \
    $${PWD}/OAIOnThisDayApi.h \
    $${PWD}/OAIPrivateFactsApi.h \
    $${PWD}/OAIRandomFactsApi.h \
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
# APIs
    $${PWD}/OAIFactOfTheDayApi.cpp \
    $${PWD}/OAINumberFactsApi.cpp \
    $${PWD}/OAIOnThisDayApi.cpp \
    $${PWD}/OAIPrivateFactsApi.cpp \
    $${PWD}/OAIRandomFactsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
