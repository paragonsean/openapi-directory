

# CreateKbDTO

Post body schema for CreateKb operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultAnswerUsedForExtraction** | **String** | Text string to be used as the answer in any Q-A which has no extracted answer from the document but has a hierarchy. Required when EnableHierarchicalExtraction field is set to True. |  [optional] |
|**enableHierarchicalExtraction** | **Boolean** | Enable hierarchical extraction of Q-A from files and urls. Value to be considered False if this field is not present. |  [optional] |
|**files** | [**List&lt;FileDTO&gt;**](FileDTO.md) | List of files from which to Extract Q-A. |  [optional] |
|**language** | **String** | Language of the knowledgebase. |  [optional] |
|**name** | **String** | Friendly name for the knowledgebase. |  |
|**qnaList** | [**List&lt;QnADTO&gt;**](QnADTO.md) | List of Q-A (QnADTO) to be added to the knowledgebase. Q-A Ids are assigned by the service and should be omitted. |  [optional] |
|**urls** | **List&lt;String&gt;** | List of URLs to be used for extracting Q-A. |  [optional] |



