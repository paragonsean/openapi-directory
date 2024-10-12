QT += network

HEADERS += \
# Models
    $${PWD}/OAIDelegatedProviders_List_200_response.h \
    $${PWD}/OAIDelegatedProviders_List_200_response_value_inner.h \
# APIs
    $${PWD}/OAIDelegatedProvidersApi.h \
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
    $${PWD}/OAIDelegatedProviders_List_200_response.cpp \
    $${PWD}/OAIDelegatedProviders_List_200_response_value_inner.cpp \
# APIs
    $${PWD}/OAIDelegatedProvidersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
