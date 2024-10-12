# BitbucketApi.Issue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignee** | [**Account**](Account.md) |  | [optional] 
**component** | [**Component**](Component.md) |  | [optional] 
**content** | [**BaseCommitSummary**](BaseCommitSummary.md) |  | [optional] 
**createdOn** | **Date** |  | [optional] 
**editedOn** | **Date** |  | [optional] 
**id** | **Number** |  | [optional] 
**kind** | **String** |  | [optional] 
**links** | [**IssueLinks**](IssueLinks.md) |  | [optional] 
**milestone** | [**Milestone**](Milestone.md) |  | [optional] 
**priority** | **String** |  | [optional] 
**reporter** | [**Account**](Account.md) |  | [optional] 
**repository** | [**Repository**](Repository.md) |  | [optional] 
**state** | **String** |  | [optional] 
**title** | **String** |  | [optional] 
**updatedOn** | **Date** |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**votes** | **Number** |  | [optional] 



## Enum: KindEnum


* `bug` (value: `"bug"`)

* `enhancement` (value: `"enhancement"`)

* `proposal` (value: `"proposal"`)

* `task` (value: `"task"`)





## Enum: PriorityEnum


* `trivial` (value: `"trivial"`)

* `minor` (value: `"minor"`)

* `major` (value: `"major"`)

* `critical` (value: `"critical"`)

* `blocker` (value: `"blocker"`)





## Enum: StateEnum


* `submitted` (value: `"submitted"`)

* `new` (value: `"new"`)

* `open` (value: `"open"`)

* `resolved` (value: `"resolved"`)

* `on hold` (value: `"on hold"`)

* `invalid` (value: `"invalid"`)

* `duplicate` (value: `"duplicate"`)

* `wontfix` (value: `"wontfix"`)

* `closed` (value: `"closed"`)




