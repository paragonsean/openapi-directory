

# CheckEntityCheckResultObjectEntityResult

This will hold all of the check results that were performed against the 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addressesCheck** | [**List&lt;AddressCheckResultObject&gt;**](AddressCheckResultObject.md) | Collection of address objects. |  [optional] |
|**adverseMediaCheck** | [**List&lt;BackgroundCheckResultObject&gt;**](BackgroundCheckResultObject.md) | !!!!! DEPRECATED !!!!! Please use the multi-result AMLResultSets structure instead.  Note: This single check result structure will be retired in v1.3 !!!!! DEPRECATED !!!!!  Collection of check results for the entity being found in any adverse media  An array sorted by type, then reverse chronological order of some/all background checks done on this entity. Older checks may have been previously done by you or another institution, and if so, these will be listed and appropriately anonymised/obfuscated.  |  [optional] |
|**amlResultSets** | [**List&lt;AMLResultSet&gt;**](AMLResultSet.md) | An array of Collections of PEP/Sanctions/WL/Media objects, as AML providers can return multiple results  |  [optional] |
|**dateOfBirthCheck** | [**DOBCheckResultObject**](DOBCheckResultObject.md) |  |  [optional] |
|**entityId** | **UUID** | Unique ID for the entity.  |  [optional] |
|**genderCheck** | [**GenderCheckResultObject**](GenderCheckResultObject.md) |  |  [optional] |
|**identityDocsCheck** | [**List&lt;IdentityDocumentCheckResultObject&gt;**](IdentityDocumentCheckResultObject.md) | Collection of identity documents (photos, scans, selfies, etc), and their check results |  [optional] |
|**nameCheck** | [**PersonalNameCheckResultObject**](PersonalNameCheckResultObject.md) |  |  [optional] |
|**pepCheck** | [**List&lt;BackgroundCheckResultObject&gt;**](BackgroundCheckResultObject.md) | !!!!! DEPRECATED !!!!! Please use the multi-result AMLResultSets structure instead.  Note: This single check result structure will be retired in v1.3 !!!!! DEPRECATED !!!!!  Collection of check results for the entity being a Politically Exposed Person  An array sorted by type, then reverse chronological order of some/all background checks done on this entity. Older checks may have been previously done by you or another institution, and if so, these will be listed and appropriately anonymised/obfuscated.  |  [optional] |
|**sanctionsCheck** | [**List&lt;BackgroundCheckResultObject&gt;**](BackgroundCheckResultObject.md) | !!!!! DEPRECATED !!!!! Please use the multi-result AMLResultSets structure instead.  Note: This single check result structure will be retired in v1.3 !!!!! DEPRECATED !!!!!  Collection of check results for the entity being on a sanctions list  An array sorted by type, then reverse chronological order of some/all background checks done on this entity. Older checks may have been previously done by you or another institution, and if so, these will be listed and appropriately anonymised/obfuscated.  |  [optional] |
|**watchlistCheck** | [**List&lt;BackgroundCheckResultObject&gt;**](BackgroundCheckResultObject.md) | !!!!! DEPRECATED !!!!! Please use the multi-result AMLResultSets structure instead.  Note: This single check result structure will be retired in v1.3 !!!!! DEPRECATED !!!!!  Collection of check results for the entity being on a watchlist  An array sorted by type, then reverse chronological order of some/all background checks done on this entity. Older checks may have been previously done by you or another institution, and if so, these will be listed and appropriately anonymised/obfuscated.  |  [optional] |



