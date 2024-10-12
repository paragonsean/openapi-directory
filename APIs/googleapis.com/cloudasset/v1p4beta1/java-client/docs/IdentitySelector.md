

# IdentitySelector

Specifies an identity for which to determine resource access, based on roles assigned either directly to them or to the groups they belong to, directly or indirectly.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**identity** | **String** | Required. The identity appear in the form of members in [IAM policy binding](https://cloud.google.com/iam/reference/rest/v1/Binding). The examples of supported forms are: \&quot;user:mike@example.com\&quot;, \&quot;group:admins@example.com\&quot;, \&quot;domain:google.com\&quot;, \&quot;serviceAccount:my-project-id@appspot.gserviceaccount.com\&quot;. Notice that wildcard characters (such as * and ?) are not supported. You must give a specific identity. |  [optional] |



