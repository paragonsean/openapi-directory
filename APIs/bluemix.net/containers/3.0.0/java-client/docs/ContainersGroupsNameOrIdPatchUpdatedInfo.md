

# ContainersGroupsNameOrIdPatchUpdatedInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autorecovery** | **String** | Enable or disable the Autorecovery mode for your container group. To enable it, enter true. If you want to disable it, enter false. Note: You can only enable/ disable Autorecovery mode if your container group was initially created with Autorecovery mode enabled. |  [optional] |
|**environment** | **List&lt;String&gt;** | A list of environment variables that you want to add to your container group. Every environment variable needs to be a key&#x3D;value pair. Every key that you use needs to be unique for this container group. Multiple environment variables are separated with comma (,) |  [optional] |
|**numberInstances** | [**ContainersGroupsNameOrIdPatchUpdatedInfoNumberInstances**](ContainersGroupsNameOrIdPatchUpdatedInfoNumberInstances.md) |  |  [optional] |



