# CloudSpannerApi.GetDatabaseDdlResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protoDescriptors** | **Blob** | Proto descriptors stored in the database. Contains a protobuf-serialized [google.protobuf.FileDescriptorSet](https://github.com/protocolbuffers/protobuf/blob/main/src/google/protobuf/descriptor.proto). For more details, see protobuffer [self description](https://developers.google.com/protocol-buffers/docs/techniques#self-description). | [optional] 
**statements** | **[String]** | A list of formatted DDL statements defining the schema of the database specified in the request. | [optional] 


