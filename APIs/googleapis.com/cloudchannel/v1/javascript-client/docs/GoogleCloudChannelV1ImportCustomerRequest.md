# CloudChannelApi.GoogleCloudChannelV1ImportCustomerRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authToken** | **String** | Optional. The super admin of the resold customer generates this token to authorize a reseller to access their Cloud Identity and purchase entitlements on their behalf. You can omit this token after authorization. See https://support.google.com/a/answer/7643790 for more details. | [optional] 
**channelPartnerId** | **String** | Optional. Cloud Identity ID of a channel partner who will be the direct reseller for the customer&#39;s order. This field is required for 2-tier transfer scenarios and can be provided via the request Parent binding as well. | [optional] 
**cloudIdentityId** | **String** | Required. Customer&#39;s Cloud Identity ID | [optional] 
**customer** | **String** | Optional. Specifies the customer that will receive imported Cloud Identity information. Format: accounts/{account_id}/customers/{customer_id} | [optional] 
**domain** | **String** | Required. Customer domain. | [optional] 
**overwriteIfExists** | **Boolean** | Required. Choose to overwrite an existing customer if found. This must be set to true if there is an existing customer with a conflicting region code or domain. | [optional] 


