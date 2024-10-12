# ContentApiForShopping.OrdersCreateTestOrderRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **String** | The CLDR territory code of the country of the test order to create. Affects the currency and addresses of orders created through &#x60;template_name&#x60;, or the addresses of orders created through &#x60;test_order&#x60;. Acceptable values are: - \&quot;&#x60;US&#x60;\&quot; - \&quot;&#x60;FR&#x60;\&quot; Defaults to \&quot;&#x60;US&#x60;\&quot;. | [optional] 
**templateName** | **String** | The test order template to use. Specify as an alternative to &#x60;testOrder&#x60; as a shortcut for retrieving a template and then creating an order using that template. Acceptable values are: - \&quot;&#x60;template1&#x60;\&quot; - \&quot;&#x60;template1a&#x60;\&quot; - \&quot;&#x60;template1b&#x60;\&quot; - \&quot;&#x60;template2&#x60;\&quot; - \&quot;&#x60;template3&#x60;\&quot;  | [optional] 
**testOrder** | [**TestOrder**](TestOrder.md) |  | [optional] 


