

# ContainersGroupsNameOrIdGetDetails


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**antiAffinity** | **String** | If set to &#x60;true&#x60; the container instances in the group are spread across separate physical compute nodes, which reduces the likelihood of containers crashing due to hardware failures. If set to &#x60;false&#x60;, the container instances in the group share the same physical compute node.  |  [optional] |
|**autorecovery** | **String** | Can be either true or false. If set to true, the Autorecovery mode is enabled for your container group. In case a container instance crashes or stops, this instance is removed and a new one is automatically recreated. If set to false, the Autorecovery mode is disabled. In case a container instances crashes or stops, it is not automatically recreated by IBM Containers. |  [optional] |
|**availabilityZone** | **String** | Current IBM Containers availability zone on Openstack.  |  [optional] |
|**cmd** | **List&lt;String&gt;** | The Docker command that was specified to be run when the container instances are started.  |  [optional] |
|**creationTime** | **String** | Timestamp when the container group was created. |  [optional] |
|**env** | **List&lt;String&gt;** | The list of environmental variables that were defined for the container group. Each environment variable consists of a unique key and a value. |  [optional] |
|**id** | **String** | Unique identifier representing a specific container group. |  [optional] |
|**image** | **String** | The unique ID of the container image your container group instances are based on. |  [optional] |
|**imageName** | **String** | The full path to the container image in your private Bluemix repository. |  [optional] |
|**memory** | **Integer** | The size of each container instance that runs in the container group in MegaByte. |  [optional] |
|**name** | **String** | The name of the container group. |  [optional] |
|**numberInstances** | [**ContainersGroupsNameOrIdGetDetailsNumberInstances**](ContainersGroupsNameOrIdGetDetailsNumberInstances.md) |  |  [optional] |
|**port** | **Integer** | The public port that has been exposed. If you specified a route, your container group is accessible from the Internet.  |  [optional] |
|**routeStatus** | [**ContainersGroupsNameOrIdGetDetailsRouteStatus**](ContainersGroupsNameOrIdGetDetailsRouteStatus.md) |  |  [optional] |
|**routes** | **List&lt;String&gt;** | The public route that is mapped to the container group. When you expose a public port, you can use the route to access your container group from the Internet. |  [optional] |
|**status** | **String** | The current status of the container group. The container group status is a composite of ACTION and STATUS:&lt;br&gt;&lt;br&gt; ACTIONS &#x3D; (CREATE, DELETE, UPDATE, ROLLBACK, SUSPEND, RESUME, ADOPT, SNAPSHOT, CHECK, RESTORE)&lt;br&gt;&lt;br&gt; STATUSES &#x3D; (IN_PROGRESS, FAILED, COMPLETE) |  [optional] |
|**updatedTime** | **String** | Timestamp when the container group was updated. If the container group was not updated before, &#x60;null&#x60; is returned. |  [optional] |
|**volumes** | **List&lt;String&gt;** | List of volumes to be associated with the container, in the format of volume name:path:mode where mode can be ro or rw. |  [optional] |



