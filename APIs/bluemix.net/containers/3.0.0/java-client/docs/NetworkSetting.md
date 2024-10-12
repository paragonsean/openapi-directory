

# NetworkSetting


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bridge** | **String** | The name of the private network bridge. |  [optional] |
|**gateway** | **String** | The IP address of the private network gateway in IPv4 format. |  [optional] |
|**ipAddress** | **String** | The private IP address that is assigned to the container. |  |
|**ipPrefixLen** | **Integer** |  |  [optional] |
|**macAddress** | **String** | The MAC address that was assigned to the container.  |  [optional] |
|**network** | [**Network**](Network.md) |  |  [optional] |
|**portMapping** | **String** | Specific to Docker. List of private container ports and their mapping to the host ports. In IBM Containers all container ports are exposed on the host by default. This attribute is returned as an empty list.  |  [optional] |
|**ports** | **List&lt;String&gt;** | All ports of the container that were exposed to the public. |  [optional] |
|**publicIpAddress** | **String** | The Public IP address that was bound to the container. |  |



