QT += network

HEADERS += \
# Models
    $${PWD}/OAIAdditionalService.h \
    $${PWD}/OAIAdditionalServiceType.h \
    $${PWD}/OAIAdditionalServicesRequest.h \
    $${PWD}/OAIAddress.h \
    $${PWD}/OAIAircraftCabinAmenities.h \
    $${PWD}/OAIAircraftCabinAmenities_Beverage.h \
    $${PWD}/OAIAircraftCabinAmenities_Entertainment.h \
    $${PWD}/OAIAircraftCabinAmenities_Food.h \
    $${PWD}/OAIAircraftCabinAmenities_Power.h \
    $${PWD}/OAIAircraftCabinAmenities_Wifi.h \
    $${PWD}/OAIAircraftEquipment.h \
    $${PWD}/OAIAllotmentDetails.h \
    $${PWD}/OAIAmenity.h \
    $${PWD}/OAIAmenity_Media.h \
    $${PWD}/OAIAmenity_Seat.h \
    $${PWD}/OAIAvailableSeatsCounter.h \
    $${PWD}/OAIBaggageAllowance.h \
    $${PWD}/OAIBaseName.h \
    $${PWD}/OAICo2Emission.h \
    $${PWD}/OAICollectionLinks.h \
    $${PWD}/OAICollection_Meta.h \
    $${PWD}/OAIContact.h \
    $${PWD}/OAIContactDictionary.h \
    $${PWD}/OAIContactPurpose.h \
    $${PWD}/OAICoordinates.h \
    $${PWD}/OAIDeck.h \
    $${PWD}/OAIDeckConfiguration.h \
    $${PWD}/OAIDescription.h \
    $${PWD}/OAIDictionaries.h \
    $${PWD}/OAIDiscount.h \
    $${PWD}/OAIDiscountTravelerType.h \
    $${PWD}/OAIDiscountType.h \
    $${PWD}/OAIDocument.h \
    $${PWD}/OAIDocumentType.h \
    $${PWD}/OAIElementaryPrice.h \
    $${PWD}/OAIEmergencyContact.h \
    $${PWD}/OAIError_400.h \
    $${PWD}/OAIError_404.h \
    $${PWD}/OAIError_500.h \
    $${PWD}/OAIExtended_Price.h \
    $${PWD}/OAIFacility.h \
    $${PWD}/OAIFareDetailsBySegment.h \
    $${PWD}/OAIFareRules.h \
    $${PWD}/OAIFee.h \
    $${PWD}/OAIFeeType.h \
    $${PWD}/OAIFlightEndPoint.h \
    $${PWD}/OAIFlightOffer.h \
    $${PWD}/OAIFlightOfferSource.h \
    $${PWD}/OAIFlightOffers.h \
    $${PWD}/OAIFlightSegment.h \
    $${PWD}/OAIFlightStop.h \
    $${PWD}/OAIIdentityDocument.h \
    $${PWD}/OAIIssue.h \
    $${PWD}/OAIIssue_Source.h \
    $${PWD}/OAIItineraries.h \
    $${PWD}/OAILink.h \
    $${PWD}/OAILocationValue.h \
    $${PWD}/OAILoyaltyProgram.h \
    $${PWD}/OAIName.h \
    $${PWD}/OAIOperatingFlight.h \
    $${PWD}/OAIPhone.h \
    $${PWD}/OAIPhoneDeviceType.h \
    $${PWD}/OAIPrice.h \
    $${PWD}/OAIPricingOptions.h \
    $${PWD}/OAIQualifiedFreeText.h \
    $${PWD}/OAISeat.h \
    $${PWD}/OAISeatMap.h \
    $${PWD}/OAISeatMap_Reply.h \
    $${PWD}/OAISeatmapTravelerPricing.h \
    $${PWD}/OAISegment.h \
    $${PWD}/OAIServiceName.h \
    $${PWD}/OAISliceDiceIndicator.h \
    $${PWD}/OAIStakeholder.h \
    $${PWD}/OAIStakeholderGender.h \
    $${PWD}/OAITax.h \
    $${PWD}/OAITermAndCondition.h \
    $${PWD}/OAITravelClass.h \
    $${PWD}/OAITraveler.h \
    $${PWD}/OAITravelerPricing.h \
    $${PWD}/OAITravelerPricingFareOption.h \
    $${PWD}/OAITravelerType.h \
    $${PWD}/OAITravelers_map.h \
