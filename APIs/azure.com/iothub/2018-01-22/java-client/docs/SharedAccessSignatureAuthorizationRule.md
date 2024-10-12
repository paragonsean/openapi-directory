

# SharedAccessSignatureAuthorizationRule

The properties of an IoT hub shared access policy.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**keyName** | **String** | The name of the shared access policy. |  |
|**primaryKey** | **String** | The primary key. |  [optional] |
|**rights** | [**RightsEnum**](#RightsEnum) | The permissions assigned to the shared access policy. |  |
|**secondaryKey** | **String** | The secondary key. |  [optional] |



## Enum: RightsEnum

| Name | Value |
|---- | -----|
| REGISTRY_READ | &quot;RegistryRead&quot; |
| REGISTRY_WRITE | &quot;RegistryWrite&quot; |
| SERVICE_CONNECT | &quot;ServiceConnect&quot; |
| DEVICE_CONNECT | &quot;DeviceConnect&quot; |
| REGISTRY_READ_REGISTRY_WRITE | &quot;RegistryRead, RegistryWrite&quot; |
| REGISTRY_READ_SERVICE_CONNECT | &quot;RegistryRead, ServiceConnect&quot; |
| REGISTRY_READ_DEVICE_CONNECT | &quot;RegistryRead, DeviceConnect&quot; |
| REGISTRY_WRITE_SERVICE_CONNECT | &quot;RegistryWrite, ServiceConnect&quot; |
| REGISTRY_WRITE_DEVICE_CONNECT | &quot;RegistryWrite, DeviceConnect&quot; |
| SERVICE_CONNECT_DEVICE_CONNECT | &quot;ServiceConnect, DeviceConnect&quot; |
| REGISTRY_READ_REGISTRY_WRITE_SERVICE_CONNECT | &quot;RegistryRead, RegistryWrite, ServiceConnect&quot; |
| REGISTRY_READ_REGISTRY_WRITE_DEVICE_CONNECT | &quot;RegistryRead, RegistryWrite, DeviceConnect&quot; |
| REGISTRY_READ_SERVICE_CONNECT_DEVICE_CONNECT | &quot;RegistryRead, ServiceConnect, DeviceConnect&quot; |
| REGISTRY_WRITE_SERVICE_CONNECT_DEVICE_CONNECT | &quot;RegistryWrite, ServiceConnect, DeviceConnect&quot; |
| REGISTRY_READ_REGISTRY_WRITE_SERVICE_CONNECT_DEVICE_CONNECT | &quot;RegistryRead, RegistryWrite, ServiceConnect, DeviceConnect&quot; |



