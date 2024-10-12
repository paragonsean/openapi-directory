

# ConfigRoomRequest

Request model for configuring a room

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adminGroupIds** | **List&lt;Long&gt;** | List of group ids  A room requires at least one admin (user or group) |  [optional] |
|**adminIds** | **List&lt;Long&gt;** | List of user ids  A room requires at least one admin (user or group) |  [optional] |
|**classification** | [**ClassificationEnum**](#ClassificationEnum) | Classification ID:  * &#x60;1&#x60; - public  * &#x60;2&#x60; - internal  * &#x60;3&#x60; - confidential  * &#x60;4&#x60; - strictly confidential    Provided (or default) classification is taken from room  when file gets uploaded without any classification. |  [optional] |
|**hasActivitiesLog** | **Boolean** | Is activities log active (for rooms only) |  [optional] |
|**inheritPermissions** | **Boolean** | Inherit permissions from parent room  (default: &#x60;false&#x60; if &#x60;parentId&#x60; is &#x60;0&#x60;; otherwise: &#x60;true&#x60;) |  [optional] |
|**newGroupMemberAcceptance** | [**NewGroupMemberAcceptanceEnum**](#NewGroupMemberAcceptanceEnum) | Behaviour when new users are added to the group:  * &#x60;autoallow&#x60;  * &#x60;pending&#x60;    Only relevant if &#x60;adminGroupIds&#x60; has items. |  [optional] |
|**recycleBinRetentionPeriod** | **Integer** | Retention period for deleted nodes in days |  [optional] |
|**takeOverPermissions** | **Boolean** | Take over existing permissions |  [optional] |



## Enum: ClassificationEnum

| Name | Value |
|---- | -----|
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |
| NUMBER_4 | 4 |



## Enum: NewGroupMemberAcceptanceEnum

| Name | Value |
|---- | -----|
| AUTOALLOW | &quot;autoallow&quot; |
| PENDING | &quot;pending&quot; |



