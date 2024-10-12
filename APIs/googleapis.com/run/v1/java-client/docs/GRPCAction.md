

# GRPCAction

GRPCAction describes an action involving a GRPC port.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**port** | **Integer** | Port number of the gRPC service. Number must be in the range 1 to 65535. |  [optional] |
|**service** | **String** | Service is the name of the service to place in the gRPC HealthCheckRequest. If this is not specified, the default behavior is defined by gRPC. |  [optional] |



