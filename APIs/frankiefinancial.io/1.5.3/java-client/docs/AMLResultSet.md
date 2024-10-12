

# AMLResultSet

Wrapper object to contain a single set of AML check results.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**checkResultsListMedia** | [**List&lt;BackgroundCheckResultObjectContainer&gt;**](BackgroundCheckResultObjectContainer.md) | Collection of check results for the entity being found in any adverse media  An array sorted by type, then reverse chronological order of some/all background checks done on this entity. Older checks may have been previously done by you or another institution, and if so, these will be listed and appropriately anonymised/obfuscated.  |  [optional] |
|**checkResultsListPEP** | [**List&lt;BackgroundCheckResultObjectContainer&gt;**](BackgroundCheckResultObjectContainer.md) | Collection of check results for the entity being a Politically Exposed Person  An array sorted by type, then reverse chronological order of some/all background checks done on this entity. Older checks may have been previously done by you or another institution, and if so, these will be listed and appropriately anonymised/obfuscated.  |  [optional] |
|**checkResultsListSanctions** | [**List&lt;BackgroundCheckResultObjectContainer&gt;**](BackgroundCheckResultObjectContainer.md) | Collection of check results for the entity being on a sanctions list  An array sorted by type, then reverse chronological order of some/all background checks done on this entity. Older checks may have been previously done by you or another institution, and if so, these will be listed and appropriately anonymised/obfuscated.  |  [optional] |
|**checkResultsListWatchlists** | [**List&lt;BackgroundCheckResultObjectContainer&gt;**](BackgroundCheckResultObjectContainer.md) | Collection of check results for the entity being on a watchlist  An array sorted by type, then reverse chronological order of some/all background checks done on this entity. Older checks may have been previously done by you or another institution, and if so, these will be listed and appropriately anonymised/obfuscated.  |  [optional] |
|**groupDetails** | [**BackgroundCheckResultObjectContainer**](BackgroundCheckResultObjectContainer.md) |  |  [optional] |



