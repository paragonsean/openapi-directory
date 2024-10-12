# MerakiDashboardApi.UpdateNetworkCameraQualityRetentionProfileRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audioRecordingEnabled** | **Boolean** | Whether or not to record audio. Can be either true or false. Defaults to false. | [optional] 
**cloudArchiveEnabled** | **Boolean** | Create redundant video backup using Cloud Archive. Can be either true or false. Defaults to false. | [optional] 
**maxRetentionDays** | **Number** | The maximum number of days for which the data will be stored, or &#39;null&#39; to keep data until storage space runs out. If the former, it can be one of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 30, 60, 90] days. | [optional] 
**motionBasedRetentionEnabled** | **Boolean** | Deletes footage older than 3 days in which no motion was detected. Can be either true or false. Defaults to false. This setting does not apply to MV2 cameras. | [optional] 
**motionDetectorVersion** | **Number** | The version of the motion detector that will be used by the camera. Only applies to Gen 2 cameras. Defaults to v2. | [optional] 
**name** | **String** | The name of the new profile. Must be unique. | [optional] 
**restrictedBandwidthModeEnabled** | **Boolean** | Disable features that require additional bandwidth such as Motion Recap. Can be either true or false. Defaults to false. This setting does not apply to MV2 cameras. | [optional] 
**scheduleId** | **String** | Schedule for which this camera will record video, or &#39;null&#39; to always record. | [optional] 
**videoSettings** | [**CreateNetworkCameraQualityRetentionProfileRequestVideoSettings**](CreateNetworkCameraQualityRetentionProfileRequestVideoSettings.md) |  | [optional] 


