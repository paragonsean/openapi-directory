# graph_hopper_directions_api

GraphHopperDirectionsApi - JavaScript client for graph_hopper_directions_api

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

This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.JavascriptClientCodegen
For more information, please visit [https://www.graphhopper.com/](https://www.graphhopper.com/)

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/), please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install graph_hopper_directions_api --save
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

To use the link you just defined in your project, switch to the directory you want to use your graph_hopper_directions_api from, and run:

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
var GraphHopperDirectionsApi = require('graph_hopper_directions_api');

var defaultClient = GraphHopperDirectionsApi.ApiClient.instance;
// Configure API key authorization: api_key
var api_key = defaultClient.authentications['api_key'];
api_key.apiKey = "YOUR API KEY"
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix['key'] = "Token"

var api = new GraphHopperDirectionsApi.ClusterAPIApi()
var clusterRequest = new GraphHopperDirectionsApi.ClusterRequest(); // {ClusterRequest} Request object that contains the problem to be solved
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.asyncClusteringProblem(clusterRequest, callback);

```

## Documentation for API Endpoints

All URIs are relative to *https://graphhopper.com/api/1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*GraphHopperDirectionsApi.ClusterAPIApi* | [**asyncClusteringProblem**](docs/ClusterAPIApi.md#asyncClusteringProblem) | **POST** /cluster/calculate | Batch Cluster Endpoint
*GraphHopperDirectionsApi.ClusterAPIApi* | [**getClusterSolution**](docs/ClusterAPIApi.md#getClusterSolution) | **GET** /cluster/solution/{jobId} | GET Batch Solution Endpoint
*GraphHopperDirectionsApi.ClusterAPIApi* | [**solveClusteringProblem**](docs/ClusterAPIApi.md#solveClusteringProblem) | **POST** /cluster | POST Cluster Endpoint
*GraphHopperDirectionsApi.GeocodingAPIApi* | [**getGeocode**](docs/GeocodingAPIApi.md#getGeocode) | **GET** /geocode | Geocoding Endpoint
*GraphHopperDirectionsApi.IsochroneAPIApi* | [**getIsochrone**](docs/IsochroneAPIApi.md#getIsochrone) | **GET** /isochrone | Isochrone Endpoint
*GraphHopperDirectionsApi.MapMatchingAPIApi* | [**postGPX**](docs/MapMatchingAPIApi.md#postGPX) | **POST** /match | Map-match a GPX file
*GraphHopperDirectionsApi.MatrixAPIApi* | [**calculateMatrix**](docs/MatrixAPIApi.md#calculateMatrix) | **POST** /matrix/calculate | Batch Matrix Endpoint
*GraphHopperDirectionsApi.MatrixAPIApi* | [**getMatrix**](docs/MatrixAPIApi.md#getMatrix) | **GET** /matrix | GET Matrix Endpoint
*GraphHopperDirectionsApi.MatrixAPIApi* | [**getMatrixSolution**](docs/MatrixAPIApi.md#getMatrixSolution) | **GET** /matrix/solution/{jobId} | GET Batch Matrix Endpoint
*GraphHopperDirectionsApi.MatrixAPIApi* | [**postMatrix**](docs/MatrixAPIApi.md#postMatrix) | **POST** /matrix | POST Matrix Endpoint
*GraphHopperDirectionsApi.RouteOptimizationAPIApi* | [**asyncVRP**](docs/RouteOptimizationAPIApi.md#asyncVRP) | **POST** /vrp/optimize | POST route optimization problem (batch mode)
*GraphHopperDirectionsApi.RouteOptimizationAPIApi* | [**getSolution**](docs/RouteOptimizationAPIApi.md#getSolution) | **GET** /vrp/solution/{jobId} | GET the solution (batch mode)
*GraphHopperDirectionsApi.RouteOptimizationAPIApi* | [**solveVRP**](docs/RouteOptimizationAPIApi.md#solveVRP) | **POST** /vrp | POST route optimization problem
*GraphHopperDirectionsApi.RoutingAPIApi* | [**getRoute**](docs/RoutingAPIApi.md#getRoute) | **GET** /route | GET Route Endpoint
*GraphHopperDirectionsApi.RoutingAPIApi* | [**postRoute**](docs/RoutingAPIApi.md#postRoute) | **POST** /route | POST Route Endpoint
*GraphHopperDirectionsApi.RoutingAPIApi* | [**routeInfoGet**](docs/RoutingAPIApi.md#routeInfoGet) | **GET** /route/info | Coverage information


## Documentation for Models

 - [GraphHopperDirectionsApi.Activity](docs/Activity.md)
 - [GraphHopperDirectionsApi.Address](docs/Address.md)
 - [GraphHopperDirectionsApi.Algorithm](docs/Algorithm.md)
 - [GraphHopperDirectionsApi.BadRequest](docs/BadRequest.md)
 - [GraphHopperDirectionsApi.Cluster](docs/Cluster.md)
 - [GraphHopperDirectionsApi.ClusterConfiguration](docs/ClusterConfiguration.md)
 - [GraphHopperDirectionsApi.ClusterConfigurationClustering](docs/ClusterConfigurationClustering.md)
 - [GraphHopperDirectionsApi.ClusterConfigurationRouting](docs/ClusterConfigurationRouting.md)
 - [GraphHopperDirectionsApi.ClusterCustomer](docs/ClusterCustomer.md)
 - [GraphHopperDirectionsApi.ClusterCustomerAddress](docs/ClusterCustomerAddress.md)
 - [GraphHopperDirectionsApi.ClusterRequest](docs/ClusterRequest.md)
 - [GraphHopperDirectionsApi.ClusterResponse](docs/ClusterResponse.md)
 - [GraphHopperDirectionsApi.Configuration](docs/Configuration.md)
 - [GraphHopperDirectionsApi.CostMatrix](docs/CostMatrix.md)
 - [GraphHopperDirectionsApi.CostMatrixData](docs/CostMatrixData.md)
 - [GraphHopperDirectionsApi.CostMatrixDataInfo](docs/CostMatrixDataInfo.md)
 - [GraphHopperDirectionsApi.Detail](docs/Detail.md)
 - [GraphHopperDirectionsApi.DriveTimeBreak](docs/DriveTimeBreak.md)
 - [GraphHopperDirectionsApi.ErrorMessage](docs/ErrorMessage.md)
 - [GraphHopperDirectionsApi.GHError](docs/GHError.md)
 - [GraphHopperDirectionsApi.GHErrorHintsInner](docs/GHErrorHintsInner.md)
 - [GraphHopperDirectionsApi.GeocodingLocation](docs/GeocodingLocation.md)
 - [GraphHopperDirectionsApi.GeocodingPoint](docs/GeocodingPoint.md)
 - [GraphHopperDirectionsApi.GeocodingResponse](docs/GeocodingResponse.md)
 - [GraphHopperDirectionsApi.GetClusterSolution404Response](docs/GetClusterSolution404Response.md)
 - [GraphHopperDirectionsApi.GroupRelation](docs/GroupRelation.md)
 - [GraphHopperDirectionsApi.InfoResponse](docs/InfoResponse.md)
 - [GraphHopperDirectionsApi.InternalErrorMessage](docs/InternalErrorMessage.md)
 - [GraphHopperDirectionsApi.IsochroneResponse](docs/IsochroneResponse.md)
 - [GraphHopperDirectionsApi.IsochroneResponsePolygon](docs/IsochroneResponsePolygon.md)
 - [GraphHopperDirectionsApi.IsochroneResponsePolygonProperties](docs/IsochroneResponsePolygonProperties.md)
 - [GraphHopperDirectionsApi.JobId](docs/JobId.md)
 - [GraphHopperDirectionsApi.JobRelation](docs/JobRelation.md)
 - [GraphHopperDirectionsApi.LineString](docs/LineString.md)
 - [GraphHopperDirectionsApi.MatrixRequest](docs/MatrixRequest.md)
 - [GraphHopperDirectionsApi.MatrixResponse](docs/MatrixResponse.md)
 - [GraphHopperDirectionsApi.MatrixResponseHintsInner](docs/MatrixResponseHintsInner.md)
 - [GraphHopperDirectionsApi.Objective](docs/Objective.md)
 - [GraphHopperDirectionsApi.Polygon](docs/Polygon.md)
 - [GraphHopperDirectionsApi.PostMatrixRequest](docs/PostMatrixRequest.md)
 - [GraphHopperDirectionsApi.Request](docs/Request.md)
 - [GraphHopperDirectionsApi.RequestRelationsInner](docs/RequestRelationsInner.md)
 - [GraphHopperDirectionsApi.Response](docs/Response.md)
 - [GraphHopperDirectionsApi.ResponseAddress](docs/ResponseAddress.md)
 - [GraphHopperDirectionsApi.ResponseInfo](docs/ResponseInfo.md)
 - [GraphHopperDirectionsApi.Route](docs/Route.md)
 - [GraphHopperDirectionsApi.RoutePoint](docs/RoutePoint.md)
 - [GraphHopperDirectionsApi.RouteRequest](docs/RouteRequest.md)
 - [GraphHopperDirectionsApi.RouteResponse](docs/RouteResponse.md)
 - [GraphHopperDirectionsApi.RouteResponsePath](docs/RouteResponsePath.md)
 - [GraphHopperDirectionsApi.RouteResponsePathInstructionsInner](docs/RouteResponsePathInstructionsInner.md)
 - [GraphHopperDirectionsApi.RouteResponsePathPoints](docs/RouteResponsePathPoints.md)
 - [GraphHopperDirectionsApi.RouteResponsePathSnappedWaypoints](docs/RouteResponsePathSnappedWaypoints.md)
 - [GraphHopperDirectionsApi.Routing](docs/Routing.md)
 - [GraphHopperDirectionsApi.Service](docs/Service.md)
 - [GraphHopperDirectionsApi.Shipment](docs/Shipment.md)
 - [GraphHopperDirectionsApi.SnappedWaypoint](docs/SnappedWaypoint.md)
 - [GraphHopperDirectionsApi.Solution](docs/Solution.md)
 - [GraphHopperDirectionsApi.SolutionUnassigned](docs/SolutionUnassigned.md)
 - [GraphHopperDirectionsApi.Stop](docs/Stop.md)
 - [GraphHopperDirectionsApi.SymmetricalMatrixRequest](docs/SymmetricalMatrixRequest.md)
 - [GraphHopperDirectionsApi.TimeWindow](docs/TimeWindow.md)
 - [GraphHopperDirectionsApi.TimeWindowBreak](docs/TimeWindowBreak.md)
 - [GraphHopperDirectionsApi.Vehicle](docs/Vehicle.md)
 - [GraphHopperDirectionsApi.VehicleBreak](docs/VehicleBreak.md)
 - [GraphHopperDirectionsApi.VehicleProfileId](docs/VehicleProfileId.md)
 - [GraphHopperDirectionsApi.VehicleType](docs/VehicleType.md)


## Documentation for Authorization


Authentication schemes defined for the API:
### api_key


- **Type**: API key
- **API key parameter name**: key
- **Location**: URL query string

