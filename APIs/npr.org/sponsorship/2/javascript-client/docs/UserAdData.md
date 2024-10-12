# NprSponsorshipService.UserAdData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipAddress** | **String** | The TCP/IP address of the client making the request. The server will attempt to grab this from the headers, so it probably does not need to be passed in the body unless you get back an error message stating that we were unable to determine an IP address from the request. | [optional] 
**userAgent** | **String** | An identifying string for the browser making the request. The server will attempt to grab this from the headers, so it probably does not need to be passed in the body unless you get back an error message stating that we were unable to determine a User-Agent from the request. | [optional] 


