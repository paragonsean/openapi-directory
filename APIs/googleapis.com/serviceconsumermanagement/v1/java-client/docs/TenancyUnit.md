

# TenancyUnit

Representation of a tenancy unit.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**consumer** | **String** | Output only. @OutputOnly Cloud resource name of the consumer of this service. For example &#39;projects/123456&#39;. |  [optional] [readonly] |
|**createTime** | **String** | Output only. @OutputOnly The time this tenancy unit was created. |  [optional] [readonly] |
|**name** | **String** | Globally unique identifier of this tenancy unit \&quot;services/{service}/{collection id}/{resource id}/tenancyUnits/{unit}\&quot; |  [optional] |
|**service** | **String** | Output only. Google Cloud API name of the managed service owning this tenancy unit. For example &#39;serviceconsumermanagement.googleapis.com&#39;. |  [optional] [readonly] |
|**tenantResources** | [**List&lt;TenantResource&gt;**](TenantResource.md) | Resources constituting the tenancy unit. There can be at most 512 tenant resources in a tenancy unit. |  [optional] |



