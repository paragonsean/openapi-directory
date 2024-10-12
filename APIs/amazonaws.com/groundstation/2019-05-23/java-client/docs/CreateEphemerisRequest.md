

# CreateEphemerisRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** | &lt;p&gt;Whether to set the ephemeris status to &lt;code&gt;ENABLED&lt;/code&gt; after validation.&lt;/p&gt; &lt;p&gt;Setting this to false will set the ephemeris status to &lt;code&gt;DISABLED&lt;/code&gt; after validation.&lt;/p&gt; |  [optional] |
|**ephemeris** | [**CreateEphemerisRequestEphemeris**](CreateEphemerisRequestEphemeris.md) |  |  [optional] |
|**expirationTime** | **OffsetDateTime** | An overall expiration time for the ephemeris in UTC, after which it will become &lt;code&gt;EXPIRED&lt;/code&gt;. |  [optional] |
|**kmsKeyArn** | **String** | The ARN of a KMS key used to encrypt the ephemeris in Ground Station. |  [optional] |
|**name** | **String** | A name string associated with the ephemeris. Used as a human-readable identifier for the ephemeris. |  |
|**priority** | **Integer** | &lt;p&gt;Customer-provided priority score to establish the order in which overlapping ephemerides should be used.&lt;/p&gt; &lt;p&gt;The default for customer-provided ephemeris priority is 1, and higher numbers take precedence.&lt;/p&gt; &lt;p&gt;Priority must be 1 or greater&lt;/p&gt; |  [optional] |
|**satelliteId** | **String** | AWS Ground Station satellite ID for this ephemeris. |  |
|**tags** | **Map&lt;String, String&gt;** | Tags assigned to an ephemeris. |  [optional] |



