# StorageManagementClient.LegalHoldProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hasLegalHold** | **Boolean** | The hasLegalHold public property is set to true by SRP if there are at least one existing tag. The hasLegalHold public property is set to false by SRP if all existing legal hold tags are cleared out. There can be a maximum of 1000 blob containers with hasLegalHold&#x3D;true for a given account. | [optional] [readonly] 
**tags** | [**[TagProperty]**](TagProperty.md) | The list of LegalHold tags of a blob container. | [optional] 


