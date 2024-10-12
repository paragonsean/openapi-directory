

# DatabaseResourceId

DatabaseResourceId will serve as primary key for any resource ingestion event.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**provider** | [**ProviderEnum**](#ProviderEnum) | Required. Cloud provider name. Ex: GCP/AWS/Azure/OnPrem/SelfManaged |  [optional] |
|**providerDescription** | **String** | Optional. Needs to be used only when the provider is PROVIDER_OTHER. |  [optional] |
|**resourceType** | **String** | Required. The type of resource this ID is identifying. Ex redis.googleapis.com/Instance, redis.googleapis.com/Cluster, alloydb.googleapis.com/Cluster, alloydb.googleapis.com/Instance, spanner.googleapis.com/Instance REQUIRED Please refer go/condor-common-datamodel |  [optional] |
|**uniqueId** | **String** | Required. A service-local token that distinguishes this resource from other resources within the same service. |  [optional] |



## Enum: ProviderEnum

| Name | Value |
|---- | -----|
| PROVIDER_UNSPECIFIED | &quot;PROVIDER_UNSPECIFIED&quot; |
| GCP | &quot;GCP&quot; |
| AWS | &quot;AWS&quot; |
| AZURE | &quot;AZURE&quot; |
| ONPREM | &quot;ONPREM&quot; |
| SELFMANAGED | &quot;SELFMANAGED&quot; |
| PROVIDER_OTHER | &quot;PROVIDER_OTHER&quot; |



