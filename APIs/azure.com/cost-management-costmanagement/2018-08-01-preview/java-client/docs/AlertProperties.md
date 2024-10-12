

# AlertProperties

The properties of an Alert.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**closeTime** | **OffsetDateTime** | The time when the alert was closed (resolved / overridden). |  [optional] [readonly] |
|**costEntityId** | **String** | The id of the creating cost-entity (budget, invoice, credit). |  [optional] [readonly] |
|**creationTime** | **OffsetDateTime** | The time when the alert was created. |  [optional] [readonly] |
|**definition** | [**AlertDefinition**](AlertDefinition.md) |  |  [optional] |
|**description** | **String** | Description of an alert. |  [optional] [readonly] |
|**details** | **Map&lt;String, String&gt;** | Specific details of an alert - key-value dictionary. |  [optional] [readonly] |
|**modificationTime** | **OffsetDateTime** | The current status when alert was modified. |  [optional] [readonly] |
|**modificationUsername** | **String** | The username who modified the alert. |  [optional] [readonly] |
|**scope** | **String** | The scope of an alert. |  [optional] [readonly] |
|**source** | [**SourceEnum**](#SourceEnum) | The source of an Alert |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | The current status of the alert. |  [optional] |
|**statusModificationTime** | **OffsetDateTime** | The current status when alert status was modified. |  [optional] [readonly] |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| PRESET | &quot;Preset&quot; |
| USER | &quot;User&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;Active&quot; |
| OVERRIDDEN | &quot;Overridden&quot; |
| RESOLVED | &quot;Resolved&quot; |
| DISMISSED | &quot;Dismissed&quot; |



