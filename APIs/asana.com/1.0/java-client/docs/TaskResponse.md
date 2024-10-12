

# TaskResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**gid** | **String** | Globally unique identifier of the resource, as a string. |  [optional] [readonly] |
|**resourceType** | **String** | The base type of this resource. |  [optional] [readonly] |
|**name** | **String** | Name of the task. This is generally a short sentence fragment that fits on a line in the UI for maximum readability. However, it can be longer. |  [optional] |
|**resourceSubtype** | [**ResourceSubtypeEnum**](#ResourceSubtypeEnum) | The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning. The resource_subtype &#x60;milestone&#x60; represent a single moment in time. This means tasks with this subtype cannot have a start_date. |  [optional] |
|**actualTimeMinutes** | **BigDecimal** | This value represents the sum of all the Time Tracking entries in the Actual Time field on a given Task. It is represented as a nullable long value. |  [optional] [readonly] |
|**approvalStatus** | [**ApprovalStatusEnum**](#ApprovalStatusEnum) | *Conditional* Reflects the approval status of this task. This field is kept in sync with &#x60;completed&#x60;, meaning &#x60;pending&#x60; translates to false while &#x60;approved&#x60;, &#x60;rejected&#x60;, and &#x60;changes_requested&#x60; translate to true. If you set completed to true, this field will be set to &#x60;approved&#x60;. |  [optional] |
|**assigneeStatus** | [**AssigneeStatusEnum**](#AssigneeStatusEnum) | *Deprecated* Scheduling status of this task for the user it is assigned to. This field can only be set if the assignee is non-null. Setting this field to \&quot;inbox\&quot; or \&quot;upcoming\&quot; inserts it at the top of the section, while the other options will insert at the bottom. |  [optional] |
|**completed** | **Boolean** | True if the task is currently marked complete, false if not. |  [optional] |
|**completedAt** | **OffsetDateTime** | The time at which this task was completed, or null if the task is incomplete. |  [optional] [readonly] |
|**completedBy** | [**UserCompact**](UserCompact.md) |  |  [optional] |
|**createdAt** | **OffsetDateTime** | The time at which this resource was created. |  [optional] [readonly] |
|**dependencies** | [**List&lt;AsanaResource&gt;**](AsanaResource.md) | [Opt In](/docs/input-output-options). Array of resources referencing tasks that this task depends on. The objects contain only the gid of the dependency. |  [optional] [readonly] |
|**dependents** | [**List&lt;AsanaResource&gt;**](AsanaResource.md) | [Opt In](/docs/input-output-options). Array of resources referencing tasks that depend on this task. The objects contain only the ID of the dependent. |  [optional] [readonly] |
|**dueAt** | **LocalDate** | The UTC date and time on which this task is due, or null if the task has no due time. This takes an ISO 8601 date string in UTC and should not be used together with &#x60;due_on&#x60;. |  [optional] |
|**dueOn** | **LocalDate** | The localized date on which this task is due, or null if the task has no due date. This takes a date with &#x60;YYYY-MM-DD&#x60; format and should not be used together with &#x60;due_at&#x60;. |  [optional] |
|**external** | [**TaskBaseAllOfExternal**](TaskBaseAllOfExternal.md) |  |  [optional] |
|**hearted** | **Boolean** | *Deprecated - please use liked instead* True if the task is hearted by the authorized user, false if not. |  [optional] [readonly] |
|**hearts** | [**List&lt;Like&gt;**](Like.md) | *Deprecated - please use likes instead* Array of likes for users who have hearted this task. |  [optional] [readonly] |
|**htmlNotes** | **String** | [Opt In](/docs/input-output-options). The notes of the text with formatting as HTML. |  [optional] |
|**isRenderedAsSeparator** | **Boolean** | [Opt In](/docs/input-output-options). In some contexts tasks can be rendered as a visual separator; for instance, subtasks can appear similar to [sections](/docs/asana-sections) without being true &#x60;section&#x60; objects. If a &#x60;task&#x60; object is rendered this way in any context it will have the property &#x60;is_rendered_as_separator&#x60; set to &#x60;true&#x60;. |  [optional] [readonly] |
|**liked** | **Boolean** | True if the task is liked by the authorized user, false if not. |  [optional] |
|**likes** | [**List&lt;Like&gt;**](Like.md) | Array of likes for users who have liked this task. |  [optional] [readonly] |
|**memberships** | [**List&lt;TaskBaseAllOfMemberships&gt;**](TaskBaseAllOfMemberships.md) | *Create-only*. Array of projects this task is associated with and the section it is in. At task creation time, this array can be used to add the task to specific sections. After task creation, these associations can be modified using the &#x60;addProject&#x60; and &#x60;removeProject&#x60; endpoints. Note that over time, more types of memberships may be added to this property. |  [optional] [readonly] |
|**modifiedAt** | **OffsetDateTime** | The time at which this task was last modified.  *Note: This does not currently reflect any changes in associations such as projects or comments that may have been added or removed from the task.* |  [optional] [readonly] |
|**notes** | **String** | Free-form textual information associated with the task (i.e. its description). |  [optional] |
|**numHearts** | **Integer** | *Deprecated - please use likes instead* The number of users who have hearted this task. |  [optional] [readonly] |
|**numLikes** | **Integer** | The number of users who have liked this task. |  [optional] [readonly] |
|**numSubtasks** | **Integer** | [Opt In](/docs/input-output-options). The number of subtasks on this task.  |  [optional] [readonly] |
|**startAt** | **LocalDate** | Date and time on which work begins for the task, or null if the task has no start time. This takes an ISO 8601 date string in UTC and should not be used together with &#x60;start_on&#x60;. *Note: &#x60;due_at&#x60; must be present in the request when setting or unsetting the &#x60;start_at&#x60; parameter.* |  [optional] |
|**startOn** | **LocalDate** | The day on which work begins for the task , or null if the task has no start date. This takes a date with &#x60;YYYY-MM-DD&#x60; format and should not be used together with &#x60;start_at&#x60;. *Note: &#x60;due_on&#x60; or &#x60;due_at&#x60; must be present in the request when setting or unsetting the &#x60;start_on&#x60; parameter.* |  [optional] |
|**assignee** | [**UserCompact**](UserCompact.md) |  |  [optional] |
|**assigneeSection** | [**TaskResponseAllOfAssigneeSection**](TaskResponseAllOfAssigneeSection.md) |  |  [optional] |
|**customFields** | [**List&lt;CustomFieldResponse&gt;**](CustomFieldResponse.md) | Array of custom field values applied to the task. These represent the custom field values recorded on this project for a particular custom field. For example, these custom field values will contain an &#x60;enum_value&#x60; property for custom fields of type &#x60;enum&#x60;, a &#x60;text_value&#x60; property for custom fields of type &#x60;text&#x60;, and so on. Please note that the &#x60;gid&#x60; returned on each custom field value *is identical* to the &#x60;gid&#x60; of the custom field, which allows referencing the custom field metadata through the &#x60;/custom_fields/custom_field-gid&#x60; endpoint. |  [optional] [readonly] |
|**followers** | [**List&lt;UserCompact&gt;**](UserCompact.md) | Array of users following this task. |  [optional] [readonly] |
|**parent** | [**TaskResponseAllOfParent**](TaskResponseAllOfParent.md) |  |  [optional] |
|**permalinkUrl** | **String** | A url that points directly to the object within Asana. |  [optional] [readonly] |
|**projects** | [**List&lt;ProjectCompact&gt;**](ProjectCompact.md) | *Create-only.* Array of projects this task is associated with. At task creation time, this array can be used to add the task to many projects at once. After task creation, these associations can be modified using the addProject and removeProject endpoints. |  [optional] [readonly] |
|**tags** | [**List&lt;TagCompact&gt;**](TagCompact.md) | Array of tags associated with this task. In order to change tags on an existing task use &#x60;addTag&#x60; and &#x60;removeTag&#x60;. |  [optional] [readonly] |
|**workspace** | [**TaskResponseAllOfWorkspace**](TaskResponseAllOfWorkspace.md) |  |  [optional] |



## Enum: ResourceSubtypeEnum

| Name | Value |
|---- | -----|
| DEFAULT_TASK | &quot;default_task&quot; |
| MILESTONE | &quot;milestone&quot; |
| SECTION | &quot;section&quot; |
| APPROVAL | &quot;approval&quot; |



## Enum: ApprovalStatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| APPROVED | &quot;approved&quot; |
| REJECTED | &quot;rejected&quot; |
| CHANGES_REQUESTED | &quot;changes_requested&quot; |



## Enum: AssigneeStatusEnum

| Name | Value |
|---- | -----|
| TODAY | &quot;today&quot; |
| UPCOMING | &quot;upcoming&quot; |
| LATER | &quot;later&quot; |
| NEW | &quot;new&quot; |
| INBOX | &quot;inbox&quot; |



