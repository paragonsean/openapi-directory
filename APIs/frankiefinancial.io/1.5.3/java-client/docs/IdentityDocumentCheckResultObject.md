

# IdentityDocumentCheckResultObject

This object holds the identityDocument that was checked and the results associated with said checks. You can also leave the checkResult blank/nil if there are no results for that identityDocument if you wish.  This is useful for returning results on a freshly crerated entity where the API user would want to confirm that the data has indeed been stored, and be able to capture relevant documentIds - perhaps to address issues as to why it wasn't checked. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**checkResult** | [**List&lt;GeneralCheckResultObject&gt;**](GeneralCheckResultObject.md) | An array in reverse chronological order of all checks done on this data point for the given entity. Older checks may have been previously done by you or another institution, and if so, these will be listed. |  [optional] |
|**idDocument** | [**IdentityDocumentObject**](IdentityDocumentObject.md) |  |  [optional] |



