

# GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfig

`ServicePerimeterConfig` specifies a set of Google Cloud resources that describe specific Service Perimeter configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessLevels** | **List&lt;String&gt;** | A list of &#x60;AccessLevel&#x60; resource names that allow resources within the &#x60;ServicePerimeter&#x60; to be accessed from the internet. &#x60;AccessLevels&#x60; listed must be in the same policy as this &#x60;ServicePerimeter&#x60;. Referencing a nonexistent &#x60;AccessLevel&#x60; is a syntax error. If no &#x60;AccessLevel&#x60; names are listed, resources within the perimeter can only be accessed via Google Cloud calls with request origins within the perimeter. Example: &#x60;\&quot;accessPolicies/MY_POLICY/accessLevels/MY_LEVEL\&quot;&#x60;. For Service Perimeter Bridge, must be empty. |  [optional] |
|**egressPolicies** | [**List&lt;GoogleIdentityAccesscontextmanagerV1EgressPolicy&gt;**](GoogleIdentityAccesscontextmanagerV1EgressPolicy.md) | List of EgressPolicies to apply to the perimeter. A perimeter may have multiple EgressPolicies, each of which is evaluated separately. Access is granted if any EgressPolicy grants it. Must be empty for a perimeter bridge. |  [optional] |
|**ingressPolicies** | [**List&lt;GoogleIdentityAccesscontextmanagerV1IngressPolicy&gt;**](GoogleIdentityAccesscontextmanagerV1IngressPolicy.md) | List of IngressPolicies to apply to the perimeter. A perimeter may have multiple IngressPolicies, each of which is evaluated separately. Access is granted if any Ingress Policy grants it. Must be empty for a perimeter bridge. |  [optional] |
|**resources** | **List&lt;String&gt;** | A list of Google Cloud resources that are inside of the service perimeter. Currently only projects and VPCs are allowed. Project format: &#x60;projects/{project_number}&#x60; VPC network format: &#x60;//compute.googleapis.com/projects/{PROJECT_ID}/global/networks/{NAME}&#x60;. |  [optional] |
|**restrictedServices** | **List&lt;String&gt;** | Google Cloud services that are subject to the Service Perimeter restrictions. For example, if &#x60;storage.googleapis.com&#x60; is specified, access to the storage buckets inside the perimeter must meet the perimeter&#39;s access restrictions. |  [optional] |
|**vpcAccessibleServices** | [**GoogleIdentityAccesscontextmanagerV1VpcAccessibleServices**](GoogleIdentityAccesscontextmanagerV1VpcAccessibleServices.md) |  |  [optional] |



