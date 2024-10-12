QT += network

HEADERS += \
# Models
    $${PWD}/OAIApiVersionSet_Get_200_response.h \
    $${PWD}/OAIApiVersionSet_ListByService_200_response.h \
    $${PWD}/OAIApiVersionSet_ListByService_200_response_value_inner.h \
    $${PWD}/OAIApiVersionSet_ListByService_200_response_value_inner_properties.h \
    $${PWD}/OAIApiVersionSet_ListByService_default_response.h \
    $${PWD}/OAIApiVersionSet_ListByService_default_response_error.h \
    $${PWD}/OAIApiVersionSet_ListByService_default_response_error_details_inner.h \
    $${PWD}/OAIApiVersionSet_Update_request.h \
    $${PWD}/OAIApiVersionSet_Update_request_properties.h \
# APIs
    $${PWD}/OAIApiVersionSetsApi.h \
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
    $${PWD}/OAIApiVersionSet_Get_200_response.cpp \
    $${PWD}/OAIApiVersionSet_ListByService_200_response.cpp \
    $${PWD}/OAIApiVersionSet_ListByService_200_response_value_inner.cpp \
    $${PWD}/OAIApiVersionSet_ListByService_200_response_value_inner_properties.cpp \
    $${PWD}/OAIApiVersionSet_ListByService_default_response.cpp \
    $${PWD}/OAIApiVersionSet_ListByService_default_response_error.cpp \
    $${PWD}/OAIApiVersionSet_ListByService_default_response_error_details_inner.cpp \
    $${PWD}/OAIApiVersionSet_Update_request.cpp \
    $${PWD}/OAIApiVersionSet_Update_request_properties.cpp \
# APIs
    $${PWD}/OAIApiVersionSetsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
