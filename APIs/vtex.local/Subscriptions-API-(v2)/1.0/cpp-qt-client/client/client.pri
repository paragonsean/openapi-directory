QT += network

HEADERS += \
# Models
    $${PWD}/OAIAdditemsubscription_groupIdRequest.h \
    $${PWD}/OAIAdditionalComponent.h \
    $${PWD}/OAIFrequency.h \
    $${PWD}/OAIInsertAddressesbygroupIdRequest.h \
    $${PWD}/OAIInsertAddressesforSubscriptionRequest.h \
    $${PWD}/OAIItem.h \
    $${PWD}/OAIItem1.h \
    $${PWD}/OAIMetadatum.h \
    $${PWD}/OAIPaymentMethod.h \
    $${PWD}/OAIPlan.h \
    $${PWD}/OAIProperties.h \
    $${PWD}/OAIPurchaseSettings.h \
    $${PWD}/OAISettings.h \
    $${PWD}/OAIShippingAddress.h \
    $${PWD}/OAISku.h \
    $${PWD}/OAIUpdateSubscriptionbygroupIdRequest.h \
    $${PWD}/OAIUpdateSubscriptionsbySubscriptionIdRequest.h \
    $${PWD}/OAIValidity.h \
# APIs
    $${PWD}/OAIReportApi.h \
    $${PWD}/OAISettingsApi.h \
    $${PWD}/OAISubscriptionGroupApi.h \
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
    $${PWD}/OAIAdditemsubscription_groupIdRequest.cpp \
    $${PWD}/OAIAdditionalComponent.cpp \
    $${PWD}/OAIFrequency.cpp \
    $${PWD}/OAIInsertAddressesbygroupIdRequest.cpp \
    $${PWD}/OAIInsertAddressesforSubscriptionRequest.cpp \
    $${PWD}/OAIItem.cpp \
    $${PWD}/OAIItem1.cpp \
    $${PWD}/OAIMetadatum.cpp \
    $${PWD}/OAIPaymentMethod.cpp \
    $${PWD}/OAIPlan.cpp \
    $${PWD}/OAIProperties.cpp \
    $${PWD}/OAIPurchaseSettings.cpp \
    $${PWD}/OAISettings.cpp \
    $${PWD}/OAIShippingAddress.cpp \
    $${PWD}/OAISku.cpp \
    $${PWD}/OAIUpdateSubscriptionbygroupIdRequest.cpp \
    $${PWD}/OAIUpdateSubscriptionsbySubscriptionIdRequest.cpp \
    $${PWD}/OAIValidity.cpp \
# APIs
    $${PWD}/OAIReportApi.cpp \
    $${PWD}/OAISettingsApi.cpp \
    $${PWD}/OAISubscriptionGroupApi.cpp \
    $${PWD}/OAISubscriptionsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
