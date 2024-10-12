

# IPAssessmentOutput


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowlisted** | **String** |  |  |
|**asn** | **String** |  |  |
|**asnPrefix** | **String** |  |  |
|**datacenter** | **String** |  |  |
|**datacenterPrefix** | **String** |  |  |
|**datasets** | **List&lt;String&gt;** |  |  |
|**denylisted** | **String** |  |  |
|**firstAppearance** | **List&lt;String&gt;** |  |  |
|**lastAppearance** | **List&lt;String&gt;** |  |  |
|**reason** | **String** |  |  |
|**risk** | [**RiskEnum**](#RiskEnum) |  |  |
|**score** | **Integer** |  |  [optional] |
|**self** | **String** |  |  [optional] |
|**sources** | **List&lt;String&gt;** |  |  |



## Enum: RiskEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| LOW | &quot;LOW&quot; |
| MEDIUM | &quot;MEDIUM&quot; |
| HIGH | &quot;HIGH&quot; |



