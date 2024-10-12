QT += network

HEADERS += \
# Models
    $${PWD}/OAIIdentityProviderBaseParameters.h \
    $${PWD}/OAIIdentityProviderContract.h \
    $${PWD}/OAIIdentityProviderContractProperties.h \
    $${PWD}/OAIIdentityProviderList.h \
    $${PWD}/OAIIdentityProviderUpdateParameters.h \
    $${PWD}/OAIIdentityProviderUpdateProperties.h \
    $${PWD}/OAIIdentityProvider_ListByService_default_response.h \
    $${PWD}/OAIIdentityProvider_ListByService_default_response_error.h \
    $${PWD}/OAIIdentityProvider_ListByService_default_response_error_details_inner.h \
# APIs
    $${PWD}/OAIIdentityProviderApi.h \
    $${PWD}/OAIIdentityProvidersApi.h \
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
    $${PWD}/OAIIdentityProviderBaseParameters.cpp \
    $${PWD}/OAIIdentityProviderContract.cpp \
    $${PWD}/OAIIdentityProviderContractProperties.cpp \
    $${PWD}/OAIIdentityProviderList.cpp \
    $${PWD}/OAIIdentityProviderUpdateParameters.cpp \
    $${PWD}/OAIIdentityProviderUpdateProperties.cpp \
    $${PWD}/OAIIdentityProvider_ListByService_default_response.cpp \
    $${PWD}/OAIIdentityProvider_ListByService_default_response_error.cpp \
    $${PWD}/OAIIdentityProvider_ListByService_default_response_error_details_inner.cpp \
# APIs
    $${PWD}/OAIIdentityProviderApi.cpp \
    $${PWD}/OAIIdentityProvidersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
