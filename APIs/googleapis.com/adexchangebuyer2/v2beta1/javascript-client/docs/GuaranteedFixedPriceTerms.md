# AdExchangeBuyerApiIi.GuaranteedFixedPriceTerms

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fixedPrices** | [**[PricePerBuyer]**](PricePerBuyer.md) | Fixed price for the specified buyer. | [optional] 
**guaranteedImpressions** | **String** | Guaranteed impressions as a percentage. This is the percentage of guaranteed looks that the buyer is guaranteeing to buy. | [optional] 
**guaranteedLooks** | **String** | Count of guaranteed looks. Required for deal, optional for product. For CPD deals, buyer changes to guaranteed_looks will be ignored. | [optional] 
**impressionCap** | **String** | The lifetime impression cap for CPM sponsorship deals. The deal will stop serving when the cap is reached. | [optional] 
**minimumDailyLooks** | **String** | Daily minimum looks for CPD deal types. For CPD deals, buyer should negotiate on this field instead of guaranteed_looks. | [optional] 
**percentShareOfVoice** | **String** | For sponsorship deals, this is the percentage of the seller&#39;s eligible impressions that the deal will serve until the cap is reached. | [optional] 
**reservationType** | **String** | The reservation type for a Programmatic Guaranteed deal. This indicates whether the number of impressions is fixed, or a percent of available impressions. If not specified, the default reservation type is STANDARD. | [optional] 



## Enum: ReservationTypeEnum


* `RESERVATION_TYPE_UNSPECIFIED` (value: `"RESERVATION_TYPE_UNSPECIFIED"`)

* `STANDARD` (value: `"STANDARD"`)

* `SPONSORSHIP` (value: `"SPONSORSHIP"`)




