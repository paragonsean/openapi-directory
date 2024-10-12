

# GoogleCloudApigeeV1PodStatus


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appVersion** | **String** | Version of the application running in the pod. |  [optional] |
|**deploymentStatus** | **String** | Status of the deployment. Valid values include: - &#x60;deployed&#x60;: Successful. - &#x60;error&#x60; : Failed. - &#x60;pending&#x60; : Pod has not yet reported on the deployment. |  [optional] |
|**deploymentStatusTime** | **String** | Time the deployment status was reported in milliseconds since epoch. |  [optional] |
|**deploymentTime** | **String** | Time the proxy was deployed in milliseconds since epoch. |  [optional] |
|**podName** | **String** | Name of the pod which is reporting the status. |  [optional] |
|**podStatus** | **String** | Overall status of the pod (not this specific deployment). Valid values include: - &#x60;active&#x60;: Up to date. - &#x60;stale&#x60; : Recently out of date. Pods that have not reported status in a long time are excluded from the output. |  [optional] |
|**podStatusTime** | **String** | Time the pod status was reported in milliseconds since epoch. |  [optional] |
|**statusCode** | **String** | Code associated with the deployment status. |  [optional] |
|**statusCodeDetails** | **String** | Human-readable message associated with the status code. |  [optional] |



