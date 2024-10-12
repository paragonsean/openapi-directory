# CloudStorageJsonApi.BucketWebsite

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mainPageSuffix** | **String** | If the requested object path is missing, the service will ensure the path has a trailing &#39;/&#39;, append this suffix, and attempt to retrieve the resulting object. This allows the creation of index.html objects to represent directory pages. | [optional] 
**notFoundPage** | **String** | If the requested object path is missing, and any mainPageSuffix object is missing, if applicable, the service will return the named object from this bucket as the content for a 404 Not Found result. | [optional] 


