

# ComplianceProperties

The Compliance score (percentage) of a Subscription is a sum of all Resources' Compliances under the given Subscription. A Resource Compliance is defined as the compliant ('healthy') Policy Definitions out of all Policy Definitions applicable to a given resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assessmentResult** | [**List&lt;ComplianceSegment&gt;**](ComplianceSegment.md) | An array of segment, which is the actually the compliance assessment. |  [optional] [readonly] |
|**assessmentTimestampUtcDate** | **OffsetDateTime** | The timestamp when the Compliance calculation was conducted. |  [optional] [readonly] |
|**resourceCount** | **Integer** | The resource count of the given subscription for which the Compliance calculation was conducted (needed for Management Group Compliance calculation). |  [optional] [readonly] |



