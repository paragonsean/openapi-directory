# StorageManagement.EncryptionService

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **Boolean** | A boolean indicating whether or not the service encrypts the data as it is stored. | [optional] 
**lastEnabledTime** | **Date** | Gets a rough estimate of the date/time when the encryption was last enabled by the user. Only returned when encryption is enabled. There might be some unencrypted blobs which were written after this time, as it is just a rough estimate. | [optional] [readonly] 


