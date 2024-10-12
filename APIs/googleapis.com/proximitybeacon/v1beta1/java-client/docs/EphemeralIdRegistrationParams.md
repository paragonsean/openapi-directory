

# EphemeralIdRegistrationParams

Information a client needs to provision and register beacons that broadcast Eddystone-EID format beacon IDs, using Elliptic curve Diffie-Hellman key exchange. See [the Eddystone specification](https://github.com/google/eddystone/tree/master/eddystone-eid) at GitHub.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxRotationPeriodExponent** | **Integer** | Indicates the maximum rotation period supported by the service. See EddystoneEidRegistration.rotation_period_exponent |  [optional] |
|**minRotationPeriodExponent** | **Integer** | Indicates the minimum rotation period supported by the service. See EddystoneEidRegistration.rotation_period_exponent |  [optional] |
|**serviceEcdhPublicKey** | **byte[]** | The beacon service&#39;s public key for use by a beacon to derive its Identity Key using Elliptic Curve Diffie-Hellman key exchange. |  [optional] |



