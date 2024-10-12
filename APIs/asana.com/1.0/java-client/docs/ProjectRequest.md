

# ProjectRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**gid** | **String** | Globally unique identifier of the resource, as a string. |  [optional] [readonly] |
|**resourceType** | **String** | The base type of this resource. |  [optional] [readonly] |
|**name** | **String** | Name of the project. This is generally a short sentence fragment that fits on a line in the UI for maximum readability. However, it can be longer. |  [optional] |
|**archived** | **Boolean** | True if the project is archived, false if not. Archived projects do not show in the UI by default and may be treated differently for queries. |  [optional] |
|**color** | [**ColorEnum**](#ColorEnum) | Color of the project. |  [optional] |
|**createdAt** | **OffsetDateTime** | The time at which this resource was created. |  [optional] [readonly] |
|**currentStatus** | [**ProjectStatusResponse**](ProjectStatusResponse.md) | *Deprecated: new integrations should prefer the &#x60;current_status_update&#x60; resource.* |  [optional] |
|**currentStatusUpdate** | [**StatusUpdateCompact**](StatusUpdateCompact.md) | The latest &#x60;status_update&#x60; posted to this project. |  [optional] |
|**customFieldSettings** | [**List&lt;CustomFieldSettingResponse&gt;**](CustomFieldSettingResponse.md) | Array of Custom Field Settings (in compact form). |  [optional] [readonly] |
|**defaultView** | [**DefaultViewEnum**](#DefaultViewEnum) | The default view (list, board, calendar, or timeline) of a project. |  [optional] |
|**dueDate** | **OffsetDateTime** | *Deprecated: new integrations should prefer the &#x60;due_on&#x60; field.* |  [optional] |
|**dueOn** | **OffsetDateTime** | The day on which this project is due. This takes a date with format YYYY-MM-DD. |  [optional] |
|**htmlNotes** | **String** | [Opt In](/docs/input-output-options). The notes of the project with formatting as HTML. |  [optional] |
|**isTemplate** | **Boolean** | [Opt In](/docs/input-output-options). *Deprecated - please use a project template endpoint instead (more in [this forum post](https://forum.asana.com/t/a-new-api-for-project-templates/156432)).* Determines if the project is a template. |  [optional] |
|**members** | [**List&lt;UserCompact&gt;**](UserCompact.md) | Array of users who are members of this project. |  [optional] [readonly] |
|**modifiedAt** | **OffsetDateTime** | The time at which this project was last modified. *Note: This does not currently reflect any changes in associations such as tasks or comments that may have been added or removed from the project.* |  [optional] [readonly] |
|**notes** | **String** | Free-form textual information associated with the project (ie., its description). |  [optional] |
|**_public** | **Boolean** | True if the project is public to its team. |  [optional] |
|**startOn** | **LocalDate** | The day on which work for this project begins, or null if the project has no start date. This takes a date with &#x60;YYYY-MM-DD&#x60; format. *Note: &#x60;due_on&#x60; or &#x60;due_at&#x60; must be present in the request when setting or unsetting the &#x60;start_on&#x60; parameter. Additionally, &#x60;start_on&#x60; and &#x60;due_on&#x60; cannot be the same date.* |  [optional] |
|**workspace** | [**ProjectBaseAllOfWorkspace**](ProjectBaseAllOfWorkspace.md) |  |  [optional] |
|**customFields** | **Map&lt;String, String&gt;** | An object where each key is a Custom Field GID and each value is an enum GID, string, number, or object. |  [optional] |
|**followers** | **String** | *Create-only*. Comma separated string of users. Followers are a subset of members who have opted in to receive \&quot;tasks added\&quot; notifications for a project. |  [optional] |
|**owner** | **String** | The current owner of the project, may be null. |  [optional] |
|**team** | **String** | The team that this project is shared with. |  [optional] |



## Enum: ColorEnum

| Name | Value |
|---- | -----|
| DARK_PINK | &quot;dark-pink&quot; |
| DARK_GREEN | &quot;dark-green&quot; |
| DARK_BLUE | &quot;dark-blue&quot; |
| DARK_RED | &quot;dark-red&quot; |
| DARK_TEAL | &quot;dark-teal&quot; |
| DARK_BROWN | &quot;dark-brown&quot; |
| DARK_ORANGE | &quot;dark-orange&quot; |
| DARK_PURPLE | &quot;dark-purple&quot; |
| DARK_WARM_GRAY | &quot;dark-warm-gray&quot; |
| LIGHT_PINK | &quot;light-pink&quot; |
| LIGHT_GREEN | &quot;light-green&quot; |
| LIGHT_BLUE | &quot;light-blue&quot; |
| LIGHT_RED | &quot;light-red&quot; |
| LIGHT_TEAL | &quot;light-teal&quot; |
| LIGHT_BROWN | &quot;light-brown&quot; |
| LIGHT_ORANGE | &quot;light-orange&quot; |
| LIGHT_PURPLE | &quot;light-purple&quot; |
| LIGHT_WARM_GRAY | &quot;light-warm-gray&quot; |



## Enum: DefaultViewEnum

| Name | Value |
|---- | -----|
| LIST | &quot;list&quot; |
| BOARD | &quot;board&quot; |
| CALENDAR | &quot;calendar&quot; |
| TIMELINE | &quot;timeline&quot; |



