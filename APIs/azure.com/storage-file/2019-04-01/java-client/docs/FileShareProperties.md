

# FileShareProperties

The properties of the file share.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**lastModifiedTime** | **OffsetDateTime** | Returns the date and time the share was last modified. |  [optional] [readonly] |
|**metadata** | **Map&lt;String, String&gt;** | A name-value pair to associate with the share as metadata. |  [optional] |
|**shareQuota** | **Integer** | The maximum size of the share, in gigabytes. Must be greater than 0, and less than or equal to 5TB (5120). |  [optional] |



