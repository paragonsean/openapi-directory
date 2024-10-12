

# Person

Person object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**persistedFaceIds** | **List&lt;UUID&gt;** | PersistedFaceIds of registered faces in the person. These persistedFaceIds are returned from Person - Add a Person Face, and will not expire. |  [optional] |
|**personId** | **UUID** | PersonId of the target face list. |  |
|**name** | **String** | User defined name, maximum length is 128. |  [optional] |
|**userData** | **String** | User specified data. Length should not exceed 16KB. |  [optional] |



