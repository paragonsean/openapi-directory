

# FulfillmentPolicyResponse

The response payload for the <b>getFulfillmentPolicies</b> method.<br /><br /><span class=\"tablenote\"><b>Note</b>: Pagination has not yet been enabled for <b>getFulfillmentPolicies</b>, so all of the pagination-related fields are for future use.</span>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fulfillmentPolicies** | [**List&lt;FulfillmentPolicy&gt;**](FulfillmentPolicy.md) | A list of all of the seller&#39;s fulfillment policies defined for the specified marketplace. This array will be returned as empty if no fulfillment policies are defined for the specified marketplace. |  [optional] |
|**href** | **String** | This field is for future use. |  [optional] |
|**limit** | **Integer** | This field is for future use. |  [optional] |
|**next** | **String** | This field is for future use. |  [optional] |
|**offset** | **Integer** | This field is for future use. |  [optional] |
|**prev** | **String** | This field is for future use. |  [optional] |
|**total** | **Integer** | The total number of fulfillment policies retrieved in the result set.  &lt;br/&gt;&lt;br/&gt;If no fulfillment policies are defined for the specified marketplace, this field is returned with a value of &lt;code&gt;0&lt;/code&gt;. |  [optional] |



