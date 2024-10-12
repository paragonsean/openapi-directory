QT += network

HEADERS += \
# Models
    $${PWD}/OAIDiagnostic_Get_200_response.h \
    $${PWD}/OAIDiagnostic_ListByService_200_response.h \
    $${PWD}/OAIDiagnostic_ListByService_200_response_value_inner.h \
    $${PWD}/OAIDiagnostic_ListByService_200_response_value_inner_properties.h \
    $${PWD}/OAIDiagnostic_ListByService_200_response_value_inner_properties_backend.h \
    $${PWD}/OAIDiagnostic_ListByService_200_response_value_inner_properties_backend_request.h \
    $${PWD}/OAIDiagnostic_ListByService_200_response_value_inner_properties_backend_request_body.h \
    $${PWD}/OAIDiagnostic_ListByService_200_response_value_inner_properties_sampling.h \
    $${PWD}/OAIDiagnostic_ListByService_default_response.h \
    $${PWD}/OAIDiagnostic_ListByService_default_response_error.h \
    $${PWD}/OAIDiagnostic_ListByService_default_response_error_details_inner.h \
# APIs
    $${PWD}/OAIDiagnosticApi.h \
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
    $${PWD}/OAIDiagnostic_Get_200_response.cpp \
    $${PWD}/OAIDiagnostic_ListByService_200_response.cpp \
    $${PWD}/OAIDiagnostic_ListByService_200_response_value_inner.cpp \
    $${PWD}/OAIDiagnostic_ListByService_200_response_value_inner_properties.cpp \
    $${PWD}/OAIDiagnostic_ListByService_200_response_value_inner_properties_backend.cpp \
    $${PWD}/OAIDiagnostic_ListByService_200_response_value_inner_properties_backend_request.cpp \
    $${PWD}/OAIDiagnostic_ListByService_200_response_value_inner_properties_backend_request_body.cpp \
    $${PWD}/OAIDiagnostic_ListByService_200_response_value_inner_properties_sampling.cpp \
    $${PWD}/OAIDiagnostic_ListByService_default_response.cpp \
    $${PWD}/OAIDiagnostic_ListByService_default_response_error.cpp \
    $${PWD}/OAIDiagnostic_ListByService_default_response_error_details_inner.cpp \
# APIs
    $${PWD}/OAIDiagnosticApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
