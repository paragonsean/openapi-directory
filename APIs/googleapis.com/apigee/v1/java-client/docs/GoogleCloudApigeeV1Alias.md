

# GoogleCloudApigeeV1Alias

Reference to a certificate or key/certificate pair.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alias** | **String** | Resource ID for this alias. Values must match the regular expression &#x60;[^/]{1,255}&#x60;. |  [optional] |
|**certsInfo** | [**GoogleCloudApigeeV1Certificate**](GoogleCloudApigeeV1Certificate.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of alias. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ALIAS_TYPE_UNSPECIFIED | &quot;ALIAS_TYPE_UNSPECIFIED&quot; |
| CERT | &quot;CERT&quot; |
| KEY_CERT | &quot;KEY_CERT&quot; |



