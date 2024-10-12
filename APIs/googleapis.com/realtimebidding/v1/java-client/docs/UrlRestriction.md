

# UrlRestriction

Deprecated. This will be removed in October 2023. For more information, see the release notes: https://developers.google.com/authorized-buyers/apis/relnotes#real-time-bidding-api Represents the URL restriction (for the URL captured by the pixel callback) for a user list.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endDate** | [**Date**](Date.md) |  |  [optional] |
|**restrictionType** | [**RestrictionTypeEnum**](#RestrictionTypeEnum) | The restriction type for the specified URL. |  [optional] |
|**startDate** | [**Date**](Date.md) |  |  [optional] |
|**url** | **String** | Required. The URL to use for applying the restriction on the user list. |  [optional] |



## Enum: RestrictionTypeEnum

| Name | Value |
|---- | -----|
| RESTRICTION_TYPE_UNSPECIFIED | &quot;RESTRICTION_TYPE_UNSPECIFIED&quot; |
| CONTAINS | &quot;CONTAINS&quot; |
| EQUALS | &quot;EQUALS&quot; |
| STARTS_WITH | &quot;STARTS_WITH&quot; |
| ENDS_WITH | &quot;ENDS_WITH&quot; |
| DOES_NOT_EQUAL | &quot;DOES_NOT_EQUAL&quot; |
| DOES_NOT_CONTAIN | &quot;DOES_NOT_CONTAIN&quot; |
| DOES_NOT_START_WITH | &quot;DOES_NOT_START_WITH&quot; |
| DOES_NOT_END_WITH | &quot;DOES_NOT_END_WITH&quot; |



