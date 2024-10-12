

# GoogleCloudApigeeV1AliasRevisionConfig


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**location** | **String** | Location of the alias file. For example, a Google Cloud Storage URI. |  [optional] |
|**name** | **String** | Name of the alias revision included in the keystore in the following format: &#x60;organizations/{org}/environments/{env}/keystores/{keystore}/aliases/{alias}/revisions/{rev}&#x60; |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ALIAS_TYPE_UNSPECIFIED | &quot;ALIAS_TYPE_UNSPECIFIED&quot; |
| CERT | &quot;CERT&quot; |
| KEY_CERT | &quot;KEY_CERT&quot; |



