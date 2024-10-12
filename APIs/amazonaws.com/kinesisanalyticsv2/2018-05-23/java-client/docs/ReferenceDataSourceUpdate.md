

# ReferenceDataSourceUpdate

When you update a reference data source configuration for a SQL-based Kinesis Data Analytics application, this object provides all the updated values (such as the source bucket name and object key name), the in-application table name that is created, and updated mapping information that maps the data in the Amazon S3 object to the in-application reference table that is created.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**referenceId** | [**String**](String.md) |  |  |
|**tableNameUpdate** | [**String**](String.md) |  |  [optional] |
|**s3ReferenceDataSourceUpdate** | [**ReferenceDataSourceUpdateS3ReferenceDataSourceUpdate**](ReferenceDataSourceUpdateS3ReferenceDataSourceUpdate.md) |  |  [optional] |
|**referenceSchemaUpdate** | [**ReferenceDataSourceUpdateReferenceSchemaUpdate**](ReferenceDataSourceUpdateReferenceSchemaUpdate.md) |  |  [optional] |



