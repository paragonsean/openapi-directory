QT += network

HEADERS += \
# Models
    $${PWD}/OAIGenerateSsoUrlResult.h \
    $${PWD}/OAIUserCollection.h \
    $${PWD}/OAIUserContract.h \
    $${PWD}/OAIUserCreateParameters.h \
    $${PWD}/OAIUserGroups_ListByUsers_200_response.h \
    $${PWD}/OAIUserGroups_ListByUsers_200_response_value_inner.h \
    $${PWD}/OAIUserIdentityCollection.h \
    $${PWD}/OAIUserIdentityContract.h \
    $${PWD}/OAIUserSubscriptions_ListByUsers_200_response.h \
    $${PWD}/OAIUserSubscriptions_ListByUsers_200_response_value_inner.h \
    $${PWD}/OAIUserTokenParameters.h \
    $${PWD}/OAIUserTokenResult.h \
    $${PWD}/OAIUserUpdateParameters.h \
    $${PWD}/OAIUsers_ListByService_default_response.h \
    $${PWD}/OAIUsers_ListByService_default_response_details_inner.h \
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
    $${PWD}/OAIUserCreateParameters.cpp \
    $${PWD}/OAIUserGroups_ListByUsers_200_response.cpp \
    $${PWD}/OAIUserGroups_ListByUsers_200_response_value_inner.cpp \
    $${PWD}/OAIUserIdentityCollection.cpp \
    $${PWD}/OAIUserIdentityContract.cpp \
    $${PWD}/OAIUserSubscriptions_ListByUsers_200_response.cpp \
    $${PWD}/OAIUserSubscriptions_ListByUsers_200_response_value_inner.cpp \
    $${PWD}/OAIUserTokenParameters.cpp \
    $${PWD}/OAIUserTokenResult.cpp \
    $${PWD}/OAIUserUpdateParameters.cpp \
    $${PWD}/OAIUsers_ListByService_default_response.cpp \
    $${PWD}/OAIUsers_ListByService_default_response_details_inner.cpp \
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
