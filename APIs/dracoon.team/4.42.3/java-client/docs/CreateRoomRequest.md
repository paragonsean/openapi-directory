

# CreateRoomRequest

Request model for creating a room

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adminGroupIds** | **List&lt;Long&gt;** | List of group ids  A room requires at least one admin (user or group) |  [optional] |
|**adminIds** | **List&lt;Long&gt;** | List of user ids  A room requires at least one admin (user or group) |  [optional] |
|**classification** | [**ClassificationEnum**](#ClassificationEnum) | Classification ID:  * &#x60;1&#x60; - public  * &#x60;2&#x60; - internal  * &#x60;3&#x60; - confidential  * &#x60;4&#x60; - strictly confidential    Provided (or default) classification is taken from room  when file gets uploaded without any classification. |  [optional] |
|**hasActivitiesLog** | **Boolean** | Is activities log active (for rooms only) |  [optional] |
|**hasRecycleBin** | **Boolean** | &amp;#128679; Deprecated since v4.10.0  Is recycle bin active (for rooms only)  Recycle bin is always on (disabling is not possible). |  [optional] |
|**inheritPermissions** | **Boolean** | Inherit permissions from parent room  (default: &#x60;false&#x60; if &#x60;parentId&#x60; is &#x60;0&#x60;; otherwise: &#x60;true&#x60;) |  [optional] |
|**name** | **String** | Name |  |
|**newGroupMemberAcceptance** | [**NewGroupMemberAcceptanceEnum**](#NewGroupMemberAcceptanceEnum) | Behaviour when new users are added to the group:  * &#x60;autoallow&#x60;  * &#x60;pending&#x60;    Only relevant if &#x60;adminGroupIds&#x60; has items. |  [optional] |
|**notes** | **String** | User notes  Use empty string to remove. |  [optional] |
|**parentId** | **Long** | Parent room ID or &#x60;null&#x60; (not 0) to create a top level room |  [optional] |
|**quota** | **Long** | Quota in byte |  [optional] |
|**recycleBinRetentionPeriod** | **Integer** | Retention period for deleted nodes in days |  [optional] |
|**timestampCreation** | **OffsetDateTime** | &amp;#128640; Since v4.22.0  Time the node was created on external file system  (default: current server datetime in UTC format) |  [optional] |
|**timestampModification** | **OffsetDateTime** | &amp;#128640; Since v4.22.0  Time the content of a node was last modified on external file system  (default: current server datetime in UTC format) |  [optional] |



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



