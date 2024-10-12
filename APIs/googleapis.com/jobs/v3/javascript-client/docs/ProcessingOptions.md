# CloudTalentSolutionApi.ProcessingOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disableStreetAddressResolution** | **Boolean** | Optional. If set to &#x60;true&#x60;, the service does not attempt to resolve a more precise address for the job. | [optional] 
**htmlSanitization** | **String** | Optional. Option for job HTML content sanitization. Applied fields are: * description * applicationInfo.instruction * incentives * qualifications * responsibilities HTML tags in these fields may be stripped if sanitiazation is not disabled. Defaults to HtmlSanitization.SIMPLE_FORMATTING_ONLY. | [optional] 



## Enum: HtmlSanitizationEnum


* `HTML_SANITIZATION_UNSPECIFIED` (value: `"HTML_SANITIZATION_UNSPECIFIED"`)

* `HTML_SANITIZATION_DISABLED` (value: `"HTML_SANITIZATION_DISABLED"`)

* `SIMPLE_FORMATTING_ONLY` (value: `"SIMPLE_FORMATTING_ONLY"`)




