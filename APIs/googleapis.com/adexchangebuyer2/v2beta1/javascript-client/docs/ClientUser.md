# AdExchangeBuyerApiIi.ClientUser

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientAccountId** | **String** | Numerical account ID of the client buyer with which the user is associated; the buyer must be a client of the current sponsor buyer. The value of this field is ignored in an update operation. | [optional] 
**email** | **String** | User&#39;s email address. The value of this field is ignored in an update operation. | [optional] 
**status** | **String** | The status of the client user. | [optional] 
**userId** | **String** | The unique numerical ID of the client user that has accepted an invitation. The value of this field is ignored in an update operation. | [optional] 



## Enum: StatusEnum


* `USER_STATUS_UNSPECIFIED` (value: `"USER_STATUS_UNSPECIFIED"`)

* `PENDING` (value: `"PENDING"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `DISABLED` (value: `"DISABLED"`)




