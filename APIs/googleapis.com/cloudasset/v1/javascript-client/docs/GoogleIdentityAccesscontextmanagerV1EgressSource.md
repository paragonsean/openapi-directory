# CloudAssetApi.GoogleIdentityAccesscontextmanagerV1EgressSource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessLevel** | **String** | An AccessLevel resource name that allows protected resources inside the ServicePerimeters to access outside the ServicePerimeter boundaries. AccessLevels listed must be in the same policy as this ServicePerimeter. Referencing a nonexistent AccessLevel will cause an error. If an AccessLevel name is not specified, only resources within the perimeter can be accessed through Google Cloud calls with request origins within the perimeter. Example: &#x60;accessPolicies/MY_POLICY/accessLevels/MY_LEVEL&#x60;. If a single &#x60;*&#x60; is specified for &#x60;access_level&#x60;, then all EgressSources will be allowed. | [optional] 


