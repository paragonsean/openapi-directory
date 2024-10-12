

# GooglePrivacyDlpV2HybridFindingDetails

Populate to associate additional data with each finding.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**containerDetails** | [**GooglePrivacyDlpV2Container**](GooglePrivacyDlpV2Container.md) |  |  [optional] |
|**fileOffset** | **String** | Offset in bytes of the line, from the beginning of the file, where the finding is located. Populate if the item being scanned is only part of a bigger item, such as a shard of a file and you want to track the absolute position of the finding. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Labels to represent user provided metadata about the data being inspected. If configured by the job, some key values may be required. The labels associated with &#x60;Finding&#x60;&#39;s produced by hybrid inspection. Label keys must be between 1 and 63 characters long and must conform to the following regular expression: &#x60;[a-z]([-a-z0-9]*[a-z0-9])?&#x60;. Label values must be between 0 and 63 characters long and must conform to the regular expression &#x60;([a-z]([-a-z0-9]*[a-z0-9])?)?&#x60;. No more than 10 labels can be associated with a given finding. Examples: * &#x60;\&quot;environment\&quot; : \&quot;production\&quot;&#x60; * &#x60;\&quot;pipeline\&quot; : \&quot;etl\&quot;&#x60; |  [optional] |
|**rowOffset** | **String** | Offset of the row for tables. Populate if the row(s) being scanned are part of a bigger dataset and you want to keep track of their absolute position. |  [optional] |
|**tableOptions** | [**GooglePrivacyDlpV2TableOptions**](GooglePrivacyDlpV2TableOptions.md) |  |  [optional] |



