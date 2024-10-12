

# AvroConfig

Configuration for writing message data in Avro format. Message payloads and metadata will be written to files as an Avro binary.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**writeMetadata** | **Boolean** | Optional. When true, write the subscription name, message_id, publish_time, attributes, and ordering_key as additional fields in the output. The subscription name, message_id, and publish_time fields are put in their own fields while all other message properties other than data (for example, an ordering_key, if present) are added as entries in the attributes map. |  [optional] |



