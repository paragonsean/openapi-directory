

# HealthResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**checks** | **Map&lt;String, Map&lt;String, String&gt;&gt;** | The \&quot;checks\&quot; object MAY have a number of unique keys, one for each logical downstream dependency or sub-component.  Since each sub-component may be backed by several nodes with varying health statuses, these keys point to arrays of objects. In case of a single-node sub-component (or if presence of nodes is not relevant), a single-element array SHOULD be used as the value, for consistency.  Please see https://tools.ietf.org/id/draft-inadarei-api-health-check-04.html#the-checks-object for details. |  [optional] |
|**description** | **String** | A human-friendly description of the service. |  [optional] |
|**links** | **Map&lt;String, String&gt;** | Is an object containing link relations and URIs [RFC3986] for external links that MAY contain more information about the health of the endpoint. |  [optional] |
|**notes** | **List&lt;String&gt;** | Array of notes relevant to current state of health. |  [optional] |
|**output** | **String** | Raw error output, in case of \&quot;fail\&quot; or \&quot;warn\&quot; states. |  [optional] |
|**releaseId** | **String** | Release version of the api implementation.  |  [optional] |
|**serviceId** | **String** | A unique identifier of the service, in the application scope. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | status indicates whether the service status is acceptable or not. |  |
|**version** | **String** | Public version of the service.  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PASS | &quot;pass&quot; |
| FAIL | &quot;fail&quot; |
| WARN | &quot;warn&quot; |



