# AndroidDeviceProvisioningPartnerApi.Operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**done** | **Boolean** | If the value is &#x60;false&#x60;, it means the operation is still in progress. If &#x60;true&#x60;, the operation is completed, and either &#x60;error&#x60; or &#x60;response&#x60; is available. | [optional] 
**error** | [**Status**](Status.md) |  | [optional] 
**metadata** | **{String: Object}** | This field will contain a &#x60;DevicesLongRunningOperationMetadata&#x60; object if the operation is created by &#x60;claimAsync&#x60;, &#x60;unclaimAsync&#x60;, or &#x60;updateMetadataAsync&#x60;. | [optional] 
**name** | **String** | The server-assigned name, which is only unique within the same service that originally returns it. If you use the default HTTP mapping, the &#x60;name&#x60; should be a resource name ending with &#x60;operations/{unique_id}&#x60;. | [optional] 
**response** | **{String: Object}** | This field will contain a &#x60;DevicesLongRunningOperationResponse&#x60; object if the operation is created by &#x60;claimAsync&#x60;, &#x60;unclaimAsync&#x60;, or &#x60;updateMetadataAsync&#x60;. | [optional] 


