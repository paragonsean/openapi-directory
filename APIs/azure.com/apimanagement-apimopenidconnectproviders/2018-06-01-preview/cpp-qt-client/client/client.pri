QT += network

HEADERS += \
# Models
    $${PWD}/OAIOpenIdConnectProvider_Get_200_response.h \
    $${PWD}/OAIOpenIdConnectProvider_ListByService_200_response.h \
    $${PWD}/OAIOpenIdConnectProvider_ListByService_200_response_value_inner.h \
    $${PWD}/OAIOpenIdConnectProvider_ListByService_200_response_value_inner_properties.h \
    $${PWD}/OAIOpenIdConnectProvider_ListByService_default_response.h \
    $${PWD}/OAIOpenIdConnectProvider_ListByService_default_response_error.h \
    $${PWD}/OAIOpenIdConnectProvider_ListByService_default_response_error_details_inner.h \
    $${PWD}/OAIOpenIdConnectProvider_Update_request.h \
    $${PWD}/OAIOpenIdConnectProvider_Update_request_properties.h \
# APIs
    $${PWD}/OAIOpenidConnectProviderApi.h \
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
    $${PWD}/OAIOpenIdConnectProvider_Get_200_response.cpp \
    $${PWD}/OAIOpenIdConnectProvider_ListByService_200_response.cpp \
    $${PWD}/OAIOpenIdConnectProvider_ListByService_200_response_value_inner.cpp \
    $${PWD}/OAIOpenIdConnectProvider_ListByService_200_response_value_inner_properties.cpp \
    $${PWD}/OAIOpenIdConnectProvider_ListByService_default_response.cpp \
    $${PWD}/OAIOpenIdConnectProvider_ListByService_default_response_error.cpp \
    $${PWD}/OAIOpenIdConnectProvider_ListByService_default_response_error_details_inner.cpp \
    $${PWD}/OAIOpenIdConnectProvider_Update_request.cpp \
    $${PWD}/OAIOpenIdConnectProvider_Update_request_properties.cpp \
# APIs
    $${PWD}/OAIOpenidConnectProviderApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
