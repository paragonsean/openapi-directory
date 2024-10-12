

# PeriodicPaymentInitiationXmlPart2StandingorderTypeJson

The body part 2 of a periodic payment initation request containes the execution related informations of the periodic payment. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dayOfExecution** | **DayOfExecution** |  |  [optional] |
|**endDate** | **LocalDate** | The last applicable day of execution. If not given, it is an infinite standing order.  |  [optional] |
|**executionRule** | **ExecutionRule** |  |  [optional] |
|**frequency** | **FrequencyCode** |  |  |
|**startDate** | **LocalDate** | The first applicable day of execution starting from this date is the first payment.  |  |



