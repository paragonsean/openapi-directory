# SasPortalApiTesting.SasPortalDeviceMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**antennaModel** | **String** | If populated, the Antenna Model Pattern to use. Format is: &#x60;RecordCreatorId:PatternId&#x60; | [optional] 
**commonChannelGroup** | **String** | Common Channel Group (CCG). A group of CBSDs in the same ICG requesting a common primary channel assignment. For more details, see [CBRSA-TS-2001 V3.0.0](https://ongoalliance.org/wp-content/uploads/2020/02/CBRSA-TS-2001-V3.0.0_Approved-for-publication.pdf). | [optional] 
**interferenceCoordinationGroup** | **String** | Interference Coordination Group (ICG). A group of CBSDs that manage their own interference with the group. For more details, see [CBRSA-TS-2001 V3.0.0](https://ongoalliance.org/wp-content/uploads/2020/02/CBRSA-TS-2001-V3.0.0_Approved-for-publication.pdf). | [optional] 
**nrqzValidated** | **Boolean** | Output only. Set to &#x60;true&#x60; if a CPI has validated that they have coordinated with the National Quiet Zone office. | [optional] [readonly] 
**nrqzValidation** | [**SasPortalNrqzValidation**](SasPortalNrqzValidation.md) |  | [optional] 


