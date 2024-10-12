# KmsInventoryApi.GoogleCloudKmsInventoryV1ProtectedResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloudProduct** | **String** | The Cloud product that owns the resource. Example: &#x60;compute&#x60; | [optional] 
**createTime** | **String** | Output only. The time at which this resource was created. The granularity is in seconds. Timestamp.nanos will always be 0. | [optional] [readonly] 
**cryptoKeyVersion** | **String** | The name of the Cloud KMS [CryptoKeyVersion](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions?hl&#x3D;en) used to protect this resource via CMEK. This field is empty if the Google Cloud product owning the resource does not provide key version data to Asset Inventory. If there are multiple key versions protecting the resource, then this is same value as the first element of crypto_key_versions. | [optional] 
**cryptoKeyVersions** | **[String]** | The names of the Cloud KMS [CryptoKeyVersion](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions?hl&#x3D;en) used to protect this resource via CMEK. This field is empty if the Google Cloud product owning the resource does not provide key versions data to Asset Inventory. The first element of this field is stored in crypto_key_version. | [optional] 
**labels** | **{String: String}** | A key-value pair of the resource&#39;s labels (v1) to their values. | [optional] 
**location** | **String** | Location can be &#x60;global&#x60;, regional like &#x60;us-east1&#x60;, or zonal like &#x60;us-west1-b&#x60;. | [optional] 
**name** | **String** | The full resource name of the resource. Example: &#x60;//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1&#x60;. | [optional] 
**project** | **String** | Format: &#x60;projects/{PROJECT_NUMBER}&#x60;. | [optional] 
**projectId** | **String** | The ID of the project that owns the resource. | [optional] 
**resourceType** | **String** | Example: &#x60;compute.googleapis.com/Disk&#x60; | [optional] 


