

# RecordSetProperties

Represents the properties of the records in the record set.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aaAARecords** | [**List&lt;AaaaRecord&gt;**](AaaaRecord.md) | The list of AAAA records in the record set. |  [optional] |
|**arecords** | [**List&lt;ARecord&gt;**](ARecord.md) | The list of A records in the record set. |  [optional] |
|**cnAMERecord** | [**CnameRecord**](CnameRecord.md) |  |  [optional] |
|**mxRecords** | [**List&lt;MxRecord&gt;**](MxRecord.md) | The list of MX records in the record set. |  [optional] |
|**nsRecords** | [**List&lt;NsRecord&gt;**](NsRecord.md) | The list of NS records in the record set. |  [optional] |
|**ptRRecords** | [**List&lt;PtrRecord&gt;**](PtrRecord.md) | The list of PTR records in the record set. |  [optional] |
|**soARecord** | [**SoaRecord**](SoaRecord.md) |  |  [optional] |
|**srVRecords** | [**List&lt;SrvRecord&gt;**](SrvRecord.md) | The list of SRV records in the record set. |  [optional] |
|**TTL** | **Long** | The TTL (time-to-live) of the records in the record set. |  [optional] |
|**txTRecords** | [**List&lt;TxtRecord&gt;**](TxtRecord.md) | The list of TXT records in the record set. |  [optional] |
|**caaRecords** | [**List&lt;CaaRecord&gt;**](CaaRecord.md) | The list of CAA records in the record set. |  [optional] |
|**fqdn** | **String** | Fully qualified domain name of the record set. |  [optional] [readonly] |
|**metadata** | **Map&lt;String, String&gt;** | The metadata attached to the record set. |  [optional] |
|**provisioningState** | **String** | provisioning State of the record set. |  [optional] [readonly] |
|**targetResource** | [**SubResource**](SubResource.md) |  |  [optional] |



