QT += network

HEADERS += \
# Models
    $${PWD}/OAIGroupCollection.h \
    $${PWD}/OAIGroupContract.h \
    $${PWD}/OAIGroupContractProperties.h \
    $${PWD}/OAIGroupCreateParameters.h \
    $${PWD}/OAIGroupCreateParametersProperties.h \
    $${PWD}/OAIGroupUpdateParameters.h \
    $${PWD}/OAIGroupUpdateParametersProperties.h \
    $${PWD}/OAIGroupUser_Create_200_response.h \
    $${PWD}/OAIGroupUser_List_200_response.h \
    $${PWD}/OAIGroupUser_List_200_response_value_inner.h \
    $${PWD}/OAIGroupUser_List_200_response_value_inner_properties.h \
    $${PWD}/OAIGroupUser_List_200_response_value_inner_properties_groups_inner.h \
    $${PWD}/OAIGroup_Get_default_response.h \
    $${PWD}/OAIGroup_Get_default_response_error.h \
    $${PWD}/OAIGroup_Get_default_response_error_details_inner.h \
# APIs
    $${PWD}/OAIGroupUsersApi.h \
    $${PWD}/OAIGroupsApi.h \
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
    $${PWD}/OAIGroupCollection.cpp \
    $${PWD}/OAIGroupContract.cpp \
    $${PWD}/OAIGroupContractProperties.cpp \
    $${PWD}/OAIGroupCreateParameters.cpp \
    $${PWD}/OAIGroupCreateParametersProperties.cpp \
    $${PWD}/OAIGroupUpdateParameters.cpp \
    $${PWD}/OAIGroupUpdateParametersProperties.cpp \
    $${PWD}/OAIGroupUser_Create_200_response.cpp \
    $${PWD}/OAIGroupUser_List_200_response.cpp \
    $${PWD}/OAIGroupUser_List_200_response_value_inner.cpp \
    $${PWD}/OAIGroupUser_List_200_response_value_inner_properties.cpp \
    $${PWD}/OAIGroupUser_List_200_response_value_inner_properties_groups_inner.cpp \
    $${PWD}/OAIGroup_Get_default_response.cpp \
    $${PWD}/OAIGroup_Get_default_response_error.cpp \
    $${PWD}/OAIGroup_Get_default_response_error_details_inner.cpp \
# APIs
    $${PWD}/OAIGroupUsersApi.cpp \
    $${PWD}/OAIGroupsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
