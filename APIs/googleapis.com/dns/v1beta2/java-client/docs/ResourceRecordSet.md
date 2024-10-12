

# ResourceRecordSet

A unit of data that is returned by the DNS servers.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kind** | **String** |  |  [optional] |
|**name** | **String** | For example, www.example.com. |  [optional] |
|**routingPolicy** | [**RRSetRoutingPolicy**](RRSetRoutingPolicy.md) |  |  [optional] |
|**rrdatas** | **List&lt;String&gt;** | As defined in RFC 1035 (section 5) and RFC 1034 (section 3.6.1) -- see examples. |  [optional] |
|**signatureRrdatas** | **List&lt;String&gt;** | As defined in RFC 4034 (section 3.2). |  [optional] |
|**ttl** | **Integer** | Number of seconds that this ResourceRecordSet can be cached by resolvers. |  [optional] |
|**type** | **String** | The identifier of a supported record type. See the list of Supported DNS record types. |  [optional] |



