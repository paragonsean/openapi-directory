# WebSecurityScannerApi.Xxe

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payloadLocation** | **String** | Location within the request where the payload was placed. | [optional] 
**payloadValue** | **String** | The XML string that triggered the XXE vulnerability. Non-payload values might be redacted. | [optional] 



## Enum: PayloadLocationEnum


* `LOCATION_UNSPECIFIED` (value: `"LOCATION_UNSPECIFIED"`)

* `COMPLETE_REQUEST_BODY` (value: `"COMPLETE_REQUEST_BODY"`)




