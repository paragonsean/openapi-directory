# DataprocMetastoreApi.DatabaseDump

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**databaseType** | **String** | The type of the database. | [optional] 
**gcsUri** | **String** | A Cloud Storage object or folder URI that specifies the source from which to import metadata. It must begin with gs://. | [optional] 
**sourceDatabase** | **String** | The name of the source database. | [optional] 
**type** | **String** | Optional. The type of the database dump. If unspecified, defaults to MYSQL. | [optional] 



## Enum: DatabaseTypeEnum


* `DATABASE_TYPE_UNSPECIFIED` (value: `"DATABASE_TYPE_UNSPECIFIED"`)

* `MYSQL` (value: `"MYSQL"`)





## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `MYSQL` (value: `"MYSQL"`)

* `AVRO` (value: `"AVRO"`)




