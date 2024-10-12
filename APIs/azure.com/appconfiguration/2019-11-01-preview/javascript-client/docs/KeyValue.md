# AppConfigurationManagementClient.KeyValue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contentType** | **String** | The content type of the key-value&#39;s value.  Providing a proper content-type can enable transformations of values when they are retrieved by applications. | [optional] [readonly] 
**eTag** | **String** | An ETag indicating the state of a key-value within a configuration store. | [optional] [readonly] 
**key** | **String** | The primary identifier of a key-value.  The key is used in unison with the label to uniquely identify a key-value. | [optional] [readonly] 
**label** | **String** | A value used to group key-values.  The label is used in unison with the key to uniquely identify a key-value. | [optional] [readonly] 
**lastModified** | **Date** | The last time a modifying operation was performed on the given key-value. | [optional] [readonly] 
**locked** | **Boolean** | A value indicating whether the key-value is locked.  A locked key-value may not be modified until it is unlocked. | [optional] [readonly] 
**tags** | **{String: String}** | A dictionary of tags that can help identify what a key-value may be applicable for. | [optional] [readonly] 
**value** | **String** | The value of the key-value. | [optional] [readonly] 


