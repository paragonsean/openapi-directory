

# SecurityPostureConfig

SecurityPostureConfig defines the flags needed to enable/disable features for the Security Posture API.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mode** | [**ModeEnum**](#ModeEnum) | Sets which mode to use for Security Posture features. |  [optional] |
|**vulnerabilityMode** | [**VulnerabilityModeEnum**](#VulnerabilityModeEnum) | Sets which mode to use for vulnerability scanning. |  [optional] |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| MODE_UNSPECIFIED | &quot;MODE_UNSPECIFIED&quot; |
| DISABLED | &quot;DISABLED&quot; |
| BASIC | &quot;BASIC&quot; |



## Enum: VulnerabilityModeEnum

| Name | Value |
|---- | -----|
| MODE_UNSPECIFIED | &quot;VULNERABILITY_MODE_UNSPECIFIED&quot; |
| DISABLED | &quot;VULNERABILITY_DISABLED&quot; |
| BASIC | &quot;VULNERABILITY_BASIC&quot; |
| ENTERPRISE | &quot;VULNERABILITY_ENTERPRISE&quot; |



