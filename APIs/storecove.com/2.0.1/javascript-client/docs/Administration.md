# StorecoveApi.Administration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **String** | The email address to send the received document to | [optional] 
**id** | **Number** | The Storecove assigned id for the Administration. | [optional] 
**legalEntityId** | **Number** | The LegalEntity the Administration belongs to. | [optional] 
**packageVersion** | **String** | The version of the package. | [optional] 
**packaging** | **String** | How to package the purchase invoice. | [optional] 
**senderEmailIdentityId** | **Number** | The id of the SenderEmailIdentity. If not provided, the Storecove default sender will be used | [optional] 



## Enum: PackageVersionEnum


* `peppol_bis_v3` (value: `"peppol_bis_v3"`)

* `aunz` (value: `"aunz"`)

* `sg` (value: `"sg"`)





## Enum: PackagingEnum


* `ubl` (value: `"ubl"`)




