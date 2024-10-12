# ServiceUsageApi.FieldPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resourcePermission** | **String** | Specifies the required permission(s) for the resource referred to by the field. It requires the field contains a valid resource reference, and the request must pass the permission checks to proceed. For example, \&quot;resourcemanager.projects.get\&quot;. | [optional] 
**resourceType** | **String** | Specifies the resource type for the resource referred to by the field. | [optional] 
**selector** | **String** | Selects one or more request or response message fields to apply this &#x60;FieldPolicy&#x60;. When a &#x60;FieldPolicy&#x60; is used in proto annotation, the selector must be left as empty. The service config generator will automatically fill the correct value. When a &#x60;FieldPolicy&#x60; is used in service config, the selector must be a comma-separated string with valid request or response field paths, such as \&quot;foo.bar\&quot; or \&quot;foo.bar,foo.baz\&quot;. | [optional] 


