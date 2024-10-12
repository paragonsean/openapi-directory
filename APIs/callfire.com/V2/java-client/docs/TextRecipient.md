

# TextRecipient

A recipient of a text message. You should provide either phone number or contact id of existing contact

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributes** | **Map&lt;String, String&gt;** | A map of string attributes associated with a recipient |  [optional] |
|**contactId** | **Long** | An id of existing contact in account |  [optional] |
|**fromNumber** | **String** | ~ |  [optional] |
|**media** | [**List&lt;Media&gt;**](Media.md) | A list of media objects&#39; ids associated with a text message |  [optional] |
|**message** | **String** | A text message |  [optional] |
|**phoneNumber** | **String** | Phone number in E.164 format (11-digit) or short code. Example: 12132000384, 67076 |  [optional] |



