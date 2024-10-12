# CloudVisionApi.ProductSet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **String** | The user-provided name for this ProductSet. Must not be empty. Must be at most 4096 characters long. | [optional] 
**indexError** | [**Status**](Status.md) |  | [optional] 
**indexTime** | **String** | Output only. The time at which this ProductSet was last indexed. Query results will reflect all updates before this time. If this ProductSet has never been indexed, this timestamp is the default value \&quot;1970-01-01T00:00:00Z\&quot;. This field is ignored when creating a ProductSet. | [optional] [readonly] 
**name** | **String** | The resource name of the ProductSet. Format is: &#x60;projects/PROJECT_ID/locations/LOC_ID/productSets/PRODUCT_SET_ID&#x60;. This field is ignored when creating a ProductSet. | [optional] 


