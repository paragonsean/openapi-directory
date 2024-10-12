

# SelectPsuAuthenticationMethodResponse

Body of the JSON response for a successful select PSU authentication method request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | **LinksSelectPsuAuthenticationMethod** |  |  [optional] |
|**challengeData** | [**ChallengeData**](ChallengeData.md) |  |  [optional] |
|**chosenScaMethod** | [**AuthenticationObject**](AuthenticationObject.md) |  |  [optional] |
|**currencyConversionFees** | [**Amount**](Amount.md) |  |  [optional] |
|**estimatedInterbankSettlementAmount** | [**Amount**](Amount.md) |  |  [optional] |
|**estimatedTotalAmount** | [**Amount**](Amount.md) |  |  [optional] |
|**psuMessage** | **String** | Text to be displayed to the PSU. |  [optional] |
|**scaStatus** | **ScaStatus** |  |  |
|**transactionFees** | [**Amount**](Amount.md) |  |  [optional] |



