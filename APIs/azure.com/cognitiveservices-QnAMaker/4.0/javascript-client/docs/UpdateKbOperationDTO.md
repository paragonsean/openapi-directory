# QnAMakerClient.UpdateKbOperationDTO

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add** | [**CreateKbInputDTO**](CreateKbInputDTO.md) | An instance of CreateKbInputDTO for add operation | [optional] 
**defaultAnswerUsedForExtraction** | **String** | Text string to be used as the answer in any Q-A which has no extracted answer from the document but has a hierarchy. Required when EnableHierarchicalExtraction field is set to True. | [optional] 
**_delete** | [**DeleteKbContentsDTO**](DeleteKbContentsDTO.md) | An instance of DeleteKbContentsDTO for delete Operation | [optional] 
**enableHierarchicalExtraction** | **Boolean** | Enable hierarchical extraction of Q-A from files and urls. The value set during KB creation will be used if this field is not present. | [optional] 
**update** | [**UpdateKbContentsDTO**](UpdateKbContentsDTO.md) | An instance of UpdateKbContentsDTO for Update Operation | [optional] 


