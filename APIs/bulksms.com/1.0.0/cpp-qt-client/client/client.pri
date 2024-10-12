QT += network

HEADERS += \
# Models
    $${PWD}/OAIBlockedNumber.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIMessage.h \
    $${PWD}/OAIMessage_status.h \
    $${PWD}/OAIMessage_submission.h \
    $${PWD}/OAIPreSignInfo.h \
    $${PWD}/OAIPreSignInfo_fields_inner.h \
    $${PWD}/OAIPreSignRequest.h \
    $${PWD}/OAIProfile.h \
    $${PWD}/OAIProfile_commerce.h \
    $${PWD}/OAIProfile_commerce_address.h \
    $${PWD}/OAIProfile_company.h \
    $${PWD}/OAIProfile_credits.h \
    $${PWD}/OAIProfile_originAddresses.h \
    $${PWD}/OAIProfile_quota.h \
    $${PWD}/OAISubmissionEntry.h \
    $${PWD}/OAISubmissionEntry_from.h \
    $${PWD}/OAISubmissionEntry_to_inner.h \
    $${PWD}/OAITransferEntry.h \
    $${PWD}/OAIWebhook.h \
    $${PWD}/OAIWebhookEntry.h \
# APIs
    $${PWD}/OAIAttachmentsApi.h \
    $${PWD}/OAIBlockedNumbersApi.h \
    $${PWD}/OAICreditsApi.h \
    $${PWD}/OAIMessageApi.h \
    $${PWD}/OAIProfileApi.h \
    $${PWD}/OAIWebhooksApi.h \
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
    $${PWD}/OAIBlockedNumber.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIMessage.cpp \
    $${PWD}/OAIMessage_status.cpp \
    $${PWD}/OAIMessage_submission.cpp \
    $${PWD}/OAIPreSignInfo.cpp \
    $${PWD}/OAIPreSignInfo_fields_inner.cpp \
    $${PWD}/OAIPreSignRequest.cpp \
    $${PWD}/OAIProfile.cpp \
    $${PWD}/OAIProfile_commerce.cpp \
    $${PWD}/OAIProfile_commerce_address.cpp \
    $${PWD}/OAIProfile_company.cpp \
    $${PWD}/OAIProfile_credits.cpp \
    $${PWD}/OAIProfile_originAddresses.cpp \
    $${PWD}/OAIProfile_quota.cpp \
    $${PWD}/OAISubmissionEntry.cpp \
    $${PWD}/OAISubmissionEntry_from.cpp \
    $${PWD}/OAISubmissionEntry_to_inner.cpp \
    $${PWD}/OAITransferEntry.cpp \
    $${PWD}/OAIWebhook.cpp \
    $${PWD}/OAIWebhookEntry.cpp \
# APIs
    $${PWD}/OAIAttachmentsApi.cpp \
    $${PWD}/OAIBlockedNumbersApi.cpp \
    $${PWD}/OAICreditsApi.cpp \
    $${PWD}/OAIMessageApi.cpp \
    $${PWD}/OAIProfileApi.cpp \
    $${PWD}/OAIWebhooksApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
