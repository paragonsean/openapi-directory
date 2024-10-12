QT += network

HEADERS += \
# Models
    $${PWD}/OAIIdentityProvider_Get_200_response.h \
    $${PWD}/OAIIdentityProvider_ListByService_200_response.h \
    $${PWD}/OAIIdentityProvider_ListByService_200_response_value_inner.h \
    $${PWD}/OAIIdentityProvider_ListByService_200_response_value_inner_properties.h \
    $${PWD}/OAIIdentityProvider_ListByService_default_response.h \
    $${PWD}/OAIIdentityProvider_ListByService_default_response_error.h \
    $${PWD}/OAIIdentityProvider_ListByService_default_response_error_details_inner.h \
    $${PWD}/OAIIdentityProvider_Update_request.h \
    $${PWD}/OAIIdentityProvider_Update_request_properties.h \
# APIs
    $${PWD}/OAIIdentityProviderApi.h \
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
    $${PWD}/OAIIdentityProvider_Get_200_response.cpp \
    $${PWD}/OAIIdentityProvider_ListByService_200_response.cpp \
    $${PWD}/OAIIdentityProvider_ListByService_200_response_value_inner.cpp \
    $${PWD}/OAIIdentityProvider_ListByService_200_response_value_inner_properties.cpp \
    $${PWD}/OAIIdentityProvider_ListByService_default_response.cpp \
    $${PWD}/OAIIdentityProvider_ListByService_default_response_error.cpp \
    $${PWD}/OAIIdentityProvider_ListByService_default_response_error_details_inner.cpp \
    $${PWD}/OAIIdentityProvider_Update_request.cpp \
    $${PWD}/OAIIdentityProvider_Update_request_properties.cpp \
# APIs
    $${PWD}/OAIIdentityProviderApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
