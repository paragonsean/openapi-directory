# ChromeUxReportApi.TimeseriesBin

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**densities** | **[Number]** | The proportion of users that experienced this bin&#39;s value for the given metric in a given collection period; the index for each of these entries corresponds to an entry in the CollectionPeriods field in the HistoryRecord message, which describes when the density was observed in the field. Thus, the length of this list of densities is equal to the length of the CollectionPeriods field in the HistoryRecord message. | [optional] 
**end** | **Object** | End is the end of the data bin. If end is not populated, then the bin has no end and is valid from start to +inf. | [optional] 
**start** | **Object** | Start is the beginning of the data bin. | [optional] 


