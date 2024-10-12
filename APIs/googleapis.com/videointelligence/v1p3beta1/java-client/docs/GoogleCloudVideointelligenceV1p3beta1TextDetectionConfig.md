

# GoogleCloudVideointelligenceV1p3beta1TextDetectionConfig

Config for TEXT_DETECTION.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**languageHints** | **List&lt;String&gt;** | Language hint can be specified if the language to be detected is known a priori. It can increase the accuracy of the detection. Language hint must be language code in BCP-47 format. Automatic language detection is performed if no hint is provided. |  [optional] |
|**model** | **String** | Model to use for text detection. Supported values: \&quot;builtin/stable\&quot; (the default if unset) and \&quot;builtin/latest\&quot;. |  [optional] |



