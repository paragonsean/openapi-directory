# DriveLabelsApi.GoogleAppsDriveLabelsV2DeltaUpdateLabelRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**languageCode** | **String** | The BCP-47 language code to use for evaluating localized Field labels when &#x60;include_label_in_response&#x60; is &#x60;true&#x60;. | [optional] 
**requests** | [**[GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestRequest]**](GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestRequest.md) | A list of updates to apply to the Label. Requests will be applied in the order they are specified. | [optional] 
**useAdminAccess** | **Boolean** | Set to &#x60;true&#x60; in order to use the user&#39;s admin credentials. The server will verify the user is an admin for the Label before allowing access. | [optional] 
**view** | **String** | When specified, only certain fields belonging to the indicated view will be returned. | [optional] 
**writeControl** | [**GoogleAppsDriveLabelsV2WriteControl**](GoogleAppsDriveLabelsV2WriteControl.md) |  | [optional] 



## Enum: ViewEnum


* `BASIC` (value: `"LABEL_VIEW_BASIC"`)

* `FULL` (value: `"LABEL_VIEW_FULL"`)




