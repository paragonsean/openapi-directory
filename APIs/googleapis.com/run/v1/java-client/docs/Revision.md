

# Revision

Revision is an immutable snapshot of code and configuration. A revision references a container image. Revisions are created by updates to a Configuration. See also: https://github.com/knative/specs/blob/main/specs/serving/overview.md#revision

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiVersion** | **String** | The API version for this call such as \&quot;serving.knative.dev/v1\&quot;. |  [optional] |
|**kind** | **String** | The kind of this resource, in this case \&quot;Revision\&quot;. |  [optional] |
|**metadata** | [**ObjectMeta**](ObjectMeta.md) |  |  [optional] |
|**spec** | [**RevisionSpec**](RevisionSpec.md) |  |  [optional] |
|**status** | [**RevisionStatus**](RevisionStatus.md) |  |  [optional] |



