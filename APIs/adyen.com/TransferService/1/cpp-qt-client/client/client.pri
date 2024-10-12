QT += network

HEADERS += \
# Models
    $${PWD}/OAIAddress.h \
    $${PWD}/OAIAmount.h \
    $${PWD}/OAIBankAccountInfo.h \
    $${PWD}/OAICounterparty.h \
    $${PWD}/OAIInternalPartyIdentification.h \
    $${PWD}/OAIInvalidField.h \
    $${PWD}/OAILink.h \
    $${PWD}/OAILinks.h \
    $${PWD}/OAIMerchantData.h \
    $${PWD}/OAIName.h \
    $${PWD}/OAINameLocation.h \
    $${PWD}/OAIPartyIdentification.h \
    $${PWD}/OAIRestServiceError.h \
    $${PWD}/OAIServiceError.h \
    $${PWD}/OAITransaction.h \
    $${PWD}/OAITransactionSearchResponse.h \
    $${PWD}/OAITransferInfoOld.h \
    $${PWD}/OAITransferOld.h \
# APIs
    $${PWD}/OAITransactionsApi.h \
    $${PWD}/OAITransfersApi.h \
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
    $${PWD}/OAIBankAccountInfo.cpp \
    $${PWD}/OAICounterparty.cpp \
    $${PWD}/OAIInternalPartyIdentification.cpp \
    $${PWD}/OAIInvalidField.cpp \
    $${PWD}/OAILink.cpp \
    $${PWD}/OAILinks.cpp \
    $${PWD}/OAIMerchantData.cpp \
    $${PWD}/OAIName.cpp \
    $${PWD}/OAINameLocation.cpp \
    $${PWD}/OAIPartyIdentification.cpp \
    $${PWD}/OAIRestServiceError.cpp \
    $${PWD}/OAIServiceError.cpp \
    $${PWD}/OAITransaction.cpp \
    $${PWD}/OAITransactionSearchResponse.cpp \
    $${PWD}/OAITransferInfoOld.cpp \
    $${PWD}/OAITransferOld.cpp \
# APIs
    $${PWD}/OAITransactionsApi.cpp \
    $${PWD}/OAITransfersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
