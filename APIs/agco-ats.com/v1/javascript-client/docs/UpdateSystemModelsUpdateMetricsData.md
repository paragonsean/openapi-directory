# AgcoApi.UpdateSystemModelsUpdateMetricsData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activeVersion** | **String** | Active version (bundle number) of update type. | [optional] 
**activeVersionByClient** | [**[UpdateSystemModelsUpdateMetricsDataActiveVersionByClientRecord]**](UpdateSystemModelsUpdateMetricsDataActiveVersionByClientRecord.md) | Generic collection that is of type ActiveVersionByClientRecord | [optional] 
**currentStateByClient** | [**[UpdateSystemModelsUpdateMetricsDataCurrentStateByClientRecord]**](UpdateSystemModelsUpdateMetricsDataCurrentStateByClientRecord.md) | Generic collection that is of type CurrentStateByClientRecord | [optional] 
**cutOffDate** | **Date** | Date that has been configured to only show the most recent clients with a cut off date. (Ex. year from current date) | [optional] 
**dataRefreshed** | **Date** | Data was refreshed at this time. | [optional] 
**filteredClientCount** | **Number** | Sum of clients represented              Filtered by updateType and lastCheckedInDate | [optional] 
**packageErrors** | [**[UpdateSystemModelsUpdateMetricsDataPackageErrorsRecord]**](UpdateSystemModelsUpdateMetricsDataPackageErrorsRecord.md) | Generic collection that is of type PackageErrorsRecord | [optional] 
**totalClientCount** | **Number** | Total clients we have ever serviced | [optional] 


