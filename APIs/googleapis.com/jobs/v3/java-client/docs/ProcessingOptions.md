

# ProcessingOptions

Input only. Options for job processing.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**disableStreetAddressResolution** | **Boolean** | Optional. If set to &#x60;true&#x60;, the service does not attempt to resolve a more precise address for the job. |  [optional] |
|**htmlSanitization** | [**HtmlSanitizationEnum**](#HtmlSanitizationEnum) | Optional. Option for job HTML content sanitization. Applied fields are: * description * applicationInfo.instruction * incentives * qualifications * responsibilities HTML tags in these fields may be stripped if sanitiazation is not disabled. Defaults to HtmlSanitization.SIMPLE_FORMATTING_ONLY. |  [optional] |



## Enum: HtmlSanitizationEnum

| Name | Value |
|---- | -----|
| HTML_SANITIZATION_UNSPECIFIED | &quot;HTML_SANITIZATION_UNSPECIFIED&quot; |
| HTML_SANITIZATION_DISABLED | &quot;HTML_SANITIZATION_DISABLED&quot; |
| SIMPLE_FORMATTING_ONLY | &quot;SIMPLE_FORMATTING_ONLY&quot; |



