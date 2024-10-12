# MyBusinessVerificationsApi.VoiceOfMerchantState

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**complyWithGuidelines** | [**ComplyWithGuidelines**](ComplyWithGuidelines.md) |  | [optional] 
**hasBusinessAuthority** | **Boolean** | Indicates whether the location has the authority (ownership) over the business on Google. If true, another location cannot take over and become the dominant listing on Maps. However, edits will not become live unless Voice of Merchant is gained (i.e. has_voice_of_merchant is true). | [optional] 
**hasVoiceOfMerchant** | **Boolean** | Indicates whether the location is in good standing and has control over the business on Google. Any edits made to the location will propagate to Maps after passing the review phase. | [optional] 
**resolveOwnershipConflict** | **Object** | Indicates that the location duplicates another location that is in good standing. | [optional] 
**verify** | [**Verify**](Verify.md) |  | [optional] 
**waitForVoiceOfMerchant** | **Object** | Indicates that the location will gain voice of merchant after passing review. | [optional] 


