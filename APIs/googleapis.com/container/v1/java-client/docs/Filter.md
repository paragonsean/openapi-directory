

# Filter

Allows filtering to one or more specific event types. If event types are present, those and only those event types will be transmitted to the cluster. Other types will be skipped. If no filter is specified, or no event types are present, all event types will be sent

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**eventType** | [**List&lt;EventTypeEnum&gt;**](#List&lt;EventTypeEnum&gt;) | Event types to allowlist. |  [optional] |



## Enum: List&lt;EventTypeEnum&gt;

| Name | Value |
|---- | -----|
| EVENT_TYPE_UNSPECIFIED | &quot;EVENT_TYPE_UNSPECIFIED&quot; |
| UPGRADE_AVAILABLE_EVENT | &quot;UPGRADE_AVAILABLE_EVENT&quot; |
| UPGRADE_EVENT | &quot;UPGRADE_EVENT&quot; |
| SECURITY_BULLETIN_EVENT | &quot;SECURITY_BULLETIN_EVENT&quot; |



