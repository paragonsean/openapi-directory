# DriveLabelsApi.GoogleAppsDriveLabelsV2UpdateLabelCopyModeRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**copyMode** | **String** | Required. Indicates how the applied Label, and Field values should be copied when a Drive item is copied. | [optional] 
**languageCode** | **String** | The BCP-47 language code to use for evaluating localized field labels. When not specified, values in the default configured language will be used. | [optional] 
**useAdminAccess** | **Boolean** | Set to &#x60;true&#x60; in order to use the user&#39;s admin credentials. The server will verify the user is an admin for the Label before allowing access. | [optional] 
**view** | **String** | When specified, only certain fields belonging to the indicated view will be returned. | [optional] 



## Enum: CopyModeEnum


* `COPY_MODE_UNSPECIFIED` (value: `"COPY_MODE_UNSPECIFIED"`)

* `DO_NOT_COPY` (value: `"DO_NOT_COPY"`)

* `ALWAYS_COPY` (value: `"ALWAYS_COPY"`)

* `COPY_APPLIABLE` (value: `"COPY_APPLIABLE"`)





## Enum: ViewEnum


* `BASIC` (value: `"LABEL_VIEW_BASIC"`)

* `FULL` (value: `"LABEL_VIEW_FULL"`)




