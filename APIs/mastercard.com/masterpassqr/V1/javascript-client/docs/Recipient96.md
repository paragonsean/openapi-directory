# SendPersonToMerchant.Recipient96

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalMerchantData** | [**AdditionalMerchantData98**](AdditionalMerchantData98.md) |  | [optional] 
**address** | [**Address97**](Address97.md) |  | 
**email** | **String** | Email address of the recipient/merchant. Phone number or email address should be provided if the partner is set up to receive notifications. Details- Conditional, 5-254 | [optional] 
**firstName** | **String** | First name of the recipient/merchant.If business name is XYZ : First name: XYZ ; Last name: XYZ; If business name is XYZ International: First name: XYZ  Last name: International ; if business name is XYZ DBA MA : First name: XYZ Last name: DBA MA.\\n\\nType: Alphanumeric Special [a-zA-Z0-9 !\&quot;#$%&amp;&#39;()*+,-./\\:;&lt;&#x3D;&gt;?@[]_&#x60;{|}~ÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÑÒÓÔÕÖÙÚÚÚÝàáâãäåçèéêëìíîïñòóôõöùúûüýÿ], Length: 1-40 | [optional] 
**lastName** | **String** | Last name of the recipient/merchant.If business name is XYZ : First name: XYZ ; Last name: XYZ; If business name is XYZ International: First name: XYZ  Last name: International ; if business name is XYZ DBA MA : First name: XYZ Last name: DBA MA.\\n\\nType: Alphanumeric Special [a-zA-Z0-9 !\&quot;#$%&amp;&#39;()*+,-./\\:;&lt;&#x3D;&gt;?@[]_&#x60;{|}~ÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÑÒÓÔÕÖÙÚÚÚÝàáâãäåçèéêëìíîïñòóôõöùúûüýÿ], Length: 1-40 | [optional] 
**merchantCategoryCode** | **String** | Mastercard defined merchant category code. This identifies the type of business of the recipient/merchant. This merchant category code should match valid code set by Mastercard rules. Details 1-4 | 
**middleName** | **String** | Middle name of the recipient/merchant.\\n\\nType: Alphanumeric Special [a-zA-Z0-9 !\&quot;#$%&amp;&#39;()*+,-./\\:;&lt;&#x3D;&gt;?@[]_&#x60;{|}~ÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÑÒÓÔÕÖÙÚÚÚÝàáâãäåçèéêëìíîïñòóôõöùúûüýÿ], Length: 1-40 | [optional] 
**phone** | **String** | Phone number of the recipient/merchant. Phone number or email address should be provided if the partner is set up to receive notifications. Details- 1-15 | [optional] 


