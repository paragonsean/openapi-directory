QT += network

HEADERS += \
# Models
    $${PWD}/OAIOpenIdConnectProviderCollection.h \
    $${PWD}/OAIOpenIdConnectProvider_Get_default_response.h \
    $${PWD}/OAIOpenIdConnectProvider_Get_default_response_details_inner.h \
    $${PWD}/OAIOpenidConnectProviderContract.h \
    $${PWD}/OAIOpenidConnectProviderContractProperties.h \
    $${PWD}/OAIOpenidConnectProviderUpdateContract.h \
    $${PWD}/OAIOpenidConnectProviderUpdateContractProperties.h \
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
    $${PWD}/OAIOpenIdConnectProvider_Get_default_response.cpp \
    $${PWD}/OAIOpenIdConnectProvider_Get_default_response_details_inner.cpp \
    $${PWD}/OAIOpenidConnectProviderContract.cpp \
    $${PWD}/OAIOpenidConnectProviderContractProperties.cpp \
    $${PWD}/OAIOpenidConnectProviderUpdateContract.cpp \
    $${PWD}/OAIOpenidConnectProviderUpdateContractProperties.cpp \
# APIs
    $${PWD}/OAIOpenIdConnectProvidersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
