QT += network

HEADERS += \
# Models
    $${PWD}/OAICache_Get_200_response.h \
    $${PWD}/OAICache_ListByService_200_response.h \
    $${PWD}/OAICache_ListByService_200_response_value_inner.h \
    $${PWD}/OAICache_ListByService_200_response_value_inner_properties.h \
    $${PWD}/OAICache_ListByService_default_response.h \
    $${PWD}/OAICache_ListByService_default_response_error.h \
    $${PWD}/OAICache_ListByService_default_response_error_details_inner.h \
    $${PWD}/OAICache_Update_request.h \
    $${PWD}/OAICache_Update_request_properties.h \
# APIs
    $${PWD}/OAICacheApi.h \
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
    $${PWD}/OAICache_Get_200_response.cpp \
    $${PWD}/OAICache_ListByService_200_response.cpp \
    $${PWD}/OAICache_ListByService_200_response_value_inner.cpp \
    $${PWD}/OAICache_ListByService_200_response_value_inner_properties.cpp \
    $${PWD}/OAICache_ListByService_default_response.cpp \
    $${PWD}/OAICache_ListByService_default_response_error.cpp \
    $${PWD}/OAICache_ListByService_default_response_error_details_inner.cpp \
    $${PWD}/OAICache_Update_request.cpp \
    $${PWD}/OAICache_Update_request_properties.cpp \
# APIs
    $${PWD}/OAICacheApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
