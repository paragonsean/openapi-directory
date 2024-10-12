# BulkSmsJsonRestApi.SubmissionEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **String** | The message content as described in the &#x60;encoding&#x60;. If the &#x60;encoding&#x60; is BINARY, the body must contain only hexadecimal digits where one byte is represented as two digits. For example, if you want to send two bytes &#39;0x05&#39; and &#39;0x1F&#39;, the message body must contain the text &#39;051F&#39;.  The message content can also contain templates, read the [body templates section](#tag/Message) for more information.  | 
**deliveryReports** | **String** | The type of delivery reports to request from the delivering network. The default value  is &#x60;ALL&#x60;. Please note that not all networks support delivery reports. ALL. All possible delivery reports ERRORS. Only error delivery reports NONE. No delivery reports | [optional] 
**encoding** | **String** | Describes the content of the message body.  Typically this is TEXT, which is the default if no value is provided.  If you need to send characters that are not covered by the [GSM 03.38](https://en.wikipedia.org/wiki/GSM_03.38) character set you will need to specify UNICODE.  If you want to send a sequence of bytes, you must use BINARY.  You can also or use the &#x60;auto-unicode&#x60; parameter of the Send Messages Operation.     If you supply the value of &#x60;TEXT&#x60; while &#x60;auto-unicode&#x60; is &#x60;true&#x60; then your message may be converted to &#x60;UNICODE&#x60;.  If you supply a value other than &#x60;TEXT&#x60; for this property while &#x60;auto-unicode&#x60; is &#x60;true&#x60; then no automatic conversion will take place.  | [optional] 
**from** | [**SubmissionEntryFrom**](SubmissionEntryFrom.md) |  | [optional] 
**longMessageMaxParts** | **Number** | The maximum number of message parts that can be used for a [concatenated message](https://en.wikipedia.org/wiki/Concatenated_SMS). The default is &#x60;3&#x60;.  | [optional] 
**messageClass** | **String** | The class of the message, as specified by §4 of the GSM 03.38 specification.  You can provide either an integer value, or a mnemonic string.  The default value is SIM_SPECIFIC. Numeric values are | Name | Value| |------|------| | FLASH_SMS | 0      | | ME_SPECIFIC | 1    | | SIM_SPECIFIC | 2   | | TE_SPECIFIC | 3   |  | [optional] 
**protocolId** | **String** | The TP-PID value from GSM 03.40[.750] §9.2.3.9.  You can provide either an integer value, or a mnemonic string.  If unspecified, this property defaults to &#x60;0&#x60;, representing the IMPLICIT value. Numeric values are listed below | Name | Value| |----- |------| | IMPLICIT              | 00 | | SHORT_MESSAGE_TYPE_0  | 64 | | REPLACE_MESSAGE_1     | 65 | | REPLACE_MESSAGE_2     | 66 | | REPLACE_MESSAGE_3     | 67 | | REPLACE_MESSAGE_4     | 68 | | REPLACE_MESSAGE_5     | 69 | | REPLACE_MESSAGE_6     | 70 | | REPLACE_MESSAGE_7     | 71 | | RETURN_CALL           | 95 | | ME_DOWNLOAD           | 125 | | ME_DEPERSONALIZE      | 126 | | SIM_DOWNLOAD          | 127 |  | [optional] 
**routingGroup** | **String** | Allows you to choose routing. The default is STANDARD.  | [optional] 
**to** | [**[SubmissionEntryToInner]**](SubmissionEntryToInner.md) | Identifies the recipients  Instead of an array of structured objects, you can also provide a single object, a simple string or an array of strings. If you supply a string, the &#x60;type&#x60; is taken as INTERNATIONAL.  | 
**userSuppliedId** | **String** | Correlate the messages created from this submission to your data.  The value can contain no more than 20 characters.  | [optional] 



## Enum: DeliveryReportsEnum


* `ALL` (value: `"ALL"`)

* `ERRORS` (value: `"ERRORS"`)

* `NONE` (value: `"NONE"`)





## Enum: EncodingEnum


* `TEXT` (value: `"TEXT"`)

* `UNICODE` (value: `"UNICODE"`)

* `BINARY` (value: `"BINARY"`)





## Enum: MessageClassEnum


* `FLASH_SMS` (value: `"FLASH_SMS"`)

* `ME_SPECIFIC` (value: `"ME_SPECIFIC"`)

* `SIM_SPECIFIC` (value: `"SIM_SPECIFIC"`)

* `TE_SPECIFIC` (value: `"TE_SPECIFIC"`)





## Enum: ProtocolIdEnum


* `IMPLICIT` (value: `"IMPLICIT"`)

* `SHORT_MESSAGE_TYPE_0` (value: `"SHORT_MESSAGE_TYPE_0"`)

* `REPLACE_MESSAGE_1` (value: `"REPLACE_MESSAGE_1"`)

* `REPLACE_MESSAGE_2` (value: `"REPLACE_MESSAGE_2"`)

* `REPLACE_MESSAGE_3` (value: `"REPLACE_MESSAGE_3"`)

* `REPLACE_MESSAGE_4` (value: `"REPLACE_MESSAGE_4"`)

* `REPLACE_MESSAGE_5` (value: `"REPLACE_MESSAGE_5"`)

* `REPLACE_MESSAGE_6` (value: `"REPLACE_MESSAGE_6"`)

* `REPLACE_MESSAGE_7` (value: `"REPLACE_MESSAGE_7"`)

* `RETURN_CALL` (value: `"RETURN_CALL"`)

* `ME_DOWNLOAD` (value: `"ME_DOWNLOAD"`)

* `ME_DEPERSONALIZE` (value: `"ME_DEPERSONALIZE"`)

* `SIM_DOWNLOAD` (value: `"SIM_DOWNLOAD"`)





## Enum: RoutingGroupEnum


* `ECONOMY` (value: `"ECONOMY"`)

* `STANDARD` (value: `"STANDARD"`)

* `PREMIUM` (value: `"PREMIUM"`)




