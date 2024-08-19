

# VideoStatus

Basic details about a video category, such as its localized title. Next Id: 18

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**embeddable** | **Boolean** | This value indicates if the video can be embedded on another website. @mutable youtube.videos.insert youtube.videos.update |  [optional] |
|**failureReason** | [**FailureReasonEnum**](#FailureReasonEnum) | This value explains why a video failed to upload. This property is only present if the uploadStatus property indicates that the upload failed. |  [optional] |
|**license** | [**LicenseEnum**](#LicenseEnum) | The video&#39;s license. @mutable youtube.videos.insert youtube.videos.update |  [optional] |
|**madeForKids** | **Boolean** |  |  [optional] |
|**privacyStatus** | [**PrivacyStatusEnum**](#PrivacyStatusEnum) | The video&#39;s privacy status. |  [optional] |
|**publicStatsViewable** | **Boolean** | This value indicates if the extended video statistics on the watch page can be viewed by everyone. Note that the view count, likes, etc will still be visible if this is disabled. @mutable youtube.videos.insert youtube.videos.update |  [optional] |
|**publishAt** | **OffsetDateTime** | The date and time when the video is scheduled to publish. It can be set only if the privacy status of the video is private.. |  [optional] |
|**rejectionReason** | [**RejectionReasonEnum**](#RejectionReasonEnum) | This value explains why YouTube rejected an uploaded video. This property is only present if the uploadStatus property indicates that the upload was rejected. |  [optional] |
|**selfDeclaredMadeForKids** | **Boolean** |  |  [optional] |
|**uploadStatus** | [**UploadStatusEnum**](#UploadStatusEnum) | The status of the uploaded video. |  [optional] |



## Enum: FailureReasonEnum

| Name | Value |
|---- | -----|
| CONVERSION | &quot;conversion&quot; |
| INVALID_FILE | &quot;invalidFile&quot; |
| EMPTY_FILE | &quot;emptyFile&quot; |
| TOO_SMALL | &quot;tooSmall&quot; |
| CODEC | &quot;codec&quot; |
| UPLOAD_ABORTED | &quot;uploadAborted&quot; |



## Enum: LicenseEnum

| Name | Value |
|---- | -----|
| YOUTUBE | &quot;youtube&quot; |
| CREATIVE_COMMON | &quot;creativeCommon&quot; |



## Enum: PrivacyStatusEnum

| Name | Value |
|---- | -----|
| PUBLIC | &quot;public&quot; |
| UNLISTED | &quot;unlisted&quot; |
| PRIVATE | &quot;private&quot; |



## Enum: RejectionReasonEnum

| Name | Value |
|---- | -----|
| COPYRIGHT | &quot;copyright&quot; |
| INAPPROPRIATE | &quot;inappropriate&quot; |
| DUPLICATE | &quot;duplicate&quot; |
| TERMS_OF_USE | &quot;termsOfUse&quot; |
| UPLOADER_ACCOUNT_SUSPENDED | &quot;uploaderAccountSuspended&quot; |
| LENGTH | &quot;length&quot; |
| CLAIM | &quot;claim&quot; |
| UPLOADER_ACCOUNT_CLOSED | &quot;uploaderAccountClosed&quot; |
| TRADEMARK | &quot;trademark&quot; |
| LEGAL | &quot;legal&quot; |



## Enum: UploadStatusEnum

| Name | Value |
|---- | -----|
| UPLOADED | &quot;uploaded&quot; |
| PROCESSED | &quot;processed&quot; |
| FAILED | &quot;failed&quot; |
| REJECTED | &quot;rejected&quot; |
| DELETED | &quot;deleted&quot; |



