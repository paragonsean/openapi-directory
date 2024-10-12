QT += network

HEADERS += \
# Models
    $${PWD}/OAIAuthorizationServer_Get_200_response.h \
    $${PWD}/OAIAuthorizationServer_ListByService_200_response.h \
    $${PWD}/OAIAuthorizationServer_ListByService_200_response_value_inner.h \
    $${PWD}/OAIAuthorizationServer_ListByService_200_response_value_inner_properties.h \
    $${PWD}/OAIAuthorizationServer_ListByService_default_response.h \
    $${PWD}/OAIAuthorizationServer_ListByService_default_response_error.h \
    $${PWD}/OAIAuthorizationServer_ListByService_default_response_error_details_inner.h \
    $${PWD}/OAIAuthorizationServer_Update_request.h \
    $${PWD}/OAIAuthorizationServer_Update_request_properties.h \
# APIs
    $${PWD}/OAIAuthorizationServerApi.h \
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
    $${PWD}/OAIAuthorizationServer_Get_200_response.cpp \
    $${PWD}/OAIAuthorizationServer_ListByService_200_response.cpp \
    $${PWD}/OAIAuthorizationServer_ListByService_200_response_value_inner.cpp \
    $${PWD}/OAIAuthorizationServer_ListByService_200_response_value_inner_properties.cpp \
    $${PWD}/OAIAuthorizationServer_ListByService_default_response.cpp \
    $${PWD}/OAIAuthorizationServer_ListByService_default_response_error.cpp \
    $${PWD}/OAIAuthorizationServer_ListByService_default_response_error_details_inner.cpp \
    $${PWD}/OAIAuthorizationServer_Update_request.cpp \
    $${PWD}/OAIAuthorizationServer_Update_request_properties.cpp \
# APIs
    $${PWD}/OAIAuthorizationServerApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
