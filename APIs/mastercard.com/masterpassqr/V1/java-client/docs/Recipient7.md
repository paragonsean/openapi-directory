

# Recipient7

Information about the recipient/merchant of the transaction.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalMerchantData** | [**AdditionalMerchantData9**](AdditionalMerchantData9.md) |  |  [optional] |
|**address** | [**Address8**](Address8.md) |  |  |
|**authenticationValue** | **String** | List of name/value pairs containing authentication  values. Refer &#39;Authentication Value URIs&#39; |  [optional] |
|**email** | **String** | Email address of the recipient/merchant.\\n\\nType: Alphanumeric Special [a-zA-Z0-9\\-@+.*$_], Length: 5-254 |  [optional] |
|**firstName** | **String** | First name of the recipient/merchant.If business name is XYZ : First name: XYZ ; Last name: XYZ; If business name is XYZ International: First name: XYZ  Last name: International ; if business name is XYZ DBA MA : First name: XYZ Last name: DBA MA.\\n\\nType: Alphanumeric Special [a-zA-Z0-9 !\&quot;#$%&amp;&#39;()*+,-./\\:;&lt;&#x3D;&gt;?@[]_&#x60;{|}~ÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÑÒÓÔÕÖÙÚÚÚÝàáâãäåçèéêëìíîïñòóôõöùúûüýÿ], Length: 1-40 |  |
|**lastName** | **String** | Last name of the recipient/merchant.If business name is XYZ : First name: XYZ ; Last name: XYZ; If business name is XYZ International: First name: XYZ  Last name: International ; if business name is XYZ DBA MA : First name: XYZ Last name: DBA MA.\\n\\nType: Alphanumeric Special [a-zA-Z0-9 !\&quot;#$%&amp;&#39;()*+,-./\\:;&lt;&#x3D;&gt;?@[]_&#x60;{|}~ÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÑÒÓÔÕÖÙÚÚÚÝàáâãäåçèéêëìíîïñòóôõöùúûüýÿ], Length: 1-40 |  |
|**merchantCategoryCode** | **String** | Mastercard defined merchant category code. This identifies the type of business of the recipient/merchant. This merchant category code should match valid code set by Mastercard rules.   Type: Numeric [0-9], Length: 1-4 |  |
|**middleName** | **String** | Middle name of the recipient/merchant.\\n\\nType: Alphanumeric Special [a-zA-Z0-9 !\&quot;#$%&amp;&#39;()*+,-./\\:;&lt;&#x3D;&gt;?@[]_&#x60;{|}~ÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÑÒÓÔÕÖÙÚÚÚÝàáâãäåçèéêëìíîïñòóôõöùúûüýÿ], Length: 1-40 |  [optional] |
|**phone** | **String** | Phone number of the recipient/merchant, Country code can be included.   Type: Numeric [0-9], Length: 1-15 |  [optional] |
|**tokenCryptogram** | [**TokenCryptogram10**](TokenCryptogram10.md) |  |  [optional] |



