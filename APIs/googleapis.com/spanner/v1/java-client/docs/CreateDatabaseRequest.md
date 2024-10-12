

# CreateDatabaseRequest

The request for CreateDatabase.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createStatement** | **String** | Required. A &#x60;CREATE DATABASE&#x60; statement, which specifies the ID of the new database. The database ID must conform to the regular expression &#x60;a-z*[a-z0-9]&#x60; and be between 2 and 30 characters in length. If the database ID is a reserved word or if it contains a hyphen, the database ID must be enclosed in backticks (&#x60;&#x60; &#x60; &#x60;&#x60;). |  [optional] |
|**databaseDialect** | [**DatabaseDialectEnum**](#DatabaseDialectEnum) | Optional. The dialect of the Cloud Spanner Database. |  [optional] |
|**encryptionConfig** | [**EncryptionConfig**](EncryptionConfig.md) |  |  [optional] |
|**extraStatements** | **List&lt;String&gt;** | Optional. A list of DDL statements to run inside the newly created database. Statements can create tables, indexes, etc. These statements execute atomically with the creation of the database: if there is an error in any statement, the database is not created. |  [optional] |
|**protoDescriptors** | **byte[]** | Optional. Proto descriptors used by CREATE/ALTER PROTO BUNDLE statements in &#39;extra_statements&#39; above. Contains a protobuf-serialized [google.protobuf.FileDescriptorSet](https://github.com/protocolbuffers/protobuf/blob/main/src/google/protobuf/descriptor.proto). To generate it, [install](https://grpc.io/docs/protoc-installation/) and run &#x60;protoc&#x60; with --include_imports and --descriptor_set_out. For example, to generate for moon/shot/app.proto, run &#x60;&#x60;&#x60; $protoc --proto_path&#x3D;/app_path --proto_path&#x3D;/lib_path \\ --include_imports \\ --descriptor_set_out&#x3D;descriptors.data \\ moon/shot/app.proto &#x60;&#x60;&#x60; For more details, see protobuffer [self description](https://developers.google.com/protocol-buffers/docs/techniques#self-description). |  [optional] |



## Enum: DatabaseDialectEnum

| Name | Value |
|---- | -----|
| DATABASE_DIALECT_UNSPECIFIED | &quot;DATABASE_DIALECT_UNSPECIFIED&quot; |
| GOOGLE_STANDARD_SQL | &quot;GOOGLE_STANDARD_SQL&quot; |
| POSTGRESQL | &quot;POSTGRESQL&quot; |



