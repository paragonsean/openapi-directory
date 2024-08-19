# SendPersonToMerchant.TokenCryptogram10

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**panSequenceNumber** | **String** |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [optional] 
**type** | **String** | CONTACTLESS_CHIP: When shared cryptogram in token_cryptogram.value is result of a contactless tap and chip information is read by the terminal, CONTACTLESS_MAGSTRIPE: When shared cryptogram in token_cryptogram.value is result of a contactless tap and the magstripe information is read by the terminal, DSRP_UCAF: When shared cryptogram in token_cryptogram.value is result of an in-app purchase and chip information to be passed in the UCAF field, DSRP_CHIP: When shared cryptogram in token_cryptogram.value is result of an in-app purchase leveraging EMV data.Values - CONTACTLESS_CHIP, CONTACTLESS_MAGSTRIPE, DSRP_UCAF, DSRP_CHIP.   Type: Alpha Special [A-Z-], Length: 1-22 | 
**value** | **String** | CONTACTLESS_CHIP - Type: Hexadecimal [A-F0-9], Length: 2-510  CONTACTLESS_MAGSTRIPE - Type: Hexadecimal [A-F0-9], Length: 2-510  DSRP_UCAF - Type: Base64 [A-Za-z0-9+/&#x3D;?:], Length: 1-510  DSRP_CHIP - Type: Hexadecimal [A-F0-9], Length: 2-510 | 


