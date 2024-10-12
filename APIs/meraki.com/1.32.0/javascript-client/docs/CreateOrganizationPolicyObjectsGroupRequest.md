# MerakiDashboardApi.CreateOrganizationPolicyObjectsGroupRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **String** | Category of a policy object group (one of: NetworkObjectGroup, GeoLocationGroup, PortObjectGroup, ApplicationGroup) | [optional] 
**name** | **String** | A name for the group of network addresses, unique within the organization (alphanumeric, space, dash, or underscore characters only) | 
**objectIds** | **[Number]** | A list of Policy Object ID&#39;s that this NetworkObjectGroup should be associated to (note: these ID&#39;s will replace the existing associated Policy Objects) | [optional] 


