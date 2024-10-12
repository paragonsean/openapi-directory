

# ResourceRecord

A DNS resource record.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Relative name of the object affected by this record. Only applicable for &#x60;CNAME&#x60; records. Example: &#39;www&#39;. |  [optional] |
|**rrdata** | **String** | Data for this record. Values vary by record type, as defined in RFC 1035 (section 5) and RFC 1034 (section 3.6.1). |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Resource record type. Example: &#x60;AAAA&#x60;. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| RECORD_TYPE_UNSPECIFIED | &quot;RECORD_TYPE_UNSPECIFIED&quot; |
| A | &quot;A&quot; |
| AAAA | &quot;AAAA&quot; |
| CNAME | &quot;CNAME&quot; |



