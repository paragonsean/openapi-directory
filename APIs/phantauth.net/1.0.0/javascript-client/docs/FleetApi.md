# PhantAuth.FleetApi

All URIs are relative to *https://phantauth.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fleetFleetnameGet**](FleetApi.md#fleetFleetnameGet) | **GET** /fleet/{fleetname} | Get a Fleet



## fleetFleetnameGet

> FleetFleetnameGet200Response fleetFleetnameGet(fleetname)

Get a Fleet

Use this endpoint to generate a random group of clients. The feleet is generated in a deterministic way, on the basis of a fleet name given as a path parameter. In the case of identical fleet names, the endpoint will generate the same fleet object. The properties of the generated fleet object are randomly generated on the basis of the fleet name. In lack of a fleet name, all calls generate a different fleet object to the randomly generated fleet name.

### Example

```javascript
import PhantAuth from 'phant_auth';

let apiInstance = new PhantAuth.FleetApi();
let fleetname = "fleetname_example"; // String |  The identifier or email address of the fleet; it is integrated in the `sub` property and is the basis of the other generated properties. 
apiInstance.fleetFleetnameGet(fleetname, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fleetname** | **String**|  The identifier or email address of the fleet; it is integrated in the &#x60;sub&#x60; property and is the basis of the other generated properties.  | 

### Return type

[**FleetFleetnameGet200Response**](FleetFleetnameGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

