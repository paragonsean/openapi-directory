QT += network

HEADERS += \
# Models
    $${PWD}/OAIApiCredentials.h \
    $${PWD}/OAIApiKey.h \
    $${PWD}/OAICountOf.h \
    $${PWD}/OAICurrentKey.h \
    $${PWD}/OAIExpiry.h \
    $${PWD}/OAIFindCredentials.h \
    $${PWD}/OAIKeyView.h \
    $${PWD}/OAIKeysApi_Current_200_response.h \
    $${PWD}/OAIKeysApi_Expiry_200_response.h \
    $${PWD}/OAIKeysApi_Find_200_response.h \
    $${PWD}/OAIProductCreateModify.h \
    $${PWD}/OAIProductView.h \
    $${PWD}/OAIProductsApi_Count_200_response.h \
    $${PWD}/OAIProductsApi_Count_request.h \
    $${PWD}/OAIProductsApi_Find_200_response.h \
    $${PWD}/OAIProductsApi_Find_request.h \
    $${PWD}/OAIProductsApi_PatchProduct2_request.h \
    $${PWD}/OAISubscriptionCreateModify.h \
    $${PWD}/OAISubscriptionView.h \
    $${PWD}/OAISubscriptionsApi_Count_request.h \
    $${PWD}/OAISubscriptionsApi_Find_200_response.h \
    $${PWD}/OAISubscriptionsApi_PutSubscription_request.h \
# APIs
    $${PWD}/OAIKeysApiApi.h \
    $${PWD}/OAIProductsApiApi.h \
    $${PWD}/OAISubscriptionsApiApi.h \
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
    $${PWD}/OAIApiCredentials.cpp \
    $${PWD}/OAIApiKey.cpp \
    $${PWD}/OAICountOf.cpp \
    $${PWD}/OAICurrentKey.cpp \
    $${PWD}/OAIExpiry.cpp \
    $${PWD}/OAIFindCredentials.cpp \
    $${PWD}/OAIKeyView.cpp \
    $${PWD}/OAIKeysApi_Current_200_response.cpp \
    $${PWD}/OAIKeysApi_Expiry_200_response.cpp \
    $${PWD}/OAIKeysApi_Find_200_response.cpp \
    $${PWD}/OAIProductCreateModify.cpp \
    $${PWD}/OAIProductView.cpp \
    $${PWD}/OAIProductsApi_Count_200_response.cpp \
    $${PWD}/OAIProductsApi_Count_request.cpp \
    $${PWD}/OAIProductsApi_Find_200_response.cpp \
    $${PWD}/OAIProductsApi_Find_request.cpp \
    $${PWD}/OAIProductsApi_PatchProduct2_request.cpp \
    $${PWD}/OAISubscriptionCreateModify.cpp \
    $${PWD}/OAISubscriptionView.cpp \
    $${PWD}/OAISubscriptionsApi_Count_request.cpp \
    $${PWD}/OAISubscriptionsApi_Find_200_response.cpp \
    $${PWD}/OAISubscriptionsApi_PutSubscription_request.cpp \
# APIs
    $${PWD}/OAIKeysApiApi.cpp \
    $${PWD}/OAIProductsApiApi.cpp \
    $${PWD}/OAISubscriptionsApiApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
