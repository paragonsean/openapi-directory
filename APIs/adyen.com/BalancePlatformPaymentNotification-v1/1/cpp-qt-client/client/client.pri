QT += network

HEADERS += \
# Models
    $${PWD}/OAIAddress.h \
    $${PWD}/OAIAmount.h \
    $${PWD}/OAIBalancePlatformNotificationResponse.h \
    $${PWD}/OAIBankAccountInfo.h \
    $${PWD}/OAICounterparty.h \
    $${PWD}/OAIIncomingTransferNotificationData.h \
    $${PWD}/OAIIncomingTransferNotificationRequest.h \
    $${PWD}/OAIMerchantData.h \
    $${PWD}/OAIName.h \
    $${PWD}/OAINameLocation.h \
    $${PWD}/OAINotificationModificationData.h \
    $${PWD}/OAIOutgoingTransferNotificationData.h \
    $${PWD}/OAIOutgoingTransferNotificationRequest.h \
    $${PWD}/OAIPaymentNotificationData.h \
    $${PWD}/OAIPaymentNotificationRequest.h \
    $${PWD}/OAIPlatformPayment.h \
    $${PWD}/OAIRelayedAuthorisationData.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAIResourceReference.h \
    $${PWD}/OAITransactionEventViolation.h \
    $${PWD}/OAITransactionNotificationData.h \
    $${PWD}/OAITransactionRuleReference.h \
    $${PWD}/OAITransactionRuleSource.h \
    $${PWD}/OAITransactionRulesResult.h \
    $${PWD}/OAIValidationResult.h \
# APIs
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
    $${PWD}/OAIAmount.cpp \
    $${PWD}/OAIBalancePlatformNotificationResponse.cpp \
    $${PWD}/OAIBankAccountInfo.cpp \
    $${PWD}/OAICounterparty.cpp \
    $${PWD}/OAIIncomingTransferNotificationData.cpp \
    $${PWD}/OAIIncomingTransferNotificationRequest.cpp \
    $${PWD}/OAIMerchantData.cpp \
    $${PWD}/OAIName.cpp \
    $${PWD}/OAINameLocation.cpp \
    $${PWD}/OAINotificationModificationData.cpp \
    $${PWD}/OAIOutgoingTransferNotificationData.cpp \
    $${PWD}/OAIOutgoingTransferNotificationRequest.cpp \
    $${PWD}/OAIPaymentNotificationData.cpp \
    $${PWD}/OAIPaymentNotificationRequest.cpp \
    $${PWD}/OAIPlatformPayment.cpp \
    $${PWD}/OAIRelayedAuthorisationData.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAIResourceReference.cpp \
    $${PWD}/OAITransactionEventViolation.cpp \
    $${PWD}/OAITransactionNotificationData.cpp \
    $${PWD}/OAITransactionRuleReference.cpp \
    $${PWD}/OAITransactionRuleSource.cpp \
    $${PWD}/OAITransactionRulesResult.cpp \
    $${PWD}/OAIValidationResult.cpp \
# APIs
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
