

# Error

This type contains a error or warning related to a call request. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**category** | **String** | The context or source of this error or warning. |  [optional] |
|**domain** | **String** | The name of the domain containing the service or application. For example, &lt;code&gt;sell&lt;/code&gt; is a domain. |  [optional] |
|**errorId** | **Integer** | A positive integer that uniquely identifies the specific error condition that occurred. Your application can use these values as error code identifiers in your customized error-handling algorithms. |  [optional] |
|**inputRefIds** | **List&lt;String&gt;** | A list of one or more specific request elements (if any) associated with the error or warning. The format of these strings depends on the request payload format. For JSON, use JSONPath notation. |  [optional] |
|**longMessage** | **String** | An expanded version of the &lt;b&gt;message&lt;/b&gt; field. &lt;br&gt;&lt;br&gt;&lt;b&gt;Maximum length:&lt;/b&gt; 200 characters |  [optional] |
|**message** | **String** | A message about the error or warning which is device agnostic and readable by end users and application developers. It explains what the error or warning is, and how to fix it (in a general sense). If applicable, the value is localized to the end user&#39;s requested locale. &lt;br&gt;&lt;br&gt;&lt;b&gt;Maximum length:&lt;/b&gt; 50 characters |  [optional] |
|**outputRefIds** | **List&lt;String&gt;** | A list of one or more specific response elements (if any) associated with the error or warning. The format of these strings depends on the request payload format. For JSON, use JSONPath notation. |  [optional] |
|**parameters** | [**List&lt;ErrorParameter&gt;**](ErrorParameter.md) | Contains a list of name-value pairs that provide additional information concerning this error or warning. Each item in the list is an input parameter that contributed to the error or warning condition. |  [optional] |
|**subdomain** | **String** | The name of the domain&#39;s subsystem or subdivision. For example, &lt;code&gt;fulfillment&lt;/code&gt; is a subdomain in the &lt;code&gt;sell&lt;/code&gt; domain. |  [optional] |



