QT += network

HEADERS += \
# Models
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorField.h \
    $${PWD}/OAIErrorLimit.h \
    $${PWD}/OAIPagination.h \
    $${PWD}/OAIProductGroup.h \
    $${PWD}/OAISubscription.h \
    $${PWD}/OAISubscriptionAddon.h \
    $${PWD}/OAISubscriptionBilling.h \
    $${PWD}/OAISubscriptionList.h \
    $${PWD}/OAISubscriptionProduct.h \
    $${PWD}/OAISubscriptionRelations.h \
    $${PWD}/OAISubscriptionUpdate.h \
# APIs
    $${PWD}/OAIV1Api.h \
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
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorField.cpp \
    $${PWD}/OAIErrorLimit.cpp \
    $${PWD}/OAIPagination.cpp \
    $${PWD}/OAIProductGroup.cpp \
    $${PWD}/OAISubscription.cpp \
    $${PWD}/OAISubscriptionAddon.cpp \
    $${PWD}/OAISubscriptionBilling.cpp \
    $${PWD}/OAISubscriptionList.cpp \
    $${PWD}/OAISubscriptionProduct.cpp \
    $${PWD}/OAISubscriptionRelations.cpp \
    $${PWD}/OAISubscriptionUpdate.cpp \
# APIs
    $${PWD}/OAIV1Api.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
