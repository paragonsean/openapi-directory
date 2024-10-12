QT += network

HEADERS += \
# Models
    $${PWD}/OAIAnalytics_200_response.h \
    $${PWD}/OAICarrier.h \
    $${PWD}/OAIHooksGet_200_response.h \
    $${PWD}/OAIHooksGet_200_response_hooks_inner.h \
    $${PWD}/OAIHooksPOST_200_response.h \
    $${PWD}/OAIMnp.h \
    $${PWD}/OAIRoaming.h \
    $${PWD}/OAISms_200_response.h \
    $${PWD}/OAISms_200_response_messages_inner.h \
    $${PWD}/OAIValidateForVoice_200_response.h \
# APIs
    $${PWD}/OAIAnalyticsApi.h \
    $${PWD}/OAIBalanceApi.h \
    $${PWD}/OAIContactsApi.h \
    $${PWD}/OAIHooksApi.h \
    $${PWD}/OAILookupApi.h \
    $${PWD}/OAIPricingApi.h \
    $${PWD}/OAISmsApi.h \
    $${PWD}/OAIStatusApi.h \
    $${PWD}/OAIValidateForVoiceApi.h \
    $${PWD}/OAIVoiceApi.h \
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
    $${PWD}/OAIAnalytics_200_response.cpp \
    $${PWD}/OAICarrier.cpp \
    $${PWD}/OAIHooksGet_200_response.cpp \
    $${PWD}/OAIHooksGet_200_response_hooks_inner.cpp \
    $${PWD}/OAIHooksPOST_200_response.cpp \
    $${PWD}/OAIMnp.cpp \
    $${PWD}/OAIRoaming.cpp \
    $${PWD}/OAISms_200_response.cpp \
    $${PWD}/OAISms_200_response_messages_inner.cpp \
    $${PWD}/OAIValidateForVoice_200_response.cpp \
# APIs
    $${PWD}/OAIAnalyticsApi.cpp \
    $${PWD}/OAIBalanceApi.cpp \
    $${PWD}/OAIContactsApi.cpp \
    $${PWD}/OAIHooksApi.cpp \
    $${PWD}/OAILookupApi.cpp \
    $${PWD}/OAIPricingApi.cpp \
    $${PWD}/OAISmsApi.cpp \
    $${PWD}/OAIStatusApi.cpp \
    $${PWD}/OAIValidateForVoiceApi.cpp \
    $${PWD}/OAIVoiceApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
