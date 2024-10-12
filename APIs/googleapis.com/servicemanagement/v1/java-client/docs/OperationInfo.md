

# OperationInfo

A message representing the message types used by a long-running operation. Example: rpc Export(ExportRequest) returns (google.longrunning.Operation) { option (google.longrunning.operation_info) = { response_type: \"ExportResponse\" metadata_type: \"ExportMetadata\" }; }

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metadataType** | **String** | Required. The message name of the metadata type for this long-running operation. If the response is in a different package from the rpc, a fully-qualified message name must be used (e.g. &#x60;google.protobuf.Struct&#x60;). Note: Altering this value constitutes a breaking change. |  [optional] |
|**responseType** | **String** | Required. The message name of the primary return type for this long-running operation. This type will be used to deserialize the LRO&#39;s response. If the response is in a different package from the rpc, a fully-qualified message name must be used (e.g. &#x60;google.protobuf.Struct&#x60;). Note: Altering this value constitutes a breaking change. |  [optional] |



