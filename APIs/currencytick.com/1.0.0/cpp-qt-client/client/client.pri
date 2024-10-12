QT += network

HEADERS += \
# Models
    $${PWD}/OAIHealthcheck_200_response.h \
    $${PWD}/OAIHealthcheck_400_response.h \
    $${PWD}/OAIHistoricalExchangeRate_200_response.h \
# APIs
    $${PWD}/OAIEndpointsApi.h \
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
    $${PWD}/OAIHealthcheck_200_response.cpp \
    $${PWD}/OAIHealthcheck_400_response.cpp \
    $${PWD}/OAIHistoricalExchangeRate_200_response.cpp \
# APIs
    $${PWD}/OAIEndpointsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
