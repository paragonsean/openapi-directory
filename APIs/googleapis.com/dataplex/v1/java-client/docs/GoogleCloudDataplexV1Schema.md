

# GoogleCloudDataplexV1Schema

Schema information describing the structure and layout of the data.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fields** | [**List&lt;GoogleCloudDataplexV1SchemaSchemaField&gt;**](GoogleCloudDataplexV1SchemaSchemaField.md) | Optional. The sequence of fields describing data in table entities. Note: BigQuery SchemaFields are immutable. |  [optional] |
|**partitionFields** | [**List&lt;GoogleCloudDataplexV1SchemaPartitionField&gt;**](GoogleCloudDataplexV1SchemaPartitionField.md) | Optional. The sequence of fields describing the partition structure in entities. If this field is empty, there are no partitions within the data. |  [optional] |
|**partitionStyle** | [**PartitionStyleEnum**](#PartitionStyleEnum) | Optional. The structure of paths containing partition data within the entity. |  [optional] |
|**userManaged** | **Boolean** | Required. Set to true if user-managed or false if managed by Dataplex. The default is false (managed by Dataplex). Set to falseto enable Dataplex discovery to update the schema. including new data discovery, schema inference, and schema evolution. Users retain the ability to input and edit the schema. Dataplex treats schema input by the user as though produced by a previous Dataplex discovery operation, and it will evolve the schema and take action based on that treatment. Set to true to fully manage the entity schema. This setting guarantees that Dataplex will not change schema fields. |  [optional] |



## Enum: PartitionStyleEnum

| Name | Value |
|---- | -----|
| PARTITION_STYLE_UNSPECIFIED | &quot;PARTITION_STYLE_UNSPECIFIED&quot; |
| HIVE_COMPATIBLE | &quot;HIVE_COMPATIBLE&quot; |



