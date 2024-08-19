# AzureMigrateV2.AssessmentOptionsProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reservedInstanceSupportedCurrencies** | **[String]** | List of supported currencies for reserved instances. | [optional] [readonly] 
**reservedInstanceSupportedLocations** | **[String]** | List of supported Azure regions for reserved instances. | [optional] [readonly] 
**reservedInstanceSupportedOffers** | **[String]** | List of supported Azure offer codes for reserved instances. | [optional] [readonly] 
**reservedInstanceVmFamilies** | **[String]** | List of supported VM Families. | [optional] [readonly] 
**vmFamilies** | [**[VmFamily]**](VmFamily.md) | Dictionary of VM families grouped by vm family name describing the targeted azure locations of VM family and the category of the family. | [optional] [readonly] 


