

# V2ApiTarget

A restriction for a specific service and optionally one or multiple specific methods. Both fields are case insensitive.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**methods** | **List&lt;String&gt;** | Optional. List of one or more methods that can be called. If empty, all methods for the service are allowed. A wildcard (*) can be used as the last symbol. Valid examples: &#x60;google.cloud.translate.v2.TranslateService.GetSupportedLanguage&#x60; &#x60;TranslateText&#x60; &#x60;Get*&#x60; &#x60;translate.googleapis.com.Get*&#x60; |  [optional] |
|**service** | **String** | The service for this restriction. It should be the canonical service name, for example: &#x60;translate.googleapis.com&#x60;. You can use [&#x60;gcloud services list&#x60;](/sdk/gcloud/reference/services/list) to get a list of services that are enabled in the project. |  [optional] |



