

# GoogleAppsDriveLabelsV2UpdateLabelCopyModeRequest

Request to update the `CopyMode` of the given Label. Changes to this policy are not revisioned, do not require publishing, and take effect immediately. \\

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**copyMode** | [**CopyModeEnum**](#CopyModeEnum) | Required. Indicates how the applied Label, and Field values should be copied when a Drive item is copied. |  [optional] |
|**languageCode** | **String** | The BCP-47 language code to use for evaluating localized field labels. When not specified, values in the default configured language will be used. |  [optional] |
|**useAdminAccess** | **Boolean** | Set to &#x60;true&#x60; in order to use the user&#39;s admin credentials. The server will verify the user is an admin for the Label before allowing access. |  [optional] |
|**view** | [**ViewEnum**](#ViewEnum) | When specified, only certain fields belonging to the indicated view will be returned. |  [optional] |



## Enum: CopyModeEnum

| Name | Value |
|---- | -----|
| COPY_MODE_UNSPECIFIED | &quot;COPY_MODE_UNSPECIFIED&quot; |
| DO_NOT_COPY | &quot;DO_NOT_COPY&quot; |
| ALWAYS_COPY | &quot;ALWAYS_COPY&quot; |
| COPY_APPLIABLE | &quot;COPY_APPLIABLE&quot; |



## Enum: ViewEnum

| Name | Value |
|---- | -----|
| BASIC | &quot;LABEL_VIEW_BASIC&quot; |
| FULL | &quot;LABEL_VIEW_FULL&quot; |



