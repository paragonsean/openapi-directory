

# ConnectionInfo

ConnectionInfo singleton resource. https://google.aip.dev/156

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**instanceUid** | **String** | Output only. The unique ID of the Instance. |  [optional] [readonly] |
|**ipAddress** | **String** | Output only. The private network IP address for the Instance. This is the default IP for the instance and is always created (even if enable_public_ip is set). This is the connection endpoint for an end-user application. |  [optional] [readonly] |
|**name** | **String** | The name of the ConnectionInfo singleton resource, e.g.: projects/{project}/locations/{location}/clusters/_*_/instances/_*_/connectionInfo This field currently has no semantic meaning. |  [optional] |



