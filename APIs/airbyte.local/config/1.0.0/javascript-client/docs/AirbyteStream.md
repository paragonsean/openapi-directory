# AirbyteConfigurationApi.AirbyteStream

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defaultCursorField** | **[String]** | Path to the field that will be used to determine if a record is new or modified since the last sync. If not provided by the source, the end user will have to specify the comparable themselves. | [optional] 
**jsonSchema** | **Object** | Stream schema using Json Schema specs. | [optional] 
**name** | **String** | Stream&#39;s name. | 
**namespace** | **String** | Optional Source-defined namespace. Airbyte streams from the same sources should have the same namespace. Currently only used by JDBC destinations to determine what schema to write to. | [optional] 
**sourceDefinedCursor** | **Boolean** | If the source defines the cursor field, then any other cursor field inputs will be ignored. If it does not, either the user_provided one is used, or the default one is used as a backup. | [optional] 
**sourceDefinedPrimaryKey** | **[[String]]** | If the source defines the primary key, paths to the fields that will be used as a primary key. If not provided by the source, the end user will have to specify the primary key themselves. | [optional] 
**supportedSyncModes** | [**[SyncMode]**](SyncMode.md) |  | [optional] 


