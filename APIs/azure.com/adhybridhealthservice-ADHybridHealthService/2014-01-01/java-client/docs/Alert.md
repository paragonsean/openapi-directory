

# Alert

 The alert details indicating an issue with service or server.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activeAlertProperties** | [**List&lt;Item&gt;**](Item.md) | The active alert properties. |  [optional] |
|**additionalInformation** | [**List&lt;AdditionalInformation&gt;**](AdditionalInformation.md) | Additional information related to the alert. |  [optional] |
|**alertId** | **UUID** | The alert Id. |  [optional] |
|**createdDate** | **OffsetDateTime** | The date and time,in UTC,when the alert was created. |  [optional] |
|**description** | **String** | The alert description. |  [optional] |
|**displayName** | **String** | The display name for the alert. |  [optional] |
|**lastUpdated** | **OffsetDateTime** | The date and time, in UTC, when the alert was last updated. |  [optional] |
|**level** | [**LevelEnum**](#LevelEnum) | The alert level which indicates the severity of the alert. |  [optional] |
|**monitorRoleType** | **String** | The monitoring role type for which the alert was raised. |  [optional] |
|**relatedLinks** | [**List&lt;HelpLink&gt;**](HelpLink.md) | The help links to get more information related to the alert. |  [optional] |
|**remediation** | **String** | The alert remediation. |  [optional] |
|**resolvedAlertProperties** | [**List&lt;Item&gt;**](Item.md) | The resolved alert properties. |  [optional] |
|**resolvedDate** | **OffsetDateTime** | The date and time, in UTC, when the alert was resolved. |  [optional] |
|**scope** | **String** | The scope of the alert. Indicates if it is a service or a server related alert. |  [optional] |
|**serviceId** | **UUID** | The service Id. |  [optional] |
|**serviceMemberId** | **UUID** | The server Id. |  [optional] |
|**shortName** | **String** | The alert short name. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The alert state which can be either active or resolved with multiple resolution types. |  [optional] |
|**tenantId** | **UUID** | The tenant Id. |  [optional] |



## Enum: LevelEnum

| Name | Value |
|---- | -----|
| WARNING | &quot;Warning&quot; |
| ERROR | &quot;Error&quot; |
| PRE_WARNING | &quot;PreWarning&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;Active&quot; |
| RESOLVED_BY_POSITIVE_RESULT | &quot;ResolvedByPositiveResult&quot; |
| RESOLVED_MANUALLY | &quot;ResolvedManually&quot; |
| RESOLVED_BY_TIMER | &quot;ResolvedByTimer&quot; |
| RESOLVED_BY_STATE_CHANGE | &quot;ResolvedByStateChange&quot; |



