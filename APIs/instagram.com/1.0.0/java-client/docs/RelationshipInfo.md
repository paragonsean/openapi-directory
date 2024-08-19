

# RelationshipInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**incomingStatus** | [**IncomingStatusEnum**](#IncomingStatusEnum) | Status of incoming relationship |  [optional] |
|**outgoingStatus** | [**OutgoingStatusEnum**](#OutgoingStatusEnum) | Status of outgoing relationship |  [optional] |
|**targetUserIsPrivate** | **Boolean** | Indicates whether target user is private or not |  [optional] |



## Enum: IncomingStatusEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| FOLLOWED_BY | &quot;followed_by&quot; |
| REQUESTED_BY | &quot;requested_by&quot; |



## Enum: OutgoingStatusEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| FOLLOWS | &quot;follows&quot; |
| REQUESTED | &quot;requested&quot; |



