# TravelPartnerApi.MissedParticipationCountDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hotelSuspendedCount** | **String** | The total number of missed participations due to one or more of your hotels being suspended due to price accuracy violations. | [optional] 
**noAvailabilityCount** | **String** | The total number of missed participation due to the hotel/itinerary combination being unavailable, or the traveler was ineligible for the rates. To participate in these auctions, you may need to provide more pricing information. | [optional] 
**noLandingPageCount** | **String** | No landing page matched the user. | [optional] 
**noPriceCount** | **String** | The total number of missed participations due to a price not being offered for the requested itinerary. | [optional] 
**noPriceCountDetails** | [**NoPriceCountDetails**](NoPriceCountDetails.md) |  | [optional] 
**noTaxBreakdownCount** | **String** | The total number of missed participation due to one or more of your hotels not specifying taxes and fees separately. | [optional] 
**otherReasonCount** | **String** | Hotel did not participate for an unknown reason. | [optional] 
**priceMissingCount** | **String** | The total number of missed participations due to either a price not being present in Google&#39;s cache or failing to successfully respond to live pricing. Comprised of the following: * Bandwidth depleted * Cache rate missing * Itinerary blocked * Live pricing not set up * Live pricing timeout * Live pricing error | [optional] 
**priceMissingCountDetails** | [**PriceMissingCountDetails**](PriceMissingCountDetails.md) |  | [optional] 
**priceProblemCount** | **String** | The total number of missed participation due to an issue with the accuracy of the price provided for the itinerary. Comprised of the following: * Hotel suspended * Price unusually high * Price unusually low * Taxes and feeds missing | [optional] 
**priceProblemCountDetails** | [**PriceProblemCountDetails**](PriceProblemCountDetails.md) |  | [optional] 
**priceUnavailableCount** | **String** | The total number of missed participation due to price listed as unavailable (-1) for the requested itinerary. Comprised of the following: * Price unavailable * Participation not likely * Other | [optional] 
**priceUnavailableCountDetails** | [**PriceUnavailableCountDetails**](PriceUnavailableCountDetails.md) |  | [optional] 


