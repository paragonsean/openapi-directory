

# GoogleCloudChannelV1ListTransferableOffersRequest

Request message for CloudChannelService.ListTransferableOffers

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingAccount** | **String** | Optional. The Billing Account to look up Offers for. Format: accounts/{account_id}/billingAccounts/{billing_account_id}. This field is only relevant for multi-currency accounts. It should be left empty for single currency accounts. |  [optional] |
|**cloudIdentityId** | **String** | Customer&#39;s Cloud Identity ID |  [optional] |
|**customerName** | **String** | A reseller should create a customer and use the resource name of that customer here. |  [optional] |
|**languageCode** | **String** | Optional. The BCP-47 language code. For example, \&quot;en-US\&quot;. The response will localize in the corresponding language code, if specified. The default value is \&quot;en-US\&quot;. |  [optional] |
|**pageSize** | **Integer** | Requested page size. Server might return fewer results than requested. If unspecified, returns at most 100 offers. The maximum value is 1000; the server will coerce values above 1000. |  [optional] |
|**pageToken** | **String** | A token for a page of results other than the first page. Obtained using ListTransferableOffersResponse.next_page_token of the previous CloudChannelService.ListTransferableOffers call. |  [optional] |
|**sku** | **String** | Required. The SKU to look up Offers for. |  [optional] |



