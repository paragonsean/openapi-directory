

# MethodPolicy

Defines policies applying to an RPC method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**requestPolicies** | [**List&lt;FieldPolicy&gt;**](FieldPolicy.md) | Policies that are applicable to the request message. |  [optional] |
|**selector** | **String** | Selects a method to which these policies should be enforced, for example, \&quot;google.pubsub.v1.Subscriber.CreateSubscription\&quot;. Refer to selector for syntax details. NOTE: This field must not be set in the proto annotation. It will be automatically filled by the service config compiler . |  [optional] |



