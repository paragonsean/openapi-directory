

# Audience

Audience with details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customProperties** | [**Map&lt;String, InnerEnum&gt;**](#Map&lt;String, InnerEnum&gt;) | Custom properties used in the definition. |  [optional] |
|**enabled** | **Boolean** |  |  [optional] |
|**estimatedTotalCount** | **Long** | Estimated total audience size. |  [optional] |
|**timestamp** | **OffsetDateTime** | Date the audience was last refreshed. |  [optional] |
|**definition** | **String** | Audience definition in OData format. |  [optional] |
|**description** | **String** | Audience description. |  [optional] |
|**estimatedCount** | **Long** | Estimated audience size. |  [optional] |
|**name** | **String** | Audience name. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Audience state. |  [optional] |



## Enum: Map&lt;String, InnerEnum&gt;

| Name | Value |
|---- | -----|
| STRING | &quot;string&quot; |
| NUMBER | &quot;number&quot; |
| BOOLEAN | &quot;boolean&quot; |
| DATE_TIME | &quot;date_time&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| CALCULATING | &quot;Calculating&quot; |
| READY | &quot;Ready&quot; |
| DISABLED | &quot;Disabled&quot; |



