QT += network

HEADERS += \
# Models
    $${PWD}/OAIOpenIdConnectProviderCollection.h \
    $${PWD}/OAIOpenIdConnectProviders_Get_default_response.h \
    $${PWD}/OAIOpenIdConnectProviders_Get_default_response_details_inner.h \
    $${PWD}/OAIOpenidConnectProviderContract.h \
    $${PWD}/OAIOpenidConnectProviderCreateContract.h \
    $${PWD}/OAIOpenidConnectProviderUpdateContract.h \
# APIs
    $${PWD}/OAIOpenIdConnectProvidersApi.h \
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
    $${PWD}/OAIOpenIdConnectProviderCollection.cpp \
    $${PWD}/OAIOpenIdConnectProviders_Get_default_response.cpp \
    $${PWD}/OAIOpenIdConnectProviders_Get_default_response_details_inner.cpp \
    $${PWD}/OAIOpenidConnectProviderContract.cpp \
    $${PWD}/OAIOpenidConnectProviderCreateContract.cpp \
    $${PWD}/OAIOpenidConnectProviderUpdateContract.cpp \
# APIs
    $${PWD}/OAIOpenIdConnectProvidersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
