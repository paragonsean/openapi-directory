# ThePlaidApi.ConnectedApplication

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationId** | **String** | This field will map to the application ID that is returned from /item/applications/list, or provided to the institution in an oauth redirect. | 
**applicationUrl** | **String** | The URL for the application&#39;s website | [optional] 
**createdAt** | **Date** | The date this application was linked in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) (YYYY-MM-DD) format in UTC. | 
**displayName** | **String** | A human-readable name of the application for display purposes | [optional] 
**logoUrl** | **String** | A URL that links to the application logo image. | [optional] 
**name** | **String** | The name of the application | 
**reasonForAccess** | **String** | A string provided by the connected app stating why they use their respective enabled products. | [optional] 
**scopes** | [**ScopesNullable**](ScopesNullable.md) |  | [optional] 


