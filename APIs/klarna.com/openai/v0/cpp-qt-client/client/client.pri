QT += network

HEADERS += \
# Models
    $${PWD}/OAIProduct.h \
    $${PWD}/OAIProductResponse.h \
# APIs
    $${PWD}/OAIOpenAiProductEndpointApi.h \
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
    $${PWD}/OAIProduct.cpp \
    $${PWD}/OAIProductResponse.cpp \
# APIs
    $${PWD}/OAIOpenAiProductEndpointApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
