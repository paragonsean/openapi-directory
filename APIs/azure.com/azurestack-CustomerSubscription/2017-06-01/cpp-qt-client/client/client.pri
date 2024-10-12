QT += network

HEADERS += \
# Models
    $${PWD}/OAICustomerSubscription.h \
    $${PWD}/OAICustomerSubscriptionList.h \
    $${PWD}/OAICustomerSubscriptionProperties.h \
    $${PWD}/OAICustomerSubscriptions_List_default_response.h \
    $${PWD}/OAICustomerSubscriptions_List_default_response_error.h \
# APIs
    $${PWD}/OAICustomerSubscriptionApi.h \
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
    $${PWD}/OAICustomerSubscription.cpp \
    $${PWD}/OAICustomerSubscriptionList.cpp \
    $${PWD}/OAICustomerSubscriptionProperties.cpp \
    $${PWD}/OAICustomerSubscriptions_List_default_response.cpp \
    $${PWD}/OAICustomerSubscriptions_List_default_response_error.cpp \
# APIs
    $${PWD}/OAICustomerSubscriptionApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
