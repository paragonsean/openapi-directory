# C++ Qt API client

# 

Climate FieldView Platform APIs

- API version: 4.0.11
- Generator version: 7.9.0

**Last Modified**: Wed Jan  4 12:47:29 UTC 2023


All endpoints are only accessible via HTTPS.

* All API endpoints are located at `https://platform.climate.com` (e.g.
`https://platform.climate.com/v4/fields`).

* The authorization token endpoint is located at
`https://api.climate.com/api/oauth/token`.

## Troubleshooting

`X-Http-Request-Id` response header will be returned on every call,
successful or not. If you experience an issue with our api and need
to contact technical support, please supply the value of the `X-Http-Request-Id`
header along with an approximate time of when the request was made.

## Request Limits

When you’re onboarded to Climate’s API platform, your `x-api-key` is assigned a custom usage plan. Usage plans are unique to each partner and have the following key attributes: 

1. Throttling information
    * burstLimit: Maximum rate limit over a period ranging from 1 second to a few seconds
    * rateLimit: A steady-state rate limit

2. Quota information
    * Limit: The maximum number of requests that can be made in a given month

When the request rate threshold is exceeded, a `429` response code is returned. Optionally, the [`Retry-After`](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.37) header may be returned: 

Following are examples of rate limit errors:

1. Rate limit exceeded:

