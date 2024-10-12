

# SubmissionEntryFrom

Identifies the sender.  Instead of a structured object, you can supply a string value here.  If you do this, the `type` of the sender is derived to be either INTERNATIONAL or ALPHANUMERIC.  If the value does not begin with a `+` and it contains at least one character that is not a digit, the type is detected as ALPHANUMERIC. Otherwise, the type is detected as INTERNATIONAL. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | **String** | The address of the sender id.  The validation for this field depends on the value of the &#x60;type&#x60;. INTERNATIONAL can start with &#x60;+&#x60;. It has a maximum length of 15 digits, and has to be longer than 6 digits. ALPHANUMERIC has a maximum length of 11 characters. SHORTCODE has a maximum length of 6 digits. REPLIABLE should not specify a value here.  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the sender id.  If you want BulkSMS to collect replies to this message on your behalf, specify the type as REPLIABLE.  If the recipient is in a country where BulkSMS does not have a local reply number, the reply may incur costs that are more expensive than sending a local SMS in that country. If you operate a service from a shortcode in a locale that allows messaging from such a shortcode, you can specify SHORTCODE for the type.  |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| INTERNATIONAL | &quot;INTERNATIONAL&quot; |
| ALPHANUMERIC | &quot;ALPHANUMERIC&quot; |
| SHORTCODE | &quot;SHORTCODE&quot; |
| REPLIABLE | &quot;REPLIABLE&quot; |



