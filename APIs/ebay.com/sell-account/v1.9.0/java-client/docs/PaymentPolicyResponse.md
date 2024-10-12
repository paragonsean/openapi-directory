

# PaymentPolicyResponse

The response payload for the <b>getPaymentPolicies</b> method. <br /><br /><span class=\"tablenote\"><b>Note</b>: Pagination has not yet been enabled for <b>getPaymentPolicies</b>, so all of the pagination-related fields are for future use.</span>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**href** | **String** | This field is for future use. |  [optional] |
|**limit** | **Integer** | This field is for future use. |  [optional] |
|**next** | **String** | This field is for future use. |  [optional] |
|**offset** | **Integer** | This field is for future use. |  [optional] |
|**paymentPolicies** | [**List&lt;PaymentPolicy&gt;**](PaymentPolicy.md) | A list of all of the seller&#39;s payment business policies defined for the specified marketplace. This array will be returned as empty if no payment business policies are defined for the specified marketplace. |  [optional] |
|**prev** | **String** | This field is for future use. |  [optional] |
|**total** | **Integer** | The total number of payment business policies retrieved in the result set.  &lt;br/&gt;&lt;br/&gt;If no payment business policies are defined for the specified marketplace, this field is returned with a value of &lt;code&gt;0&lt;/code&gt;. |  [optional] |



