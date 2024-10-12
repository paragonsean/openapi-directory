

# DiscoverableParticipant

A participant to be discovered.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**documentTypes** | [**List&lt;DocumentTypesEnum&gt;**](#List&lt;DocumentTypesEnum&gt;) | An array of document types to discover. The default is &#39;[\&quot;invoice\&quot;, \&quot;creditnote\&quot;]&#39;. This is ignored when only checking existence. |  [optional] |
|**identifier** | **String** | The actual identifier. |  |
|**metaScheme** | **String** | The meta scheme of the identifier. For Peppol this is always &#39;iso6523-actorid-upis&#39;. |  [optional] |
|**network** | **String** | The network to check. Currently only &#39;peppol&#39; is supported. |  [optional] |
|**scheme** | **String** | The scheme of the identifier. See &lt;&lt;_receiver_identifiers_list&gt;&gt; for a list. |  |



## Enum: List&lt;DocumentTypesEnum&gt;

| Name | Value |
|---- | -----|
| INVOICE | &quot;invoice&quot; |
| CREDITNOTE | &quot;creditnote&quot; |
| INVOICE_RESPONSE | &quot;invoice_response&quot; |
| ORDER | &quot;order&quot; |
| ORDERING | &quot;ordering&quot; |
| ORDER_RESPONSE | &quot;order_response&quot; |



