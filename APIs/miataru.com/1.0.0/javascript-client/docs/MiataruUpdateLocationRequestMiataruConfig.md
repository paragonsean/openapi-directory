# Miataru.MiataruUpdateLocationRequestMiataruConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enableLocationHistory** | **String** | If the client tells the server to store a location history the server automatically disables the pre-configured data time-out behavior that removes location data after a given amount of time. Nevertheless the user is limited to the server-side pre-configured amount of location history entries. This is either True or False. | [default to &#39;False&#39;]
**locationDataRetentionTime** | **String** | The LocationDataRetentionTime is the amount of minutes the server will keep that Location Data before it is removed/deleted automatically. | [default to &#39;30&#39;]


