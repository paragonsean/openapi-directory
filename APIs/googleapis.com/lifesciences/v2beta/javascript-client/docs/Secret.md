# CloudLifeSciencesApi.Secret

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cipherText** | **String** | The value of the cipherText response from the &#x60;encrypt&#x60; method. This field is intentionally unaudited. | [optional] 
**keyName** | **String** | The name of the Cloud KMS key that will be used to decrypt the secret value. The VM service account must have the required permissions and authentication scopes to invoke the &#x60;decrypt&#x60; method on the specified key. | [optional] 


