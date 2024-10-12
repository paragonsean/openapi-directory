QT += network

HEADERS += \
# Models
    $${PWD}/OAIDiagnosticCollection.h \
    $${PWD}/OAIDiagnosticContract.h \
    $${PWD}/OAIDiagnosticContractProperties.h \
    $${PWD}/OAIDiagnosticLogger_CreateOrUpdate_200_response.h \
    $${PWD}/OAIDiagnosticLogger_ListByService_200_response.h \
    $${PWD}/OAIDiagnosticLogger_ListByService_200_response_value_inner.h \
    $${PWD}/OAIDiagnosticLogger_ListByService_200_response_value_inner_properties.h \
    $${PWD}/OAIDiagnostic_ListByService_default_response.h \
    $${PWD}/OAIDiagnostic_ListByService_default_response_error.h \
    $${PWD}/OAIDiagnostic_ListByService_default_response_error_details_inner.h \
# APIs
    $${PWD}/OAIDiagnosticLoggersApi.h \
    $${PWD}/OAIDiagnosticsApi.h \
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
    $${PWD}/OAIDiagnosticCollection.cpp \
    $${PWD}/OAIDiagnosticContract.cpp \
    $${PWD}/OAIDiagnosticContractProperties.cpp \
    $${PWD}/OAIDiagnosticLogger_CreateOrUpdate_200_response.cpp \
    $${PWD}/OAIDiagnosticLogger_ListByService_200_response.cpp \
    $${PWD}/OAIDiagnosticLogger_ListByService_200_response_value_inner.cpp \
    $${PWD}/OAIDiagnosticLogger_ListByService_200_response_value_inner_properties.cpp \
    $${PWD}/OAIDiagnostic_ListByService_default_response.cpp \
    $${PWD}/OAIDiagnostic_ListByService_default_response_error.cpp \
    $${PWD}/OAIDiagnostic_ListByService_default_response_error_details_inner.cpp \
# APIs
    $${PWD}/OAIDiagnosticLoggersApi.cpp \
    $${PWD}/OAIDiagnosticsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
