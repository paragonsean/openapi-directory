

# Source

Represents display or publishing preferences of user's own account. Returned as an additional entity when verifying and updated credentials, as an attribute of Account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fields** | [**List&lt;Field&gt;**](Field.md) | Metadata about the account. |  [optional] |
|**followRequestsCount** | **Integer** | The number of pending follow requests |  [optional] |
|**language** | **String** | The default posting language for new statuses, ISO 639-1 language two-letter code. |  [optional] |
|**note** | **String** | Profile bio |  [optional] |
|**privacy** | [**PrivacyEnum**](#PrivacyEnum) | The default post privacy to be used for new statuses. |  [optional] |
|**sensitive** | **Boolean** | Whether new statuses should be marked sensitive by default. |  [optional] |



## Enum: PrivacyEnum

| Name | Value |
|---- | -----|
| PUBLIC | &quot;public&quot; |
| UNLISTED | &quot;unlisted&quot; |
| PRIVATE | &quot;private&quot; |
| DIRECT | &quot;direct&quot; |



