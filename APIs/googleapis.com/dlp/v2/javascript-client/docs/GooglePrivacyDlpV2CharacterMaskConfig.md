# SensitiveDataProtectionDlp.GooglePrivacyDlpV2CharacterMaskConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charactersToIgnore** | [**[GooglePrivacyDlpV2CharsToIgnore]**](GooglePrivacyDlpV2CharsToIgnore.md) | When masking a string, items in this list will be skipped when replacing characters. For example, if the input string is &#x60;555-555-5555&#x60; and you instruct Cloud DLP to skip &#x60;-&#x60; and mask 5 characters with &#x60;*&#x60;, Cloud DLP returns &#x60;***-**5-5555&#x60;. | [optional] 
**maskingCharacter** | **String** | Character to use to mask the sensitive values—for example, &#x60;*&#x60; for an alphabetic string such as a name, or &#x60;0&#x60; for a numeric string such as ZIP code or credit card number. This string must have a length of 1. If not supplied, this value defaults to &#x60;*&#x60; for strings, and &#x60;0&#x60; for digits. | [optional] 
**numberToMask** | **Number** | Number of characters to mask. If not set, all matching chars will be masked. Skipped characters do not count towards this tally. If &#x60;number_to_mask&#x60; is negative, this denotes inverse masking. Cloud DLP masks all but a number of characters. For example, suppose you have the following values: - &#x60;masking_character&#x60; is &#x60;*&#x60; - &#x60;number_to_mask&#x60; is &#x60;-4&#x60; - &#x60;reverse_order&#x60; is &#x60;false&#x60; - &#x60;CharsToIgnore&#x60; includes &#x60;-&#x60; - Input string is &#x60;1234-5678-9012-3456&#x60; The resulting de-identified string is &#x60;****-****-****-3456&#x60;. Cloud DLP masks all but the last four characters. If &#x60;reverse_order&#x60; is &#x60;true&#x60;, all but the first four characters are masked as &#x60;1234-****-****-****&#x60;. | [optional] 
**reverseOrder** | **Boolean** | Mask characters in reverse order. For example, if &#x60;masking_character&#x60; is &#x60;0&#x60;, &#x60;number_to_mask&#x60; is &#x60;14&#x60;, and &#x60;reverse_order&#x60; is &#x60;false&#x60;, then the input string &#x60;1234-5678-9012-3456&#x60; is masked as &#x60;00000000000000-3456&#x60;. If &#x60;masking_character&#x60; is &#x60;*&#x60;, &#x60;number_to_mask&#x60; is &#x60;3&#x60;, and &#x60;reverse_order&#x60; is &#x60;true&#x60;, then the string &#x60;12345&#x60; is masked as &#x60;12***&#x60;. | [optional] 


