

# CodeReferenceRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activeBranches** | **List&lt;String&gt;** | The currently active branches of the repository. Each previously uploaded report that belongs to a non-reported active branch is being deleted. |  [optional] |
|**branch** | **String** | The source control branch on where the scan was performed. (Source of the branch selector on the ConfigCat Dashboard) |  |
|**commitHash** | **String** | The related commit&#39;s hash. (Appears on the ConfigCat Dashboard) |  [optional] |
|**commitUrl** | **String** | The related commit&#39;s URL. (Appears on the ConfigCat Dashboard) |  [optional] |
|**configId** | **UUID** | The Config&#39;s identifier the scanning was performed against. |  |
|**flagReferences** | [**List&lt;FlagReference&gt;**](FlagReference.md) | The actual code reference collection. |  [optional] |
|**repository** | **String** | The source control repository that contains the scanned code. (Source of the repository selector on the ConfigCat Dashboard) |  |
|**uploader** | **String** | The scanning tool&#39;s name. (Appears on the ConfigCat Dashboard) |  [optional] |



