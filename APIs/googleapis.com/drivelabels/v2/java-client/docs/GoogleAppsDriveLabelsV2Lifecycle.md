

# GoogleAppsDriveLabelsV2Lifecycle

The lifecycle state of an object, such as label, field, or choice. The lifecycle enforces the following transitions: * `UNPUBLISHED_DRAFT` (starting state) * `UNPUBLISHED_DRAFT` -> `PUBLISHED` * `UNPUBLISHED_DRAFT` -> (Deleted) * `PUBLISHED` -> `DISABLED` * `DISABLED` -> `PUBLISHED` * `DISABLED` -> (Deleted) The published and disabled states have some distinct characteristics: * Published—Some kinds of changes might be made to an object in this state, in which case `has_unpublished_changes` will be true. Also, some kinds of changes are not permitted. Generally, any change that would invalidate or cause new restrictions on existing metadata related to the label are rejected. * Disabled—When disabled, the configured `DisabledPolicy` takes effect.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**disabledPolicy** | [**GoogleAppsDriveLabelsV2LifecycleDisabledPolicy**](GoogleAppsDriveLabelsV2LifecycleDisabledPolicy.md) |  |  [optional] |
|**hasUnpublishedChanges** | **Boolean** | Output only. Whether the object associated with this lifecycle has unpublished changes. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The state of the object associated with this lifecycle. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| UNPUBLISHED_DRAFT | &quot;UNPUBLISHED_DRAFT&quot; |
| PUBLISHED | &quot;PUBLISHED&quot; |
| DISABLED | &quot;DISABLED&quot; |
| DELETED | &quot;DELETED&quot; |



