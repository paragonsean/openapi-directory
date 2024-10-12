# CloudDnsApi.ResourceRecordSet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **String** |  | [optional] [default to &#39;dns#resourceRecordSet&#39;]
**name** | **String** | For example, www.example.com. | [optional] 
**routingPolicy** | [**RRSetRoutingPolicy**](RRSetRoutingPolicy.md) |  | [optional] 
**rrdatas** | **[String]** | As defined in RFC 1035 (section 5) and RFC 1034 (section 3.6.1) -- see examples. | [optional] 
**signatureRrdatas** | **[String]** | As defined in RFC 4034 (section 3.2). | [optional] 
**ttl** | **Number** | Number of seconds that this ResourceRecordSet can be cached by resolvers. | [optional] 
**type** | **String** | The identifier of a supported record type. See the list of Supported DNS record types. | [optional] 


