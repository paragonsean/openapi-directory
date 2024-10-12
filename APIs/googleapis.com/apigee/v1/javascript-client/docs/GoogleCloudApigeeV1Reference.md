# ApigeeApi.GoogleCloudApigeeV1Reference

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | Optional. A human-readable description of this reference. | [optional] 
**name** | **String** | Required. The resource id of this reference. Values must match the regular expression [\\w\\s\\-.]+. | [optional] 
**refers** | **String** | Required. The id of the resource to which this reference refers. Must be the id of a resource that exists in the parent environment and is of the given resource_type. | [optional] 
**resourceType** | **String** | The type of resource referred to by this reference. Valid values are &#39;KeyStore&#39; or &#39;TrustStore&#39;. | [optional] 


