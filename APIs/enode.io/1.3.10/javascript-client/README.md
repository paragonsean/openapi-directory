# enode_api

EnodeApi - JavaScript client for enode_api
Download [OpenAPI 3.0 Specification](/OpenAPI-Enode-v1.4.0.json)

Download [Postman Collection](/Postman-Enode-v1.4.0.json)

The Enode API is designed to make smart charging applications easy to develop. We provide an abstraction layer that reduces the complexity when extracting vehicle data and sending commands to vehicles from a variety of manufacturers.

The API has a RESTful architecture and utilizes OAuth2 authorization.

We are always available to handle any issues or just answer your questions. Feel free to reach out on post@enode.io


## Registration for API access
In order to use the API you will need a `client_id` and `client_secret`. Please contact us if you are interested in using our API in production, and we will provide these credentials.

# Authorization
Vehicle / hardware access via the Enode API is granted to your application by the User in a standard OAuth `Authorization Code` flow.

> The authorization scheme documented here is the recommended approach for most situations. However, it is also possible to user other OAuth flows, non-confidential clients, and temporary users. Please feel free to contact us if you have any questions about your use-case or the integration of your existing infrastructure.

### Preparation: Configure your OAuth client

Because Enode API implements the OAuth 2.0 spec completely and without modifications, you can avoid rolling your own OAuth client implementation and instead use a well-supported and battle-tested implementation. This is strongly recommended. Information on available OAuth clients for many languages is available [here](https://oauth.net/code/)

To configure your chosen OAuth client, you will need these details:
- Your `client_id`
- Your `client_secret`
- Authorization URL: `https://link.test.enode.io/oauth2/auth`
- Token URL: `https://link.test.enode.io/oauth2/token`

```javascript
// Node.js + openid-client example
const enodeIssuer = await Issuer.discover('https://link.test.enode.io');
const client = new enodeIssuer.Client({
  client_id: 'xyz',
  client_secret: 'shhhhh',
  redirect_uris: ['http://localhost:5000/callback'],
  response_types: ['code'],
});
```


### Preparation: Obtain a client access token via OAuth Client Credentials Grant
Your OAuth client will have a method for using the `OAuth 2.0 Client Credentials Grant` to obtain an access token.

```javascript
// Node.js + openid-client example
const clientAccessToken = await client.grant({grant_type: \"client_credentials\"});
```

This access token belongs to your client and is used for administrative actions, such as the next step.

This token should be cached by your server and reused until it expires, at which point your server should request a new one.



### Step 1. Generate an Enode Link session for your User and launch the OAuth flow

When your User indicates that they want to connect their hardware to your app, your server must call [Link User](#operation/postUsersUseridLink) to generate an Enode Link session for your User. The User ID can be any string that uniquely identifies the User, but it is recommended that you use the primary key by which you identify the User within your application.

Example Request:
```
POST /users/{userId}/link HTTP/1.1
Authorization: Bearer {access_token}
{
  \"forceLanguage\": \"nb-NO\",
  \"vendor\": \"Tesla\",
}
```

Example Response:
```
{
    \"linkState\": \"ZjE2MzMxMGFiYmU4MzcxOTU1ZmRjMTU5NGU2ZmE4YTU3NjViMzIwY2YzNG\",
}
```

The returned linkState must be stored by your server, attached to the session of the authenticated user for which it was generated.

Your OAuth client will provide a method to construct an authorization URL for your user. That method will require these details:
- Redirect URI - The URI to which your user should be redirected when the Oauth flow completes
- Scope - The OAuth scope(s) you wish to request access to (see list of valid values [here](#section/Authentication/AccessTokenBearer))
- State - The value of `linkState` from the request above

To launch the OAuth flow, send your user to the authorization URL constructed by your OAuth client. This can be done in an embedded webview within a native iOS/Android app, or in the system's default browser.

```javascript
// Node.js + openid-client + express example

// Construct an OAuth authorization URL
const authorizationUrl = client.authorizationUrl({
  scope: \"offline_access all\",
  state: linkState
});

// Redirect user to authorization URL
res.redirect(authorizationUrl);
```


### Step 2. User grants consent
In the Link UI webapp the user will follow 3 steps:

1. Choose their hardware from a list of supported manufacturers (EVs and charging boxes). For certain EV makes it will be necessary to also select a charge box.
2. For each selection, the user will be presented with the login screen for that particular hardware. The user must successfully log in.
3. A summary of the requested scopes will be presented to the user. The user must choose whether to grant access to your application.


### Step 3. OAuth flow concludes with a callback
When the user has completed their interactions, they will be redirected to the `Redirect URI` you provided in Step 1, with various metadata appended as query parameters.

Your OAuth client will have a method to parse and validate that metadata, and fetch the granted access and refresh tokens.

Among that metadata will be a `state` value - you must verify that it is equal to the `linkState` value persisted in Step 1, as [a countermeasure against CSRF attacks](https://tools.ietf.org/html/rfc6819#section-4.4.1.8).

```javascript
// Node.js + openid-client + express example

// Fetch linkState from user session
const linkState = get(req, 'session.linkState');

// Parse relevant parameters from request URL
const params = client.callbackParams(req);

// Exchange authorization code for access and refresh tokens
// In this example, openid-client does the linkState validation check for us
const tokenSet = await client.oauthCallback('http://localhost:5000/callback', params, {state: linkState})
```

With the access token in hand, you can now access resources on behalf of the user.


# Errors And Problems
## OAuth Authorization Request

When the User has completed the process of allowing/denying access in Enode Link, they will be redirected to your configured redirect URI. If something has gone wrong, query parameters `error` and `error_description` will be set as documented in [Section 4.1.2.1](https://tools.ietf.org/html/rfc6749#section-4.1.2.1) of the OAuth 2.0 spec:

|error                      |error_description|
|---------------------------|-----------------|
|invalid_request            |The request is missing a required parameter, includes an invalid parameter value, includes a parameter more than once, or is otherwise malformed.|
|unauthorized_client        |The client is not authorized to request an authorization code using this method.|
|access_denied              |The resource owner or authorization server denied the request.|
|unsupported_response_type  |The authorization server does not support obtaining an authorization code using this method.|
|invalid_scope              |The requested scope is invalid, unknown, or malformed.|
|server_error               |The authorization server encountered an unexpected condition that prevented it from fulfilling the request.|
|temporarily_unavailable    |The authorization server is currently unable to handle the request due to a temporary overloading or maintenance of the server|

Example:
```
https://website.example/oauth_callback?state=e0a86fe5&error=access_denied&error_description=The+resource+owner+or+authorization+server+denied+the+request.
```


## Errors when accessing a User's resources

When using an `access_token` to access a User's resources, the following HTTP Status Codes in the 4XX range may be encountered:

|HTTP Status Code           |Explanation      |
|---------------------------|-----------------|
|400 Bad Request            |The request payload has failed schema validation / parsing
|401 Unauthorized           |Authentication details are missing or invalid
|403 Forbidden              |Authentication succeeded, but the authenticated user doesn't have access to the resource
|404 Not Found              |A non-existent resource is requested
|429 Too Many Requests      |Rate limiting by the vendor has prevented us from completing the request


In all cases, an [RFC7807 Problem Details](https://tools.ietf.org/html/rfc7807) body is returned to aid in debugging.

Example:
```
HTTP/1.1 400 Bad Request
Content-Type: application/problem+json
{
  \"type\": \"https://docs.enode.io/problems/payload-validation-error\",
  \"title\": \"Payload validation failed\",
  \"detail\": \"\\\"authorizationRequest.scope\\\" is required\",
}
```


This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.3.10
- Package version: 1.3.10
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.JavascriptClientCodegen

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/), please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install enode_api --save
```

Finally, you need to build the module:

```shell
npm run build
```

##### Local development

To use the library locally without publishing to a remote npm registry, first install the dependencies by changing into the directory containing `package.json` (and this README). Let's call this `JAVASCRIPT_CLIENT_DIR`. Then run:

```shell
npm install
```

Next, [link](https://docs.npmjs.com/cli/link) it globally in npm with the following, also from `JAVASCRIPT_CLIENT_DIR`:

```shell
npm link
```

To use the link you just defined in your project, switch to the directory you want to use your enode_api from, and run:

```shell
npm link /path/to/<JAVASCRIPT_CLIENT_DIR>
```

Finally, you need to build the module:

```shell
npm run build
```

#### git

If the library is hosted at a git repository, e.g.https://github.com/GIT_USER_ID/GIT_REPO_ID
then install it via:

```shell
    npm install GIT_USER_ID/GIT_REPO_ID --save
```

### For browser

The library also works in the browser environment via npm and [browserify](http://browserify.org/). After following
the above steps with Node.js and installing browserify with `npm install -g browserify`,
perform the following (assuming *main.js* is your entry file):

```shell
browserify main.js > bundle.js
```

Then include *bundle.js* in the HTML pages.

### Webpack Configuration

Using Webpack you may encounter the following error: "Module not found: Error:
Cannot resolve module", most certainly you should disable AMD loader. Add/merge
the following section to your webpack config:

```javascript
module: {
  rules: [
    {
      parser: {
        amd: false
      }
    }
  ]
}
```

## Getting Started

Please follow the [installation](#installation) instruction and execute the following JS code:

```javascript
var EnodeApi = require('enode_api');

var defaultClient = EnodeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: UserAccessToken
var UserAccessToken = defaultClient.authentications['UserAccessToken'];
UserAccessToken.accessToken = "YOUR ACCESS TOKEN"

var api = new EnodeApi.ChargersApi()
var chargerId = "chargerId_example"; // {String} ID of the Charger
var opts = {
  'controlChargerChargingRequest': new EnodeApi.ControlChargerChargingRequest() // {ControlChargerChargingRequest} 
};
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
api.controlChargerCharging(chargerId, opts, callback);

```

## Documentation for API Endpoints

All URIs are relative to *https://api.test.enode.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*EnodeApi.ChargersApi* | [**controlChargerCharging**](docs/ChargersApi.md#controlChargerCharging) | **POST** /chargers/{chargerId}/charging | Control Charging
*EnodeApi.ChargersApi* | [**getCharger**](docs/ChargersApi.md#getCharger) | **GET** /chargers/{chargerId} | Get Charger
*EnodeApi.ChargersApi* | [**getChargers**](docs/ChargersApi.md#getChargers) | **GET** /chargers | List Chargers
*EnodeApi.ChargingLocationsApi* | [**deleteCharginglocationsCharginglocationid**](docs/ChargingLocationsApi.md#deleteCharginglocationsCharginglocationid) | **DELETE** /charging-locations/{chargingLocationId} | Delete Charging Location
*EnodeApi.ChargingLocationsApi* | [**getCharginglocations**](docs/ChargingLocationsApi.md#getCharginglocations) | **GET** /charging-locations | List Charging Locations
*EnodeApi.ChargingLocationsApi* | [**getCharginglocationsCharginglocationid**](docs/ChargingLocationsApi.md#getCharginglocationsCharginglocationid) | **GET** /charging-locations/{chargingLocationId} | Get Charging Location
*EnodeApi.ChargingLocationsApi* | [**postCharginglocations**](docs/ChargingLocationsApi.md#postCharginglocations) | **POST** /charging-locations | Create Charging Location
*EnodeApi.ChargingLocationsApi* | [**putCharginglocationsCharginglocationid**](docs/ChargingLocationsApi.md#putCharginglocationsCharginglocationid) | **PUT** /charging-locations/{chargingLocationId} | Update Charging Location
*EnodeApi.MeApi* | [**disconnectVendor**](docs/MeApi.md#disconnectVendor) | **DELETE** /me/vendors/{vendor} | Disconnect Vendor
*EnodeApi.MeApi* | [**getMe**](docs/MeApi.md#getMe) | **GET** /me | Get My User
*EnodeApi.ServiceHealthApi* | [**getHealthReady**](docs/ServiceHealthApi.md#getHealthReady) | **GET** /health/ready | Check Service Readiness
*EnodeApi.ServiceHealthApi* | [**getHealthVendors**](docs/ServiceHealthApi.md#getHealthVendors) | **GET** /health/vendors | Check Available Vendors
*EnodeApi.StatisticsApi* | [**getStatisticsCharging**](docs/StatisticsApi.md#getStatisticsCharging) | **GET** /statistics/charging | Get User Charging Statistics
*EnodeApi.UserManagementApi* | [**deleteUsersUserid**](docs/UserManagementApi.md#deleteUsersUserid) | **DELETE** /users/{userId} | Unlink User
*EnodeApi.UserManagementApi* | [**deleteUsersUseridAuthorization**](docs/UserManagementApi.md#deleteUsersUseridAuthorization) | **DELETE** /users/{userId}/authorization | Deauthorize User
*EnodeApi.UserManagementApi* | [**postUsersUseridLink**](docs/UserManagementApi.md#postUsersUseridLink) | **POST** /users/{userId}/link | Link User
*EnodeApi.VehiclesApi* | [**getVehicleChargestate**](docs/VehiclesApi.md#getVehicleChargestate) | **GET** /vehicles/{vehicleId}/charge-state | Get Vehicle Charge State
*EnodeApi.VehiclesApi* | [**getVehicles**](docs/VehiclesApi.md#getVehicles) | **GET** /vehicles | List Vehicles
*EnodeApi.VehiclesApi* | [**getVehiclesVehicleid**](docs/VehiclesApi.md#getVehiclesVehicleid) | **GET** /vehicles/{vehicleId} | Get Vehicle
*EnodeApi.VehiclesApi* | [**getVehiclesVehicleidInformation**](docs/VehiclesApi.md#getVehiclesVehicleidInformation) | **GET** /vehicles/{vehicleId}/information | Get Vehicle Information
*EnodeApi.VehiclesApi* | [**getVehiclesVehicleidLocation**](docs/VehiclesApi.md#getVehiclesVehicleidLocation) | **GET** /vehicles/{vehicleId}/location | Get Vehicle Location
*EnodeApi.VehiclesApi* | [**getVehiclesVehicleidOdometer**](docs/VehiclesApi.md#getVehiclesVehicleidOdometer) | **GET** /vehicles/{vehicleId}/odometer | Get Vehicle Odometer
*EnodeApi.VehiclesApi* | [**getVehiclesVehicleidSmartchargingpolicy**](docs/VehiclesApi.md#getVehiclesVehicleidSmartchargingpolicy) | **GET** /vehicles/{vehicleId}/smart-charging-policy | Get Vehicle Smart Charging Policy
*EnodeApi.VehiclesApi* | [**postVehiclesVehicleidCharging**](docs/VehiclesApi.md#postVehiclesVehicleidCharging) | **POST** /vehicles/{vehicleId}/charging | Start / Stop Charging
*EnodeApi.VehiclesApi* | [**postVehiclesVehicleidWatch**](docs/VehiclesApi.md#postVehiclesVehicleidWatch) | **POST** /vehicles/{vehicleId}/watch | Start Watching Vehicle
*EnodeApi.VehiclesApi* | [**putVehiclesVehicleidSmartchargingpolicy**](docs/VehiclesApi.md#putVehiclesVehicleidSmartchargingpolicy) | **PUT** /vehicles/{vehicleId}/smart-charging-policy | Update Vehicle Smart Charging Policy
*EnodeApi.WebhooksApi* | [**postWebhooksFirehoseTest**](docs/WebhooksApi.md#postWebhooksFirehoseTest) | **POST** /webhooks/firehose/test | Test Firehose Webhook
*EnodeApi.WebhooksApi* | [**putWebhooksFirehose**](docs/WebhooksApi.md#putWebhooksFirehose) | **PUT** /webhooks/firehose | Update Firehose Webhook


## Documentation for Models

 - [EnodeApi.ControlChargerChargingRequest](docs/ControlChargerChargingRequest.md)
 - [EnodeApi.GetCharger200Response](docs/GetCharger200Response.md)
 - [EnodeApi.GetCharger200ResponseChargeState](docs/GetCharger200ResponseChargeState.md)
 - [EnodeApi.GetCharger200ResponseInformation](docs/GetCharger200ResponseInformation.md)
 - [EnodeApi.GetHealthVendors200ResponseInner](docs/GetHealthVendors200ResponseInner.md)
 - [EnodeApi.GetMe200Response](docs/GetMe200Response.md)
 - [EnodeApi.GetMe200ResponseLinkedVendorsInner](docs/GetMe200ResponseLinkedVendorsInner.md)
 - [EnodeApi.GetStatisticsCharging200ResponseInner](docs/GetStatisticsCharging200ResponseInner.md)
 - [EnodeApi.GetStatisticsCharging200ResponseInnerKw](docs/GetStatisticsCharging200ResponseInnerKw.md)
 - [EnodeApi.GetStatisticsCharging200ResponseInnerPrice](docs/GetStatisticsCharging200ResponseInnerPrice.md)
 - [EnodeApi.GetVehicleChargestate200Response](docs/GetVehicleChargestate200Response.md)
 - [EnodeApi.GetVehiclesVehicleid200Response](docs/GetVehiclesVehicleid200Response.md)
 - [EnodeApi.GetVehiclesVehicleidInformation200Response](docs/GetVehiclesVehicleidInformation200Response.md)
 - [EnodeApi.GetVehiclesVehicleidLocation200Response](docs/GetVehiclesVehicleidLocation200Response.md)
 - [EnodeApi.GetVehiclesVehicleidOdometer200Response](docs/GetVehiclesVehicleidOdometer200Response.md)
 - [EnodeApi.PostCharginglocationsRequest](docs/PostCharginglocationsRequest.md)
 - [EnodeApi.PostUsersUseridLink200Response](docs/PostUsersUseridLink200Response.md)
 - [EnodeApi.PostUsersUseridLinkRequest](docs/PostUsersUseridLinkRequest.md)
 - [EnodeApi.PostVehiclesVehicleidWatchRequest](docs/PostVehiclesVehicleidWatchRequest.md)
 - [EnodeApi.PutVehiclesVehicleidSmartchargingpolicyRequest](docs/PutVehiclesVehicleidSmartchargingpolicyRequest.md)
 - [EnodeApi.PutWebhooksFirehoseRequest](docs/PutWebhooksFirehoseRequest.md)


## Documentation for Authorization


Authentication schemes defined for the API:
### ClientAccessToken


- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: 
- **Scopes**: N/A

### UserAccessToken


- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://link.test.enode.io/oauth2/auth
- **Scopes**: 
  - all: Read and write all resources
  - charger:charge_state: Read charger charge state
  - charger:information: Read charger information
  - charging_location: Read &amp; write user&#39;s charging locations
  - control:charger:charging: Control charger charging
  - control:vehicle:charging: Control vehicle charging
  - vehicle:charge_state: Read vehicle charge state
  - vehicle:information: Read vehicle information
  - vehicle:location: Read vehicle location
  - vehicle:odometer: Read vehicle odometer
  - vehicle:smart_charging_policy: Read &amp; write vehicle smart charging policy

