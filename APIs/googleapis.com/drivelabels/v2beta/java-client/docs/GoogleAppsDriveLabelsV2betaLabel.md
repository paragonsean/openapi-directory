

# GoogleAppsDriveLabelsV2betaLabel

A label defines a taxonomy that can be applied to Drive items in order to organize and search across items. Labels can be simple strings, or can contain fields that describe additional metadata that can be further used to organize and search Drive items.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appliedCapabilities** | [**GoogleAppsDriveLabelsV2betaLabelAppliedCapabilities**](GoogleAppsDriveLabelsV2betaLabelAppliedCapabilities.md) |  |  [optional] |
|**appliedLabelPolicy** | [**GoogleAppsDriveLabelsV2betaLabelAppliedLabelPolicy**](GoogleAppsDriveLabelsV2betaLabelAppliedLabelPolicy.md) |  |  [optional] |
|**createTime** | **String** | Output only. The time this label was created. |  [optional] [readonly] |
|**creator** | [**GoogleAppsDriveLabelsV2betaUserInfo**](GoogleAppsDriveLabelsV2betaUserInfo.md) |  |  [optional] |
|**customer** | **String** | Output only. The customer this label belongs to. For example: \&quot;customers/123abc789.\&quot; |  [optional] [readonly] |
|**disableTime** | **String** | Output only. The time this label was disabled. This value has no meaning when the label is not disabled. |  [optional] [readonly] |
|**disabler** | [**GoogleAppsDriveLabelsV2betaUserInfo**](GoogleAppsDriveLabelsV2betaUserInfo.md) |  |  [optional] |
|**displayHints** | [**GoogleAppsDriveLabelsV2betaLabelDisplayHints**](GoogleAppsDriveLabelsV2betaLabelDisplayHints.md) |  |  [optional] |
|**fields** | [**List&lt;GoogleAppsDriveLabelsV2betaField&gt;**](GoogleAppsDriveLabelsV2betaField.md) | List of fields in descending priority order. |  [optional] |
|**id** | **String** | Output only. Globally unique identifier of this label. ID makes up part of the label &#x60;name&#x60;, but unlike &#x60;name&#x60;, ID is consistent between revisions. Matches the regex: &#x60;([a-zA-Z0-9])+&#x60; |  [optional] [readonly] |
|**labelType** | [**LabelTypeEnum**](#LabelTypeEnum) | Required. The type of label. |  [optional] |
|**learnMoreUri** | **String** | Custom URL to present to users to allow them to learn more about this label and how it should be used. |  [optional] |
|**lifecycle** | [**GoogleAppsDriveLabelsV2betaLifecycle**](GoogleAppsDriveLabelsV2betaLifecycle.md) |  |  [optional] |
|**lockStatus** | [**GoogleAppsDriveLabelsV2betaLockStatus**](GoogleAppsDriveLabelsV2betaLockStatus.md) |  |  [optional] |
|**name** | **String** | Output only. Resource name of the label. Will be in the form of either: &#x60;labels/{id}&#x60; or &#x60;labels/{id}@{revision_id}&#x60; depending on the request. See &#x60;id&#x60; and &#x60;revision_id&#x60; below. |  [optional] [readonly] |
|**properties** | [**GoogleAppsDriveLabelsV2betaLabelProperties**](GoogleAppsDriveLabelsV2betaLabelProperties.md) |  |  [optional] |
|**publishTime** | **String** | Output only. The time this label was published. This value has no meaning when the label is not published. |  [optional] [readonly] |
|**publisher** | [**GoogleAppsDriveLabelsV2betaUserInfo**](GoogleAppsDriveLabelsV2betaUserInfo.md) |  |  [optional] |
|**revisionCreateTime** | **String** | Output only. The time this label revision was created. |  [optional] [readonly] |
|**revisionCreator** | [**GoogleAppsDriveLabelsV2betaUserInfo**](GoogleAppsDriveLabelsV2betaUserInfo.md) |  |  [optional] |
|**revisionId** | **String** | Output only. Revision ID of the label. Revision ID might be part of the label &#x60;name&#x60; depending on the request issued. A new revision is created whenever revisioned properties of a label are changed. Matches the regex: &#x60;([a-zA-Z0-9])+&#x60; |  [optional] [readonly] |
|**schemaCapabilities** | [**GoogleAppsDriveLabelsV2betaLabelSchemaCapabilities**](GoogleAppsDriveLabelsV2betaLabelSchemaCapabilities.md) |  |  [optional] |



## Enum: LabelTypeEnum

| Name | Value |
|---- | -----|
| LABEL_TYPE_UNSPECIFIED | &quot;LABEL_TYPE_UNSPECIFIED&quot; |
| SHARED | &quot;SHARED&quot; |
| ADMIN | &quot;ADMIN&quot; |
| GOOGLE_APP | &quot;GOOGLE_APP&quot; |



