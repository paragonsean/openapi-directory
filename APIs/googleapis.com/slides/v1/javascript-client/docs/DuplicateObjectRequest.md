# GoogleSlidesApi.DuplicateObjectRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objectId** | **String** | The ID of the object to duplicate. | [optional] 
**objectIds** | **{String: String}** | The object being duplicated may contain other objects, for example when duplicating a slide or a group page element. This map defines how the IDs of duplicated objects are generated: the keys are the IDs of the original objects and its values are the IDs that will be assigned to the corresponding duplicate object. The ID of the source object&#39;s duplicate may be specified in this map as well, using the same value of the &#x60;object_id&#x60; field as a key and the newly desired ID as the value. All keys must correspond to existing IDs in the presentation. All values must be unique in the presentation and must start with an alphanumeric character or an underscore (matches regex &#x60;[a-zA-Z0-9_]&#x60;); remaining characters may include those as well as a hyphen or colon (matches regex &#x60;[a-zA-Z0-9_-:]&#x60;). The length of the new ID must not be less than 5 or greater than 50. If any IDs of source objects are omitted from the map, a new random ID will be assigned. If the map is empty or unset, all duplicate objects will receive a new random ID. | [optional] 


