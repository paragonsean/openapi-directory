# OpenChannelMarketApi.Transaction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | The total amount paid in cents | 
**appId** | **String** | The id of the app involved with this transaction | 
**customData** | **Object** | A custom JSON object that you can create and attach to this record | [optional] 
**date** | **Number** | The date (in millis) of when this transaction occurred | 
**developerAmount** | **Number** | The total amount paid to the developer in cents | [optional] 
**developerId** | **String** | The id of the developer involved with this transaction | 
**feeAmount** | **Number** | The total amount paid to payment processing fees in cents | [optional] 
**marketplaceAmount** | **Number** | The total amount paid to the marketplace owner in cents | [optional] 
**ownershipId** | **String** | The id for the ownership associated with this transaction | 
**transactionId** | **String** | The id for this transaction | 
**type** | **String** | The type for this transaction | 
**userId** | **String** | The id of the user making the transaction | 



## Enum: TypeEnum


* `payment` (value: `"payment"`)

* `refund` (value: `"refund"`)




