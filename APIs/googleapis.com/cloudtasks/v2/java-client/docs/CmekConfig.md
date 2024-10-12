

# CmekConfig

Describes the customer-managed encryption key (CMEK) configuration associated with a project and location.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kmsKey** | **String** | Resource name of the Cloud KMS key, of the form &#x60;projects/PROJECT_ID/locations/LOCATION_ID/keyRings/KEY_RING_ID/cryptoKeys/KEY_ID&#x60;, that will be used to encrypt the Queues &amp; Tasks in the region. Setting this as blank will turn off CMEK encryption. |  [optional] |
|**name** | **String** | Output only. The config resource name which includes the project and location and must end in &#39;cmekConfig&#39;, in the format projects/PROJECT_ID/locations/LOCATION_ID/cmekConfig&#x60; |  [optional] [readonly] |



