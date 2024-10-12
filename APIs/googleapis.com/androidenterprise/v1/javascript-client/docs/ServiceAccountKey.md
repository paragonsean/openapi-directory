# GooglePlayEmmApi.ServiceAccountKey

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **String** | The body of the private key credentials file, in string format. This is only populated when the ServiceAccountKey is created, and is not stored by Google. | [optional] 
**id** | **String** | An opaque, unique identifier for this ServiceAccountKey. Assigned by the server. | [optional] 
**publicData** | **String** | Public key data for the credentials file. This is an X.509 cert. If you are using the googleCredentials key type, this is identical to the cert that can be retrieved by using the X.509 cert url inside of the credentials file. | [optional] 
**type** | **String** | The file format of the generated key data. | [optional] 



## Enum: TypeEnum


* `googleCredentials` (value: `"googleCredentials"`)

* `pkcs12` (value: `"pkcs12"`)




