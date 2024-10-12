# BackupForGkeApi.ResourceFilter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groupKinds** | [**[GroupKind]**](GroupKind.md) | Optional. (Filtering parameter) Any resource subject to transformation must belong to one of the listed \&quot;types\&quot;. If this field is not provided, no type filtering will be performed (all resources of all types matching previous filtering parameters will be candidates for transformation). | [optional] 
**jsonPath** | **String** | Optional. This is a [JSONPath] (https://github.com/json-path/JsonPath/blob/master/README.md) expression that matches specific fields of candidate resources and it operates as a filtering parameter (resources that are not matched with this expression will not be candidates for transformation). | [optional] 
**namespaces** | **[String]** | Optional. (Filtering parameter) Any resource subject to transformation must be contained within one of the listed Kubernetes Namespace in the Backup. If this field is not provided, no namespace filtering will be performed (all resources in all Namespaces, including all cluster-scoped resources, will be candidates for transformation). | [optional] 


