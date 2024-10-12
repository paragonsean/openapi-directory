

# LogEvent

Log event information

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attribute1** | **String** | Attribute 1 |  [optional] |
|**attribute2** | **String** | Attribute 2 |  [optional] |
|**attribute3** | **String** | Attribute 3 |  [optional] |
|**authParentSource** | **String** | Auth parent source ID |  [optional] |
|**authParentTarget** | **String** | Auth parent target ID |  [optional] |
|**customerId** | **Long** | Unique identifier for the customer |  [optional] |
|**id** | **Long** | Event ID |  |
|**message** | **String** | Event description |  |
|**objectId1** | **Long** | Object ID 1 |  [optional] |
|**objectId2** | **Long** | Object ID 2 |  [optional] |
|**objectName1** | **String** | Object name 1 |  [optional] |
|**objectName2** | **String** | Object name 2 |  [optional] |
|**objectType1** | **Integer** | Object type 1 |  [optional] |
|**objectType2** | **Integer** | Object type 2 |  [optional] |
|**operationId** | **Integer** | Operation type ID |  [optional] |
|**operationName** | **String** | Operation name |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Operation status:  * &#x60;0&#x60; - Success  * &#x60;2&#x60; - Error |  [optional] |
|**time** | **OffsetDateTime** | Event timestamp |  |
|**userClient** | **String** | Client |  [optional] |
|**userId** | **Long** | Unique identifier for the user |  |
|**userIp** | **String** | User IP |  [optional] |
|**userName** | **String** | Username |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_2 | 2 |



