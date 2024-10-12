

# ServiceMetadata

Metadata describing the service and additional service specific information used to identify the job or unit of work at hand.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**jobMetadata** | **Map&lt;String, Object&gt;** | Additional metadata provided by service teams to describe service specific job information that was triggered by the original principal. |  [optional] |
|**principalSubject** | **String** | A string representing the principal_subject associated with the identity. For most identities, the format will be &#x60;principal://iam.googleapis.com/{identity pool name}/subject/{subject)&#x60; except for some GKE identities (GKE_WORKLOAD, FREEFORM, GKE_HUB_WORKLOAD) that are still in the legacy format &#x60;serviceAccount:{identity pool name}[{subject}]&#x60; If the identity is a Google account (e.g. workspace user account or service account), this will be the email of the prefixed by &#x60;serviceAccount:&#x60;. For example: &#x60;serviceAccount:my-service-account@project-1.iam.gserviceaccount.com&#x60;. If the identity is an individual user, the identity will be formatted as: &#x60;user:user_ABC@email.com&#x60;. |  [optional] |
|**serviceDomain** | **String** | The service&#39;s fully qualified domain name, e.g. \&quot;dataproc.googleapis.com\&quot;. |  [optional] |



