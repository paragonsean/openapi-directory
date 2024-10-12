

# GoogleCloudDataplexV1Partition

Represents partition metadata contained within entity instances.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**etag** | **String** | Optional. The etag for this partition. |  [optional] |
|**location** | **String** | Required. Immutable. The location of the entity data within the partition, for example, gs://bucket/path/to/entity/key1&#x3D;value1/key2&#x3D;value2. Or projects//datasets//tables/ |  [optional] |
|**name** | **String** | Output only. Partition values used in the HTTP URL must be double encoded. For example, url_encode(url_encode(value)) can be used to encode \&quot;US:CA/CA#Sunnyvale so that the request URL ends with \&quot;/partitions/US%253ACA/CA%2523Sunnyvale\&quot;. The name field in the response retains the encoded format. |  [optional] [readonly] |
|**values** | **List&lt;String&gt;** | Required. Immutable. The set of values representing the partition, which correspond to the partition schema defined in the parent entity. |  [optional] |



