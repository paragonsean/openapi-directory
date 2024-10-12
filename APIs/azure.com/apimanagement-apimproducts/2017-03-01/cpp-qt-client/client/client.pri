QT += network

HEADERS += \
# Models
    $${PWD}/OAIProductApi_CreateOrUpdate_200_response.h \
    $${PWD}/OAIProductApi_CreateOrUpdate_200_response_allOf_allOf_authenticationSettings.h \
    $${PWD}/OAIProductApi_CreateOrUpdate_200_response_allOf_allOf_authenticationSettings_oAuth2.h \
    $${PWD}/OAIProductApi_CreateOrUpdate_200_response_allOf_allOf_subscriptionKeyParameterNames.h \
    $${PWD}/OAIProductApi_ListByProduct_200_response.h \
    $${PWD}/OAIProductApi_ListByProduct_200_response_value_inner.h \
    $${PWD}/OAIProductCollection.h \
    $${PWD}/OAIProductContract.h \
    $${PWD}/OAIProductContractProperties.h \
    $${PWD}/OAIProductEntityBaseParameters.h \
    $${PWD}/OAIProductGroup_CreateOrUpdate_200_response.h \
    $${PWD}/OAIProductGroup_ListByProduct_200_response.h \
    $${PWD}/OAIProductGroup_ListByProduct_200_response_value_inner.h \
    $${PWD}/OAIProductPolicy_ListByProduct_200_response.h \
    $${PWD}/OAIProductPolicy_ListByProduct_200_response_value_inner.h \
    $${PWD}/OAIProductSubscriptions_List_200_response.h \
    $${PWD}/OAIProductSubscriptions_List_200_response_value_inner.h \
    $${PWD}/OAIProductUpdateParameters.h \
    $${PWD}/OAIProduct_List_default_response.h \
    $${PWD}/OAIProduct_List_default_response_details_inner.h \
# APIs
    $${PWD}/OAIProductApisApi.h \
    $${PWD}/OAIProductGroupsApi.h \
    $${PWD}/OAIProductPolicyApi.h \
    $${PWD}/OAIProductSubscriptionsApi.h \
    $${PWD}/OAIProductsApi.h \
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
    $${PWD}/OAIProductApi_CreateOrUpdate_200_response.cpp \
    $${PWD}/OAIProductApi_CreateOrUpdate_200_response_allOf_allOf_authenticationSettings.cpp \
    $${PWD}/OAIProductApi_CreateOrUpdate_200_response_allOf_allOf_authenticationSettings_oAuth2.cpp \
    $${PWD}/OAIProductApi_CreateOrUpdate_200_response_allOf_allOf_subscriptionKeyParameterNames.cpp \
    $${PWD}/OAIProductApi_ListByProduct_200_response.cpp \
    $${PWD}/OAIProductApi_ListByProduct_200_response_value_inner.cpp \
    $${PWD}/OAIProductCollection.cpp \
    $${PWD}/OAIProductContract.cpp \
    $${PWD}/OAIProductContractProperties.cpp \
    $${PWD}/OAIProductEntityBaseParameters.cpp \
    $${PWD}/OAIProductGroup_CreateOrUpdate_200_response.cpp \
    $${PWD}/OAIProductGroup_ListByProduct_200_response.cpp \
    $${PWD}/OAIProductGroup_ListByProduct_200_response_value_inner.cpp \
    $${PWD}/OAIProductPolicy_ListByProduct_200_response.cpp \
    $${PWD}/OAIProductPolicy_ListByProduct_200_response_value_inner.cpp \
    $${PWD}/OAIProductSubscriptions_List_200_response.cpp \
    $${PWD}/OAIProductSubscriptions_List_200_response_value_inner.cpp \
    $${PWD}/OAIProductUpdateParameters.cpp \
    $${PWD}/OAIProduct_List_default_response.cpp \
    $${PWD}/OAIProduct_List_default_response_details_inner.cpp \
# APIs
    $${PWD}/OAIProductApisApi.cpp \
    $${PWD}/OAIProductGroupsApi.cpp \
    $${PWD}/OAIProductPolicyApi.cpp \
    $${PWD}/OAIProductSubscriptionsApi.cpp \
    $${PWD}/OAIProductsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
