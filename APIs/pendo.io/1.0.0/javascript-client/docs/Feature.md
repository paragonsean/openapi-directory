# PendoFeedbackApi.Feature

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appUrl** | **String** | URL for this Feature | [optional] 
**createdAt** | **String** |  | [optional] 
**createdByUserId** | **Number** |  | [optional] 
**declinedAt** | **String** |  | [optional] 
**description** | **String** |  | [optional] 
**developingAt** | **String** |  | [optional] 
**effort** | **Number** | How much Effort is assigned to the development of this Feature. Not visible to EndUsers | [optional] 
**formEntry** | **String** | a JSON serialized version of the Form containing the description and other fields for this Feature. | [optional] 
**id** | **Number** |  | [optional] 
**isPrivate** | **Boolean** | Is this Feature hidden from EndUsers? | [optional] 
**mergedToFeatureId** | **Number** | If this Feature was merged into another, the ID of the preserved Feature | [optional] 
**plannedAt** | **String** |  | [optional] 
**products** | **[String]** |  | [optional] 
**releasedAt** | **String** |  | [optional] 
**resolution** | **String** | The latest Resolution set by the VendorUser | [optional] 
**resolvedByUserId** | **Number** |  | [optional] 
**status** | **String** |  | [optional] 
**statusChangedAt** | **String** |  | [optional] 
**tags** | **Object** | Tags can contain simple tags or categorised tags. Simple tags are supplied as an array of Strings Simple Tag Example: [&#39;Foo&#39;, &#39;Bar&#39;].  To put the tags in categories replace the Strings with maps of using tag category as the key and tag value as the value where value can be array of strings, e.g Categorised Tag Example: [ {&#39;Color&#39;:[&#39;Red&#39;, &#39;Yellow&#39;]},  {&#39;Flavor&#39;:[&#39;Cherry&#39;]} ]  Simple and categorised tags can be mixed in the same array. Below validations are done on the tag values of both simple and categorised tags: 1. Tag values must be strings 2. Tags must be at least 2 characters in length 3. Invalid characters (we dont accept following characters in tag value)  , | { } : &lt; &gt;  | [optional] 
**title** | **String** |  | [optional] 
**updatedAt** | **String** |  | [optional] 
**updatedByUserId** | **Number** |  | [optional] 
**uploads** | **[String]** |  | [optional] 
**vendorId** | **Number** |  | [optional] 
**viewCount** | **Number** | How many times has this Feature been viewed. May only be visible to VendorUsers, depending on config | [optional] 
**waitingAt** | **String** |  | [optional] 



## Enum: StatusEnum


* `new` (value: `"new"`)

* `waiting` (value: `"waiting"`)

* `planned` (value: `"planned"`)

* `developing` (value: `"developing"`)

* `released` (value: `"released"`)

* `declined` (value: `"declined"`)




