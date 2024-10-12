

# ServiceSasParameters

The parameters to list service SAS credentials of a specific resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**canonicalizedResource** | **String** | The canonical path to the signed resource. |  |
|**endPk** | **String** | The end of partition key. |  [optional] |
|**endRk** | **String** | The end of row key. |  [optional] |
|**keyToSign** | **String** | The key to sign the account SAS token with. |  [optional] |
|**rscc** | **String** | The response header override for cache control. |  [optional] |
|**rscd** | **String** | The response header override for content disposition. |  [optional] |
|**rsce** | **String** | The response header override for content encoding. |  [optional] |
|**rscl** | **String** | The response header override for content language. |  [optional] |
|**rsct** | **String** | The response header override for content type. |  [optional] |
|**signedExpiry** | **OffsetDateTime** | The time at which the shared access signature becomes invalid. |  [optional] |
|**signedIdentifier** | **String** | A unique value up to 64 characters in length that correlates to an access policy specified for the container, queue, or table. |  [optional] |
|**signedIp** | **String** | An IP address or a range of IP addresses from which to accept requests. |  [optional] |
|**signedPermission** | [**SignedPermissionEnum**](#SignedPermissionEnum) | The signed permissions for the service SAS. Possible values include: Read (r), Write (w), Delete (d), List (l), Add (a), Create (c), Update (u) and Process (p). |  [optional] |
|**signedProtocol** | [**SignedProtocolEnum**](#SignedProtocolEnum) | The protocol permitted for a request made with the account SAS. |  [optional] |
|**signedResource** | [**SignedResourceEnum**](#SignedResourceEnum) | The signed services accessible with the service SAS. Possible values include: Blob (b), Container (c), File (f), Share (s). |  [optional] |
|**signedStart** | **OffsetDateTime** | The time at which the SAS becomes valid. |  [optional] |
|**startPk** | **String** | The start of partition key. |  [optional] |
|**startRk** | **String** | The start of row key. |  [optional] |



## Enum: SignedPermissionEnum

| Name | Value |
|---- | -----|
| R | &quot;r&quot; |
| D | &quot;d&quot; |
| W | &quot;w&quot; |
| L | &quot;l&quot; |
| A | &quot;a&quot; |
| C | &quot;c&quot; |
| U | &quot;u&quot; |
| P | &quot;p&quot; |



## Enum: SignedProtocolEnum

| Name | Value |
|---- | -----|
| HTTPS_HTTP | &quot;https,http&quot; |
| HTTPS | &quot;https&quot; |



## Enum: SignedResourceEnum

| Name | Value |
|---- | -----|
| B | &quot;b&quot; |
| C | &quot;c&quot; |
| F | &quot;f&quot; |
| S | &quot;s&quot; |



