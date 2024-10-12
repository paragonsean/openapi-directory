QT += network

HEADERS += \
# Models
    $${PWD}/OAIProductApis_ListByProducts_200_response.h \
    $${PWD}/OAIProductApis_ListByProducts_200_response_value_inner.h \
    $${PWD}/OAIProductCollection.h \
    $${PWD}/OAIProductContract.h \
    $${PWD}/OAIProductGroups_ListByProducts_200_response.h \
    $${PWD}/OAIProductGroups_ListByProducts_200_response_value_inner.h \
    $${PWD}/OAIProductSubscriptions_ListByProducts_200_response.h \
    $${PWD}/OAIProductSubscriptions_ListByProducts_200_response_value_inner.h \
    $${PWD}/OAIProductUpdateParameters.h \
    $${PWD}/OAIProducts_ListByService_default_response.h \
    $${PWD}/OAIProducts_ListByService_default_response_details_inner.h \
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
    $${PWD}/OAIProductApis_ListByProducts_200_response.cpp \
    $${PWD}/OAIProductApis_ListByProducts_200_response_value_inner.cpp \
    $${PWD}/OAIProductCollection.cpp \
    $${PWD}/OAIProductContract.cpp \
    $${PWD}/OAIProductGroups_ListByProducts_200_response.cpp \
    $${PWD}/OAIProductGroups_ListByProducts_200_response_value_inner.cpp \
    $${PWD}/OAIProductSubscriptions_ListByProducts_200_response.cpp \
    $${PWD}/OAIProductSubscriptions_ListByProducts_200_response_value_inner.cpp \
    $${PWD}/OAIProductUpdateParameters.cpp \
    $${PWD}/OAIProducts_ListByService_default_response.cpp \
    $${PWD}/OAIProducts_ListByService_default_response_details_inner.cpp \
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
