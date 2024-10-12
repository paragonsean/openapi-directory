# PrivateDnsManagementClient.RecordSetProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aRecords** | [**[ARecord]**](ARecord.md) | The list of A records in the record set. | [optional] 
**aaaaRecords** | [**[AaaaRecord]**](AaaaRecord.md) | The list of AAAA records in the record set. | [optional] 
**cnameRecord** | [**CnameRecord**](CnameRecord.md) |  | [optional] 
**fqdn** | **String** | Fully qualified domain name of the record set. | [optional] [readonly] 
**isAutoRegistered** | **Boolean** | Is the record set auto-registered in the Private DNS zone through a virtual network link? | [optional] [readonly] 
**metadata** | **{String: String}** | The metadata attached to the record set. | [optional] 
**mxRecords** | [**[MxRecord]**](MxRecord.md) | The list of MX records in the record set. | [optional] 
**ptrRecords** | [**[PtrRecord]**](PtrRecord.md) | The list of PTR records in the record set. | [optional] 
**soaRecord** | [**SoaRecord**](SoaRecord.md) |  | [optional] 
**srvRecords** | [**[SrvRecord]**](SrvRecord.md) | The list of SRV records in the record set. | [optional] 
**ttl** | **Number** | The TTL (time-to-live) of the records in the record set. | [optional] 
**txtRecords** | [**[TxtRecord]**](TxtRecord.md) | The list of TXT records in the record set. | [optional] 


