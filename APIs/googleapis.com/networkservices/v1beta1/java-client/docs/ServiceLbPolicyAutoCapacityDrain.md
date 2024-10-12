

# ServiceLbPolicyAutoCapacityDrain

Option to specify if an unhealthy IG/NEG should be considered for global load balancing and traffic routing.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enable** | **Boolean** | Optional. If set to &#39;True&#39;, an unhealthy IG/NEG will be set as drained. - An IG/NEG is considered unhealthy if less than 25% of the instances/endpoints in the IG/NEG are healthy. - This option will never result in draining more than 50% of the configured IGs/NEGs for the Backend Service. |  [optional] |



