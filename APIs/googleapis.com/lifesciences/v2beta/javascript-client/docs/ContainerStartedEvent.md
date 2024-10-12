# CloudLifeSciencesApi.ContainerStartedEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionId** | **Number** | The numeric ID of the action that started this container. | [optional] 
**ipAddress** | **String** | The public IP address that can be used to connect to the container. This field is only populated when at least one port mapping is present. If the instance was created with a private address, this field will be empty even if port mappings exist. | [optional] 
**portMappings** | **{String: Number}** | The container-to-host port mappings installed for this container. This set will contain any ports exposed using the &#x60;PUBLISH_EXPOSED_PORTS&#x60; flag as well as any specified in the &#x60;Action&#x60; definition. | [optional] 


