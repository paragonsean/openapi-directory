# CloudSpannerApi.KeyRange

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endClosed** | **[Object]** | If the end is closed, then the range includes all rows whose first &#x60;len(end_closed)&#x60; key columns exactly match &#x60;end_closed&#x60;. | [optional] 
**endOpen** | **[Object]** | If the end is open, then the range excludes rows whose first &#x60;len(end_open)&#x60; key columns exactly match &#x60;end_open&#x60;. | [optional] 
**startClosed** | **[Object]** | If the start is closed, then the range includes all rows whose first &#x60;len(start_closed)&#x60; key columns exactly match &#x60;start_closed&#x60;. | [optional] 
**startOpen** | **[Object]** | If the start is open, then the range excludes rows whose first &#x60;len(start_open)&#x60; key columns exactly match &#x60;start_open&#x60;. | [optional] 


