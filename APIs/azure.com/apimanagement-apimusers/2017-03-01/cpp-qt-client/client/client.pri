QT += network

HEADERS += \
# Models
    $${PWD}/OAIGenerateSsoUrlResult.h \
    $${PWD}/OAIUserCollection.h \
    $${PWD}/OAIUserContract.h \
    $${PWD}/OAIUserContractProperties.h \
    $${PWD}/OAIUserCreateParameterProperties.h \
    $${PWD}/OAIUserCreateParameters.h \
    $${PWD}/OAIUserEntityBaseParameters.h \
    $${PWD}/OAIUserGroup_List_200_response.h \
    $${PWD}/OAIUserGroup_List_200_response_value_inner.h \
    $${PWD}/OAIUserGroup_List_200_response_value_inner_properties.h \
    $${PWD}/OAIUserIdentityCollection.h \
    $${PWD}/OAIUserIdentityContract.h \
    $${PWD}/OAIUserSubscription_List_200_response.h \
    $${PWD}/OAIUserSubscription_List_200_response_value_inner.h \
    $${PWD}/OAIUserSubscription_List_200_response_value_inner_properties.h \
    $${PWD}/OAIUserTokenParameters.h \
    $${PWD}/OAIUserTokenResult.h \
    $${PWD}/OAIUserUpdateParameters.h \
    $${PWD}/OAIUserUpdateParametersProperties.h \
    $${PWD}/OAIUser_ListByService_default_response.h \
    $${PWD}/OAIUser_ListByService_default_response_details_inner.h \
# APIs
    $${PWD}/OAIUserGroupsApi.h \
    $${PWD}/OAIUserIdentitiesApi.h \
    $${PWD}/OAIUserSubscriptionsApi.h \
    $${PWD}/OAIUsersApi.h \
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
    $${PWD}/OAIGenerateSsoUrlResult.cpp \
    $${PWD}/OAIUserCollection.cpp \
    $${PWD}/OAIUserContract.cpp \
    $${PWD}/OAIUserContractProperties.cpp \
    $${PWD}/OAIUserCreateParameterProperties.cpp \
    $${PWD}/OAIUserCreateParameters.cpp \
    $${PWD}/OAIUserEntityBaseParameters.cpp \
    $${PWD}/OAIUserGroup_List_200_response.cpp \
    $${PWD}/OAIUserGroup_List_200_response_value_inner.cpp \
    $${PWD}/OAIUserGroup_List_200_response_value_inner_properties.cpp \
    $${PWD}/OAIUserIdentityCollection.cpp \
    $${PWD}/OAIUserIdentityContract.cpp \
    $${PWD}/OAIUserSubscription_List_200_response.cpp \
    $${PWD}/OAIUserSubscription_List_200_response_value_inner.cpp \
    $${PWD}/OAIUserSubscription_List_200_response_value_inner_properties.cpp \
    $${PWD}/OAIUserTokenParameters.cpp \
    $${PWD}/OAIUserTokenResult.cpp \
    $${PWD}/OAIUserUpdateParameters.cpp \
    $${PWD}/OAIUserUpdateParametersProperties.cpp \
    $${PWD}/OAIUser_ListByService_default_response.cpp \
    $${PWD}/OAIUser_ListByService_default_response_details_inner.cpp \
# APIs
    $${PWD}/OAIUserGroupsApi.cpp \
    $${PWD}/OAIUserIdentitiesApi.cpp \
    $${PWD}/OAIUserSubscriptionsApi.cpp \
    $${PWD}/OAIUsersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
