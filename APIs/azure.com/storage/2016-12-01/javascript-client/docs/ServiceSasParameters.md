# StorageManagement.ServiceSasParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**canonicalizedResource** | **String** | The canonical path to the signed resource. | 
**endPk** | **String** | The end of partition key. | [optional] 
**endRk** | **String** | The end of row key. | [optional] 
**keyToSign** | **String** | The key to sign the account SAS token with. | [optional] 
**rscc** | **String** | The response header override for cache control. | [optional] 
**rscd** | **String** | The response header override for content disposition. | [optional] 
**rsce** | **String** | The response header override for content encoding. | [optional] 
**rscl** | **String** | The response header override for content language. | [optional] 
**rsct** | **String** | The response header override for content type. | [optional] 
**signedExpiry** | **Date** | The time at which the shared access signature becomes invalid. | [optional] 
**signedIdentifier** | **String** | A unique value up to 64 characters in length that correlates to an access policy specified for the container, queue, or table. | [optional] 
**signedIp** | **String** | An IP address or a range of IP addresses from which to accept requests. | [optional] 
**signedPermission** | **String** | The signed permissions for the service SAS. Possible values include: Read (r), Write (w), Delete (d), List (l), Add (a), Create (c), Update (u) and Process (p). | [optional] 
**signedProtocol** | **String** | The protocol permitted for a request made with the account SAS. | [optional] 
**signedResource** | **String** | The signed services accessible with the service SAS. Possible values include: Blob (b), Container (c), File (f), Share (s). | 
**signedStart** | **Date** | The time at which the SAS becomes valid. | [optional] 
**startPk** | **String** | The start of partition key. | [optional] 
**startRk** | **String** | The start of row key. | [optional] 



## Enum: SignedPermissionEnum


* `r` (value: `"r"`)

* `d` (value: `"d"`)

* `w` (value: `"w"`)

* `l` (value: `"l"`)

* `a` (value: `"a"`)

* `c` (value: `"c"`)

* `u` (value: `"u"`)

* `p` (value: `"p"`)





## Enum: SignedProtocolEnum


* `https,http` (value: `"https,http"`)

* `https` (value: `"https"`)





## Enum: SignedResourceEnum


* `b` (value: `"b"`)

* `c` (value: `"c"`)

* `f` (value: `"f"`)

* `s` (value: `"s"`)




