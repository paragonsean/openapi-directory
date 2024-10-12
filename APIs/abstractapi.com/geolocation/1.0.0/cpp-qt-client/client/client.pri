QT += network

HEADERS += \
# Models
    $${PWD}/OAIInline_response_200.h \
    $${PWD}/OAIInline_response_200_connection.h \
    $${PWD}/OAIInline_response_200_currency.h \
    $${PWD}/OAIInline_response_200_flag.h \
    $${PWD}/OAIInline_response_200_security.h \
    $${PWD}/OAIInline_response_200_timezone.h \
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
    $${PWD}/OAIInline_response_200.cpp \
    $${PWD}/OAIInline_response_200_connection.cpp \
    $${PWD}/OAIInline_response_200_currency.cpp \
    $${PWD}/OAIInline_response_200_flag.cpp \
    $${PWD}/OAIInline_response_200_security.cpp \
    $${PWD}/OAIInline_response_200_timezone.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
