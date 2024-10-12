# CloudBillingApi.BillingAccount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **String** | The display name given to the billing account, such as &#x60;My Billing Account&#x60;. This name is displayed in the Google Cloud Console. | [optional] 
**masterBillingAccount** | **String** | If this account is a [subaccount](https://cloud.google.com/billing/docs/concepts), then this will be the resource name of the parent billing account that it is being resold through. Otherwise this will be empty. | [optional] 
**name** | **String** | Output only. The resource name of the billing account. The resource name has the form &#x60;billingAccounts/{billing_account_id}&#x60;. For example, &#x60;billingAccounts/012345-567890-ABCDEF&#x60; would be the resource name for billing account &#x60;012345-567890-ABCDEF&#x60;. | [optional] [readonly] 
**open** | **Boolean** | Output only. True if the billing account is open, and will therefore be charged for any usage on associated projects. False if the billing account is closed, and therefore projects associated with it are unable to use paid services. | [optional] [readonly] 
**parent** | **String** | Output only. The billing account&#39;s parent resource identifier. Use the &#x60;MoveBillingAccount&#x60; method to update the account&#39;s parent resource if it is a organization. Format: - &#x60;organizations/{organization_id}&#x60;, for example, &#x60;organizations/12345678&#x60; - &#x60;billingAccounts/{billing_account_id}&#x60;, for example, &#x60;billingAccounts/012345-567890-ABCDEF&#x60; | [optional] [readonly] 


