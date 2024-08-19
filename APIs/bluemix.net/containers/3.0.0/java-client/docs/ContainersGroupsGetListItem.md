

# ContainersGroupsGetListItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creationTime** | **String** | Time when the container group is created. |  [optional] |
|**id** | **String** | Unique identifier of the container group. |  [optional] |
|**name** | **String** | Name of the container group. |  [optional] |
|**port** | **Integer** | The port number that is exposed to the public during container group creation. |  [optional] |
|**routes** | **List&lt;String&gt;** | The public route that is mapped to the container group. You can use this route to access your container group from the Internet. |  [optional] |
|**status** | **String** | Current status of the container group. The container group status is a composite of ACTION and STATUS:&lt;br&gt;&lt;br&gt; ACTIONS &#x3D; (CREATE, DELETE, UPDATE, ROLLBACK, SUSPEND, RESUME, ADOPT, SNAPSHOT, CHECK, RESTORE)&lt;br&gt;&lt;br&gt; STATUSES &#x3D; (IN_PROGRESS, FAILED, COMPLETE) |  [optional] |
|**updatedTime** | **String** | Time when the container group is changed and updated. |  [optional] |



