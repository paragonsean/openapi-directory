

# RepresentativeInfoResponse

The result of a representative info lookup query.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**divisions** | [**Map&lt;String, GeographicDivision&gt;**](GeographicDivision.md) | A map of political geographic divisions that contain the requested address, keyed by the unique Open Civic Data identifier for this division. |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;civicinfo#representativeInfoResponse\&quot;. |  [optional] |
|**normalizedInput** | [**SimpleAddressType**](SimpleAddressType.md) |  |  [optional] |
|**offices** | [**List&lt;Office&gt;**](Office.md) | Elected offices referenced by the divisions listed above. Will only be present if includeOffices was true in the request. |  [optional] |
|**officials** | [**List&lt;Official&gt;**](Official.md) | Officials holding the offices listed above. Will only be present if includeOffices was true in the request. |  [optional] |



