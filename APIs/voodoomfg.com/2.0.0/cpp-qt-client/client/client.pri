QT += network

HEADERS += \
# Models
    $${PWD}/OAIConfirmOrderBody.h \
    $${PWD}/OAICreateModelBody.h \
    $${PWD}/OAICreateOrderBody.h \
    $${PWD}/OAIMaterial.h \
    $${PWD}/OAIModel.h \
    $${PWD}/OAIModelQuote.h \
    $${PWD}/OAIOrder.h \
    $${PWD}/OAIOrderPrint.h \
    $${PWD}/OAIPrint.h \
    $${PWD}/OAIProductionOptions.h \
    $${PWD}/OAIProductionOptionsCosts.h \
    $${PWD}/OAIQuote.h \
    $${PWD}/OAIRate.h \
    $${PWD}/OAIShippingAddress.h \
    $${PWD}/OAIShippingOptionsBody.h \
    $${PWD}/OAI_order_confirm_post_200_response.h \
    $${PWD}/OAI_order_create_post_200_response.h \
    $${PWD}/OAI_order_shipping_post_200_response.h \
# APIs
    $${PWD}/OAIMaterialsApi.h \
    $${PWD}/OAIModelApi.h \
    $${PWD}/OAIOrderApi.h \
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
    $${PWD}/OAIConfirmOrderBody.cpp \
    $${PWD}/OAICreateModelBody.cpp \
    $${PWD}/OAICreateOrderBody.cpp \
    $${PWD}/OAIMaterial.cpp \
    $${PWD}/OAIModel.cpp \
    $${PWD}/OAIModelQuote.cpp \
    $${PWD}/OAIOrder.cpp \
    $${PWD}/OAIOrderPrint.cpp \
    $${PWD}/OAIPrint.cpp \
    $${PWD}/OAIProductionOptions.cpp \
    $${PWD}/OAIProductionOptionsCosts.cpp \
    $${PWD}/OAIQuote.cpp \
    $${PWD}/OAIRate.cpp \
    $${PWD}/OAIShippingAddress.cpp \
    $${PWD}/OAIShippingOptionsBody.cpp \
    $${PWD}/OAI_order_confirm_post_200_response.cpp \
    $${PWD}/OAI_order_create_post_200_response.cpp \
    $${PWD}/OAI_order_shipping_post_200_response.cpp \
# APIs
    $${PWD}/OAIMaterialsApi.cpp \
    $${PWD}/OAIModelApi.cpp \
    $${PWD}/OAIOrderApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
