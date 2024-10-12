# PendoFeedbackApi.EndUserPingUser

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowedProducts** | **[String]** | Supplied as an array of maps where each map describes an existing or new product e.g [{id:exising_product_id, name:existing name}, {id:new_product_id, name: new product name}].  Existing product id/names held in your account can be referenced at https://feedback.pendo.io/app/#/vendor/products | [optional] 
**createdAt** | **String** |  | [optional] 
**email** | **String** |  | [optional] 
**fullName** | **String** |  | [optional] 
**id** | **String** |  | [optional] 
**roles** | **String** |  | [optional] 
**tags** | **Object** | Tags can contain simple tags or categorised tags. Simple tags are supplied as an array of Strings Simple Tag Example: [&#39;Foo&#39;, &#39;Bar&#39;].  To put the tags in categories replace the Strings with maps of using tag category as the key and tag value as the value where value can be array of strings, e.g Categorised Tag Example: [ {&#39;Color&#39;:[&#39;Red&#39;, &#39;Yellow&#39;]},  {&#39;Flavor&#39;:[&#39;Cherry&#39;]} ]  Simple and categorised tags can be mixed in the same array. Below validations are done on the tag values of both simple and categorised tags: 1. Tag values must be strings 2. Tags must be at least 2 characters in length 3. Invalid characters (we dont accept following characters in tag value)  , | { } : &lt; &gt;  | [optional] 



## Enum: RolesEnum


* `endUser` (value: `"endUser"`)




