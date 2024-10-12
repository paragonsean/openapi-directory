QT += network

HEADERS += \
# Models
    $${PWD}/OAIEmailTemplate_CreateOrUpdate_request.h \
    $${PWD}/OAIEmailTemplate_CreateOrUpdate_request_properties.h \
    $${PWD}/OAIEmailTemplate_Get_200_response.h \
    $${PWD}/OAIEmailTemplate_ListByService_200_response.h \
    $${PWD}/OAIEmailTemplate_ListByService_200_response_value_inner.h \
    $${PWD}/OAIEmailTemplate_ListByService_200_response_value_inner_properties.h \
    $${PWD}/OAIEmailTemplate_ListByService_200_response_value_inner_properties_parameters_inner.h \
    $${PWD}/OAIEmailTemplate_ListByService_default_response.h \
    $${PWD}/OAIEmailTemplate_ListByService_default_response_error.h \
    $${PWD}/OAIEmailTemplate_ListByService_default_response_error_details_inner.h \
# APIs
    $${PWD}/OAIEmailTemplateApi.h \
    $${PWD}/OAIEmailTemplatesApi.h \
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
    $${PWD}/OAIEmailTemplate_CreateOrUpdate_request.cpp \
    $${PWD}/OAIEmailTemplate_CreateOrUpdate_request_properties.cpp \
    $${PWD}/OAIEmailTemplate_Get_200_response.cpp \
    $${PWD}/OAIEmailTemplate_ListByService_200_response.cpp \
    $${PWD}/OAIEmailTemplate_ListByService_200_response_value_inner.cpp \
    $${PWD}/OAIEmailTemplate_ListByService_200_response_value_inner_properties.cpp \
    $${PWD}/OAIEmailTemplate_ListByService_200_response_value_inner_properties_parameters_inner.cpp \
    $${PWD}/OAIEmailTemplate_ListByService_default_response.cpp \
    $${PWD}/OAIEmailTemplate_ListByService_default_response_error.cpp \
    $${PWD}/OAIEmailTemplate_ListByService_default_response_error_details_inner.cpp \
# APIs
    $${PWD}/OAIEmailTemplateApi.cpp \
    $${PWD}/OAIEmailTemplatesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
