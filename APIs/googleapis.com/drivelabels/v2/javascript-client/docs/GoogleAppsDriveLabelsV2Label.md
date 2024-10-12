# DriveLabelsApi.GoogleAppsDriveLabelsV2Label

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appliedCapabilities** | [**GoogleAppsDriveLabelsV2LabelAppliedCapabilities**](GoogleAppsDriveLabelsV2LabelAppliedCapabilities.md) |  | [optional] 
**appliedLabelPolicy** | [**GoogleAppsDriveLabelsV2LabelAppliedLabelPolicy**](GoogleAppsDriveLabelsV2LabelAppliedLabelPolicy.md) |  | [optional] 
**createTime** | **String** | Output only. The time this label was created. | [optional] [readonly] 
**creator** | [**GoogleAppsDriveLabelsV2UserInfo**](GoogleAppsDriveLabelsV2UserInfo.md) |  | [optional] 
**customer** | **String** | Output only. The customer this label belongs to. For example: \&quot;customers/123abc789.\&quot; | [optional] [readonly] 
**disableTime** | **String** | Output only. The time this label was disabled. This value has no meaning when the label is not disabled. | [optional] [readonly] 
**disabler** | [**GoogleAppsDriveLabelsV2UserInfo**](GoogleAppsDriveLabelsV2UserInfo.md) |  | [optional] 
**displayHints** | [**GoogleAppsDriveLabelsV2LabelDisplayHints**](GoogleAppsDriveLabelsV2LabelDisplayHints.md) |  | [optional] 
**fields** | [**[GoogleAppsDriveLabelsV2Field]**](GoogleAppsDriveLabelsV2Field.md) | List of fields in descending priority order. | [optional] 
**id** | **String** | Output only. Globally unique identifier of this label. ID makes up part of the label &#x60;name&#x60;, but unlike &#x60;name&#x60;, ID is consistent between revisions. Matches the regex: &#x60;([a-zA-Z0-9])+&#x60; | [optional] [readonly] 
**labelType** | **String** | Required. The type of label. | [optional] 
**learnMoreUri** | **String** | Custom URL to present to users to allow them to learn more about this label and how it should be used. | [optional] 
**lifecycle** | [**GoogleAppsDriveLabelsV2Lifecycle**](GoogleAppsDriveLabelsV2Lifecycle.md) |  | [optional] 
**lockStatus** | [**GoogleAppsDriveLabelsV2LockStatus**](GoogleAppsDriveLabelsV2LockStatus.md) |  | [optional] 
**name** | **String** | Output only. Resource name of the label. Will be in the form of either: &#x60;labels/{id}&#x60; or &#x60;labels/{id}@{revision_id}&#x60; depending on the request. See &#x60;id&#x60; and &#x60;revision_id&#x60; below. | [optional] [readonly] 
**properties** | [**GoogleAppsDriveLabelsV2LabelProperties**](GoogleAppsDriveLabelsV2LabelProperties.md) |  | [optional] 
**publishTime** | **String** | Output only. The time this label was published. This value has no meaning when the label is not published. | [optional] [readonly] 
**publisher** | [**GoogleAppsDriveLabelsV2UserInfo**](GoogleAppsDriveLabelsV2UserInfo.md) |  | [optional] 
**revisionCreateTime** | **String** | Output only. The time this label revision was created. | [optional] [readonly] 
**revisionCreator** | [**GoogleAppsDriveLabelsV2UserInfo**](GoogleAppsDriveLabelsV2UserInfo.md) |  | [optional] 
**revisionId** | **String** | Output only. Revision ID of the label. Revision ID might be part of the label &#x60;name&#x60; depending on the request issued. A new revision is created whenever revisioned properties of a label are changed. Matches the regex: &#x60;([a-zA-Z0-9])+&#x60; | [optional] [readonly] 
**schemaCapabilities** | [**GoogleAppsDriveLabelsV2LabelSchemaCapabilities**](GoogleAppsDriveLabelsV2LabelSchemaCapabilities.md) |  | [optional] 



## Enum: LabelTypeEnum


* `LABEL_TYPE_UNSPECIFIED` (value: `"LABEL_TYPE_UNSPECIFIED"`)

* `SHARED` (value: `"SHARED"`)

* `ADMIN` (value: `"ADMIN"`)

* `GOOGLE_APP` (value: `"GOOGLE_APP"`)




