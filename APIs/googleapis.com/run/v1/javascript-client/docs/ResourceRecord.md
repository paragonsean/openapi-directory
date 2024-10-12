# CloudRunAdminApi.ResourceRecord

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | Relative name of the object affected by this record. Only applicable for &#x60;CNAME&#x60; records. Example: &#39;www&#39;. | [optional] 
**rrdata** | **String** | Data for this record. Values vary by record type, as defined in RFC 1035 (section 5) and RFC 1034 (section 3.6.1). | [optional] 
**type** | **String** | Resource record type. Example: &#x60;AAAA&#x60;. | [optional] 



## Enum: TypeEnum


* `RECORD_TYPE_UNSPECIFIED` (value: `"RECORD_TYPE_UNSPECIFIED"`)

* `A` (value: `"A"`)

* `AAAA` (value: `"AAAA"`)

* `CNAME` (value: `"CNAME"`)




