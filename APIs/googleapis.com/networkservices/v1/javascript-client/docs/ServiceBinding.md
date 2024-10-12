# NetworkServicesApi.ServiceBinding

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The timestamp when the resource was created. | [optional] [readonly] 
**description** | **String** | Optional. A free-text description of the resource. Max length 1024 characters. | [optional] 
**labels** | **{String: String}** | Optional. Set of label tags associated with the ServiceBinding resource. | [optional] 
**name** | **String** | Required. Name of the ServiceBinding resource. It matches pattern &#x60;projects/_*_/locations/global/serviceBindings/service_binding_name&#x60;. | [optional] 
**service** | **String** | Required. The full Service Directory Service name of the format projects/_*_/locations/_*_/namespaces/_*_/services/_* | [optional] 
**serviceId** | **String** | Output only. The unique identifier of the Service Directory Service against which the Service Binding resource is validated. This is populated when the Service Binding resource is used in another resource (like Backend Service). This is of the UUID4 format. | [optional] [readonly] 
**updateTime** | **String** | Output only. The timestamp when the resource was updated. | [optional] [readonly] 


