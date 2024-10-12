

# QualificationType

 The QualificationType data structure represents a Qualification type, a description of a property of a Worker that must match the requirements of a HIT for the Worker to be able to accept the HIT. The type also describes how a Worker can obtain a Qualification of that type, such as through a Qualification test. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**qualificationTypeId** | [**String**](String.md) |  |  [optional] |
|**creationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**name** | [**String**](String.md) |  |  [optional] |
|**description** | [**String**](String.md) |  |  [optional] |
|**keywords** | [**String**](String.md) |  |  [optional] |
|**qualificationTypeStatus** | [**QualificationTypeStatus**](QualificationTypeStatus.md) |  |  [optional] |
|**test** | [**String**](String.md) |  |  [optional] |
|**testDurationInSeconds** | [**Integer**](Integer.md) |  |  [optional] |
|**answerKey** | [**String**](String.md) |  |  [optional] |
|**retryDelayInSeconds** | [**Integer**](Integer.md) |  |  [optional] |
|**isRequestable** | [**Boolean**](Boolean.md) |  |  [optional] |
|**autoGranted** | [**Boolean**](Boolean.md) |  |  [optional] |
|**autoGrantedValue** | [**Integer**](Integer.md) |  |  [optional] |



