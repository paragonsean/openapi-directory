

# ListConstraint

A `Constraint` that allows or disallows a list of string values, which are configured by an Organization's policy administrator with a `Policy`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**suggestedValue** | **String** | Optional. The Google Cloud Console will try to default to a configuration that matches the value specified in this &#x60;Constraint&#x60;. |  [optional] |
|**supportsUnder** | **Boolean** | Indicates whether subtrees of Cloud Resource Manager resource hierarchy can be used in &#x60;Policy.allowed_values&#x60; and &#x60;Policy.denied_values&#x60;. For example, &#x60;\&quot;under:folders/123\&quot;&#x60; would match any resource under the &#39;folders/123&#39; folder. |  [optional] |



