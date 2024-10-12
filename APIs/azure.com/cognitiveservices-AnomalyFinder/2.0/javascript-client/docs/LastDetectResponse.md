# AnomalyFinderClient.LastDetectResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expectedValue** | **Number** | Expected value of the latest point. | [optional] 
**isAnomaly** | **Boolean** | Anomaly status of the latest point, true means the latest point is an anomaly either in negative direction or positive direction. | [optional] 
**isNegativeAnomaly** | **Boolean** | Anomaly status in negative direction of the latest point. True means the latest point is an anomaly and its real value is smaller than the expected one. | [optional] 
**isPositiveAnomaly** | **Boolean** | Anomaly status in positive direction of the latest point. True means the latest point is an anomaly and its real value is larger than the expected one. | [optional] 
**lowerMargin** | **Number** | Lower margin of the latest point. LowerMargin is used to calculate lowerBoundary, which equals to expectedValue - (100 - sensitivity)*lowerMargin.  | [optional] 
**period** | **Number** | Frequency extracted from the series, zero means no recurrent pattern has been found. | [optional] 
**suggestedWindow** | **Number** | Suggested input series points needed for detecting the latest point. | [optional] 
**upperMargin** | **Number** | Upper margin of the latest point. UpperMargin is used to calculate upperBoundary, which equals to expectedValue + (100 - sensitivity)*upperMargin. If the value of latest point is between upperBoundary and lowerBoundary, it should be treated as normal value. By adjusting sensitivity value, anomaly status of latest point can be changed. | [optional] 


