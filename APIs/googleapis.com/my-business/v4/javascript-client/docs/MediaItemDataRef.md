# GoogleMyBusinessApi.MediaItemDataRef

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resourceName** | **String** | The unique ID for this media item&#39;s binary data. Used to upload the photo data with [UpdateMedia] and when creating a new media item from those bytes with CreateMediaItem. Example of uploading bytes: &#x60;curl -X POST -T{path_to_file} \&quot;http://mybusiness.googleapis.com/upload/v1/media/{resource_name}?upload_type&#x3D;media\&quot;&#x60; For CreateMediaItem calls, set this as the &#x60;MediaItem&#x60; &#x60;data_ref&#x60;. | [optional] 


