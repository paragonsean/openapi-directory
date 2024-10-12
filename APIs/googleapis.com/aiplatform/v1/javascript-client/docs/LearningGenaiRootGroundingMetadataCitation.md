# VertexAiApi.LearningGenaiRootGroundingMetadataCitation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endIndex** | **Number** | Index in the prediction output where the citation ends (exclusive). Must be &gt; start_index and &lt; len(output). | [optional] 
**factIndex** | **Number** | Index of the fact supporting this claim. Should be within the range of the &#x60;world_facts&#x60; in the GenerateResponse. | [optional] 
**score** | **Number** | Confidence score of this entailment. Value is [0,1] with 1 is the most confidence. | [optional] 
**startIndex** | **Number** | Index in the prediction output where the citation starts (inclusive). Must be &gt;&#x3D; 0 and &lt; end_index. | [optional] 


