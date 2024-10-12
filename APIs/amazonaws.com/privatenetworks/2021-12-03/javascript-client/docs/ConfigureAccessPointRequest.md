# AwsPrivate5G.ConfigureAccessPointRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessPointArn** | **String** | The Amazon Resource Name (ARN) of the network resource. | 
**cpiSecretKey** | **String** | A Base64 encoded string of the CPI certificate associated with the CPI user who is certifying the coordinates of the network resource.  | [optional] 
**cpiUserId** | **String** | The CPI user ID of the CPI user who is certifying the coordinates of the network resource.  | [optional] 
**cpiUserPassword** | **String** | The CPI password associated with the CPI certificate in &lt;code&gt;cpiSecretKey&lt;/code&gt;. | [optional] 
**cpiUsername** | **String** | The CPI user name of the CPI user who is certifying the coordinates of the radio unit. | [optional] 
**position** | [**ConfigureAccessPointRequestPosition**](ConfigureAccessPointRequestPosition.md) |  | [optional] 


