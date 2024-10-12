# CloudHealthcareApi.GoogleCloudHealthcareV1beta1DeidentifyOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**characterMaskConfig** | [**CharacterMaskConfig**](CharacterMaskConfig.md) |  | [optional] 
**contextualDeid** | **Object** | Fields that don&#39;t match a KeepField or CleanTextField &#x60;action&#x60; in the BASIC profile are collected into a contextual phrase list. For fields that match a CleanTextField &#x60;action&#x60; in FieldMetadata or ProfileType, the process attempts to transform phrases matching these contextual entries. These contextual phrases are replaced with the token \&quot;[CTX]\&quot;. This feature uses an additional InfoType during inspection. | [optional] 
**cryptoHashConfig** | [**CryptoHashConfig**](CryptoHashConfig.md) |  | [optional] 
**dateShiftConfig** | [**DateShiftConfig**](DateShiftConfig.md) |  | [optional] 
**keepExtensions** | **Object** | The behavior for handling FHIR extensions that aren&#39;t otherwise specified for de-identification. If provided, all extensions are preserved during de-identification by default. If unspecified, all extensions are removed during de-identification by default. | [optional] 


