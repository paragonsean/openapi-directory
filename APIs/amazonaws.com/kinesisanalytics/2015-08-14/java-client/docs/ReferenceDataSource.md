

# ReferenceDataSource

Describes the reference data source by providing the source information (S3 bucket name and object key name), the resulting in-application table name that is created, and the necessary schema to map the data elements in the Amazon S3 object to the in-application table.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**tableName** | [**String**](String.md) |  |  |
|**s3ReferenceDataSource** | [**ReferenceDataSourceS3ReferenceDataSource**](ReferenceDataSourceS3ReferenceDataSource.md) |  |  [optional] |
|**referenceSchema** | [**ReferenceDataSourceReferenceSchema**](ReferenceDataSourceReferenceSchema.md) |  |  |



