# StorecoveApi.DiscoverableParticipant

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**documentTypes** | **[String]** | An array of document types to discover. The default is &#39;[\&quot;invoice\&quot;, \&quot;creditnote\&quot;]&#39;. This is ignored when only checking existence. | [optional] 
**identifier** | **String** | The actual identifier. | 
**metaScheme** | **String** | The meta scheme of the identifier. For Peppol this is always &#39;iso6523-actorid-upis&#39;. | [optional] [default to &#39;iso6523-actorid-upis&#39;]
**network** | **String** | The network to check. Currently only &#39;peppol&#39; is supported. | [optional] [default to &#39;peppol&#39;]
**scheme** | **String** | The scheme of the identifier. See &lt;&lt;_receiver_identifiers_list&gt;&gt; for a list. | 



## Enum: [DocumentTypesEnum]


* `invoice` (value: `"invoice"`)

* `creditnote` (value: `"creditnote"`)

* `invoice_response` (value: `"invoice_response"`)

* `order` (value: `"order"`)

* `ordering` (value: `"ordering"`)

* `order_response` (value: `"order_response"`)




