# YouTubeDataApiV3.VideoStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embeddable** | **Boolean** | This value indicates if the video can be embedded on another website. @mutable youtube.videos.insert youtube.videos.update | [optional] 
**failureReason** | **String** | This value explains why a video failed to upload. This property is only present if the uploadStatus property indicates that the upload failed. | [optional] 
**license** | **String** | The video&#39;s license. @mutable youtube.videos.insert youtube.videos.update | [optional] 
**madeForKids** | **Boolean** |  | [optional] 
**privacyStatus** | **String** | The video&#39;s privacy status. | [optional] 
**publicStatsViewable** | **Boolean** | This value indicates if the extended video statistics on the watch page can be viewed by everyone. Note that the view count, likes, etc will still be visible if this is disabled. @mutable youtube.videos.insert youtube.videos.update | [optional] 
**publishAt** | **Date** | The date and time when the video is scheduled to publish. It can be set only if the privacy status of the video is private.. | [optional] 
**rejectionReason** | **String** | This value explains why YouTube rejected an uploaded video. This property is only present if the uploadStatus property indicates that the upload was rejected. | [optional] 
**selfDeclaredMadeForKids** | **Boolean** |  | [optional] 
**uploadStatus** | **String** | The status of the uploaded video. | [optional] 



## Enum: FailureReasonEnum


* `conversion` (value: `"conversion"`)

* `invalidFile` (value: `"invalidFile"`)

* `emptyFile` (value: `"emptyFile"`)

* `tooSmall` (value: `"tooSmall"`)

* `codec` (value: `"codec"`)

* `uploadAborted` (value: `"uploadAborted"`)





## Enum: LicenseEnum


* `youtube` (value: `"youtube"`)

* `creativeCommon` (value: `"creativeCommon"`)





## Enum: PrivacyStatusEnum


* `public` (value: `"public"`)

* `unlisted` (value: `"unlisted"`)

* `private` (value: `"private"`)





## Enum: RejectionReasonEnum


* `copyright` (value: `"copyright"`)

* `inappropriate` (value: `"inappropriate"`)

* `duplicate` (value: `"duplicate"`)

* `termsOfUse` (value: `"termsOfUse"`)

* `uploaderAccountSuspended` (value: `"uploaderAccountSuspended"`)

* `length` (value: `"length"`)

* `claim` (value: `"claim"`)

* `uploaderAccountClosed` (value: `"uploaderAccountClosed"`)

* `trademark` (value: `"trademark"`)

* `legal` (value: `"legal"`)





## Enum: UploadStatusEnum


* `uploaded` (value: `"uploaded"`)

* `processed` (value: `"processed"`)

* `failed` (value: `"failed"`)

* `rejected` (value: `"rejected"`)

* `deleted` (value: `"deleted"`)




