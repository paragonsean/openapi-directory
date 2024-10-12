

# Dataset

A collection of data for an identity pool. An identity pool can have multiple datasets. A dataset is per identity and can be general or associated with a particular entity in an application (like a saved game). Datasets are automatically created if they don't exist. Data is synced by dataset, and a dataset can hold up to 1MB of key-value pairs.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**identityId** | [**String**](String.md) |  |  [optional] |
|**datasetName** | [**String**](String.md) |  |  [optional] |
|**creationDate** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastModifiedDate** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastModifiedBy** | [**String**](String.md) |  |  [optional] |
|**dataStorage** | [**Integer**](Integer.md) |  |  [optional] |
|**numRecords** | [**Integer**](Integer.md) |  |  [optional] |



