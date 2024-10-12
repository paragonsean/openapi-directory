# SendPersonToMerchant.TokenCryptogram128

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**panSequenceNumber** | **String** | PAN Sequence Number distinguishes among separate cards having the same PAN. Processors  with chip-reading capability may pass this information for Contactless Chip and Contactless Magstripe transactions. When the token_cryptogram.type contains one the following types CONTACTLESS_CHIP, CONTACTLESS_MAGSTRIPE, DSRP_CHIP, then the pan_sequence_number may be present. Details: Numeric[0-9], Length: 3 | [optional] 
**type** | **String** | CONTACTLESS_CHIP: When shared cryptogram in token_cryptogram.value is result of a contactless tap and chip information is read by the terminal, CONTACTLESS_MAGSTRIPE: When shared cryptogram in token_cryptogram.value is result of a contactless tap and the magstripe information is read by the terminal, DSRP_UCAF: When shared cryptogram in token_cryptogram.value is result of an in-app purchase and chip information to be passed in the UCAF field, DSRP_CHIP: When shared cryptogram in token_cryptogram.value is result of an in-app purchase leveraging EMV data. Values - CONTACTLESS_CHIP, CONTACTLESS_MAGSTRIPE, DSRP_UCAF, DSRP_CHIP. | 
**value** | **String** | Contains formatted chip data. Details- alphanumeric, 1-255. | 


