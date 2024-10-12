QT += network

HEADERS += \
# Models
    $${PWD}/OAICancelGiftCardTransactionRequest.h \
    $${PWD}/OAICart.h \
    $${PWD}/OAICart1.h \
    $${PWD}/OAIClient.h \
    $${PWD}/OAIClientProfile.h \
    $${PWD}/OAICreateGiftCardRequest.h \
    $${PWD}/OAICreateGiftCardTransactionRequest.h \
    $${PWD}/OAIGetGiftCardusingJSONRequest.h \
    $${PWD}/OAIItem.h \
    $${PWD}/OAIItem1.h \
    $${PWD}/OAIItem2.h \
    $${PWD}/OAIOrderInfo.h \
    $${PWD}/OAIPaging.h \
    $${PWD}/OAIPriceTag.h \
    $${PWD}/OAIResponse.h \
    $${PWD}/OAIResponse2.h \
    $${PWD}/OAIResponse3.h \
    $${PWD}/OAIResponse5.h \
    $${PWD}/OAIResponse6.h \
    $${PWD}/OAIResponse7.h \
    $${PWD}/OAISelf.h \
    $${PWD}/OAISettleGiftCardTransactionRequest.h \
    $${PWD}/OAIShipping.h \
    $${PWD}/OAITransactions.h \
# APIs
    $${PWD}/OAIGiftCardApi.h \
    $${PWD}/OAITransactionApi.h \
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
    $${PWD}/OAICancelGiftCardTransactionRequest.cpp \
    $${PWD}/OAICart.cpp \
    $${PWD}/OAICart1.cpp \
    $${PWD}/OAIClient.cpp \
    $${PWD}/OAIClientProfile.cpp \
    $${PWD}/OAICreateGiftCardRequest.cpp \
    $${PWD}/OAICreateGiftCardTransactionRequest.cpp \
    $${PWD}/OAIGetGiftCardusingJSONRequest.cpp \
    $${PWD}/OAIItem.cpp \
    $${PWD}/OAIItem1.cpp \
    $${PWD}/OAIItem2.cpp \
    $${PWD}/OAIOrderInfo.cpp \
    $${PWD}/OAIPaging.cpp \
    $${PWD}/OAIPriceTag.cpp \
    $${PWD}/OAIResponse.cpp \
    $${PWD}/OAIResponse2.cpp \
    $${PWD}/OAIResponse3.cpp \
    $${PWD}/OAIResponse5.cpp \
    $${PWD}/OAIResponse6.cpp \
    $${PWD}/OAIResponse7.cpp \
    $${PWD}/OAISelf.cpp \
    $${PWD}/OAISettleGiftCardTransactionRequest.cpp \
    $${PWD}/OAIShipping.cpp \
    $${PWD}/OAITransactions.cpp \
# APIs
    $${PWD}/OAIGiftCardApi.cpp \
    $${PWD}/OAITransactionApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