<br>HTTP/1.1 429 
<br>Content-Type: application/json
<br>Content-Length: 32

   {\"message\":\"Too Many Requests\"}

2. Quota exhausted:
<br>HTTP/1.1 429 
<br>Content-Type: application/json
<br>Content-Length: 29

    {\"message\":\"Limit Exceeded\"}

## Pagination

Pagination is performed via headers. Any request which returns a `\"results\"`
array may be paginated. The following figure shows how query results are laid out with
X-Limit=4 and no filter applied.

<img style=\"width:70%;height:auto;\" src=\"https://s3-us-west-2.amazonaws.com/climate-com/images/svg_upload_tests/paging.png\">

* If there are no results, a response code of `304` will be returned.

* If the response is the last set of results, a response code of `200` or
`206` will be returned.

* If there are more results, a response code of `206` will be returned.

* If `X-Next-Token` is provided in the request headers but the token has
expired, a response code of `409` will be returned. This is only applicable
for some endpoints; see specific endpoint documentation below.

#### X-Limit

The page size can be controlled with the `X-Limit` header. Valid values are
`1-100` and defaults to `100`.

#### X-Next-Token

If the results are paginated, a response header of `X-Next-Token` will be
returned. Use the associated value in the subsequent request (via the `X-Next-Token`
request header) to retrieve the next page. The following sequence diagram shows how to
use `X-Next-Token` to fetch all the records.

<img src=\"https://s3-us-west-2.amazonaws.com/climate-com/images/svg_upload_tests/x-next-token.svg\">


## Chunked Uploads

Uploads larger than `5MiB` (`5242880 bytes`) must be done in `5MiB` chunks
(with the exception of the final chunk). Each chunk request MUST contain a
`Content-Range` header specifying the portion of the upload, and a `Content-Type`
header specifying binary content type (`application/octet-stream`). Range
uploads must be contiguous. The maximum upload size is capped at `500MiB` (`524288000 bytes`).

## Chunked Downloads

Downloads larger than `5MiB` (`5242880 bytes`) must be done in `1-5MiB`
chunks (with the exception of the final chunk, which may be less than `1MiB`).
Each chunk request MUST contain a `Range` header specifying the requested portion of the download,
and an `Accept` header specifying binary and json content types  (`application/octet-stream,application/json`)
or all content types (`*_/_*`).

## Drivers

If you need drivers to process agronomic data, download the ADAPT plugin below. We only support the plugin in the Windows environment, minimum is Windows 7 SP1.

For asPlanted, asHarvested and asApplied data:
* [ADAPT Plugin](https://dev.fieldview.com/drivers/ClimateADAPTPlugin_latest.exe)
<br>Release notes can be found [here](https://dev.fieldview.com/drivers/adapt-release-notes.txt).
<br>Download and use of the ADAPT plugin means that you agree to the EULA for use of the ADAPT plugin. 
<br>Please review the [EULA](https://dev.fieldview.com/EULA/ADAPT%20Plugin%20EULA-06-19.pdf) (last updated on June 6th, 2019) before download and use of the ADAPT plugin.
<br>For more information, please refer to:
  * [ADAPT Resources](https://adaptframework.org/)
  * [ADAPT Overview](https://aggateway.atlassian.net/wiki/spaces/ADM/overview)
  * [ADAPT FAQ](https://aggateway.atlassian.net/wiki/spaces/ADM/pages/165942474/ADAPT+Frequently-Asked+Questions+FAQ)
  * [ADAPT Videos](https://adaptframework.org/adapt-videos/)

## Sample Test Data

Sample agronomic data:
* [asPlanted and asHarvested data](https://dev.fieldview.com/sample-agronomic-data/Planting_Harvesting_data_04_18_2018_21_46_18.zip)
* [asApplied data set 1](https://dev.fieldview.com/sample-agronomic-data/as-applied-data1.zip)
* [asApplied data set 2](https://dev.fieldview.com/sample-agronomic-data/as-applied-data2.zip)
<br>To upload the sample data to your account, please follow the instructions in this [link](https://support.climate.com/kt#/kA02A000000AaxzSAC/en_US).

Sample soil data:
* [Sample soil data](https://dev.fieldview.com/sample-soil-data/soil-sample.xml)
---



*Automatically generated by the [OpenAPI Generator](https://openapi-generator.tech)*


## Requirements

Building the API client library requires:

1. CMake 3.2+
2. Qt
3. C++ Compiler

## Getting Started

example.h:
```c++

#include <iostream>
#include "../client/OAIBoundariesApi.h"

using namespace test_namespace;

class Example : public QObject {
    Q_OBJECT
    OAIBoundariesQuery create();
public Q_SLOTS:
   void exampleFunction1();
};

```

example.cpp:
```c++

#include "../client/OAIBoundariesApi.h"
#include "example.h"
#include <QTimer>
#include <QEventLoop>

OAIBoundariesQuery Example::create(){
    OAIBoundariesQuery obj;
 return obj;
}

void Example::exampleFunction1(){
     OAIBoundariesApi apiInstance;
     
      // Configure API key authorization: api_key
      apiInstance.setApiKey("YOUR API KEY NAME","YOUR API KEY");

      //OAuth Authentication supported right now

      QEventLoop loop;
      connect(&apiInstance, &OAIBoundariesApi::fetchBoundariesSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIBoundariesApi::fetchBoundariesSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      OAIBoundariesQuery oai_boundaries_query = create(); // OAIBoundariesQuery | 
      apiInstance.fetchBoundaries(oai_boundaries_query);
      QTimer::singleShot(5000, &loop, &QEventLoop::quit);
      loop.exec();
  }

```

## Documentation for Servers

Parameterized Servers are supported. Define a server in the API for each endpoint with arbitrary numbers of variables:

```yaml
servers:
- url: http://{server}:{port}/{basePath}
  description: Description of the Server
  variables:
    server:
        enum:
          - 'petstore'
          - 'qa-petstore'
          - 'dev-petstore'
        default: 'petstore'
    port:
      enum:
        - '3000'
        - '1000'
      default: '3000'
    basePath:
      default: v1
```
To change the default variable, use this function in each Api:
```c++
int setDefaultServerValue(int serverIndex,const QString &operation, const QString &variable,const QString &val);
```
The parameter "serverIndex" will choose a server from the server list for each endpoint. There is always at least one server with index 0. The Parameter "operation" should be the desired endpoint operationid.
Variable is the name of the variable you wish to change and the value is the new default Value.
The function will return -1 when the variable does not exists, -2 if value is not defined in the variable enum and -3 if the operation is not found.

If your endpoint has multiple server objects in the servers array, you can set the server that will be used with this function:
```c++
void setServerIndex(const QString &operation, int serverIndex);
```
Parameter "operation" should be your operationid. "serverIndex" is the index you want to set as your default server. The function will check if there is a server with your index.
Here is an example of multiple servers in the servers array. The first server will have index 0 and the second will have index 1.
```yaml
servers:
- url: http://{server}:8080/
  description: Description of the Server
  variables:
    server:
        enum:
          - 'petstore'
          - 'qa-petstore'
          - 'dev-petstore'
        default: 'petstore'
- url: https://localhost:8080/v1
```

## Documentation for Authorization

Authentication schemes defined for the API:
### api_key


- **Type**: API key
- **API key parameter name**: X-Api-Key
- **Location**: HTTP header

### oauth2_authorization_code


- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://climate.com/static/app-login/
- **Scopes**: 
  - asApplied:read: Required for retrieving as applied data
  - asApplied:write: Required for uploading application data
  - asHarvested:read: Required for retrieving harvest data
  - asHarvested:write: Required for uploading harvest data
  - asPlanted:read: Required for retrieving planting data
  - asPlanted:write: Required for uploading planting data
  - avroAgronomicData:read: Required for retrieving agronomic data
  - boundaries:write: *Originally missing*
  - customerInsights:read: Required for retrieving customer insights metrics data
  - diagnostics:read: Required for retrieving CNH machine diagnostic data
  - exports:read: Required for requesting or retrieving exports
  - farmOrganizations:read: Required for retrieving farm organization information
  - fields:read: Required for retrieving field and boundary information
  - fields:write: Required for uploading field boundaries
  - imagery:write: Required for uploading imagery
  - operations:read: Required for retrieving operation information
  - plantingActivitySummary:read: Required for retrieving planting activity summary data
  - platform: (DEPRECATED) Legacy scope used for some Platform APIs
  - resourceOwners:read: Required for retrieving resource owner information
  - rx:write: Required for uploading prescriptions
  - scouting:read: Required for retrieving user\\&#39;s scouting information
  - soil:write: Required for uploading soil sample results
  - standCount:write: *Originally missing*
  - weedCount:write: *Originally missing*


## Author

developer@climate.com


## License

 for more information visit []()