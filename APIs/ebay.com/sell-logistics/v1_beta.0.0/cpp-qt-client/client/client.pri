QT += network

HEADERS += \
# Models
    $${PWD}/OAIAdditionalOption.h \
    $${PWD}/OAIAmount.h \
    $${PWD}/OAIContact.h \
    $${PWD}/OAIContactAddress.h \
    $${PWD}/OAICreateShipmentFromQuoteRequest.h \
    $${PWD}/OAIDimensions.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorParameter.h \
    $${PWD}/OAIOrder.h \
    $${PWD}/OAIPackageSpecification.h \
    $${PWD}/OAIPhoneNumber.h \
    $${PWD}/OAIPickupSlot.h \
    $${PWD}/OAIPurchasedRate.h \
    $${PWD}/OAIRate.h \
    $${PWD}/OAIShipment.h \
    $${PWD}/OAIShipmentCancellation.h \
    $${PWD}/OAIShippingQuote.h \
    $${PWD}/OAIShippingQuoteRequest.h \
    $${PWD}/OAIWeight.h \
# APIs
    $${PWD}/OAIShipmentApi.h \
    $${PWD}/OAIShippingQuoteApi.h \
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
    $${PWD}/OAIAdditionalOption.cpp \
    $${PWD}/OAIAmount.cpp \
    $${PWD}/OAIContact.cpp \
    $${PWD}/OAIContactAddress.cpp \
    $${PWD}/OAICreateShipmentFromQuoteRequest.cpp \
    $${PWD}/OAIDimensions.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorParameter.cpp \
    $${PWD}/OAIOrder.cpp \
    $${PWD}/OAIPackageSpecification.cpp \
    $${PWD}/OAIPhoneNumber.cpp \
    $${PWD}/OAIPickupSlot.cpp \
    $${PWD}/OAIPurchasedRate.cpp \
    $${PWD}/OAIRate.cpp \
    $${PWD}/OAIShipment.cpp \
    $${PWD}/OAIShipmentCancellation.cpp \
    $${PWD}/OAIShippingQuote.cpp \
    $${PWD}/OAIShippingQuoteRequest.cpp \
    $${PWD}/OAIWeight.cpp \
# APIs
    $${PWD}/OAIShipmentApi.cpp \
    $${PWD}/OAIShippingQuoteApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
