# AnomalyFinderClient.EntireDetectResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expectedValues** | **[Number]** | ExpectedValues contain expected value for each input point. The index of the array is consistent with the input series. | 
**isAnomaly** | **[Boolean]** | IsAnomaly contains anomaly properties for each input point. True means an anomaly either negative or positive has been detected. The index of the array is consistent with the input series. | 
**isNegativeAnomaly** | **[Boolean]** | IsNegativeAnomaly contains anomaly status in negative direction for each input point. True means a negative anomaly has been detected. A negative anomaly means the point is detected as an anomaly and its real value is smaller than the expected one. The index of the array is consistent with the input series. | 
**isPositiveAnomaly** | **[Boolean]** | IsPositiveAnomaly contain anomaly status in positive direction for each input point. True means a positive anomaly has been detected. A positive anomaly means the point is detected as an anomaly and its real value is larger than the expected one. The index of the array is consistent with the input series. | 
**lowerMargins** | **[Number]** | LowerMargins contain lower margin of each input point. LowerMargin is used to calculate lowerBoundary, which equals to expectedValue - (100 - sensitivity)*lowerMargin. Points between the boundary can be marked as normal ones in client side. The index of the array is consistent with the input series. | 
**period** | **Number** | Frequency extracted from the series, zero means no recurrent pattern has been found. | 
**upperMargins** | **[Number]** | UpperMargins contain upper margin of each input point. UpperMargin is used to calculate upperBoundary, which equals to expectedValue + (100 - sensitivity)*upperMargin. Anomalies in response can be filtered by upperBoundary and lowerBoundary. By adjusting sensitivity value, less significant anomalies can be filtered in client side. The index of the array is consistent with the input series. | 


