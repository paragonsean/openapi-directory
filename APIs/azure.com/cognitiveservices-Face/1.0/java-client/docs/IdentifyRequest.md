

# IdentifyRequest

Request body for identify face operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**confidenceThreshold** | **BigDecimal** | A number ranging from 0 to 1 indicating a level of confidence associated with a property. |  [optional] |
|**faceIds** | **List&lt;UUID&gt;** | Array of query faces faceIds, created by the Face - Detect. Each of the faces are identified independently. The valid number of faceIds is between [1, 10]. |  |
|**largePersonGroupId** | **String** | LargePersonGroupId of the target large person group, created by LargePersonGroup - Create. Parameter personGroupId and largePersonGroupId should not be provided at the same time. |  [optional] |
|**maxNumOfCandidatesReturned** | **Integer** | The range of maxNumOfCandidatesReturned is between 1 and 5 (default is 1). |  [optional] |
|**personGroupId** | **String** | PersonGroupId of the target person group, created by PersonGroup - Create. Parameter personGroupId and largePersonGroupId should not be provided at the same time. |  [optional] |



