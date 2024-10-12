QT += network

HEADERS += \
# Models
    $${PWD}/OAIBackend_Get_200_response.h \
    $${PWD}/OAIBackend_ListByService_200_response.h \
    $${PWD}/OAIBackend_ListByService_200_response_value_inner.h \
    $${PWD}/OAIBackend_ListByService_200_response_value_inner_properties.h \
    $${PWD}/OAIBackend_ListByService_default_response.h \
    $${PWD}/OAIBackend_ListByService_default_response_error.h \
    $${PWD}/OAIBackend_ListByService_default_response_error_details_inner.h \
    $${PWD}/OAIBackend_Reconnect_request.h \
    $${PWD}/OAIBackend_Reconnect_request_properties.h \
    $${PWD}/OAIBackend_Update_request.h \
    $${PWD}/OAIBackend_Update_request_properties.h \
# APIs
    $${PWD}/OAIBackendApi.h \
    $${PWD}/OAIBackendReconnectApi.h \
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
    $${PWD}/OAIBackend_Get_200_response.cpp \
    $${PWD}/OAIBackend_ListByService_200_response.cpp \
    $${PWD}/OAIBackend_ListByService_200_response_value_inner.cpp \
    $${PWD}/OAIBackend_ListByService_200_response_value_inner_properties.cpp \
    $${PWD}/OAIBackend_ListByService_default_response.cpp \
    $${PWD}/OAIBackend_ListByService_default_response_error.cpp \
    $${PWD}/OAIBackend_ListByService_default_response_error_details_inner.cpp \
    $${PWD}/OAIBackend_Reconnect_request.cpp \
    $${PWD}/OAIBackend_Reconnect_request_properties.cpp \
    $${PWD}/OAIBackend_Update_request.cpp \
    $${PWD}/OAIBackend_Update_request_properties.cpp \
# APIs
    $${PWD}/OAIBackendApi.cpp \
    $${PWD}/OAIBackendReconnectApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
