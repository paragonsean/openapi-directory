# Asana.StatusUpdateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **String** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resourceType** | **String** | The base type of this resource. | [optional] [readonly] 
**resourceSubtype** | **String** | The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning. The &#x60;resource_subtype&#x60;s for &#x60;status&#x60; objects represent the type of their parent. | [optional] [readonly] 
**title** | **String** | The title of the status update. | [optional] 
**htmlText** | **String** | [Opt In](/docs/input-output-options). The text content of the status update with formatting as HTML. | [optional] 
**statusType** | **String** | The type associated with the status update. This represents the current state of the object this object is on. | 
**text** | **String** | The text content of the status update. | 
**author** | [**UserCompact**](UserCompact.md) |  | [optional] 
**createdAt** | **Date** | The time at which this resource was created. | [optional] [readonly] 
**createdBy** | [**UserCompact**](UserCompact.md) |  | [optional] 
**hearted** | **Boolean** | *Deprecated - please use liked instead* True if the status is hearted by the authorized user, false if not. | [optional] [readonly] 
**hearts** | [**[Like]**](Like.md) | *Deprecated - please use likes instead* Array of likes for users who have hearted this status. | [optional] [readonly] 
**liked** | **Boolean** | True if the status is liked by the authorized user, false if not. | [optional] 
**likes** | [**[Like]**](Like.md) | Array of likes for users who have liked this status. | [optional] [readonly] 
**modifiedAt** | **Date** | The time at which this project status was last modified. *Note: This does not currently reflect any changes in associations such as comments that may have been added or removed from the status.* | [optional] [readonly] 
**numHearts** | **Number** | *Deprecated - please use likes instead* The number of users who have hearted this status. | [optional] [readonly] 
**numLikes** | **Number** | The number of users who have liked this status. | [optional] [readonly] 
**parent** | [**StatusUpdateResponseAllOfParent**](StatusUpdateResponseAllOfParent.md) |  | [optional] 



## Enum: ResourceSubtypeEnum


* `project_status_update` (value: `"project_status_update"`)

* `portfolio_status_update` (value: `"portfolio_status_update"`)

* `goal_status_update` (value: `"goal_status_update"`)





## Enum: StatusTypeEnum


* `on_track` (value: `"on_track"`)

* `at_risk` (value: `"at_risk"`)

* `off_track` (value: `"off_track"`)

* `on_hold` (value: `"on_hold"`)

* `complete` (value: `"complete"`)

* `achieved` (value: `"achieved"`)

* `partial` (value: `"partial"`)

* `missed` (value: `"missed"`)

* `dropped` (value: `"dropped"`)




