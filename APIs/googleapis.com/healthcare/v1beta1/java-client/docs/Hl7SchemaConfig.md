

# Hl7SchemaConfig

Root config message for HL7v2 schema. This contains a schema structure of groups and segments, and filters that determine which messages to apply the schema structure to.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**messageSchemaConfigs** | [**Map&lt;String, SchemaGroup&gt;**](SchemaGroup.md) | Map from each HL7v2 message type and trigger event pair, such as ADT_A04, to its schema configuration root group. |  [optional] |
|**version** | [**List&lt;VersionSource&gt;**](VersionSource.md) | Each VersionSource is tested and only if they all match is the schema used for the message. |  [optional] |



