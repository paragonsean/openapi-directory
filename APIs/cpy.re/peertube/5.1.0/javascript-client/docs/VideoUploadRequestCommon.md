# PeerTube.VideoUploadRequestCommon

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **Number** | category id of the video (see [/videos/categories](#operation/getCategories)) | [optional] 
**channelId** | **Number** | Channel id that will contain this video | 
**commentsEnabled** | **Boolean** | Enable or disable comments for this video | [optional] 
**description** | **String** | Video description | [optional] 
**downloadEnabled** | **Boolean** | Enable or disable downloading for this video | [optional] 
**language** | **String** | language id of the video (see [/videos/languages](#operation/getLanguages)) | [optional] 
**licence** | **Number** | licence id of the video (see [/videos/licences](#operation/getLicences)) | [optional] 
**name** | **String** | Video name | 
**nsfw** | **Boolean** | Whether or not this video contains sensitive content | [optional] 
**originallyPublishedAt** | **Date** | Date when the content was originally published | [optional] 
**previewfile** | **File** | Video preview file | [optional] 
**privacy** | [**VideoPrivacySet**](VideoPrivacySet.md) |  | [optional] 
**scheduleUpdate** | [**VideoScheduledUpdate**](VideoScheduledUpdate.md) |  | [optional] 
**support** | **String** | A text tell the audience how to support the video creator | [optional] 
**tags** | **[String]** | Video tags (maximum 5 tags each between 2 and 30 characters) | [optional] 
**thumbnailfile** | **File** | Video thumbnail file | [optional] 
**waitTranscoding** | **Boolean** | Whether or not we wait transcoding before publish the video | [optional] 


