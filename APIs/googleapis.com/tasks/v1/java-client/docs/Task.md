

# Task


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**completed** | **String** | Completion date of the task (as a RFC 3339 timestamp). This field is omitted if the task has not been completed. |  [optional] |
|**deleted** | **Boolean** | Flag indicating whether the task has been deleted. The default is False. |  [optional] |
|**due** | **String** | Due date of the task (as a RFC 3339 timestamp). Optional. The due date only records date information; the time portion of the timestamp is discarded when setting the due date. It isn&#39;t possible to read or write the time that a task is due via the API. |  [optional] |
|**etag** | **String** | ETag of the resource. |  [optional] |
|**hidden** | **Boolean** | Flag indicating whether the task is hidden. This is the case if the task had been marked completed when the task list was last cleared. The default is False. This field is read-only. |  [optional] |
|**id** | **String** | Task identifier. |  [optional] |
|**kind** | **String** | Type of the resource. This is always \&quot;tasks#task\&quot;. |  [optional] |
|**links** | [**List&lt;TaskLinksInner&gt;**](TaskLinksInner.md) | Collection of links. This collection is read-only. |  [optional] |
|**notes** | **String** | Notes describing the task. Optional. |  [optional] |
|**parent** | **String** | Parent task identifier. This field is omitted if it is a top-level task. This field is read-only. Use the \&quot;move\&quot; method to move the task under a different parent or to the top level. |  [optional] |
|**position** | **String** | String indicating the position of the task among its sibling tasks under the same parent task or at the top level. If this string is greater than another task&#39;s corresponding position string according to lexicographical ordering, the task is positioned after the other task under the same parent task (or at the top level). This field is read-only. Use the \&quot;move\&quot; method to move the task to another position. |  [optional] |
|**selfLink** | **String** | URL pointing to this task. Used to retrieve, update, or delete this task. |  [optional] |
|**status** | **String** | Status of the task. This is either \&quot;needsAction\&quot; or \&quot;completed\&quot;. |  [optional] |
|**title** | **String** | Title of the task. |  [optional] |
|**updated** | **String** | Last modification time of the task (as a RFC 3339 timestamp). |  [optional] |



