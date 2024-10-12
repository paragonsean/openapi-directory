

# GoogleAppsDriveLabelsV2DeltaUpdateLabelRequest

The set of requests for updating aspects of a Label. If any request is not valid, no requests will be applied.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**languageCode** | **String** | The BCP-47 language code to use for evaluating localized Field labels when &#x60;include_label_in_response&#x60; is &#x60;true&#x60;. |  [optional] |
|**requests** | [**List&lt;GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestRequest&gt;**](GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestRequest.md) | A list of updates to apply to the Label. Requests will be applied in the order they are specified. |  [optional] |
|**useAdminAccess** | **Boolean** | Set to &#x60;true&#x60; in order to use the user&#39;s admin credentials. The server will verify the user is an admin for the Label before allowing access. |  [optional] |
|**view** | [**ViewEnum**](#ViewEnum) | When specified, only certain fields belonging to the indicated view will be returned. |  [optional] |
|**writeControl** | [**GoogleAppsDriveLabelsV2WriteControl**](GoogleAppsDriveLabelsV2WriteControl.md) |  |  [optional] |



## Enum: ViewEnum

| Name | Value |
|---- | -----|
| BASIC | &quot;LABEL_VIEW_BASIC&quot; |
| FULL | &quot;LABEL_VIEW_FULL&quot; |



