

# GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecExtractiveContentSpec

A specification for configuring the extractive content in a search response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxExtractiveAnswerCount** | **Integer** | The maximum number of extractive answers returned in each search result. An extractive answer is a verbatim answer extracted from the original document, which provides a precise and contextually relevant answer to the search query. If the number of matching answers is less than the &#x60;max_extractive_answer_count&#x60;, return all of the answers. Otherwise, return the &#x60;max_extractive_answer_count&#x60;. At most five answers are returned for each SearchResult. |  [optional] |
|**maxExtractiveSegmentCount** | **Integer** | The max number of extractive segments returned in each search result. Only applied if the DataStore is set to DataStore.ContentConfig.CONTENT_REQUIRED or DataStore.solution_types is SOLUTION_TYPE_CHAT. An extractive segment is a text segment extracted from the original document that is relevant to the search query, and, in general, more verbose than an extractive answer. The segment could then be used as input for LLMs to generate summaries and answers. If the number of matching segments is less than &#x60;max_extractive_segment_count&#x60;, return all of the segments. Otherwise, return the &#x60;max_extractive_segment_count&#x60;. |  [optional] |
|**numNextSegments** | **Integer** | Return at most &#x60;num_next_segments&#x60; segments after each selected segments. |  [optional] |
|**numPreviousSegments** | **Integer** | Specifies whether to also include the adjacent from each selected segments. Return at most &#x60;num_previous_segments&#x60; segments before each selected segments. |  [optional] |



