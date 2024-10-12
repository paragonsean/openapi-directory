# openapi-java-client

Climate FieldView Platform APIs
- API version: 4.0.11
  - Build date: 2024-10-12T10:02:32.334271-04:00[America/New_York]
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
1. Java 1.8+
2. Maven (3.8.3+)/Gradle (7.2+)

## Installation

To install the API client library to your local Maven repository, simply execute:

```shell
mvn clean install
```

To deploy it to a remote Maven repository instead, configure the settings of the repository and execute:

```shell
mvn clean deploy
```

Refer to the [OSSRH Guide](http://central.sonatype.org/pages/ossrh-guide.html) for more information.

### Maven users

Add this dependency to your project's POM:

```xml
<dependency>
  <groupId>org.openapitools</groupId>
  <artifactId>openapi-java-client</artifactId>
  <version>4.0.11</version>
  <scope>compile</scope>
</dependency>
```

### Gradle users

Add this dependency to your project's build file:

```groovy
  repositories {
    mavenCentral()     // Needed if the 'openapi-java-client' jar has been published to maven central.
    mavenLocal()       // Needed if the 'openapi-java-client' jar has been published to the local maven repo.
  }

  dependencies {
     implementation "org.openapitools:openapi-java-client:4.0.11"
  }
```

### Others

At first generate the JAR by executing:

```shell
mvn clean package
```

Then manually install the following JARs:

* `target/openapi-java-client-4.0.11.jar`
* `target/lib/*.jar`

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Java code:

```java

// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.model.*;
import org.openapitools.client.api.BoundariesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://platform.climate.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2_authorization_code
    OAuth oauth2_authorization_code = (OAuth) defaultClient.getAuthentication("oauth2_authorization_code");
    oauth2_authorization_code.setAccessToken("YOUR ACCESS TOKEN");

    BoundariesApi apiInstance = new BoundariesApi(defaultClient);
    BoundariesQuery boundariesQuery = new BoundariesQuery(); // BoundariesQuery | 
    try {
      Boundaries result = apiInstance.fetchBoundaries(boundariesQuery);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoundariesApi#fetchBoundaries");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

## Documentation for API Endpoints

All URIs are relative to *https://platform.climate.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BoundariesApi* | [**fetchBoundaries**](docs/BoundariesApi.md#fetchBoundaries) | **POST** /v4/boundaries/query | Retrieve Boundaries in batch
*BoundariesApi* | [**fetchBoundaryById**](docs/BoundariesApi.md#fetchBoundaryById) | **GET** /v4/boundaries/{boundaryId} | Retrieve a Boundary by ID
*BoundariesApi* | [**uploadBoundary**](docs/BoundariesApi.md#uploadBoundary) | **POST** /v4/boundaries | Upload a boundary
*ExportsApi* | [**fetchExportContentsById**](docs/ExportsApi.md#fetchExportContentsById) | **GET** /v4/exports/{exportId}/contents | Retrieve the binary contents of a processed export request.
*ExportsApi* | [**fetchExportStatusById**](docs/ExportsApi.md#fetchExportStatusById) | **GET** /v4/exports/{exportId}/status | Retrieve the status of an Export.
*ExportsApi* | [**postExport**](docs/ExportsApi.md#postExport) | **POST** /v4/exports | Initiate a new export request.
*FarmOrganizationsApi* | [**fetchFarmOrganizationByTypeAndId**](docs/FarmOrganizationsApi.md#fetchFarmOrganizationByTypeAndId) | **GET** /v4/farmOrganizations/{farmOrganizationType}/{farmOrganizationId} | Retrieve a specific farm organization by organization type and ID
*FieldsApi* | [**fetchAllFields**](docs/FieldsApi.md#fetchAllFields) | **GET** /v4/fields/all | Retrieve list of all Fields the user has access to.
*FieldsApi* | [**fetchFieldById**](docs/FieldsApi.md#fetchFieldById) | **GET** /v4/fields/{fieldId} | Retrieve a specific Field by ID
*FieldsApi* | [**fetchFields**](docs/FieldsApi.md#fetchFields) | **GET** /v4/fields | Retrieve list of Fields
*LayersApi* | [**v4LayersAsAppliedActivityIdContentsGet**](docs/LayersApi.md#v4LayersAsAppliedActivityIdContentsGet) | **GET** /v4/layers/asApplied/{activityId}/contents | Retrieve the raw application activity
*LayersApi* | [**v4LayersAsAppliedGet**](docs/LayersApi.md#v4LayersAsAppliedGet) | **GET** /v4/layers/asApplied | Retrieve a list of application activities
*LayersApi* | [**v4LayersAsHarvestedActivityIdContentsGet**](docs/LayersApi.md#v4LayersAsHarvestedActivityIdContentsGet) | **GET** /v4/layers/asHarvested/{activityId}/contents | Retrieve the raw harvest activity
*LayersApi* | [**v4LayersAsHarvestedGet**](docs/LayersApi.md#v4LayersAsHarvestedGet) | **GET** /v4/layers/asHarvested | Retrieve a list of harvest activities
*LayersApi* | [**v4LayersAsPlantedActivityIdContentsGet**](docs/LayersApi.md#v4LayersAsPlantedActivityIdContentsGet) | **GET** /v4/layers/asPlanted/{activityId}/contents | Retrieve the raw planting activity
*LayersApi* | [**v4LayersAsPlantedGet**](docs/LayersApi.md#v4LayersAsPlantedGet) | **GET** /v4/layers/asPlanted | Retrieve a list of planting activities
*LayersApi* | [**v4LayersScoutingObservationsGet**](docs/LayersApi.md#v4LayersScoutingObservationsGet) | **GET** /v4/layers/scoutingObservations | Retrieve a list of scouting observations
*LayersApi* | [**v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGet**](docs/LayersApi.md#v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGet) | **GET** /v4/layers/scoutingObservations/{scoutingObservationId}/attachments/{attachmentId}/contents | Retrieve the binary contents of a scouting observation’s attachment.
*LayersApi* | [**v4LayersScoutingObservationsScoutingObservationIdAttachmentsGet**](docs/LayersApi.md#v4LayersScoutingObservationsScoutingObservationIdAttachmentsGet) | **GET** /v4/layers/scoutingObservations/{scoutingObservationId}/attachments | Retrieve attachments associated with a given scouting observation.
*LayersApi* | [**v4LayersScoutingObservationsScoutingObservationIdGet**](docs/LayersApi.md#v4LayersScoutingObservationsScoutingObservationIdGet) | **GET** /v4/layers/scoutingObservations/{scoutingObservationId} | Retrieve individual scouting observation
*OperationsApi* | [**fetchOperations**](docs/OperationsApi.md#fetchOperations) | **GET** /v4/operations/all | Retrieve the operations accessible to a a given user.
*ResourceOwnersApi* | [**getResourceOwner**](docs/ResourceOwnersApi.md#getResourceOwner) | **GET** /v4/resourceOwners/{resourceOwnerId} | Retrieve a resource owner by ID
*UploadsApi* | [**chunkedUpload**](docs/UploadsApi.md#chunkedUpload) | **PUT** /v4/uploads/{uploadId} | Chunked upload of data
*UploadsApi* | [**fetchUploadStatusById**](docs/UploadsApi.md#fetchUploadStatusById) | **GET** /v4/uploads/{uploadId}/status | Retrieve Upload status
*UploadsApi* | [**fetchUploadStatuses**](docs/UploadsApi.md#fetchUploadStatuses) | **POST** /v4/uploads/status/query | Retrieve Upload statuses in batch
*UploadsApi* | [**postUpload**](docs/UploadsApi.md#postUpload) | **POST** /v4/uploads | Initiate a new upload


## Documentation for Models

 - [ApplicationActivities](docs/ApplicationActivities.md)
 - [ApplicationActivityContents](docs/ApplicationActivityContents.md)
 - [ApplicationActivitySummary](docs/ApplicationActivitySummary.md)
 - [Area](docs/Area.md)
 - [Boundaries](docs/Boundaries.md)
 - [BoundariesQuery](docs/BoundariesQuery.md)
 - [Boundary](docs/Boundary.md)
 - [BoundaryProperties](docs/BoundaryProperties.md)
 - [BoundaryUpload](docs/BoundaryUpload.md)
 - [CreatedExport](docs/CreatedExport.md)
 - [Error](docs/Error.md)
 - [ErrorError](docs/ErrorError.md)
 - [Export](docs/Export.md)
 - [ExportContents](docs/ExportContents.md)
 - [ExportStatus](docs/ExportStatus.md)
 - [FarmOrganization](docs/FarmOrganization.md)
 - [Field](docs/Field.md)
 - [Fields](docs/Fields.md)
 - [Geometry](docs/Geometry.md)
 - [HarvestActivities](docs/HarvestActivities.md)
 - [HarvestActivityContents](docs/HarvestActivityContents.md)
 - [HarvestActivitySummary](docs/HarvestActivitySummary.md)
 - [Operation](docs/Operation.md)
 - [Operations](docs/Operations.md)
 - [Parent](docs/Parent.md)
 - [PlantingActivities](docs/PlantingActivities.md)
 - [PlantingActivityContents](docs/PlantingActivityContents.md)
 - [PlantingActivitySummary](docs/PlantingActivitySummary.md)
 - [Point](docs/Point.md)
 - [ResourceOwner](docs/ResourceOwner.md)
 - [ScoutingObservation](docs/ScoutingObservation.md)
 - [ScoutingObservationAttachment](docs/ScoutingObservationAttachment.md)
 - [ScoutingObservationAttachmentContents](docs/ScoutingObservationAttachmentContents.md)
 - [ScoutingObservationAttachments](docs/ScoutingObservationAttachments.md)
 - [ScoutingObservationSummary](docs/ScoutingObservationSummary.md)
 - [ScoutingObservations](docs/ScoutingObservations.md)
 - [ScoutingTag](docs/ScoutingTag.md)
 - [Upload](docs/Upload.md)
 - [UploadStatus](docs/UploadStatus.md)
 - [UploadStatusQuery](docs/UploadStatusQuery.md)
 - [UploadStatuses](docs/UploadStatuses.md)
 - [UploadedBoundaryId](docs/UploadedBoundaryId.md)


<a id="documentation-for-authorization"></a>
## Documentation for Authorization


Authentication schemes defined for the API:
<a id="api_key"></a>
### api_key

- **Type**: API key
- **API key parameter name**: X-Api-Key
- **Location**: HTTP header

<a id="oauth2_authorization_code"></a>
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


## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author

developer@climate.com

