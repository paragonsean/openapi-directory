

# AppUpdateEvent

An event generated when a new version of an app is uploaded to Google Play. Notifications are sent for new public versions only: alpha, beta, or canary versions do not generate this event. To fetch up-to-date version history for an app, use Products.Get on the EMM API.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**productId** | **String** | The id of the product (e.g. \&quot;app:com.google.android.gm\&quot;) that was updated. This field will always be present. |  [optional] |



