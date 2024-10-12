

# RoundUpObject

Provides information about how a Round Up was applied, such as whether or not a boost was included in the Round Up. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | [**MoneyObject**](MoneyObject.md) | The total amount of this Round Up, including any boosts, represented as a negative value.  |  |
|**boostPortion** | [**MoneyObject**](MoneyObject.md) | The portion of the Round Up &#x60;amount&#x60; owing to boosted Round Ups, represented as a negative value. If no boost was added to the Round Up this field will be &#x60;null&#x60;.  |  |



