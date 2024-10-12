

# LastAdminUserRoom

Room information

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **Long** | Room ID |  |
|**lastAdminInGroup** | **Boolean** | Determines whether user is last admin of a room due to being the last member of last admin group |  |
|**lastAdminInGroupId** | **Long** | ID of the last admin group where the user is the only remaining member  (returned only if &#x60;lastAdminInGroup&#x60; is &#x60;true&#x60;) |  [optional] |
|**name** | **String** | Room name |  |
|**parentId** | **Long** | Parent room ID |  [optional] |
|**parentPath** | **String** | Parent node path  &#x60;/&#x60; if node is a root node (room) |  |



