

# ClientConfig

All xds configs for a particular client.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientScope** | **String** | For xDS clients, the scope in which the data is used. For example, gRPC indicates the data plane target or that the data is associated with gRPC server(s). |  [optional] |
|**genericXdsConfigs** | [**List&lt;GenericXdsConfig&gt;**](GenericXdsConfig.md) | Represents generic xDS config and the exact config structure depends on the type URL (like Cluster if it is CDS) |  [optional] |
|**node** | [**Node**](Node.md) |  |  [optional] |
|**xdsConfig** | [**List&lt;PerXdsConfig&gt;**](PerXdsConfig.md) | This field is deprecated in favor of generic_xds_configs which is much simpler and uniform in structure. |  [optional] |



