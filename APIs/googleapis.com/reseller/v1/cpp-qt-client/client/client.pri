QT += network

HEADERS += \
# Models
    $${PWD}/OAIAddress.h \
    $${PWD}/OAIChangePlanRequest.h \
    $${PWD}/OAICustomer.h \
    $${PWD}/OAIPrimaryAdmin.h \
    $${PWD}/OAIRenewalSettings.h \
    $${PWD}/OAIResellernotifyGetwatchdetailsResponse.h \
    $${PWD}/OAIResellernotifyResource.h \
    $${PWD}/OAISeats.h \
    $${PWD}/OAISubscription.h \
    $${PWD}/OAISubscription_plan.h \
    $${PWD}/OAISubscription_plan_commitmentInterval.h \
    $${PWD}/OAISubscription_transferInfo.h \
    $${PWD}/OAISubscription_trialSettings.h \
    $${PWD}/OAISubscriptions.h \
# APIs
    $${PWD}/OAICustomersApi.h \
    $${PWD}/OAIResellernotifyApi.h \
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
    $${PWD}/OAIAddress.cpp \
    $${PWD}/OAIChangePlanRequest.cpp \
    $${PWD}/OAICustomer.cpp \
    $${PWD}/OAIPrimaryAdmin.cpp \
    $${PWD}/OAIRenewalSettings.cpp \
    $${PWD}/OAIResellernotifyGetwatchdetailsResponse.cpp \
    $${PWD}/OAIResellernotifyResource.cpp \
    $${PWD}/OAISeats.cpp \
    $${PWD}/OAISubscription.cpp \
    $${PWD}/OAISubscription_plan.cpp \
    $${PWD}/OAISubscription_plan_commitmentInterval.cpp \
    $${PWD}/OAISubscription_transferInfo.cpp \
    $${PWD}/OAISubscription_trialSettings.cpp \
    $${PWD}/OAISubscriptions.cpp \
# APIs
    $${PWD}/OAICustomersApi.cpp \
    $${PWD}/OAIResellernotifyApi.cpp \
    $${PWD}/OAISubscriptionsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
