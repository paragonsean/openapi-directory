# GenomicsApi.ContainerStoppedEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionId** | **Number** | The numeric ID of the action that started this container. | [optional] 
**exitStatus** | **Number** | The exit status of the container. | [optional] 
**stderr** | **String** | The tail end of any content written to standard error by the container. If the content emits large amounts of debugging noise or contains sensitive information, you can prevent the content from being printed by setting the &#x60;DISABLE_STANDARD_ERROR_CAPTURE&#x60; flag. Note that only a small amount of the end of the stream is captured here. The entire stream is stored in the &#x60;/google/logs&#x60; directory mounted into each action, and can be copied off the machine as described elsewhere. | [optional] 


