# OsfApiv2Documentation.Attributes9

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkout** | **String** | SOON TO BE DEPRECATED, see relationships checkout. | [optional] [readonly] 
**currentUserCanComment** | **Boolean** | Whether or not the current user is allowed to post comments. | [optional] [readonly] 
**currentVersion** | **Number** | Version number of the file. | [optional] [readonly] 
**dateCreated** | **Date** | The time at which the file was created, as an iso8601 formatted timestamp. | [optional] [readonly] 
**dateModified** | **Date** | The time at which the file was last modified, as an iso8601 formatted timestamp. | [optional] [readonly] 
**deleteAllowed** | **Boolean** | Whether or not deletion of the file is allowed. | [optional] [readonly] 
**extra** | **Object** | Extra information, contains &#x60;hashes&#x60; (&#x60;sha256&#x60;, &#x60;md5&#x60;) and &#x60;downloads&#x60; count. | [optional] [readonly] 
**guid** | **String** | Global unique identifier (GUID) for this file (if one has been assigned). | [optional] [readonly] 
**kind** | **String** | The kind of files object it is (&#x60;file&#x60; or &#x60;folder&#x60;). | [optional] [readonly] 
**lastTouched** | **Date** | The time at which the file external metadata was last retrieved as an iso8601 formatted timestamp (does not apply to OSF Storage files). | [optional] [readonly] 
**materializedPath** | **String** | Unix-style path to the file relative to the provider root. | [optional] [readonly] 
**name** | **String** | Name of the file | [optional] 
**path** | **String** | The unique identifier for this file entity for this project and storage provider. | [optional] [readonly] 
**provider** | **String** | The id of the file provider (e.g., &#x60;osfstorage&#x60;) | [optional] [readonly] 
**size** | **Number** | Size of the file in bytes. | [optional] [readonly] 
**tags** | **[String]** | A list of strings that describe this file, as entered by project contributors. | [optional] [readonly] 


