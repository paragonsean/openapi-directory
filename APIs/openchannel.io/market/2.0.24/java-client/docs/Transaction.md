

# Transaction

A transaction for an app initiated by a user

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Integer** | The total amount paid in cents |  |
|**appId** | **String** | The id of the app involved with this transaction |  |
|**customData** | **Object** | A custom JSON object that you can create and attach to this record |  [optional] |
|**date** | **Long** | The date (in millis) of when this transaction occurred |  |
|**developerAmount** | **Integer** | The total amount paid to the developer in cents |  [optional] |
|**developerId** | **String** | The id of the developer involved with this transaction |  |
|**feeAmount** | **Integer** | The total amount paid to payment processing fees in cents |  [optional] |
|**marketplaceAmount** | **Integer** | The total amount paid to the marketplace owner in cents |  [optional] |
|**ownershipId** | **String** | The id for the ownership associated with this transaction |  |
|**transactionId** | **String** | The id for this transaction |  |
|**type** | [**TypeEnum**](#TypeEnum) | The type for this transaction |  |
|**userId** | **String** | The id of the user making the transaction |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PAYMENT | &quot;payment&quot; |
| REFUND | &quot;refund&quot; |



