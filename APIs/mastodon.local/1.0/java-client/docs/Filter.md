

# Filter

Represents a user-defined filter for determining which statuses should not be shown to the user.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**context** | [**List&lt;ContextEnum&gt;**](#List&lt;ContextEnum&gt;) | The contexts in which the filter should be applied. |  [optional] |
|**expiresAt** | **String** | When the filter should no longer be applied. ISO 8601 Datetime, or null if the filter does not expire |  [optional] |
|**id** | **String** | The ID of the filter in the database. Cast from an integer, but not guaranteed to be a number. |  [optional] |
|**irreversible** | **Boolean** | Should matching entities in home and notifications be dropped by the server? |  [optional] |
|**phrase** | **String** | The text to be filtered. |  [optional] |
|**wholeWord** | **Boolean** | Should the filter consider word boundaries? |  [optional] |



## Enum: List&lt;ContextEnum&gt;

| Name | Value |
|---- | -----|
| HOME | &quot;home&quot; |
| NOTIFICATIONS | &quot;notifications&quot; |
| PUBLIC | &quot;public&quot; |
| THREAD | &quot;thread&quot; |



