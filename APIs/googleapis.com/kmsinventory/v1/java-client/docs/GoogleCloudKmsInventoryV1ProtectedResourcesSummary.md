

# GoogleCloudKmsInventoryV1ProtectedResourcesSummary

Aggregate information about the resources protected by a Cloud KMS key in the same Cloud organization as the key.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cloudProducts** | **Map&lt;String, String&gt;** | The number of resources protected by the key grouped by Cloud product. |  [optional] |
|**locations** | **Map&lt;String, String&gt;** | The number of resources protected by the key grouped by region. |  [optional] |
|**name** | **String** | The full name of the ProtectedResourcesSummary resource. Example: projects/test-project/locations/us/keyRings/test-keyring/cryptoKeys/test-key/protectedResourcesSummary |  [optional] |
|**projectCount** | **Integer** | The number of distinct Cloud projects in the same Cloud organization as the key that have resources protected by the key. |  [optional] |
|**resourceCount** | **String** | The total number of protected resources in the same Cloud organization as the key. |  [optional] |
|**resourceTypes** | **Map&lt;String, String&gt;** | The number of resources protected by the key grouped by resource type. |  [optional] |



