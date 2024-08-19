# AlloyDbApi.StorageDatabasecenterPartnerapiV1mainDatabaseResourceId

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **String** | Required. Cloud provider name. Ex: GCP/AWS/Azure/OnPrem/SelfManaged | [optional] 
**providerDescription** | **String** | Optional. Needs to be used only when the provider is PROVIDER_OTHER. | [optional] 
**resourceType** | **String** | Required. The type of resource this ID is identifying. Ex redis.googleapis.com/Instance, redis.googleapis.com/Cluster, alloydb.googleapis.com/Cluster, alloydb.googleapis.com/Instance, spanner.googleapis.com/Instance REQUIRED Please refer go/condor-common-datamodel | [optional] 
**uniqueId** | **String** | Required. A service-local token that distinguishes this resource from other resources within the same service. | [optional] 



## Enum: ProviderEnum


* `PROVIDER_UNSPECIFIED` (value: `"PROVIDER_UNSPECIFIED"`)

* `GCP` (value: `"GCP"`)

* `AWS` (value: `"AWS"`)

* `AZURE` (value: `"AZURE"`)

* `ONPREM` (value: `"ONPREM"`)

* `SELFMANAGED` (value: `"SELFMANAGED"`)

* `PROVIDER_OTHER` (value: `"PROVIDER_OTHER"`)




