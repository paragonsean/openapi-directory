

# AppleTestFlightGroupRequest

Apple details for fetching test flight groups from Apple Developer Portal. pass either apple_id or bundle_identifier to get the test flight groups. if both are passed than apple_id will take preference

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appleId** | **String** | apple_id of the app for which test flight groups need to be fetched. |  [optional] |
|**bundleIdentifier** | **String** | apple_id of the app for which test flight groups need to be fetched. |  [optional] |
|**cookie** | **String** | The 30-day session cookie for multi-factor authentication backed accounts. |  [optional] |
|**password** | **String** | The password for the Apple Developer account. |  [optional] |
|**serviceConnectionId** | **String** | The service_connection_id of the stored Apple credentials instead of username, password. |  [optional] |
|**teamIdentifier** | **String** | Identifier of the team to use when logged in. |  [optional] |
|**username** | **String** | The username for the Apple Developer account. |  [optional] |



