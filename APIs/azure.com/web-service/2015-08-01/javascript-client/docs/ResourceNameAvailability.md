# WebSiteManagementClient.ResourceNameAvailability

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **String** |  | [optional] 
**nameAvailable** | **Boolean** | True indicates name is valid and available.  False indicates the name is invalid, unavailable, or both. | [optional] 
**reason** | **String** | Required if nameAvailable is false. &#39;Invalid&#39; indicates the name provided does not match Azure WebApp service’s naming requirements. &#39;AlreadyExists&#39; indicates that the name is already in use and is therefore unavailable. | [optional] 


