

# GrpcRouteFaultInjectionPolicy

The specification for fault injection introduced into traffic to test the resiliency of clients to destination service failure. As part of fault injection, when clients send requests to a destination, delays can be introduced on a percentage of requests before sending those requests to the destination service. Similarly requests from clients can be aborted by for a percentage of requests.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**abort** | [**GrpcRouteFaultInjectionPolicyAbort**](GrpcRouteFaultInjectionPolicyAbort.md) |  |  [optional] |
|**delay** | [**GrpcRouteFaultInjectionPolicyDelay**](GrpcRouteFaultInjectionPolicyDelay.md) |  |  [optional] |



