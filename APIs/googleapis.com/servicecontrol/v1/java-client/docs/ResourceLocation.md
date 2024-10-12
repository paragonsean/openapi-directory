

# ResourceLocation

Location information about a resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currentLocations** | **List&lt;String&gt;** | The locations of a resource after the execution of the operation. Requests to create or delete a location based resource must populate the &#39;current_locations&#39; field and not the &#39;original_locations&#39; field. For example: \&quot;europe-west1-a\&quot; \&quot;us-east1\&quot; \&quot;nam3\&quot; |  [optional] |
|**originalLocations** | **List&lt;String&gt;** | The locations of a resource prior to the execution of the operation. Requests that mutate the resource&#39;s location must populate both the &#39;original_locations&#39; as well as the &#39;current_locations&#39; fields. For example: \&quot;europe-west1-a\&quot; \&quot;us-east1\&quot; \&quot;nam3\&quot; |  [optional] |



