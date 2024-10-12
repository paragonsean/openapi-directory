# QnAMakerClient.PromptDTO

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayOrder** | **Number** | Index of the prompt - used in ordering of the prompts | [optional] 
**displayText** | **String** | Text displayed to represent a follow up question prompt | [optional] 
**qna** | [**QnADTO**](QnADTO.md) | QnADTO - Either QnaId or QnADTO needs to be present in a PromptDTO object | [optional] 
**qnaId** | **Number** | Qna id corresponding to the prompt - if QnaId is present, QnADTO object is ignored. | [optional] 


