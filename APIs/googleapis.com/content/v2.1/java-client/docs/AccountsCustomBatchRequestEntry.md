

# AccountsCustomBatchRequestEntry

A batch entry encoding a single non-batch accounts request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**account** | [**Account**](Account.md) |  |  [optional] |
|**accountId** | **String** | The ID of the targeted account. Only defined if the method is not &#x60;insert&#x60;. |  [optional] |
|**batchId** | **Integer** | An entry ID, unique within the batch request. |  [optional] |
|**force** | **Boolean** | Whether the account should be deleted if the account has offers. Only applicable if the method is &#x60;delete&#x60;. |  [optional] |
|**labelIds** | **List&lt;String&gt;** | Label IDs for the &#39;updatelabels&#39; request. |  [optional] |
|**linkRequest** | [**AccountsCustomBatchRequestEntryLinkRequest**](AccountsCustomBatchRequestEntryLinkRequest.md) |  |  [optional] |
|**merchantId** | **String** | The ID of the managing account. |  [optional] |
|**method** | **String** | The method of the batch entry. Acceptable values are: - \&quot;&#x60;claimWebsite&#x60;\&quot; - \&quot;&#x60;delete&#x60;\&quot; - \&quot;&#x60;get&#x60;\&quot; - \&quot;&#x60;insert&#x60;\&quot; - \&quot;&#x60;link&#x60;\&quot; - \&quot;&#x60;update&#x60;\&quot;  |  [optional] |
|**overwrite** | **Boolean** | Only applicable if the method is &#x60;claimwebsite&#x60;. Indicates whether or not to take the claim from another account in case there is a conflict. |  [optional] |
|**view** | **String** | Controls which fields are visible. Only applicable if the method is &#39;get&#39;. |  [optional] |



