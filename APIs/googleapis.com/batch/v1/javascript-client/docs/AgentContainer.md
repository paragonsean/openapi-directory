# BatchApi.AgentContainer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commands** | **[String]** | Overrides the &#x60;CMD&#x60; specified in the container. If there is an ENTRYPOINT (either in the container image or with the entrypoint field below) then commands are appended as arguments to the ENTRYPOINT. | [optional] 
**entrypoint** | **String** | Overrides the &#x60;ENTRYPOINT&#x60; specified in the container. | [optional] 
**imageUri** | **String** | The URI to pull the container image from. | [optional] 
**options** | **String** | Arbitrary additional options to include in the \&quot;docker run\&quot; command when running this container, e.g. \&quot;--network host\&quot;. | [optional] 
**volumes** | **[String]** | Volumes to mount (bind mount) from the host machine files or directories into the container, formatted to match docker run&#39;s --volume option, e.g. /foo:/bar, or /foo:/bar:ro | [optional] 


