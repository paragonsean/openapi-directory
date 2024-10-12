

# TagSettingsProperties

Tag filter information for the VM.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**filterOperator** | [**FilterOperatorEnum**](#FilterOperatorEnum) | Filter VMs by Any or All specified tags. |  [optional] |
|**tags** | **Map&lt;String, List&lt;String&gt;&gt;** | Dictionary of tags with its list of values. |  [optional] |



## Enum: FilterOperatorEnum

| Name | Value |
|---- | -----|
| ALL | &quot;All&quot; |
| ANY | &quot;Any&quot; |



