# BetsApi.SingleBetRequestBody

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delayedBetId** | **String** | The delayed bet identifier | [optional] 
**freeBetId** | **String** | The ID number of the free bet token if used in conjunction with this bet | [optional] 
**priceDen** | **Number** | When the odds are shown in vulgar fractions this is the denominator of the fraction. For example: 2 in 5/2 | [optional] 
**priceNum** | **Number** | When the odds are shown in vulgar fractions this is the numerator of the fraction. For example: 5 in 5/2 | [optional] 
**priceType** | **String** | The type of price taken by the customer when the bet is made. Can be one of the following: L - Live Fixed price, S - Starting price - Horse and Greyhound racing or G - Guaranteed best price. | 
**selectionId** | **String** | The unique ID for the selection of the bet | 
**stake** | **Number** | The amount of the stake placed on the bet | 
**type** | **String** | The type of bet placed. Can be one of the following: W - Win or E- EachWay | 


