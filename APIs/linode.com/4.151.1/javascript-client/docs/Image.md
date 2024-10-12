# LinodeApi.Image

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **Date** | When this Image was created. | [optional] [readonly] 
**createdBy** | **String** | The name of the User who created this Image, or \&quot;linode\&quot; for public Images.  | [optional] [readonly] 
**deprecated** | **Boolean** | Whether or not this Image is deprecated. Will only be true for deprecated public Images.  | [optional] [readonly] 
**description** | **String** | A detailed description of this Image. | [optional] 
**eol** | **Date** | The date of the public Image&#39;s planned end of life. &#x60;None&#x60; for private Images.  | [optional] [readonly] 
**expiry** | **Date** | Only Images created automatically from a deleted Linode (type&#x3D;automatic) will expire.  | [optional] [readonly] 
**id** | **String** | The unique ID of this Image. | [optional] [readonly] 
**isPublic** | **Boolean** | True if the Image is a public distribution image. False if Image is private Account-specific Image. | [optional] [readonly] 
**label** | **String** | A short description of the Image.  | [optional] 
**size** | **Number** | The minimum size this Image needs to deploy. Size is in MB.  | [optional] [readonly] 
**status** | **String** | The current status of this Image.  Only Images in an \&quot;available\&quot; status can be deployed. Images in a \&quot;creating\&quot; status are being created from a Linode Disk, and will become \&quot;available\&quot; shortly. Images in a \&quot;pending_upload\&quot; status are waiting for data to be [uploaded](/docs/api/images/#image-upload), and become \&quot;available\&quot; after the upload and processing are complete.  The \&quot;+order_by\&quot; and \&quot;+order\&quot; operators are not available for [filtering](/docs/api/#filtering-and-sorting) on this key.  | [optional] [readonly] 
**type** | **String** | How the Image was created.  \&quot;Manual\&quot; Images can be created at any time.  \&quot;Automatic\&quot; Images are created automatically from a deleted Linode.  | [optional] [readonly] 
**updated** | **Date** | When this Image was last updated. | [optional] [readonly] 
**vendor** | **String** | The upstream distribution vendor. &#x60;None&#x60; for private Images.  | [optional] [readonly] 



## Enum: StatusEnum


* `creating` (value: `"creating"`)

* `pending_upload` (value: `"pending_upload"`)

* `available` (value: `"available"`)





## Enum: TypeEnum


* `manual` (value: `"manual"`)

* `automatic` (value: `"automatic"`)




