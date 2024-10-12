

# OpenInfo

Information related to the opening state of the business.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**canReopen** | **Boolean** | Output only. Indicates whether this business is eligible for re-open. |  [optional] |
|**openingDate** | [**Date**](Date.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Indicates whether or not the Location is currently open for business. All locations are open by default, unless updated to be closed. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| OPEN_FOR_BUSINESS_UNSPECIFIED | &quot;OPEN_FOR_BUSINESS_UNSPECIFIED&quot; |
| OPEN | &quot;OPEN&quot; |
| CLOSED_PERMANENTLY | &quot;CLOSED_PERMANENTLY&quot; |
| CLOSED_TEMPORARILY | &quot;CLOSED_TEMPORARILY&quot; |



