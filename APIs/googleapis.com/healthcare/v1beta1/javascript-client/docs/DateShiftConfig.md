# CloudHealthcareApi.DateShiftConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cryptoKey** | **Blob** | An AES 128/192/256 bit key. The date shift is computed based on this key and the patient ID. If the patient ID is empty for a DICOM resource, the date shift is computed based on this key and the study instance UID. If crypto_key is not set, then kms_wrapped is used to calculate the date shift. If neither is set, a default key is generated for each de-identify operation. Must not be set if kms_wrapped is set. | [optional] 
**kmsWrapped** | [**KmsWrappedCryptoKey**](KmsWrappedCryptoKey.md) |  | [optional] 


