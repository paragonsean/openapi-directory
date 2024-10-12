

# ModelConfiguration

Configuration represents the \"floating HEAD\" of a linear history of Revisions, and optionally how the containers those revisions reference are built. Users create new Revisions by updating the Configuration's spec. The \"latest created\" revision's name is available under status, as is the \"latest ready\" revision's name.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiVersion** | **String** | The API version for this call such as \&quot;serving.knative.dev/v1\&quot;. |  [optional] |
|**kind** | **String** | The kind of resource, in this case always \&quot;Configuration\&quot;. |  [optional] |
|**metadata** | [**ObjectMeta**](ObjectMeta.md) |  |  [optional] |
|**spec** | [**ConfigurationSpec**](ConfigurationSpec.md) |  |  [optional] |
|**status** | [**ConfigurationStatus**](ConfigurationStatus.md) |  |  [optional] |



