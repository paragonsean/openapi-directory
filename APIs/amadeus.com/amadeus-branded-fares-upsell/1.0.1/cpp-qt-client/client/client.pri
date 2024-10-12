QT += network

HEADERS += \
# Models
    $${PWD}/OAIAdditionalService.h \
    $${PWD}/OAIAdditionalServiceType.h \
    $${PWD}/OAIAdditionalServicesRequest.h \
    $${PWD}/OAIAircraftEquipment.h \
    $${PWD}/OAIAllotmentDetails.h \
    $${PWD}/OAIAmenity.h \
    $${PWD}/OAIAmenityType.h \
    $${PWD}/OAIBaggageAllowance.h \
    $${PWD}/OAICo2Emission.h \
    $${PWD}/OAICollection_Meta_Upsell.h \
    $${PWD}/OAICoverage.h \
    $${PWD}/OAIDescription.h \
    $${PWD}/OAIDictionaries.h \
    $${PWD}/OAIError_400.h \
    $${PWD}/OAIError_500.h \
    $${PWD}/OAIExtendedPricingOptions.h \
    $${PWD}/OAIExtended_Price.h \
    $${PWD}/OAIFareDetailsBySegment.h \
    $${PWD}/OAIFareRules.h \
    $${PWD}/OAIFee.h \
    $${PWD}/OAIFeeType.h \
    $${PWD}/OAIFlightEndPoint.h \
    $${PWD}/OAIFlightOffer.h \
    $${PWD}/OAIFlightOfferSource.h \
    $${PWD}/OAIFlightOfferUpsellIn.h \
    $${PWD}/OAIFlightSegment.h \
    $${PWD}/OAIFlightStop.h \
    $${PWD}/OAIGet_Upsell_Query.h \
    $${PWD}/OAIIssue.h \
    $${PWD}/OAIIssue_Source.h \
    $${PWD}/OAIItineraries.h \
    $${PWD}/OAILocationValue.h \
    $${PWD}/OAIOneWayUpselledCombinations.h \
    $${PWD}/OAIOperatingFlight.h \
    $${PWD}/OAIOriginalFlightEndPoint.h \
    $${PWD}/OAIOriginalFlightStop.h \
    $${PWD}/OAIPayment.h \
    $${PWD}/OAIPaymentBrand.h \
    $${PWD}/OAIPrice.h \
    $${PWD}/OAIPricingOptions.h \
    $${PWD}/OAISegment.h \
    $${PWD}/OAIServiceName.h \
    $${PWD}/OAISliceDiceIndicator.h \
    $${PWD}/OAISuccess_Upsell.h \
    $${PWD}/OAITax.h \
    $${PWD}/OAITermAndCondition.h \
    $${PWD}/OAITravelClass.h \
    $${PWD}/OAITravelerPricing.h \
    $${PWD}/OAITravelerPricingFareOption.h \
    $${PWD}/OAITravelerType.h \
# APIs
    $${PWD}/OAIShoppingApi.h \
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
    $${PWD}/OAIAdditionalService.cpp \
    $${PWD}/OAIAdditionalServiceType.cpp \
    $${PWD}/OAIAdditionalServicesRequest.cpp \
    $${PWD}/OAIAircraftEquipment.cpp \
    $${PWD}/OAIAllotmentDetails.cpp \
    $${PWD}/OAIAmenity.cpp \
    $${PWD}/OAIAmenityType.cpp \
    $${PWD}/OAIBaggageAllowance.cpp \
    $${PWD}/OAICo2Emission.cpp \
    $${PWD}/OAICollection_Meta_Upsell.cpp \
    $${PWD}/OAICoverage.cpp \
    $${PWD}/OAIDescription.cpp \
    $${PWD}/OAIDictionaries.cpp \
    $${PWD}/OAIError_400.cpp \
    $${PWD}/OAIError_500.cpp \
    $${PWD}/OAIExtendedPricingOptions.cpp \
    $${PWD}/OAIExtended_Price.cpp \
    $${PWD}/OAIFareDetailsBySegment.cpp \
    $${PWD}/OAIFareRules.cpp \
    $${PWD}/OAIFee.cpp \
    $${PWD}/OAIFeeType.cpp \
    $${PWD}/OAIFlightEndPoint.cpp \
    $${PWD}/OAIFlightOffer.cpp \
    $${PWD}/OAIFlightOfferSource.cpp \
    $${PWD}/OAIFlightOfferUpsellIn.cpp \
    $${PWD}/OAIFlightSegment.cpp \
    $${PWD}/OAIFlightStop.cpp \
    $${PWD}/OAIGet_Upsell_Query.cpp \
    $${PWD}/OAIIssue.cpp \
    $${PWD}/OAIIssue_Source.cpp \
    $${PWD}/OAIItineraries.cpp \
    $${PWD}/OAILocationValue.cpp \
    $${PWD}/OAIOneWayUpselledCombinations.cpp \
    $${PWD}/OAIOperatingFlight.cpp \
    $${PWD}/OAIOriginalFlightEndPoint.cpp \
    $${PWD}/OAIOriginalFlightStop.cpp \
    $${PWD}/OAIPayment.cpp \
    $${PWD}/OAIPaymentBrand.cpp \
    $${PWD}/OAIPrice.cpp \
    $${PWD}/OAIPricingOptions.cpp \
    $${PWD}/OAISegment.cpp \
    $${PWD}/OAIServiceName.cpp \
    $${PWD}/OAISliceDiceIndicator.cpp \
    $${PWD}/OAISuccess_Upsell.cpp \
    $${PWD}/OAITax.cpp \
    $${PWD}/OAITermAndCondition.cpp \
    $${PWD}/OAITravelClass.cpp \
    $${PWD}/OAITravelerPricing.cpp \
    $${PWD}/OAITravelerPricingFareOption.cpp \
    $${PWD}/OAITravelerType.cpp \
# APIs
    $${PWD}/OAIShoppingApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
