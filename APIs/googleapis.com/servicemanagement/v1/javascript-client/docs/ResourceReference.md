# ServiceManagementApi.ResourceReference

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**childType** | **String** | The resource type of a child collection that the annotated field references. This is useful for annotating the &#x60;parent&#x60; field that doesn&#39;t have a fixed resource type. Example: message ListLogEntriesRequest { string parent &#x3D; 1 [(google.api.resource_reference) &#x3D; { child_type: \&quot;logging.googleapis.com/LogEntry\&quot; }; } | [optional] 
**type** | **String** | The resource type that the annotated field references. Example: message Subscription { string topic &#x3D; 2 [(google.api.resource_reference) &#x3D; { type: \&quot;pubsub.googleapis.com/Topic\&quot; }]; } Occasionally, a field may reference an arbitrary resource. In this case, APIs use the special value * in their resource reference. Example: message GetIamPolicyRequest { string resource &#x3D; 2 [(google.api.resource_reference) &#x3D; { type: \&quot;*\&quot; }]; } | [optional] 


