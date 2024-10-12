

# EntireDetectResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**expectedValues** | **List&lt;Float&gt;** | ExpectedValues contain expected value for each input point. The index of the array is consistent with the input series. |  |
|**isAnomaly** | **List&lt;Boolean&gt;** | IsAnomaly contains anomaly properties for each input point. True means an anomaly either negative or positive has been detected. The index of the array is consistent with the input series. |  |
|**isNegativeAnomaly** | **List&lt;Boolean&gt;** | IsNegativeAnomaly contains anomaly status in negative direction for each input point. True means a negative anomaly has been detected. A negative anomaly means the point is detected as an anomaly and its real value is smaller than the expected one. The index of the array is consistent with the input series. |  |
|**isPositiveAnomaly** | **List&lt;Boolean&gt;** | IsPositiveAnomaly contain anomaly status in positive direction for each input point. True means a positive anomaly has been detected. A positive anomaly means the point is detected as an anomaly and its real value is larger than the expected one. The index of the array is consistent with the input series. |  |
|**lowerMargins** | **List&lt;Float&gt;** | LowerMargins contain lower margin of each input point. LowerMargin is used to calculate lowerBoundary, which equals to expectedValue - (100 - sensitivity)*lowerMargin. Points between the boundary can be marked as normal ones in client side. The index of the array is consistent with the input series. |  |
|**period** | **Integer** | Frequency extracted from the series, zero means no recurrent pattern has been found. |  |
|**upperMargins** | **List&lt;Float&gt;** | UpperMargins contain upper margin of each input point. UpperMargin is used to calculate upperBoundary, which equals to expectedValue + (100 - sensitivity)*upperMargin. Anomalies in response can be filtered by upperBoundary and lowerBoundary. By adjusting sensitivity value, less significant anomalies can be filtered in client side. The index of the array is consistent with the input series. |  |



