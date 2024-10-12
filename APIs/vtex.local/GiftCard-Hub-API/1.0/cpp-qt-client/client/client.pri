QT += network

HEADERS += \
# Models
    $${PWD}/OAICart.h \
    $${PWD}/OAICart1.h \
    $${PWD}/OAICart2.h \
    $${PWD}/OAIClient.h \
    $${PWD}/OAIClientProfile.h \
    $${PWD}/OAICreateGiftCardCancellationTransactionRequest.h \
    $${PWD}/OAICreateGiftCardSettlementTransactionRequest.h \
    $${PWD}/OAICreateGiftCardTransactionRequest.h \
    $${PWD}/OAICreateGiftCardinGiftCardProviderRequest.h \
    $${PWD}/OAICreateUpdateGiftCardProviderbyIDRequest.h \
    $${PWD}/OAIGetGiftCardfromGiftCardProviderRequest.h \
    $${PWD}/OAIItem.h \
    $${PWD}/OAIItem1.h \
    $${PWD}/OAIOrderInfo.h \
    $${PWD}/OAIShipping.h \
# APIs
    $${PWD}/OAIProviderApi.h \
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
    $${PWD}/OAICart.cpp \
    $${PWD}/OAICart1.cpp \
    $${PWD}/OAICart2.cpp \
    $${PWD}/OAIClient.cpp \
    $${PWD}/OAIClientProfile.cpp \
    $${PWD}/OAICreateGiftCardCancellationTransactionRequest.cpp \
    $${PWD}/OAICreateGiftCardSettlementTransactionRequest.cpp \
    $${PWD}/OAICreateGiftCardTransactionRequest.cpp \
    $${PWD}/OAICreateGiftCardinGiftCardProviderRequest.cpp \
    $${PWD}/OAICreateUpdateGiftCardProviderbyIDRequest.cpp \
    $${PWD}/OAIGetGiftCardfromGiftCardProviderRequest.cpp \
    $${PWD}/OAIItem.cpp \
    $${PWD}/OAIItem1.cpp \
    $${PWD}/OAIOrderInfo.cpp \
    $${PWD}/OAIShipping.cpp \
# APIs
    $${PWD}/OAIProviderApi.cpp \
    $${PWD}/OAITransactionApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
