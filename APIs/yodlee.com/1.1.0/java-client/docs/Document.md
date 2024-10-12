

# Document


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountID** | **Long** | The unique identifier for the account. The account ID to which the document is linked.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank, investment, creditCard, loan, insurance&lt;br&gt; |  [optional] [readonly] |
|**docType** | [**DocTypeEnum**](#DocTypeEnum) | Indicates the type of the document.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank, investment, creditCard, loan, insurance&lt;br&gt; |  [optional] [readonly] |
|**formType** | **String** | Indicates the type of the tax form.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank, investment, creditCard, loan, insurance&lt;br&gt; |  [optional] [readonly] |
|**id** | **String** | The document&#39;s primary key and unique identifier.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank, investment, creditCard, loan, insurance&lt;br&gt; |  [optional] [readonly] |
|**lastUpdated** | **String** | Indicates the date and time the document was last updated.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank, investment, creditCard, loan, insurance&lt;br&gt; |  [optional] [readonly] |
|**name** | **String** | Indicates the name of the document.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank, investment, creditCard, loan, insurance&lt;br&gt; |  [optional] [readonly] |
|**source** | **String** | Indicates the source of the document download.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank, investment, creditCard, loan, insurance&lt;br&gt; |  [optional] [readonly] |
|**status** | **String** | Indicates the status of the document download.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank, investment, creditCard, loan, insurance&lt;br&gt; |  [optional] [readonly] |



## Enum: DocTypeEnum

| Name | Value |
|---- | -----|
| STMT | &quot;STMT&quot; |
| TAX | &quot;TAX&quot; |
| EBILL | &quot;EBILL&quot; |



