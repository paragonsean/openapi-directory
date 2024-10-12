

# AdminCorpus


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customDimensions** | [**List&lt;AdminDimension&gt;**](AdminDimension.md) |  |  [optional] |
|**description** | **String** | A description for the corpus. |  [optional] |
|**dtProvision** | **String** | The time at which the corpus was provisioned. |  [optional] |
|**enabled** | **Boolean** | Whether the corpus is enabled for use or not. |  [optional] |
|**encoderId** | **String** | This is an advanced setting for changing the underlying model type.  The default value is \&quot;1\&quot;, which is Vectara&#39;s high-performing global model. Underlying models may be swapped for some paying customers by contacting our support team. |  [optional] |
|**encrypted** | **Boolean** | Encryption is on by default and cannot be turned off. |  [optional] |
|**filterAttributes** | [**List&lt;AdminFilterAttribute&gt;**](AdminFilterAttribute.md) |  |  [optional] |
|**id** | **Long** | The Corpus ID. |  [optional] |
|**metadataMaxBytes** | **Long** | An optional maximum size of the metadata that each document can contain. |  [optional] |
|**name** | **String** | The name of the corpus. |  [optional] |
|**swapIenc** | **Boolean** | The default query encoder is designed for normal question-answering types of queries when the text contains the answer.  Swapping the index encoder is generally rare, but can be used to help directly match questions to questions.  This can be useful if you have a FAQ dataset and you want to directly match the user question to the question in the FAQ. |  [optional] |
|**swapQenc** | **Boolean** |  |  [optional] |
|**textless** | **Boolean** | When a corpus is \&quot;textless\&quot;, Vectara does not store the original text. Instead, Vectara converts the text to vectors and only retains metadata. |  [optional] |



