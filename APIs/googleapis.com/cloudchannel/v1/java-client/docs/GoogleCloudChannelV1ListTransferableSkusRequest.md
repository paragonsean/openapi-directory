

# GoogleCloudChannelV1ListTransferableSkusRequest

Request message for CloudChannelService.ListTransferableSkus

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authToken** | **String** | Optional. The super admin of the resold customer generates this token to authorize a reseller to access their Cloud Identity and purchase entitlements on their behalf. You can omit this token after authorization. See https://support.google.com/a/answer/7643790 for more details. |  [optional] |
|**cloudIdentityId** | **String** | Customer&#39;s Cloud Identity ID |  [optional] |
|**customerName** | **String** | A reseller is required to create a customer and use the resource name of the created customer here. Customer_name uses the format: accounts/{account_id}/customers/{customer_id} |  [optional] |
|**languageCode** | **String** | The BCP-47 language code. For example, \&quot;en-US\&quot;. The response will localize in the corresponding language code, if specified. The default value is \&quot;en-US\&quot;. Optional. |  [optional] |
|**pageSize** | **Integer** | The requested page size. Server might return fewer results than requested. If unspecified, returns at most 100 SKUs. The maximum value is 1000; the server will coerce values above 1000. Optional. |  [optional] |
|**pageToken** | **String** | A token for a page of results other than the first page. Obtained using ListTransferableSkusResponse.next_page_token of the previous CloudChannelService.ListTransferableSkus call. Optional. |  [optional] |



