

# AlbumPrivacy

The privacy settings of the album.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**password** | **String** | The privacy-enabled password to see this album. Present only when &#x60;privacy.view&#x60; is &#x60;password&#x60;. |  [optional] |
|**view** | [**ViewEnum**](#ViewEnum) | Who can view the album:  Option descriptions:  * &#x60;anybody&#x60; - Anyone can view the album.  * &#x60;embed_only&#x60; - Only owner can see album, can be embedded off-site  * &#x60;password&#x60; - Only those with the password can view the album.  |  |



## Enum: ViewEnum

| Name | Value |
|---- | -----|
| ANYBODY | &quot;anybody&quot; |
| EMBED_ONLY | &quot;embed_only&quot; |
| PASSWORD | &quot;password&quot; |



