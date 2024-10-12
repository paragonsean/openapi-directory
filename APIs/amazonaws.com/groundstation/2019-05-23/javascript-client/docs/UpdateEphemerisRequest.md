# AwsGroundStation.UpdateEphemerisRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **Boolean** | Whether the ephemeris is enabled or not. Changing this value will not require the ephemeris to be re-validated. | 
**name** | **String** | A name string associated with the ephemeris. Used as a human-readable identifier for the ephemeris. | [optional] 
**priority** | **Number** | &lt;p&gt;Customer-provided priority score to establish the order in which overlapping ephemerides should be used.&lt;/p&gt; &lt;p&gt;The default for customer-provided ephemeris priority is 1, and higher numbers take precedence.&lt;/p&gt; &lt;p&gt;Priority must be 1 or greater&lt;/p&gt; | [optional] 


