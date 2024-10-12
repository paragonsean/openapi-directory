

# GoogleAppsDriveLabelsV2DisableLabelRequest

Request to deprecate a published Label.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**disabledPolicy** | [**GoogleAppsDriveLabelsV2LifecycleDisabledPolicy**](GoogleAppsDriveLabelsV2LifecycleDisabledPolicy.md) |  |  [optional] |
|**languageCode** | **String** | The BCP-47 language code to use for evaluating localized field labels. When not specified, values in the default configured language will be used. |  [optional] |
|**updateMask** | **String** | The fields that should be updated. At least one field must be specified. The root &#x60;disabled_policy&#x60; is implied and should not be specified. A single &#x60;*&#x60; can be used as short-hand for updating every field. |  [optional] |
|**useAdminAccess** | **Boolean** | Set to &#x60;true&#x60; in order to use the user&#39;s admin credentials. The server will verify the user is an admin for the Label before allowing access. |  [optional] |
|**writeControl** | [**GoogleAppsDriveLabelsV2WriteControl**](GoogleAppsDriveLabelsV2WriteControl.md) |  |  [optional] |



