# ServiceConsumerManagementApi.CreateTenancyUnitRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenancyUnitId** | **String** | Optional. Optional service producer-provided identifier of the tenancy unit. Must be no longer than 40 characters and preferably URI friendly. If it isn&#39;t provided, a UID for the tenancy unit is automatically generated. The identifier must be unique across a managed service. If the tenancy unit already exists for the managed service and service consumer pair, calling &#x60;CreateTenancyUnit&#x60; returns the existing tenancy unit if the provided identifier is identical or empty, otherwise the call fails. | [optional] 


