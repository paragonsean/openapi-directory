# FaceClient.FindSimilarRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**faceId** | **String** | FaceId of the query face. User needs to call Face - Detect first to get a valid faceId. Note that this faceId is not persisted and will expire 24 hours after the detection call | 
**faceIds** | **[String]** | An array of candidate faceIds. All of them are created by Face - Detect and the faceIds will expire 24 hours after the detection call. The number of faceIds is limited to 1000. Parameter faceListId, largeFaceListId and faceIds should not be provided at the same time. | [optional] 
**faceListId** | **String** | An existing user-specified unique candidate face list, created in Face List - Create a Face List. Face list contains a set of persistedFaceIds which are persisted and will never expire. Parameter faceListId, largeFaceListId and faceIds should not be provided at the same time. | [optional] 
**largeFaceListId** | **String** | An existing user-specified unique candidate large face list, created in LargeFaceList - Create. Large face list contains a set of persistedFaceIds which are persisted and will never expire. Parameter faceListId, largeFaceListId and faceIds should not be provided at the same time. | [optional] 
**maxNumOfCandidatesReturned** | **Number** | The number of top similar faces returned. The valid range is [1, 1000]. | [optional] 
**mode** | **String** | Similar face searching mode. It can be \&quot;matchPerson\&quot; or \&quot;matchFace\&quot;. | [optional] [default to &#39;matchPerson&#39;]



## Enum: ModeEnum


* `matchPerson` (value: `"matchPerson"`)

* `matchFace` (value: `"matchFace"`)




