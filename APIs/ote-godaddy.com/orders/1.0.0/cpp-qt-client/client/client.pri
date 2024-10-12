QT += network

HEADERS += \
# Models
    $${PWD}/OAIAddress.h \
    $${PWD}/OAIBillTo.h \
    $${PWD}/OAIContact.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorField.h \
    $${PWD}/OAIErrorLimit.h \
    $${PWD}/OAILineItem.h \
    $${PWD}/OAILineItemPricing.h \
    $${PWD}/OAILineItemPricingTaxDetail.h \
    $${PWD}/OAILineItemSummary.h \
    $${PWD}/OAILineItemTaxCollector.h \
    $${PWD}/OAILineItemUnitPricing.h \
    $${PWD}/OAIOrder.h \
    $${PWD}/OAIOrderFee.h \
    $${PWD}/OAIOrderList.h \
    $${PWD}/OAIOrderPricing.h \
    $${PWD}/OAIOrderSummary.h \
    $${PWD}/OAIOrderSummaryPricing.h \
    $${PWD}/OAIPagination.h \
    $${PWD}/OAIPayment.h \
# APIs
    $${PWD}/OAIV1Api.h \
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
    $${PWD}/OAIBillTo.cpp \
    $${PWD}/OAIContact.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorField.cpp \
    $${PWD}/OAIErrorLimit.cpp \
    $${PWD}/OAILineItem.cpp \
    $${PWD}/OAILineItemPricing.cpp \
    $${PWD}/OAILineItemPricingTaxDetail.cpp \
    $${PWD}/OAILineItemSummary.cpp \
    $${PWD}/OAILineItemTaxCollector.cpp \
    $${PWD}/OAILineItemUnitPricing.cpp \
    $${PWD}/OAIOrder.cpp \
    $${PWD}/OAIOrderFee.cpp \
    $${PWD}/OAIOrderList.cpp \
    $${PWD}/OAIOrderPricing.cpp \
    $${PWD}/OAIOrderSummary.cpp \
    $${PWD}/OAIOrderSummaryPricing.cpp \
    $${PWD}/OAIPagination.cpp \
    $${PWD}/OAIPayment.cpp \
# APIs
    $${PWD}/OAIV1Api.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
