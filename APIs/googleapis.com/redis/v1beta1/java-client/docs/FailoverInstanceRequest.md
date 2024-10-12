

# FailoverInstanceRequest

Request for Failover.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataProtectionMode** | [**DataProtectionModeEnum**](#DataProtectionModeEnum) | Optional. Available data protection modes that the user can choose. If it&#39;s unspecified, data protection mode will be LIMITED_DATA_LOSS by default. |  [optional] |



## Enum: DataProtectionModeEnum

| Name | Value |
|---- | -----|
| DATA_PROTECTION_MODE_UNSPECIFIED | &quot;DATA_PROTECTION_MODE_UNSPECIFIED&quot; |
| LIMITED_DATA_LOSS | &quot;LIMITED_DATA_LOSS&quot; |
| FORCE_DATA_LOSS | &quot;FORCE_DATA_LOSS&quot; |



