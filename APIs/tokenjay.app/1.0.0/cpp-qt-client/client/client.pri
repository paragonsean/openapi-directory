QT += network

HEADERS += \
# Models
    $${PWD}/OAIAction.h \
    $${PWD}/OAIAddRequestResponse.h \
    $${PWD}/OAIAgeUsdExchangeInfo.h \
    $${PWD}/OAIAgeUsdInfo.h \
    $${PWD}/OAICheckResponse.h \
    $${PWD}/OAICreatePaymentRequest.h \
    $${PWD}/OAIErgoPayResponse.h \
    $${PWD}/OAIFetchActionResponse.h \
    $${PWD}/OAIGenuineToken.h \
    $${PWD}/OAIMosaikApp.h \
    $${PWD}/OAIMosaikManifest.h \
    $${PWD}/OAINodePeer.h \
    $${PWD}/OAINotificationCheckResponse.h \
    $${PWD}/OAIPaymentRequestStateResponse.h \
    $${PWD}/OAITokenPrice.h \
    $${PWD}/OAIViewElement.h \
# APIs
    $${PWD}/OAIAgeUsdApi.h \
    $${PWD}/OAIBabelFeeControllerApi.h \
    $${PWD}/OAIBabelFeeNewOfferControllerApi.h \
    $${PWD}/OAIBoxConsolidationControllerApi.h \
    $${PWD}/OAIPaymentPortalApi.h \
    $${PWD}/OAIPeerDetectionApi.h \
    $${PWD}/OAITokenBurnControllerApi.h \
    $${PWD}/OAITokenPricesApi.h \
    $${PWD}/OAITokenVerificationApi.h \
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
    $${PWD}/OAIAction.cpp \
    $${PWD}/OAIAddRequestResponse.cpp \
    $${PWD}/OAIAgeUsdExchangeInfo.cpp \
    $${PWD}/OAIAgeUsdInfo.cpp \
    $${PWD}/OAICheckResponse.cpp \
    $${PWD}/OAICreatePaymentRequest.cpp \
    $${PWD}/OAIErgoPayResponse.cpp \
    $${PWD}/OAIFetchActionResponse.cpp \
    $${PWD}/OAIGenuineToken.cpp \
    $${PWD}/OAIMosaikApp.cpp \
    $${PWD}/OAIMosaikManifest.cpp \
    $${PWD}/OAINodePeer.cpp \
    $${PWD}/OAINotificationCheckResponse.cpp \
    $${PWD}/OAIPaymentRequestStateResponse.cpp \
    $${PWD}/OAITokenPrice.cpp \
    $${PWD}/OAIViewElement.cpp \
# APIs
    $${PWD}/OAIAgeUsdApi.cpp \
    $${PWD}/OAIBabelFeeControllerApi.cpp \
    $${PWD}/OAIBabelFeeNewOfferControllerApi.cpp \
    $${PWD}/OAIBoxConsolidationControllerApi.cpp \
    $${PWD}/OAIPaymentPortalApi.cpp \
    $${PWD}/OAIPeerDetectionApi.cpp \
    $${PWD}/OAITokenBurnControllerApi.cpp \
    $${PWD}/OAITokenPricesApi.cpp \
    $${PWD}/OAITokenVerificationApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
