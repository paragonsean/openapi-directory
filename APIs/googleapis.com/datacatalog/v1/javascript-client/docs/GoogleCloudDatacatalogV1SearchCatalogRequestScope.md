# GoogleCloudDataCatalogApi.GoogleCloudDatacatalogV1SearchCatalogRequestScope

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**includeGcpPublicDatasets** | **Boolean** | If &#x60;true&#x60;, include Google Cloud public datasets in search results. By default, they are excluded. See [Google Cloud Public Datasets](/public-datasets) for more information. | [optional] 
**includeOrgIds** | **[String]** | The list of organization IDs to search within. To find your organization ID, follow the steps from [Creating and managing organizations] (/resource-manager/docs/creating-managing-organization). | [optional] 
**includeProjectIds** | **[String]** | The list of project IDs to search within. For more information on the distinction between project names, IDs, and numbers, see [Projects](/docs/overview/#projects). | [optional] 
**includePublicTagTemplates** | **Boolean** | Optional. This field is deprecated. The search mechanism for public and private tag templates is the same. | [optional] 
**restrictedLocations** | **[String]** | Optional. The list of locations to search within. If empty, all locations are searched. Returns an error if any location in the list isn&#39;t one of the [Supported regions](https://cloud.google.com/data-catalog/docs/concepts/regions#supported_regions). If a location is unreachable, its name is returned in the &#x60;SearchCatalogResponse.unreachable&#x60; field. To get additional information on the error, repeat the search request and set the location name as the value of this parameter. | [optional] 
**starredOnly** | **Boolean** | Optional. If &#x60;true&#x60;, search only among starred entries. By default, all results are returned, starred or not. | [optional] 


