QT += network

HEADERS += \
# Models
    $${PWD}/OAITag_CreateOrUpdate_request.h \
    $${PWD}/OAITag_Get_200_response.h \
    $${PWD}/OAITag_ListByService_200_response.h \
    $${PWD}/OAITag_ListByService_200_response_value_inner.h \
    $${PWD}/OAITag_ListByService_200_response_value_inner_properties.h \
    $${PWD}/OAITag_ListByService_default_response.h \
    $${PWD}/OAITag_ListByService_default_response_error.h \
    $${PWD}/OAITag_ListByService_default_response_error_details_inner.h \
# APIs
    $${PWD}/OAITagApi.h \
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
    $${PWD}/OAITag_CreateOrUpdate_request.cpp \
    $${PWD}/OAITag_Get_200_response.cpp \
    $${PWD}/OAITag_ListByService_200_response.cpp \
    $${PWD}/OAITag_ListByService_200_response_value_inner.cpp \
    $${PWD}/OAITag_ListByService_200_response_value_inner_properties.cpp \
    $${PWD}/OAITag_ListByService_default_response.cpp \
    $${PWD}/OAITag_ListByService_default_response_error.cpp \
    $${PWD}/OAITag_ListByService_default_response_error_details_inner.cpp \
# APIs
    $${PWD}/OAITagApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
