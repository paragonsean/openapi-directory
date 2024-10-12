

# IdentifyResult

Response body for identify face operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**candidates** | [**List&lt;IdentifyCandidate&gt;**](IdentifyCandidate.md) | Identified person candidates for that face (ranked by confidence). Array size should be no larger than input maxNumOfCandidatesReturned. If no person is identified, will return an empty array. |  |
|**faceId** | **UUID** | FaceId of the query face |  |



