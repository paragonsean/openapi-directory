

# RequestStatistics

if showStats=true was specified in the request this field will contain information about the request payload.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**documentsCount** | **Integer** | Number of documents submitted in the request. |  |
|**erroneousDocumentsCount** | **Integer** | Number of invalid documents. This includes empty, over-size limit or non-supported languages documents. |  |
|**transactionsCount** | **Long** | Number of transactions for the request. |  |
|**validDocumentsCount** | **Integer** | Number of valid documents. This excludes empty, over-size limit or non-supported languages documents. |  |



