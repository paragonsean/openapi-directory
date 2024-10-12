

# Xxe

Information reported for an XXE.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**payloadLocation** | [**PayloadLocationEnum**](#PayloadLocationEnum) | Location within the request where the payload was placed. |  [optional] |
|**payloadValue** | **String** | The XML string that triggered the XXE vulnerability. Non-payload values might be redacted. |  [optional] |



## Enum: PayloadLocationEnum

| Name | Value |
|---- | -----|
| LOCATION_UNSPECIFIED | &quot;LOCATION_UNSPECIFIED&quot; |
| COMPLETE_REQUEST_BODY | &quot;COMPLETE_REQUEST_BODY&quot; |



