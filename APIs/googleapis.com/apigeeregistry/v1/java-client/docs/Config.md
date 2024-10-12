

# Config

Available configurations to provision an Instance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cmekKeyName** | **String** | Required. The Customer Managed Encryption Key (CMEK) used for data encryption. The CMEK name should follow the format of &#x60;projects/([^/]+)/locations/([^/]+)/keyRings/([^/]+)/cryptoKeys/([^/]+)&#x60;, where the &#x60;location&#x60; must match InstanceConfig.location. |  [optional] |
|**location** | **String** | Output only. The GCP location where the Instance resides. |  [optional] [readonly] |



