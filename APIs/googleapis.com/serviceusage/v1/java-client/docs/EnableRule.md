

# EnableRule

The consumer policy rule that defines usable services and service groups.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enableType** | [**EnableTypeEnum**](#EnableTypeEnum) | Client and resource project enable type. |  [optional] |
|**groups** | **List&lt;String&gt;** | DEPRECATED: Please use field &#x60;values&#x60;. Service group should have prefix &#x60;groups/&#x60;. The names of the service groups that are enabled (Not Implemented). Example: &#x60;groups/googleServices&#x60;. |  [optional] |
|**services** | **List&lt;String&gt;** | DEPRECATED: Please use field &#x60;values&#x60;. Service should have prefix &#x60;services/&#x60;. The names of the services that are enabled. Example: &#x60;storage.googleapis.com&#x60;. |  [optional] |
|**values** | **List&lt;String&gt;** | The names of the services or service groups that are enabled. Example: &#x60;services/storage.googleapis.com&#x60;, &#x60;groups/googleServices&#x60;, &#x60;groups/allServices&#x60;. |  [optional] |



## Enum: EnableTypeEnum

| Name | Value |
|---- | -----|
| ENABLE_TYPE_UNSPECIFIED | &quot;ENABLE_TYPE_UNSPECIFIED&quot; |
| CLIENT | &quot;CLIENT&quot; |
| RESOURCE | &quot;RESOURCE&quot; |
| V1_COMPATIBLE | &quot;V1_COMPATIBLE&quot; |



