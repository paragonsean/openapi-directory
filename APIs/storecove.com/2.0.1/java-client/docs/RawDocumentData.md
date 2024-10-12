

# RawDocumentData

A document to send, in base64 encoded format.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**document** | **String** | The base64 encoded version of the document. |  |
|**documentTypeId** | **String** | The document type id of the document. Required when parse &#x3D;&#x3D; false. |  [optional] |
|**parse** | **Boolean** | *** NOTE: only parse &#x3D;&#x3D; true is currently supported *** *** NOTE: parsing is only supported for documentType &#x3D;&#x3D; &#39;invoice&#39; *** Whether or not to parse the document. If true, the data will be extracted from the document and used to construct a new document. If false, the document will be sent as is. In this case, you must ensure the document validates without any errors against the relevant validation artifacts for that processId/documentTypeId. We automatically apply updates of the validation artificats, respecting the grace period provided by the issuer. During that period, documents that validate against either the old as well as against the new artifacts are accepted. After the grace period, your document must validate against the new artifacts. You are also responsible for making sure your receiver is able to receive the updated document. |  [optional] |
|**parseStrategy** | [**ParseStrategyEnum**](#ParseStrategyEnum) | How to parse the document. Only needed when parse &#x3D;&#x3D; true. |  [optional] |
|**processId** | **String** | The process id of the document. Required when parse &#x3D;&#x3D; false. |  [optional] |



## Enum: ParseStrategyEnum

| Name | Value |
|---- | -----|
| UBL | &quot;ubl&quot; |
| CII | &quot;cii&quot; |
| IDOC | &quot;idoc&quot; |



