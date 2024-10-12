# DnsManagementClient.RecordSetProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aAAARecords** | [**[AaaaRecord]**](AaaaRecord.md) | The list of AAAA records in the record set. | [optional] 
**aRecords** | [**[ARecord]**](ARecord.md) | The list of A records in the record set. | [optional] 
**cNAMERecord** | [**CnameRecord**](CnameRecord.md) |  | [optional] 
**mXRecords** | [**[MxRecord]**](MxRecord.md) | The list of MX records in the record set. | [optional] 
**nSRecords** | [**[NsRecord]**](NsRecord.md) | The list of NS records in the record set. | [optional] 
**pTRRecords** | [**[PtrRecord]**](PtrRecord.md) | The list of PTR records in the record set. | [optional] 
**sOARecord** | [**SoaRecord**](SoaRecord.md) |  | [optional] 
**sRVRecords** | [**[SrvRecord]**](SrvRecord.md) | The list of SRV records in the record set. | [optional] 
**TTL** | **Number** | The TTL (time-to-live) of the records in the record set. | [optional] 
**tXTRecords** | [**[TxtRecord]**](TxtRecord.md) | The list of TXT records in the record set. | [optional] 
**caaRecords** | [**[CaaRecord]**](CaaRecord.md) | The list of CAA records in the record set. | [optional] 
**fqdn** | **String** | Fully qualified domain name of the record set. | [optional] [readonly] 
**metadata** | **{String: String}** | The metadata attached to the record set. | [optional] 


