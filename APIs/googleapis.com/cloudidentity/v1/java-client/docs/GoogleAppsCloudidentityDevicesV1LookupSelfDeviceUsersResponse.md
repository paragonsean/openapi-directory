

# GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponse

Response containing resource names of the DeviceUsers associated with the caller's credentials.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customer** | **String** | The customer resource name that may be passed back to other Devices API methods such as List, Get, etc. |  [optional] |
|**names** | **List&lt;String&gt;** | [Resource names](https://cloud.google.com/apis/design/resource_names) of the DeviceUsers in the format: &#x60;devices/{device}/deviceUsers/{user_resource}&#x60;, where device is the unique ID assigned to a Device and user_resource is the unique user ID |  [optional] |
|**nextPageToken** | **String** | Token to retrieve the next page of results. Empty if there are no more results. |  [optional] |



