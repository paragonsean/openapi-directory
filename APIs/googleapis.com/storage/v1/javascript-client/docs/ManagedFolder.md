# CloudStorageJsonApi.ManagedFolder

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **String** | The name of the bucket containing this managed folder. | [optional] 
**createTime** | **Date** | The creation time of the managed folder in RFC 3339 format. | [optional] 
**id** | **String** | The ID of the managed folder, including the bucket name and managed folder name. | [optional] 
**kind** | **String** | The kind of item this is. For managed folders, this is always storage#managedFolder. | [optional] [default to &#39;storage#managedFolder&#39;]
**metageneration** | **String** | The version of the metadata for this managed folder. Used for preconditions and for detecting changes in metadata. | [optional] 
**name** | **String** | The name of the managed folder. Required if not specified by URL parameter. | [optional] 
**selfLink** | **String** | The link to this managed folder. | [optional] 
**updateTime** | **Date** | The last update time of the managed folder metadata in RFC 3339 format. | [optional] 


