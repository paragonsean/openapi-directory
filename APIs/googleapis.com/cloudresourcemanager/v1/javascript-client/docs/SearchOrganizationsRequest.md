# CloudResourceManagerApi.SearchOrganizationsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **String** | An optional query string used to filter the Organizations to return in the response. Filter rules are case-insensitive. Organizations may be filtered by &#x60;owner.directoryCustomerId&#x60; or by &#x60;domain&#x60;, where the domain is a G Suite domain, for example: * Filter &#x60;owner.directorycustomerid:123456789&#x60; returns Organization resources with &#x60;owner.directory_customer_id&#x60; equal to &#x60;123456789&#x60;. * Filter &#x60;domain:google.com&#x60; returns Organization resources corresponding to the domain &#x60;google.com&#x60;. This field is optional. | [optional] 
**pageSize** | **Number** | The maximum number of Organizations to return in the response. The server can return fewer organizations than requested. If unspecified, server picks an appropriate default. | [optional] 
**pageToken** | **String** | A pagination token returned from a previous call to &#x60;SearchOrganizations&#x60; that indicates from where listing should continue. This field is optional. | [optional] 


