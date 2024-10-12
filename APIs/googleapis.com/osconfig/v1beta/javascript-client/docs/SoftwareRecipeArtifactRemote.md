# OsConfigApi.SoftwareRecipeArtifactRemote

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checksum** | **String** | Must be provided if &#x60;allow_insecure&#x60; is &#x60;false&#x60;. SHA256 checksum in hex format, to compare to the checksum of the artifact. If the checksum is not empty and it doesn&#39;t match the artifact then the recipe installation fails before running any of the steps. | [optional] 
**uri** | **String** | URI from which to fetch the object. It should contain both the protocol and path following the format {protocol}://{location}. | [optional] 


