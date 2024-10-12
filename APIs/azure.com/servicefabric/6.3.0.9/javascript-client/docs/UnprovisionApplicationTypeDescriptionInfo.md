# ServiceFabricClientApis.UnprovisionApplicationTypeDescriptionInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationTypeVersion** | **String** | The version of the application type as defined in the application manifest. | 
**async** | **Boolean** | The flag indicating whether or not unprovision should occur asynchronously. When set to true, the unprovision operation returns when the request is accepted by the system, and the unprovision operation continues without any timeout limit. The default value is false. However, we recommend setting it to true for large application packages that were provisioned. | [optional] 


