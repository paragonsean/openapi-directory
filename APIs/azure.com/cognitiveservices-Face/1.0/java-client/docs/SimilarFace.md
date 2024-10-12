

# SimilarFace

Response body for find similar face operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**confidence** | **BigDecimal** | A number ranging from 0 to 1 indicating a level of confidence associated with a property. |  |
|**faceId** | **UUID** | FaceId of candidate face when find by faceIds. faceId is created by Face - Detect and will expire 24 hours after the detection call |  [optional] |
|**persistedFaceId** | **UUID** | PersistedFaceId of candidate face when find by faceListId. persistedFaceId in face list is persisted and will not expire. As showed in below response |  [optional] |



