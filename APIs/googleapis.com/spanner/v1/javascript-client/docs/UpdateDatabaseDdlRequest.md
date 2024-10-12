# CloudSpannerApi.UpdateDatabaseDdlRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operationId** | **String** | If empty, the new update request is assigned an automatically-generated operation ID. Otherwise, &#x60;operation_id&#x60; is used to construct the name of the resulting Operation. Specifying an explicit operation ID simplifies determining whether the statements were executed in the event that the UpdateDatabaseDdl call is replayed, or the return value is otherwise lost: the database and &#x60;operation_id&#x60; fields can be combined to form the name of the resulting longrunning.Operation: &#x60;/operations/&#x60;. &#x60;operation_id&#x60; should be unique within the database, and must be a valid identifier: &#x60;a-z*&#x60;. Note that automatically-generated operation IDs always begin with an underscore. If the named operation already exists, UpdateDatabaseDdl returns &#x60;ALREADY_EXISTS&#x60;. | [optional] 
**protoDescriptors** | **Blob** | Optional. Proto descriptors used by CREATE/ALTER PROTO BUNDLE statements. Contains a protobuf-serialized [google.protobuf.FileDescriptorSet](https://github.com/protocolbuffers/protobuf/blob/main/src/google/protobuf/descriptor.proto). To generate it, [install](https://grpc.io/docs/protoc-installation/) and run &#x60;protoc&#x60; with --include_imports and --descriptor_set_out. For example, to generate for moon/shot/app.proto, run &#x60;&#x60;&#x60; $protoc --proto_path&#x3D;/app_path --proto_path&#x3D;/lib_path \\ --include_imports \\ --descriptor_set_out&#x3D;descriptors.data \\ moon/shot/app.proto &#x60;&#x60;&#x60; For more details, see protobuffer [self description](https://developers.google.com/protocol-buffers/docs/techniques#self-description). | [optional] 
**statements** | **[String]** | Required. DDL statements to be applied to the database. | [optional] 


