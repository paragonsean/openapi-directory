# DracoonApi.ConfigRoomRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adminGroupIds** | **[Number]** | List of group ids  A room requires at least one admin (user or group) | [optional] 
**adminIds** | **[Number]** | List of user ids  A room requires at least one admin (user or group) | [optional] 
**classification** | **Number** | Classification ID:  * &#x60;1&#x60; - public  * &#x60;2&#x60; - internal  * &#x60;3&#x60; - confidential  * &#x60;4&#x60; - strictly confidential    Provided (or default) classification is taken from room  when file gets uploaded without any classification. | [optional] [default to ClassificationEnum.2]
**hasActivitiesLog** | **Boolean** | Is activities log active (for rooms only) | [optional] [default to true]
**inheritPermissions** | **Boolean** | Inherit permissions from parent room  (default: &#x60;false&#x60; if &#x60;parentId&#x60; is &#x60;0&#x60;; otherwise: &#x60;true&#x60;) | [optional] 
**newGroupMemberAcceptance** | **String** | Behaviour when new users are added to the group:  * &#x60;autoallow&#x60;  * &#x60;pending&#x60;    Only relevant if &#x60;adminGroupIds&#x60; has items. | [optional] [default to &#39;autoallow&#39;]
**recycleBinRetentionPeriod** | **Number** | Retention period for deleted nodes in days | [optional] 
**takeOverPermissions** | **Boolean** | Take over existing permissions | [optional] 



## Enum: ClassificationEnum


* `1` (value: `1`)

* `2` (value: `2`)

* `3` (value: `3`)

* `4` (value: `4`)





## Enum: NewGroupMemberAcceptanceEnum


* `autoallow` (value: `"autoallow"`)

* `pending` (value: `"pending"`)