# APIs
    $${PWD}/OAIDisplaySeatMapsApi.h \
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
    $${PWD}/OAIAddress.cpp \
    $${PWD}/OAIAircraftCabinAmenities.cpp \
    $${PWD}/OAIAircraftCabinAmenities_Beverage.cpp \
    $${PWD}/OAIAircraftCabinAmenities_Entertainment.cpp \
    $${PWD}/OAIAircraftCabinAmenities_Food.cpp \
    $${PWD}/OAIAircraftCabinAmenities_Power.cpp \
    $${PWD}/OAIAircraftCabinAmenities_Wifi.cpp \
    $${PWD}/OAIAircraftEquipment.cpp \
    $${PWD}/OAIAllotmentDetails.cpp \
    $${PWD}/OAIAmenity.cpp \
    $${PWD}/OAIAmenity_Media.cpp \
    $${PWD}/OAIAmenity_Seat.cpp \
    $${PWD}/OAIAvailableSeatsCounter.cpp \
    $${PWD}/OAIBaggageAllowance.cpp \
    $${PWD}/OAIBaseName.cpp \
    $${PWD}/OAICo2Emission.cpp \
    $${PWD}/OAICollectionLinks.cpp \
    $${PWD}/OAICollection_Meta.cpp \
    $${PWD}/OAIContact.cpp \
    $${PWD}/OAIContactDictionary.cpp \
    $${PWD}/OAIContactPurpose.cpp \
    $${PWD}/OAICoordinates.cpp \
    $${PWD}/OAIDeck.cpp \
    $${PWD}/OAIDeckConfiguration.cpp \
    $${PWD}/OAIDescription.cpp \
    $${PWD}/OAIDictionaries.cpp \
    $${PWD}/OAIDiscount.cpp \
    $${PWD}/OAIDiscountTravelerType.cpp \
    $${PWD}/OAIDiscountType.cpp \
    $${PWD}/OAIDocument.cpp \
    $${PWD}/OAIDocumentType.cpp \
    $${PWD}/OAIElementaryPrice.cpp \
    $${PWD}/OAIEmergencyContact.cpp \
    $${PWD}/OAIError_400.cpp \
    $${PWD}/OAIError_404.cpp \
    $${PWD}/OAIError_500.cpp \
    $${PWD}/OAIExtended_Price.cpp \
    $${PWD}/OAIFacility.cpp \
    $${PWD}/OAIFareDetailsBySegment.cpp \
    $${PWD}/OAIFareRules.cpp \
    $${PWD}/OAIFee.cpp \
    $${PWD}/OAIFeeType.cpp \
    $${PWD}/OAIFlightEndPoint.cpp \
    $${PWD}/OAIFlightOffer.cpp \
    $${PWD}/OAIFlightOfferSource.cpp \
    $${PWD}/OAIFlightOffers.cpp \
    $${PWD}/OAIFlightSegment.cpp \
    $${PWD}/OAIFlightStop.cpp \
    $${PWD}/OAIIdentityDocument.cpp \
    $${PWD}/OAIIssue.cpp \
    $${PWD}/OAIIssue_Source.cpp \
    $${PWD}/OAIItineraries.cpp \
    $${PWD}/OAILink.cpp \
    $${PWD}/OAILocationValue.cpp \
    $${PWD}/OAILoyaltyProgram.cpp \
    $${PWD}/OAIName.cpp \
    $${PWD}/OAIOperatingFlight.cpp \
    $${PWD}/OAIPhone.cpp \
    $${PWD}/OAIPhoneDeviceType.cpp \
    $${PWD}/OAIPrice.cpp \
    $${PWD}/OAIPricingOptions.cpp \
    $${PWD}/OAIQualifiedFreeText.cpp \
    $${PWD}/OAISeat.cpp \
    $${PWD}/OAISeatMap.cpp \
    $${PWD}/OAISeatMap_Reply.cpp \
    $${PWD}/OAISeatmapTravelerPricing.cpp \
    $${PWD}/OAISegment.cpp \
    $${PWD}/OAIServiceName.cpp \
    $${PWD}/OAISliceDiceIndicator.cpp \
    $${PWD}/OAIStakeholder.cpp \
    $${PWD}/OAIStakeholderGender.cpp \
    $${PWD}/OAITax.cpp \
    $${PWD}/OAITermAndCondition.cpp \
    $${PWD}/OAITravelClass.cpp \
    $${PWD}/OAITraveler.cpp \
    $${PWD}/OAITravelerPricing.cpp \
    $${PWD}/OAITravelerPricingFareOption.cpp \
    $${PWD}/OAITravelerType.cpp \
    $${PWD}/OAITravelers_map.cpp \
# APIs
    $${PWD}/OAIDisplaySeatMapsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
