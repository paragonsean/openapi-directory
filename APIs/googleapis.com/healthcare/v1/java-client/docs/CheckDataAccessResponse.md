

# CheckDataAccessResponse

Checks if a particular data_id of a User data mapping in the given consent store is consented for a given use.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**consentDetails** | [**Map&lt;String, ConsentEvaluation&gt;**](ConsentEvaluation.md) | The resource names of all evaluated Consents mapped to their evaluation. |  [optional] |
|**consented** | **Boolean** | Whether the requested resource is consented for the given use. |  [optional] |



