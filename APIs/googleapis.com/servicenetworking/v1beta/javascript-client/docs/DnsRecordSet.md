# ServiceNetworkingApi.DnsRecordSet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **[String]** | Required. As defined in RFC 1035 (section 5) and RFC 1034 (section 3.6.1) for examples see https://cloud.google.com/dns/records/json-record. | [optional] 
**domain** | **String** | Required. The DNS or domain name of the record set, e.g. &#x60;test.example.com&#x60;. Cloud DNS requires that a DNS suffix ends with a trailing dot. | [optional] 
**ttl** | **String** | Required. The period of time for which this RecordSet can be cached by resolvers. | [optional] 
**type** | **String** | Required. The identifier of a supported record type. | [optional] 


