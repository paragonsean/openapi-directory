QT += network

HEADERS += \
# Models
    $${PWD}/OAISubscriptionCollection.h \
    $${PWD}/OAISubscriptionContract.h \
    $${PWD}/OAISubscriptionContractProperties.h \
    $${PWD}/OAISubscriptionCreateParameterProperties.h \
    $${PWD}/OAISubscriptionCreateParameters.h \
    $${PWD}/OAISubscriptionUpdateParameterProperties.h \
    $${PWD}/OAISubscriptionUpdateParameters.h \
    $${PWD}/OAISubscription_List_default_response.h \
    $${PWD}/OAISubscription_List_default_response_error.h \
    $${PWD}/OAISubscription_List_default_response_error_details_inner.h \
# APIs
    $${PWD}/OAISubscriptionsApi.h \
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
    $${PWD}/OAISubscriptionCollection.cpp \
    $${PWD}/OAISubscriptionContract.cpp \
    $${PWD}/OAISubscriptionContractProperties.cpp \
    $${PWD}/OAISubscriptionCreateParameterProperties.cpp \
    $${PWD}/OAISubscriptionCreateParameters.cpp \
    $${PWD}/OAISubscriptionUpdateParameterProperties.cpp \
    $${PWD}/OAISubscriptionUpdateParameters.cpp \
    $${PWD}/OAISubscription_List_default_response.cpp \
    $${PWD}/OAISubscription_List_default_response_error.cpp \
    $${PWD}/OAISubscription_List_default_response_error_details_inner.cpp \
# APIs
    $${PWD}/OAISubscriptionsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
