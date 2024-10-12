

# DataMaskingPolicyProperties

The properties of a database data masking policy.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationPrincipals** | **String** | The list of the application principals. This is a legacy parameter and is no longer used. |  [optional] [readonly] |
|**dataMaskingState** | [**DataMaskingStateEnum**](#DataMaskingStateEnum) | The state of the data masking policy. |  |
|**exemptPrincipals** | **String** | The list of the exempt principals. Specifies the semicolon-separated list of database users for which the data masking policy does not apply. The specified users receive data results without masking for all of the database queries. |  [optional] |
|**maskingLevel** | **String** | The masking level. This is a legacy parameter and is no longer used. |  [optional] [readonly] |



## Enum: DataMaskingStateEnum

| Name | Value |
|---- | -----|
| DISABLED | &quot;Disabled&quot; |
| ENABLED | &quot;Enabled&quot; |



