

# AudienceExport

An audience export is a list of users in an audience at the time of the list's creation. One audience may have multiple audience exports created for different days.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**audience** | **String** | Required. The audience resource name. This resource name identifies the audience being listed and is shared between the Analytics Data &amp; Admin APIs. Format: &#x60;properties/{property}/audiences/{audience}&#x60; |  [optional] |
|**audienceDisplayName** | **String** | Output only. The descriptive display name for this audience. For example, \&quot;Purchasers\&quot;. |  [optional] [readonly] |
|**beginCreatingTime** | **String** | Output only. The time when CreateAudienceExport was called and the AudienceExport began the &#x60;CREATING&#x60; state. |  [optional] [readonly] |
|**creationQuotaTokensCharged** | **Integer** | Output only. The total quota tokens charged during creation of the AudienceExport. Because this token count is based on activity from the &#x60;CREATING&#x60; state, this tokens charged will be fixed once an AudienceExport enters the &#x60;ACTIVE&#x60; or &#x60;FAILED&#x60; states. |  [optional] [readonly] |
|**dimensions** | [**List&lt;V1betaAudienceDimension&gt;**](V1betaAudienceDimension.md) | Required. The dimensions requested and displayed in the query response. |  [optional] |
|**errorMessage** | **String** | Output only. Error message is populated when an audience export fails during creation. A common reason for such a failure is quota exhaustion. |  [optional] [readonly] |
|**name** | **String** | Output only. Identifier. The audience export resource name assigned during creation. This resource name identifies this &#x60;AudienceExport&#x60;. Format: &#x60;properties/{property}/audienceExports/{audience_export}&#x60; |  [optional] [readonly] |
|**percentageCompleted** | **Double** | Output only. The percentage completed for this audience export ranging between 0 to 100. |  [optional] [readonly] |
|**rowCount** | **Integer** | Output only. The total number of rows in the AudienceExport result. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The current state for this AudienceExport. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| FAILED | &quot;FAILED&quot; |



