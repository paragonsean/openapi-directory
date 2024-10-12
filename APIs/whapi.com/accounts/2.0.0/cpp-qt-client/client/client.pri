QT += network

HEADERS += \
# Models
    $${PWD}/OAIAccountBalance.h \
    $${PWD}/OAIAccountErrors.h \
    $${PWD}/OAIAccountFlagsSet.h \
    $${PWD}/OAIAccounts.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIFlags_inner.h \
    $${PWD}/OAIGetPayments.h \
    $${PWD}/OAIOnlineAccount.h \
    $${PWD}/OAIPayment.h \
    $${PWD}/OAIPhone.h \
    $${PWD}/OAIPinStatus.h \
    $${PWD}/OAIPlusCard.h \
    $${PWD}/OAIPlusCardDetails.h \
    $${PWD}/OAIRetailAccount.h \
# APIs
    $${PWD}/OAIAccountsApi.h \
    $${PWD}/OAICardNumberApi.h \
    $${PWD}/OAIFlagsApi.h \
    $${PWD}/OAILostApi.h \
    $${PWD}/OAIOmniApi.h \
    $${PWD}/OAIPINApi.h \
    $${PWD}/OAIPhoneApi.h \
    $${PWD}/OAIPlusCardApi.h \
    $${PWD}/OAIStolenApi.h \
    $${PWD}/OAIWalletApi.h \
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
    $${PWD}/OAIAccountBalance.cpp \
    $${PWD}/OAIAccountErrors.cpp \
    $${PWD}/OAIAccountFlagsSet.cpp \
    $${PWD}/OAIAccounts.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIFlags_inner.cpp \
    $${PWD}/OAIGetPayments.cpp \
    $${PWD}/OAIOnlineAccount.cpp \
    $${PWD}/OAIPayment.cpp \
    $${PWD}/OAIPhone.cpp \
    $${PWD}/OAIPinStatus.cpp \
    $${PWD}/OAIPlusCard.cpp \
    $${PWD}/OAIPlusCardDetails.cpp \
    $${PWD}/OAIRetailAccount.cpp \
# APIs
    $${PWD}/OAIAccountsApi.cpp \
    $${PWD}/OAICardNumberApi.cpp \
    $${PWD}/OAIFlagsApi.cpp \
    $${PWD}/OAILostApi.cpp \
    $${PWD}/OAIOmniApi.cpp \
    $${PWD}/OAIPINApi.cpp \
    $${PWD}/OAIPhoneApi.cpp \
    $${PWD}/OAIPlusCardApi.cpp \
    $${PWD}/OAIStolenApi.cpp \
    $${PWD}/OAIWalletApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
