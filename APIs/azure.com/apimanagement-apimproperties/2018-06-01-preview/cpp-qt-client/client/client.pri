QT += network

HEADERS += \
# Models
    $${PWD}/OAIProperty_Get_200_response.h \
    $${PWD}/OAIProperty_ListByService_200_response.h \
    $${PWD}/OAIProperty_ListByService_200_response_value_inner.h \
    $${PWD}/OAIProperty_ListByService_200_response_value_inner_properties.h \
    $${PWD}/OAIProperty_ListByService_default_response.h \
    $${PWD}/OAIProperty_ListByService_default_response_error.h \
    $${PWD}/OAIProperty_ListByService_default_response_error_details_inner.h \
    $${PWD}/OAIProperty_Update_request.h \
    $${PWD}/OAIProperty_Update_request_properties.h \
# APIs
    $${PWD}/OAIPropertyApi.h \
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
    $${PWD}/OAIProperty_Get_200_response.cpp \
    $${PWD}/OAIProperty_ListByService_200_response.cpp \
    $${PWD}/OAIProperty_ListByService_200_response_value_inner.cpp \
    $${PWD}/OAIProperty_ListByService_200_response_value_inner_properties.cpp \
    $${PWD}/OAIProperty_ListByService_default_response.cpp \
    $${PWD}/OAIProperty_ListByService_default_response_error.cpp \
    $${PWD}/OAIProperty_ListByService_default_response_error_details_inner.cpp \
    $${PWD}/OAIProperty_Update_request.cpp \
    $${PWD}/OAIProperty_Update_request_properties.cpp \
# APIs
    $${PWD}/OAIPropertyApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
