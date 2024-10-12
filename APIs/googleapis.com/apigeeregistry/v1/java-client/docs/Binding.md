

# Binding

Associates `members`, or principals, with a `role`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**condition** | [**Expr**](Expr.md) |  |  [optional] |
|**members** | **List&lt;String&gt;** | Specifies the principals requesting access for a Google Cloud resource. &#x60;members&#x60; can have the following values: * &#x60;allUsers&#x60;: A special identifier that represents anyone who is on the internet; with or without a Google account. * &#x60;allAuthenticatedUsers&#x60;: A special identifier that represents anyone who is authenticated with a Google account or a service account. Does not include identities that come from external identity providers (IdPs) through identity federation. * &#x60;user:{emailid}&#x60;: An email address that represents a specific Google account. For example, &#x60;alice@example.com&#x60; . * &#x60;serviceAccount:{emailid}&#x60;: An email address that represents a Google service account. For example, &#x60;my-other-app@appspot.gserviceaccount.com&#x60;. * &#x60;serviceAccount:{projectid}.svc.id.goog[{namespace}/{kubernetes-sa}]&#x60;: An identifier for a [Kubernetes service account](https://cloud.google.com/kubernetes-engine/docs/how-to/kubernetes-service-accounts). For example, &#x60;my-project.svc.id.goog[my-namespace/my-kubernetes-sa]&#x60;. * &#x60;group:{emailid}&#x60;: An email address that represents a Google group. For example, &#x60;admins@example.com&#x60;. * &#x60;domain:{domain}&#x60;: The G Suite domain (primary) that represents all the users of that domain. For example, &#x60;google.com&#x60; or &#x60;example.com&#x60;. * &#x60;deleted:user:{emailid}?uid&#x3D;{uniqueid}&#x60;: An email address (plus unique identifier) representing a user that has been recently deleted. For example, &#x60;alice@example.com?uid&#x3D;123456789012345678901&#x60;. If the user is recovered, this value reverts to &#x60;user:{emailid}&#x60; and the recovered user retains the role in the binding. * &#x60;deleted:serviceAccount:{emailid}?uid&#x3D;{uniqueid}&#x60;: An email address (plus unique identifier) representing a service account that has been recently deleted. For example, &#x60;my-other-app@appspot.gserviceaccount.com?uid&#x3D;123456789012345678901&#x60;. If the service account is undeleted, this value reverts to &#x60;serviceAccount:{emailid}&#x60; and the undeleted service account retains the role in the binding. * &#x60;deleted:group:{emailid}?uid&#x3D;{uniqueid}&#x60;: An email address (plus unique identifier) representing a Google group that has been recently deleted. For example, &#x60;admins@example.com?uid&#x3D;123456789012345678901&#x60;. If the group is recovered, this value reverts to &#x60;group:{emailid}&#x60; and the recovered group retains the role in the binding. |  [optional] |
|**role** | **String** | Role that is assigned to the list of &#x60;members&#x60;, or principals. For example, &#x60;roles/viewer&#x60;, &#x60;roles/editor&#x60;, or &#x60;roles/owner&#x60;. |  [optional] |



