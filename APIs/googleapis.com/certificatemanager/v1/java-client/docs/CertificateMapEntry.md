

# CertificateMapEntry

Defines a certificate map entry.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certificates** | **List&lt;String&gt;** | A set of Certificates defines for the given &#x60;hostname&#x60;. There can be defined up to four certificates in each Certificate Map Entry. Each certificate must match pattern &#x60;projects/_*_/locations/_*_/certificates/_*&#x60;. |  [optional] |
|**createTime** | **String** | Output only. The creation timestamp of a Certificate Map Entry. |  [optional] [readonly] |
|**description** | **String** | One or more paragraphs of text description of a certificate map entry. |  [optional] |
|**hostname** | **String** | A Hostname (FQDN, e.g. &#x60;example.com&#x60;) or a wildcard hostname expression (&#x60;*.example.com&#x60;) for a set of hostnames with common suffix. Used as Server Name Indication (SNI) for selecting a proper certificate. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Set of labels associated with a Certificate Map Entry. |  [optional] |
|**matcher** | [**MatcherEnum**](#MatcherEnum) | A predefined matcher for particular cases, other than SNI selection. |  [optional] |
|**name** | **String** | A user-defined name of the Certificate Map Entry. Certificate Map Entry names must be unique globally and match pattern &#x60;projects/_*_/locations/_*_/certificateMaps/_*_/certificateMapEntries/_*&#x60;. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. A serving state of this Certificate Map Entry. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The update timestamp of a Certificate Map Entry. |  [optional] [readonly] |



## Enum: MatcherEnum

| Name | Value |
|---- | -----|
| MATCHER_UNSPECIFIED | &quot;MATCHER_UNSPECIFIED&quot; |
| PRIMARY | &quot;PRIMARY&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| SERVING_STATE_UNSPECIFIED | &quot;SERVING_STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| PENDING | &quot;PENDING&quot; |



