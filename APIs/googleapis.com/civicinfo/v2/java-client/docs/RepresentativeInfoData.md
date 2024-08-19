

# RepresentativeInfoData


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**divisions** | [**Map&lt;String, GeographicDivision&gt;**](GeographicDivision.md) | A map of political geographic divisions that contain the requested address, keyed by the unique Open Civic Data identifier for this division. |  [optional] |
|**offices** | [**List&lt;Office&gt;**](Office.md) | Elected offices referenced by the divisions listed above. Will only be present if includeOffices was true in the request. |  [optional] |
|**officials** | [**List&lt;Official&gt;**](Official.md) | Officials holding the offices listed above. Will only be present if includeOffices was true in the request. |  [optional] |



