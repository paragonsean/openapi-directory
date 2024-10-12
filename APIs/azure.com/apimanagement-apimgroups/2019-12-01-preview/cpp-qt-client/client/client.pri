QT += network

HEADERS += \
# Models
    $${PWD}/OAIGroupUser_Create_200_response.h \
    $${PWD}/OAIGroupUser_List_200_response.h \
    $${PWD}/OAIGroupUser_List_200_response_value_inner.h \
    $${PWD}/OAIGroupUser_List_200_response_value_inner_properties.h \
    $${PWD}/OAIGroup_CreateOrUpdate_request.h \
    $${PWD}/OAIGroup_CreateOrUpdate_request_properties.h \
    $${PWD}/OAIGroup_Get_200_response.h \
    $${PWD}/OAIGroup_ListByService_200_response.h \
    $${PWD}/OAIGroup_ListByService_200_response_value_inner.h \
    $${PWD}/OAIGroup_ListByService_200_response_value_inner_properties.h \
    $${PWD}/OAIGroup_ListByService_default_response.h \
    $${PWD}/OAIGroup_ListByService_default_response_error.h \
    $${PWD}/OAIGroup_ListByService_default_response_error_details_inner.h \
    $${PWD}/OAIGroup_Update_request.h \
    $${PWD}/OAIGroup_Update_request_properties.h \
# APIs
    $${PWD}/OAIGroupApi.h \
    $${PWD}/OAIGroupUserApi.h \
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
    $${PWD}/OAIGroupUser_Create_200_response.cpp \
    $${PWD}/OAIGroupUser_List_200_response.cpp \
    $${PWD}/OAIGroupUser_List_200_response_value_inner.cpp \
    $${PWD}/OAIGroupUser_List_200_response_value_inner_properties.cpp \
    $${PWD}/OAIGroup_CreateOrUpdate_request.cpp \
    $${PWD}/OAIGroup_CreateOrUpdate_request_properties.cpp \
    $${PWD}/OAIGroup_Get_200_response.cpp \
    $${PWD}/OAIGroup_ListByService_200_response.cpp \
    $${PWD}/OAIGroup_ListByService_200_response_value_inner.cpp \
    $${PWD}/OAIGroup_ListByService_200_response_value_inner_properties.cpp \
    $${PWD}/OAIGroup_ListByService_default_response.cpp \
    $${PWD}/OAIGroup_ListByService_default_response_error.cpp \
    $${PWD}/OAIGroup_ListByService_default_response_error_details_inner.cpp \
    $${PWD}/OAIGroup_Update_request.cpp \
    $${PWD}/OAIGroup_Update_request_properties.cpp \
# APIs
    $${PWD}/OAIGroupApi.cpp \
    $${PWD}/OAIGroupUserApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
