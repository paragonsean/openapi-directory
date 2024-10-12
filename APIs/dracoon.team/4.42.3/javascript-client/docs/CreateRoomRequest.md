# DracoonApi.CreateRoomRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adminGroupIds** | **[Number]** | List of group ids  A room requires at least one admin (user or group) | [optional] 
**adminIds** | **[Number]** | List of user ids  A room requires at least one admin (user or group) | [optional] 
**classification** | **Number** | Classification ID:  * &#x60;1&#x60; - public  * &#x60;2&#x60; - internal  * &#x60;3&#x60; - confidential  * &#x60;4&#x60; - strictly confidential    Provided (or default) classification is taken from room  when file gets uploaded without any classification. | [optional] [default to ClassificationEnum.2]
**hasActivitiesLog** | **Boolean** | Is activities log active (for rooms only) | [optional] [default to true]
**hasRecycleBin** | **Boolean** | &amp;#128679; Deprecated since v4.10.0  Is recycle bin active (for rooms only)  Recycle bin is always on (disabling is not possible). | [optional] 
**inheritPermissions** | **Boolean** | Inherit permissions from parent room  (default: &#x60;false&#x60; if &#x60;parentId&#x60; is &#x60;0&#x60;; otherwise: &#x60;true&#x60;) | [optional] 
**name** | **String** | Name | 
**newGroupMemberAcceptance** | **String** | Behaviour when new users are added to the group:  * &#x60;autoallow&#x60;  * &#x60;pending&#x60;    Only relevant if &#x60;adminGroupIds&#x60; has items. | [optional] [default to &#39;autoallow&#39;]
**notes** | **String** | User notes  Use empty string to remove. | [optional] 
**parentId** | **Number** | Parent room ID or &#x60;null&#x60; (not 0) to create a top level room | [optional] 
**quota** | **Number** | Quota in byte | [optional] 
**recycleBinRetentionPeriod** | **Number** | Retention period for deleted nodes in days | [optional] 
**timestampCreation** | **Date** | &amp;#128640; Since v4.22.0  Time the node was created on external file system  (default: current server datetime in UTC format) | [optional] 
**timestampModification** | **Date** | &amp;#128640; Since v4.22.0  Time the content of a node was last modified on external file system  (default: current server datetime in UTC format) | [optional] 



## Enum: ClassificationEnum


* `1` (value: `1`)

* `2` (value: `2`)

* `3` (value: `3`)

* `4` (value: `4`)





## Enum: NewGroupMemberAcceptanceEnum


* `autoallow` (value: `"autoallow"`)

* `pending` (value: `"pending"`)




