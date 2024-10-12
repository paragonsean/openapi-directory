

# AlertFilter

The OData filters to be used for Alert

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appearedOnTime** | **OffsetDateTime** | Specifies the appeared time (in UTC) of the alerts to be filtered. Only &#39;Greater-Than&#39; and &#39;Lesser-Than&#39; operators are supported for this property. |  [optional] |
|**severity** | [**SeverityEnum**](#SeverityEnum) | Specifies the severity of the alerts to be filtered. Only &#39;Equality&#39; operator is supported for this property. |  [optional] |
|**sourceName** | **String** | Specifies the source name of the alerts to be filtered. Only &#39;Equality&#39; operator is supported for this property. |  [optional] |
|**sourceType** | [**SourceTypeEnum**](#SourceTypeEnum) | Specifies the source type of the alerts to be filtered. Only &#39;Equality&#39; operator is supported for this property. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Specifies the status of the alerts to be filtered. Only &#39;Equality&#39; operator is supported for this property. |  [optional] |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| INFORMATIONAL | &quot;Informational&quot; |
| WARNING | &quot;Warning&quot; |
| CRITICAL | &quot;Critical&quot; |



## Enum: SourceTypeEnum

| Name | Value |
|---- | -----|
| RESOURCE | &quot;Resource&quot; |
| DEVICE | &quot;Device&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;Active&quot; |
| CLEARED | &quot;Cleared&quot; |



