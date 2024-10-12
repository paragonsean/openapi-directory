

# PatientDiscoveryRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**patient** | [**PatientDiscoveryRequestPatient**](PatientDiscoveryRequestPatient.md) |  |  |
|**requestId** | **UUID** | a nonce, unique for each HTTP request. |  |
|**timestamp** | **OffsetDateTime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ |  |
|**transactionId** | **UUID** | correlation-Id for patient discovery and subsequent care context linkage |  |



