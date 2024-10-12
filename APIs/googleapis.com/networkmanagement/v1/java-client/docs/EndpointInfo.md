

# EndpointInfo

For display only. The specification of the endpoints for the test. EndpointInfo is derived from source and destination Endpoint and validated by the backend data plane model.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**destinationIp** | **String** | Destination IP address. |  [optional] |
|**destinationNetworkUri** | **String** | URI of the network where this packet is sent to. |  [optional] |
|**destinationPort** | **Integer** | Destination port. Only valid when protocol is TCP or UDP. |  [optional] |
|**protocol** | **String** | IP protocol in string format, for example: \&quot;TCP\&quot;, \&quot;UDP\&quot;, \&quot;ICMP\&quot;. |  [optional] |
|**sourceAgentUri** | **String** | URI of the source telemetry agent this packet originates from. |  [optional] |
|**sourceIp** | **String** | Source IP address. |  [optional] |
|**sourceNetworkUri** | **String** | URI of the network where this packet originates from. |  [optional] |
|**sourcePort** | **Integer** | Source port. Only valid when protocol is TCP or UDP. |  [optional] |



