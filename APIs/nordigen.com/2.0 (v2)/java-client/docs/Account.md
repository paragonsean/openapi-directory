

# Account

The representation of a bank account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**created** | **OffsetDateTime** | The date &amp; time at which the account object was created. |  [optional] [readonly] |
|**iban** | **String** | The Account IBAN |  [optional] [readonly] |
|**id** | **UUID** | The ID of this Account, used to refer to this account in other API calls. |  [optional] [readonly] |
|**institutionId** | **String** | The ASPSP associated with this account. |  [optional] [readonly] |
|**lastAccessed** | **OffsetDateTime** | The date &amp; time at which the account object was last accessed. |  [optional] [readonly] |
|**ownerName** | **String** | The name of the account owner. |  [optional] [readonly] |
|**status** | **AccountStatusEnum** | The processing status of this account. |  [optional] [readonly] |



