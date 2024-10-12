QT += network

HEADERS += \
# Models
    $${PWD}/OAIPolicy_Get_200_response.h \
    $${PWD}/OAIPolicy_ListByService_200_response.h \
    $${PWD}/OAIPolicy_ListByService_200_response_value_inner.h \
    $${PWD}/OAIPolicy_ListByService_200_response_value_inner_properties.h \
    $${PWD}/OAIPolicy_ListByService_default_response.h \
    $${PWD}/OAIPolicy_ListByService_default_response_error.h \
    $${PWD}/OAIPolicy_ListByService_default_response_error_details_inner.h \
# APIs
    $${PWD}/OAIPolicyApi.h \
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
    $${PWD}/OAIPolicy_Get_200_response.cpp \
    $${PWD}/OAIPolicy_ListByService_200_response.cpp \
    $${PWD}/OAIPolicy_ListByService_200_response_value_inner.cpp \
    $${PWD}/OAIPolicy_ListByService_200_response_value_inner_properties.cpp \
    $${PWD}/OAIPolicy_ListByService_default_response.cpp \
    $${PWD}/OAIPolicy_ListByService_default_response_error.cpp \
    $${PWD}/OAIPolicy_ListByService_default_response_error_details_inner.cpp \
# APIs
    $${PWD}/OAIPolicyApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
