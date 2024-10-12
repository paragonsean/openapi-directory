# LinodeApi.ObjectStorageObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**etag** | **String** | An MD-5 hash of the object. &#x60;null&#x60; if this object represents a prefix.  | [optional] 
**isTruncated** | **Boolean** | Designates if there is another page of bucket objects. | [optional] 
**lastModified** | **Date** | The date and time this object was last modified. &#x60;null&#x60; if this object represents a prefix.  | [optional] 
**name** | **String** | The name of this object or prefix.  | [optional] 
**nextMarker** | **String** | Returns the value you should pass to the &#x60;marker&#x60; query parameter to get the next page of objects. If there is no next page, &#x60;null&#x60; will be returned.  | [optional] 
**owner** | **String** | The owner of this object, as a UUID. &#x60;null&#x60; if this object represents a prefix.  | [optional] 
**size** | **Number** | The size of this object, in bytes. &#x60;null&#x60; if this object represents a prefix.  | [optional] 


