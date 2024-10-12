# openapi-java-client

GraphHopper Directions API
- API version: 1.0.0
  - Build date: 2024-10-12T10:01:20.208084-04:00[America/New_York]
  - Generator version: 7.9.0


With the [GraphHopper Directions API](https://www.graphhopper.com/products/) you can integrate A-to-B route planning, turn-by-turn navigation,
route optimization, isochrone calculations and other tools in your application.

The GraphHopper Directions API consists of the following RESTful web services:

 * [Routing API](#tag/Routing-API),
 * [Route Optimization API](#tag/Route-Optimization-API),
 * [Isochrone API](#tag/Isochrone-API),
 * [Map Matching API](#tag/Map-Matching-API),
 * [Matrix API](#tag/Matrix-API),
 * [Geocoding API](#tag/Geocoding-API) and
 * [Cluster API](#tag/Cluster-API).

# Explore our APIs

## Get started

1. [Sign up for GraphHopper](https://support.graphhopper.com/a/solutions/articles/44001976025)
2. [Create an API key](https://support.graphhopper.com/a/solutions/articles/44001976027)

Each API part has its own documentation. Jump to the desired API part and learn about the API through the given examples and tutorials.

In addition, for each API there are specific sample requests that you can send via Insomnia or Postman to see what the requests and responses look like.

## Insomnia

To explore our APIs with [Insomnia](https://insomnia.rest/), follow these steps:

1. Open Insomnia and Import [our workspace](https://raw.githubusercontent.com/graphhopper/directions-api-doc/master/web/restclients/GraphHopper-Direction-API-Insomnia.json).
2. Specify [your API key](https://graphhopper.com/dashboard/#/register) in your workspace: Manage Environments -> Base Environment -> `\"api_key\": your API key`
3. Start exploring

![Insomnia](./img/insomnia.png)

## Postman

To explore our APIs with [Postman](https://www.getpostman.com/), follow these steps:

1. Import our [request collections](https://raw.githubusercontent.com/graphhopper/directions-api-doc/master/web/restclients/graphhopper_directions_api.postman_collection.json) as well as our [environment file](https://raw.githubusercontent.com/graphhopper/directions-api-doc/master/web/restclients/graphhopper_directions_api.postman_environment.json).
2. Specify [your API key](https://graphhopper.com/dashboard/#/register) in your environment: `\"api_key\": your API key`
3. Start exploring

![Postman](./img/postman.png)

## API Client Libraries

To speed up development and make coding easier, we offer the following client libraries:

 * [JavaScript client](https://github.com/graphhopper/directions-api-js-client) - try the [live examples](https://graphhopper.com/api/1/examples/)
 * [Others](https://github.com/graphhopper/directions-api-clients) like C#, Ruby, PHP, Python, ... automatically created for the Route Optimization API

### Bandwidth reduction

If you create your own client, make sure it supports http/2 and gzipped responses for best speed.

If you use the Matrix, the Route Optimization API or the Cluster API and want to solve large problems, we recommend you to reduce bandwidth
by [compressing your POST request](https://gist.github.com/karussell/82851e303ea7b3459b2dea01f18949f4)
and specifying the header as follows: `Content-Encoding: gzip`. This will also avoid the HTTP 413 error \"Request Entity Too Large\".

## Contact Us

If you have problems or questions, please read the following information:

- [FAQ](https://graphhopper.com/api/1/docs/FAQ/)
- [Public forum](https://discuss.graphhopper.com/c/directions-api)
- [Contact us](https://www.graphhopper.com/contact-form/)
- [GraphHopper Status Page](https://status.graphhopper.com/)

To stay informed about the latest developments, you can

- follow us on [twitter](https://twitter.com/graphhopper/),
- read [our blog](https://graphhopper.com/blog/),
- watch [our documentation repository](https://github.com/graphhopper/directions-api-doc),
- sign up for our newsletter or
- [our forum](https://discuss.graphhopper.com/c/directions-api).

Select the channel you like the most.


# Map Data and Routing Profiles

Currently, our main data source is [OpenStreetMap](https://www.openstreetmap.org). We also integrated other network data providers.
This chapter gives an overview about the options you have.

## OpenStreetMap

#### Geographical Coverage

[OpenStreetMap](https://www.openstreetmap.org) covers the whole world. If you want to see for yourself if we can provide data suitable for your region,
please visit [GraphHopper Maps](https://graphhopper.com/maps/).
You can edit and modify OpenStreetMap data if you find that important information is missing, e.g. a weight limit for a bridge.
[Here](https://wiki.openstreetmap.org/wiki/Beginners%27_guide) is a beginner's guide that shows how to add data. If you have edited data, we usually consider your data after 1 week at the latest.

#### Supported Vehicle Profiles

The Routing, Matrix and Route Optimization APIs support the following vehicle profiles:

Name       | Description           | Restrictions              | Icon
-----------|:----------------------|:--------------------------|:---------------------------------------------------------
car        | Car mode              | car access                | ![car image](https://graphhopper.com/maps/img/car.png)
small_truck| Small truck like a Mercedes Sprinter, Ford Transit or Iveco Daily | height=2.7m, width=2+0.4m, length=5.5m, weight=2080+1400 kg | ![small truck image](https://graphhopper.com/maps/img/small_truck.png)
truck      | Truck like a MAN or Mercedes-Benz Actros | height=3.7m, width=2.6+0.5m, length=12m, weight=13000 + 13000 kg, hgv=yes, 3 Axes | ![truck image](https://graphhopper.com/maps/img/truck.png)
scooter    | Moped mode | Fast inner city, often used for food delivery, is able to ignore certain bollards, maximum speed of roughly 50km/h | ![scooter image](https://graphhopper.com/maps/img/scooter.png)
foot       | Pedestrian or walking without dangerous [SAC-scales](https://wiki.openstreetmap.org/wiki/Key:sac_scale) | foot access         | ![foot image](https://graphhopper.com/maps/img/foot.png)
hike       | Pedestrian or walking with priority for more beautiful hiking tours and potentially a bit longer than `foot`. Walking duration is influenced by elevation differences.  | foot access         | ![hike image](https://graphhopper.com/maps/img/hike.png)
bike       | Trekking bike avoiding hills | bike access  | ![bike image](https://graphhopper.com/maps/img/bike.png)
mtb        | Mountainbike          | bike access         | ![Mountainbike image](https://graphhopper.com/maps/img/mtb.png)
racingbike| Bike preferring roads | bike access         | ![racingbike image](https://graphhopper.com/maps/img/racingbike.png)

Please note:

 * all motor vehicles (`car`, `small_truck`, `truck` and `scooter`) support turn restrictions via `turn_costs=true`
 * the free package supports only the vehicle profiles `car`, `bike` or `foot`
 * up to 2 different vehicle profiles can be used in a single optimization request. The number of vehicles is unaffected and depends on your subscription.
 * we offer custom vehicle profiles with different properties, different speed profiles or different access options. To find out more about custom profiles, please [contact us](https://www.graphhopper.com/contact-form/).
 * a sophisticated `motorcycle` profile is available up on request. It is powered by the [Kurviger](https://kurviger.de/en) Routing API and favors curves and slopes while avoiding cities and highways.
 
## TomTom

If you want to include traffic, you can purchase the TomTom Add-on.
This Add-on only uses TomTom's road network and historical traffic information.
Live traffic is not yet considered. If you are interested to learn how we consider traffic information, we recommend that you read [this article](https://www.graphhopper.com/blog/2017/11/06/time-dependent-optimization/).

Please note the following:

 * Currently we only offer this for our [Route Optimization API](#tag/Route-Optimization-API).
 * In addition to our terms, you need to accept TomTom's [End User License Aggreement](https://www.graphhopper.com/tomtom-end-user-license-agreement/).
 * We do *not* use TomTom's web services. We only use their data with our software.
 
[Contact us](https://www.graphhopper.com/contact-form/) for more details.

#### Geographical Coverage

We offer

- Europe including Russia
- North, Central and South America
- Saudi Arabia
- United Arab Emirates
- South Africa
- Australia

#### Supported Vehicle Profiles

Name       | Description           | Restrictions              | Icon
-----------|:----------------------|:--------------------------|:---------------------------------------------------------
car        | Car mode              | car access                | ![car image](https://graphhopper.com/maps/img/car.png)
small_truck| Small truck like a Mercedes Sprinter, Ford Transit or Iveco Daily | height=2.7m, width=2+0.4m, length=5.5m, weight=2080+1400 kg | ![small truck image](https://graphhopper.com/maps/img/small_truck.png)


  For more information, please visit [https://www.graphhopper.com/](https://www.graphhopper.com/)

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
  <version>1.0.0</version>
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
     implementation "org.openapitools:openapi-java-client:1.0.0"
  }
```

### Others

At first generate the JAR by executing:

```shell
mvn clean package
```

Then manually install the following JARs:

* `target/openapi-java-client-1.0.0.jar`
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
import org.openapitools.client.api.ClusterApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graphhopper.com/api/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ClusterApiApi apiInstance = new ClusterApiApi(defaultClient);
    ClusterRequest clusterRequest = new ClusterRequest(); // ClusterRequest | Request object that contains the problem to be solved
    try {
      JobId result = apiInstance.asyncClusteringProblem(clusterRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApiApi#asyncClusteringProblem");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

## Documentation for API Endpoints

All URIs are relative to *https://graphhopper.com/api/1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ClusterApiApi* | [**asyncClusteringProblem**](docs/ClusterApiApi.md#asyncClusteringProblem) | **POST** /cluster/calculate | Batch Cluster Endpoint
*ClusterApiApi* | [**getClusterSolution**](docs/ClusterApiApi.md#getClusterSolution) | **GET** /cluster/solution/{jobId} | GET Batch Solution Endpoint
*ClusterApiApi* | [**solveClusteringProblem**](docs/ClusterApiApi.md#solveClusteringProblem) | **POST** /cluster | POST Cluster Endpoint
*GeocodingApiApi* | [**getGeocode**](docs/GeocodingApiApi.md#getGeocode) | **GET** /geocode | Geocoding Endpoint
*IsochroneApiApi* | [**getIsochrone**](docs/IsochroneApiApi.md#getIsochrone) | **GET** /isochrone | Isochrone Endpoint
*MapMatchingApiApi* | [**postGPX**](docs/MapMatchingApiApi.md#postGPX) | **POST** /match | Map-match a GPX file
*MatrixApiApi* | [**calculateMatrix**](docs/MatrixApiApi.md#calculateMatrix) | **POST** /matrix/calculate | Batch Matrix Endpoint
*MatrixApiApi* | [**getMatrix**](docs/MatrixApiApi.md#getMatrix) | **GET** /matrix | GET Matrix Endpoint
*MatrixApiApi* | [**getMatrixSolution**](docs/MatrixApiApi.md#getMatrixSolution) | **GET** /matrix/solution/{jobId} | GET Batch Matrix Endpoint
*MatrixApiApi* | [**postMatrix**](docs/MatrixApiApi.md#postMatrix) | **POST** /matrix | POST Matrix Endpoint
*RouteOptimizationApiApi* | [**asyncVRP**](docs/RouteOptimizationApiApi.md#asyncVRP) | **POST** /vrp/optimize | POST route optimization problem (batch mode)
*RouteOptimizationApiApi* | [**getSolution**](docs/RouteOptimizationApiApi.md#getSolution) | **GET** /vrp/solution/{jobId} | GET the solution (batch mode)
*RouteOptimizationApiApi* | [**solveVRP**](docs/RouteOptimizationApiApi.md#solveVRP) | **POST** /vrp | POST route optimization problem
*RoutingApiApi* | [**getRoute**](docs/RoutingApiApi.md#getRoute) | **GET** /route | GET Route Endpoint
*RoutingApiApi* | [**postRoute**](docs/RoutingApiApi.md#postRoute) | **POST** /route | POST Route Endpoint
*RoutingApiApi* | [**routeInfoGet**](docs/RoutingApiApi.md#routeInfoGet) | **GET** /route/info | Coverage information


## Documentation for Models

 - [Activity](docs/Activity.md)
 - [Address](docs/Address.md)
 - [Algorithm](docs/Algorithm.md)
 - [BadRequest](docs/BadRequest.md)
 - [Cluster](docs/Cluster.md)
 - [ClusterConfiguration](docs/ClusterConfiguration.md)
 - [ClusterConfigurationClustering](docs/ClusterConfigurationClustering.md)
 - [ClusterConfigurationRouting](docs/ClusterConfigurationRouting.md)
 - [ClusterCustomer](docs/ClusterCustomer.md)
 - [ClusterCustomerAddress](docs/ClusterCustomerAddress.md)
 - [ClusterRequest](docs/ClusterRequest.md)
 - [ClusterResponse](docs/ClusterResponse.md)
 - [CostMatrix](docs/CostMatrix.md)
 - [CostMatrixData](docs/CostMatrixData.md)
 - [CostMatrixDataInfo](docs/CostMatrixDataInfo.md)
 - [Detail](docs/Detail.md)
 - [DriveTimeBreak](docs/DriveTimeBreak.md)
 - [ErrorMessage](docs/ErrorMessage.md)
 - [GHError](docs/GHError.md)
 - [GHErrorHintsInner](docs/GHErrorHintsInner.md)
 - [GeocodingLocation](docs/GeocodingLocation.md)
 - [GeocodingPoint](docs/GeocodingPoint.md)
 - [GeocodingResponse](docs/GeocodingResponse.md)
 - [GetClusterSolution404Response](docs/GetClusterSolution404Response.md)
 - [GroupRelation](docs/GroupRelation.md)
 - [InfoResponse](docs/InfoResponse.md)
 - [InternalErrorMessage](docs/InternalErrorMessage.md)
 - [IsochroneResponse](docs/IsochroneResponse.md)
 - [IsochroneResponsePolygon](docs/IsochroneResponsePolygon.md)
 - [IsochroneResponsePolygonProperties](docs/IsochroneResponsePolygonProperties.md)
 - [JobId](docs/JobId.md)
 - [JobRelation](docs/JobRelation.md)
 - [LineString](docs/LineString.md)
 - [MatrixRequest](docs/MatrixRequest.md)
 - [MatrixResponse](docs/MatrixResponse.md)
 - [MatrixResponseHintsInner](docs/MatrixResponseHintsInner.md)
 - [ModelConfiguration](docs/ModelConfiguration.md)
 - [Objective](docs/Objective.md)
 - [Polygon](docs/Polygon.md)
 - [PostMatrixRequest](docs/PostMatrixRequest.md)
 - [Request](docs/Request.md)
 - [RequestRelationsInner](docs/RequestRelationsInner.md)
 - [Response](docs/Response.md)
 - [ResponseAddress](docs/ResponseAddress.md)
 - [ResponseInfo](docs/ResponseInfo.md)
 - [Route](docs/Route.md)
 - [RoutePoint](docs/RoutePoint.md)
 - [RouteRequest](docs/RouteRequest.md)
 - [RouteResponse](docs/RouteResponse.md)
 - [RouteResponsePath](docs/RouteResponsePath.md)
 - [RouteResponsePathInstructionsInner](docs/RouteResponsePathInstructionsInner.md)
 - [RouteResponsePathPoints](docs/RouteResponsePathPoints.md)
 - [RouteResponsePathSnappedWaypoints](docs/RouteResponsePathSnappedWaypoints.md)
 - [Routing](docs/Routing.md)
 - [Service](docs/Service.md)
 - [Shipment](docs/Shipment.md)
 - [SnappedWaypoint](docs/SnappedWaypoint.md)
 - [Solution](docs/Solution.md)
 - [SolutionUnassigned](docs/SolutionUnassigned.md)
 - [Stop](docs/Stop.md)
 - [SymmetricalMatrixRequest](docs/SymmetricalMatrixRequest.md)
 - [TimeWindow](docs/TimeWindow.md)
 - [TimeWindowBreak](docs/TimeWindowBreak.md)
 - [Vehicle](docs/Vehicle.md)
 - [VehicleBreak](docs/VehicleBreak.md)
 - [VehicleProfileId](docs/VehicleProfileId.md)
 - [VehicleType](docs/VehicleType.md)


<a id="documentation-for-authorization"></a>
## Documentation for Authorization


Authentication schemes defined for the API:
<a id="api_key"></a>
### api_key

- **Type**: API key
- **API key parameter name**: key
- **Location**: URL query string


## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author

support@graphhopper.com

