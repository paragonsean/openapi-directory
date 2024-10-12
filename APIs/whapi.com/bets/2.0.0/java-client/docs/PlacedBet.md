

# PlacedBet


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cashinValue** | **Double** | The cash in value of the bet. For example £0.88. When no value is given or no value is present, no cash in is available |  [optional] |
|**estimatedReturns** | **Double** | The estimated value of the returns if the bet is successful. Note: when an estimated return isn’t available, as in the case of a bet placed on a horse at SP (starting price) where the actual price is unknown when the bet is placed, ‘NOT_AVAILABLE’ will appear in the response field. |  |
|**freeBetValue** | **Double** | If a free bet token is used for the bet, this element represents the value |  [optional] |
|**id** | **String** | The unique identifier of the bet |  |
|**legs** | [**List&lt;PlacedBetLeg&gt;**](PlacedBetLeg.md) |  |  [optional] |
|**numLines** | **Integer** | Number of lines of bets |  [optional] |
|**numSelections** | **Integer** | Number of selections that the bet is made of |  [optional] |
|**receipt** | **String** | The unique identifier of the receipt for the bet |  [optional] |
|**settled** | **Boolean** | Whether the bet is settled |  |
|**stake** | **Double** | The bet stake, which represents the total value of the bet. For example: £ 12.34 |  |
|**stakePerLine** | **Double** | The individual stake on each line of the bet. For example: £ 6.17 |  [optional] |
|**status** | **String** | The status of the bet. Can be one of the following: A - Active, S - suspended, C - Cashed Out |  |
|**transDateTime** | **String** | The time the bet was placed |  |
|**typeCode** | **String** | The bet type code of the bet. For example: TBL (Treble) |  |
|**typeName** | **String** | The name of the bet type. For example: Double |  |
|**winnings** | **Double** | Actual value of the returns from this bet |  |



