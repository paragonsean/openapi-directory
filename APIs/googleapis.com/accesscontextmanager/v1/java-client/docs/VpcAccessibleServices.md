

# VpcAccessibleServices

Specifies how APIs are allowed to communicate within the Service Perimeter.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedServices** | **List&lt;String&gt;** | The list of APIs usable within the Service Perimeter. Must be empty unless &#39;enable_restriction&#39; is True. You can specify a list of individual services, as well as include the &#39;RESTRICTED-SERVICES&#39; value, which automatically includes all of the services protected by the perimeter. |  [optional] |
|**enableRestriction** | **Boolean** | Whether to restrict API calls within the Service Perimeter to the list of APIs specified in &#39;allowed_services&#39;. |  [optional] |



