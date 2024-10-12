

# Image

Image object

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**created** | **OffsetDateTime** | When this Image was created. |  [optional] [readonly] |
|**createdBy** | **String** | The name of the User who created this Image, or \&quot;linode\&quot; for public Images.  |  [optional] [readonly] |
|**deprecated** | **Boolean** | Whether or not this Image is deprecated. Will only be true for deprecated public Images.  |  [optional] [readonly] |
|**description** | **String** | A detailed description of this Image. |  [optional] |
|**eol** | **OffsetDateTime** | The date of the public Image&#39;s planned end of life. &#x60;None&#x60; for private Images.  |  [optional] [readonly] |
|**expiry** | **OffsetDateTime** | Only Images created automatically from a deleted Linode (type&#x3D;automatic) will expire.  |  [optional] [readonly] |
|**id** | **String** | The unique ID of this Image. |  [optional] [readonly] |
|**isPublic** | **Boolean** | True if the Image is a public distribution image. False if Image is private Account-specific Image. |  [optional] [readonly] |
|**label** | **String** | A short description of the Image.  |  [optional] |
|**size** | **Integer** | The minimum size this Image needs to deploy. Size is in MB.  |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | The current status of this Image.  Only Images in an \&quot;available\&quot; status can be deployed. Images in a \&quot;creating\&quot; status are being created from a Linode Disk, and will become \&quot;available\&quot; shortly. Images in a \&quot;pending_upload\&quot; status are waiting for data to be [uploaded](/docs/api/images/#image-upload), and become \&quot;available\&quot; after the upload and processing are complete.  The \&quot;+order_by\&quot; and \&quot;+order\&quot; operators are not available for [filtering](/docs/api/#filtering-and-sorting) on this key.  |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | How the Image was created.  \&quot;Manual\&quot; Images can be created at any time.  \&quot;Automatic\&quot; Images are created automatically from a deleted Linode.  |  [optional] [readonly] |
|**updated** | **OffsetDateTime** | When this Image was last updated. |  [optional] [readonly] |
|**vendor** | **String** | The upstream distribution vendor. &#x60;None&#x60; for private Images.  |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;creating&quot; |
| PENDING_UPLOAD | &quot;pending_upload&quot; |
| AVAILABLE | &quot;available&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| MANUAL | &quot;manual&quot; |
| AUTOMATIC | &quot;automatic&quot; |



