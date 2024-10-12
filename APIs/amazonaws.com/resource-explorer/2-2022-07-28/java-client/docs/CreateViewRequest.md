

# CreateViewRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientToken** | **String** | This value helps ensure idempotency. Resource Explorer uses this value to prevent the accidental creation of duplicate versions. We recommend that you generate a &lt;a href&#x3D;\&quot;https://wikipedia.org/wiki/Universally_unique_identifier\&quot;&gt;UUID-type value&lt;/a&gt; to ensure the uniqueness of your views. |  [optional] |
|**filters** | [**CreateViewRequestFilters**](CreateViewRequestFilters.md) |  |  [optional] |
|**includedProperties** | [**List&lt;IncludedProperty&gt;**](IncludedProperty.md) | &lt;p&gt;Specifies optional fields that you want included in search results from this view. It is a list of objects that each describe a field to include.&lt;/p&gt; &lt;p&gt;The default is an empty list, with no optional fields included in the results.&lt;/p&gt; |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | Tag key and value pairs that are attached to the view. |  [optional] |
|**viewName** | **String** | &lt;p&gt;The name of the new view. This name appears in the list of views in Resource Explorer.&lt;/p&gt; &lt;p&gt;The name must be no more than 64 characters long, and can include letters, digits, and the dash (-) character. The name must be unique within its Amazon Web Services Region.&lt;/p&gt; |  |



