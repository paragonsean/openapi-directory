

# RecordSetProperties

Represents the properties of the records in the record set.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aRecords** | [**List&lt;ARecord&gt;**](ARecord.md) | The list of A records in the record set. |  [optional] |
|**aaaaRecords** | [**List&lt;AaaaRecord&gt;**](AaaaRecord.md) | The list of AAAA records in the record set. |  [optional] |
|**cnameRecord** | [**CnameRecord**](CnameRecord.md) |  |  [optional] |
|**fqdn** | **String** | Fully qualified domain name of the record set. |  [optional] [readonly] |
|**isAutoRegistered** | **Boolean** | Is the record set auto-registered in the Private DNS zone through a virtual network link? |  [optional] [readonly] |
|**metadata** | **Map&lt;String, String&gt;** | The metadata attached to the record set. |  [optional] |
|**mxRecords** | [**List&lt;MxRecord&gt;**](MxRecord.md) | The list of MX records in the record set. |  [optional] |
|**ptrRecords** | [**List&lt;PtrRecord&gt;**](PtrRecord.md) | The list of PTR records in the record set. |  [optional] |
|**soaRecord** | [**SoaRecord**](SoaRecord.md) |  |  [optional] |
|**srvRecords** | [**List&lt;SrvRecord&gt;**](SrvRecord.md) | The list of SRV records in the record set. |  [optional] |
|**ttl** | **Long** | The TTL (time-to-live) of the records in the record set. |  [optional] |
|**txtRecords** | [**List&lt;TxtRecord&gt;**](TxtRecord.md) | The list of TXT records in the record set. |  [optional] |



