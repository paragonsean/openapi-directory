

# GoogleCloudRetailV2betaMerchantCenterAccountLink

Represents a link between a Merchant Center account and a branch. After a link is established, products from the linked Merchant Center account are streamed to the linked branch.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**branchId** | **String** | Required. The branch ID (e.g. 0/1/2) within the catalog that products from merchant_center_account_id are streamed to. When updating this field, an empty value will use the currently configured default branch. However, changing the default branch later on won&#39;t change the linked branch here. A single branch ID can only have one linked Merchant Center account ID. |  [optional] |
|**feedFilters** | [**List&lt;GoogleCloudRetailV2betaMerchantCenterAccountLinkMerchantCenterFeedFilter&gt;**](GoogleCloudRetailV2betaMerchantCenterAccountLinkMerchantCenterFeedFilter.md) | Criteria for the Merchant Center feeds to be ingested via the link. All offers will be ingested if the list is empty. Otherwise the offers will be ingested from selected feeds. |  [optional] |
|**feedLabel** | **String** | The FeedLabel used to perform filtering. Note: this replaces [region_id](https://developers.google.com/shopping-content/reference/rest/v2.1/products#Product.FIELDS.feed_label). Example value: &#x60;US&#x60;. Example value: &#x60;FeedLabel1&#x60;. |  [optional] |
|**id** | **String** | Output only. Immutable. MerchantCenterAccountLink identifier, which is the final component of name. This field is auto generated and follows the convention: &#x60;BranchId_MerchantCenterAccountId&#x60;. &#x60;projects/_*_/locations/global/catalogs/default_catalog/merchantCenterAccountLinks/id_1&#x60;. |  [optional] [readonly] |
|**languageCode** | **String** | Language of the title/description and other string attributes. Use language tags defined by [BCP 47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt). ISO 639-1. This specifies the language of offers in Merchant Center that will be accepted. If empty, no language filtering will be performed. Example value: &#x60;en&#x60;. |  [optional] |
|**merchantCenterAccountId** | **String** | Required. The linked [Merchant center account id](https://developers.google.com/shopping-content/guides/accountstatuses). The account must be a standalone account or a sub-account of a MCA. |  [optional] |
|**name** | **String** | Output only. Immutable. Full resource name of the Merchant Center Account Link, such as &#x60;projects/_*_/locations/global/catalogs/default_catalog/merchantCenterAccountLinks/merchant_center_account_link&#x60;. |  [optional] [readonly] |
|**projectId** | **String** | Output only. Google Cloud project ID. |  [optional] [readonly] |
|**source** | **String** | Optional. An optional arbitrary string that could be used as a tag for tracking link source. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. Represents the state of the link. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| PENDING | &quot;PENDING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| FAILED | &quot;FAILED&quot; |



