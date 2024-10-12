QT += network

HEADERS += \
# Models
    $${PWD}/OAIAccount_unauthorized.h \
    $${PWD}/OAIAvailable_numbers.h \
    $${PWD}/OAIAvailablenumber.h \
    $${PWD}/OAIInbound_numbers.h \
    $${PWD}/OAIOwnednumber.h \
    $${PWD}/OAIResponse.h \
    $${PWD}/OAIResponse420.h \
    $${PWD}/OAIUnauthorized.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
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
    $${PWD}/OAIAccount_unauthorized.cpp \
    $${PWD}/OAIAvailable_numbers.cpp \
    $${PWD}/OAIAvailablenumber.cpp \
    $${PWD}/OAIInbound_numbers.cpp \
    $${PWD}/OAIOwnednumber.cpp \
    $${PWD}/OAIResponse.cpp \
    $${PWD}/OAIResponse420.cpp \
    $${PWD}/OAIUnauthorized.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
