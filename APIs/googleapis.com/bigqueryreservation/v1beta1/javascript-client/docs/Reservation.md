# BigQueryReservationApi.Reservation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**concurrency** | **String** | Job concurrency target which sets a soft upper bound on the number of jobs that can run concurrently in this reservation. This is a soft target due to asynchronous nature of the system and various optimizations for small queries. Default value is 0 which means that concurrency target will be automatically computed by the system. NOTE: this field is exposed as &#x60;target_job_concurrency&#x60; in the Information Schema, DDL and BQ CLI. | [optional] 
**creationTime** | **String** | Output only. Creation time of the reservation. | [optional] [readonly] 
**ignoreIdleSlots** | **Boolean** | If false, any query or pipeline job using this reservation will use idle slots from other reservations within the same admin project. If true, a query or pipeline job using this reservation will execute with the slot capacity specified in the slot_capacity field at most. | [optional] 
**multiRegionAuxiliary** | **Boolean** | Applicable only for reservations located within one of the BigQuery multi-regions (US or EU). If set to true, this reservation is placed in the organization&#39;s secondary region which is designated for disaster recovery purposes. If false, this reservation is placed in the organization&#39;s default region. | [optional] 
**name** | **String** | The resource name of the reservation, e.g., &#x60;projects/_*_/locations/_*_/reservations/team1-prod&#x60;. The reservation_id must only contain lower case alphanumeric characters or dashes. It must start with a letter and must not end with a dash. Its maximum length is 64 characters. | [optional] 
**slotCapacity** | **String** | Minimum slots available to this reservation. A slot is a unit of computational power in BigQuery, and serves as the unit of parallelism. Queries using this reservation might use more slots during runtime if ignore_idle_slots is set to false. If the new reservation&#39;s slot capacity exceeds the project&#39;s slot capacity or if total slot capacity of the new reservation and its siblings exceeds the project&#39;s slot capacity, the request will fail with &#x60;google.rpc.Code.RESOURCE_EXHAUSTED&#x60;. NOTE: for reservations in US or EU multi-regions, slot capacity constraints are checked separately for default and auxiliary regions. See multi_region_auxiliary flag for more details. | [optional] 
**updateTime** | **String** | Output only. Last update time of the reservation. | [optional] [readonly] 


