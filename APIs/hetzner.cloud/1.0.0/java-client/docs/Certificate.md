

# Certificate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certificate** | **String** | Certificate and chain in PEM format, in order so that each record directly certifies the one preceding |  |
|**created** | **String** | Point in time when the Resource was created (in ISO-8601 format) |  |
|**domainNames** | **List&lt;String&gt;** | Domains and subdomains covered by the Certificate |  |
|**fingerprint** | **String** | SHA256 fingerprint of the Certificate |  |
|**id** | **Integer** | ID of the Resource |  |
|**labels** | **Map&lt;String, String&gt;** | User-defined labels (key-value pairs) |  |
|**name** | **String** | Name of the Resource. Must be unique per Project. |  |
|**notValidAfter** | **String** | Point in time when the Certificate stops being valid (in ISO-8601 format) |  |
|**notValidBefore** | **String** | Point in time when the Certificate becomes valid (in ISO-8601 format) |  |
|**status** | [**CertificateStatus**](CertificateStatus.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of the Certificate |  [optional] |
|**usedBy** | [**List&lt;CertificateUsedByInner&gt;**](CertificateUsedByInner.md) | Resources currently using the Certificate |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UPLOADED | &quot;uploaded&quot; |
| MANAGED | &quot;managed&quot; |



