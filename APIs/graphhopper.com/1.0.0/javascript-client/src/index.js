/**
 * GraphHopper Directions API
 *  With the [GraphHopper Directions API](https://www.graphhopper.com/products/) you can integrate A-to-B route planning, turn-by-turn navigation, route optimization, isochrone calculations and other tools in your application.  The GraphHopper Directions API consists of the following RESTful web services:   * [Routing API](#tag/Routing-API),  * [Route Optimization API](#tag/Route-Optimization-API),  * [Isochrone API](#tag/Isochrone-API),  * [Map Matching API](#tag/Map-Matching-API),  * [Matrix API](#tag/Matrix-API),  * [Geocoding API](#tag/Geocoding-API) and  * [Cluster API](#tag/Cluster-API).  # Explore our APIs  ## Get started  1. [Sign up for GraphHopper](https://support.graphhopper.com/a/solutions/articles/44001976025) 2. [Create an API key](https://support.graphhopper.com/a/solutions/articles/44001976027)  Each API part has its own documentation. Jump to the desired API part and learn about the API through the given examples and tutorials.  In addition, for each API there are specific sample requests that you can send via Insomnia or Postman to see what the requests and responses look like.  ## Insomnia  To explore our APIs with [Insomnia](https://insomnia.rest/), follow these steps:  1. Open Insomnia and Import [our workspace](https://raw.githubusercontent.com/graphhopper/directions-api-doc/master/web/restclients/GraphHopper-Direction-API-Insomnia.json). 2. Specify [your API key](https://graphhopper.com/dashboard/#/register) in your workspace: Manage Environments -> Base Environment -> `\"api_key\": your API key` 3. Start exploring  ![Insomnia](./img/insomnia.png)  ## Postman  To explore our APIs with [Postman](https://www.getpostman.com/), follow these steps:  1. Import our [request collections](https://raw.githubusercontent.com/graphhopper/directions-api-doc/master/web/restclients/graphhopper_directions_api.postman_collection.json) as well as our [environment file](https://raw.githubusercontent.com/graphhopper/directions-api-doc/master/web/restclients/graphhopper_directions_api.postman_environment.json). 2. Specify [your API key](https://graphhopper.com/dashboard/#/register) in your environment: `\"api_key\": your API key` 3. Start exploring  ![Postman](./img/postman.png)  ## API Client Libraries  To speed up development and make coding easier, we offer the following client libraries:   * [JavaScript client](https://github.com/graphhopper/directions-api-js-client) - try the [live examples](https://graphhopper.com/api/1/examples/)  * [Others](https://github.com/graphhopper/directions-api-clients) like C#, Ruby, PHP, Python, ... automatically created for the Route Optimization API  ### Bandwidth reduction  If you create your own client, make sure it supports http/2 and gzipped responses for best speed.  If you use the Matrix, the Route Optimization API or the Cluster API and want to solve large problems, we recommend you to reduce bandwidth by [compressing your POST request](https://gist.github.com/karussell/82851e303ea7b3459b2dea01f18949f4) and specifying the header as follows: `Content-Encoding: gzip`. This will also avoid the HTTP 413 error \"Request Entity Too Large\".  ## Contact Us  If you have problems or questions, please read the following information:  - [FAQ](https://graphhopper.com/api/1/docs/FAQ/) - [Public forum](https://discuss.graphhopper.com/c/directions-api) - [Contact us](https://www.graphhopper.com/contact-form/) - [GraphHopper Status Page](https://status.graphhopper.com/)  To stay informed about the latest developments, you can  - follow us on [twitter](https://twitter.com/graphhopper/), - read [our blog](https://graphhopper.com/blog/), - watch [our documentation repository](https://github.com/graphhopper/directions-api-doc), - sign up for our newsletter or - [our forum](https://discuss.graphhopper.com/c/directions-api).  Select the channel you like the most.   # Map Data and Routing Profiles  Currently, our main data source is [OpenStreetMap](https://www.openstreetmap.org). We also integrated other network data providers. This chapter gives an overview about the options you have.  ## OpenStreetMap  #### Geographical Coverage  [OpenStreetMap](https://www.openstreetmap.org) covers the whole world. If you want to see for yourself if we can provide data suitable for your region, please visit [GraphHopper Maps](https://graphhopper.com/maps/). You can edit and modify OpenStreetMap data if you find that important information is missing, e.g. a weight limit for a bridge. [Here](https://wiki.openstreetmap.org/wiki/Beginners%27_guide) is a beginner's guide that shows how to add data. If you have edited data, we usually consider your data after 1 week at the latest.  #### Supported Vehicle Profiles  The Routing, Matrix and Route Optimization APIs support the following vehicle profiles:  Name       | Description           | Restrictions              | Icon -----------|:----------------------|:--------------------------|:--------------------------------------------------------- car        | Car mode              | car access                | ![car image](https://graphhopper.com/maps/img/car.png) small_truck| Small truck like a Mercedes Sprinter, Ford Transit or Iveco Daily | height=2.7m, width=2+0.4m, length=5.5m, weight=2080+1400 kg | ![small truck image](https://graphhopper.com/maps/img/small_truck.png) truck      | Truck like a MAN or Mercedes-Benz Actros | height=3.7m, width=2.6+0.5m, length=12m, weight=13000 + 13000 kg, hgv=yes, 3 Axes | ![truck image](https://graphhopper.com/maps/img/truck.png) scooter    | Moped mode | Fast inner city, often used for food delivery, is able to ignore certain bollards, maximum speed of roughly 50km/h | ![scooter image](https://graphhopper.com/maps/img/scooter.png) foot       | Pedestrian or walking without dangerous [SAC-scales](https://wiki.openstreetmap.org/wiki/Key:sac_scale) | foot access         | ![foot image](https://graphhopper.com/maps/img/foot.png) hike       | Pedestrian or walking with priority for more beautiful hiking tours and potentially a bit longer than `foot`. Walking duration is influenced by elevation differences.  | foot access         | ![hike image](https://graphhopper.com/maps/img/hike.png) bike       | Trekking bike avoiding hills | bike access  | ![bike image](https://graphhopper.com/maps/img/bike.png) mtb        | Mountainbike          | bike access         | ![Mountainbike image](https://graphhopper.com/maps/img/mtb.png) racingbike| Bike preferring roads | bike access         | ![racingbike image](https://graphhopper.com/maps/img/racingbike.png)  Please note:   * all motor vehicles (`car`, `small_truck`, `truck` and `scooter`) support turn restrictions via `turn_costs=true`  * the free package supports only the vehicle profiles `car`, `bike` or `foot`  * up to 2 different vehicle profiles can be used in a single optimization request. The number of vehicles is unaffected and depends on your subscription.  * we offer custom vehicle profiles with different properties, different speed profiles or different access options. To find out more about custom profiles, please [contact us](https://www.graphhopper.com/contact-form/).  * a sophisticated `motorcycle` profile is available up on request. It is powered by the [Kurviger](https://kurviger.de/en) Routing API and favors curves and slopes while avoiding cities and highways.   ## TomTom  If you want to include traffic, you can purchase the TomTom Add-on. This Add-on only uses TomTom's road network and historical traffic information. Live traffic is not yet considered. If you are interested to learn how we consider traffic information, we recommend that you read [this article](https://www.graphhopper.com/blog/2017/11/06/time-dependent-optimization/).  Please note the following:   * Currently we only offer this for our [Route Optimization API](#tag/Route-Optimization-API).  * In addition to our terms, you need to accept TomTom's [End User License Aggreement](https://www.graphhopper.com/tomtom-end-user-license-agreement/).  * We do *not* use TomTom's web services. We only use their data with our software.   [Contact us](https://www.graphhopper.com/contact-form/) for more details.  #### Geographical Coverage  We offer  - Europe including Russia - North, Central and South America - Saudi Arabia - United Arab Emirates - South Africa - Australia  #### Supported Vehicle Profiles  Name       | Description           | Restrictions              | Icon -----------|:----------------------|:--------------------------|:--------------------------------------------------------- car        | Car mode              | car access                | ![car image](https://graphhopper.com/maps/img/car.png) small_truck| Small truck like a Mercedes Sprinter, Ford Transit or Iveco Daily | height=2.7m, width=2+0.4m, length=5.5m, weight=2080+1400 kg | ![small truck image](https://graphhopper.com/maps/img/small_truck.png) 
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@graphhopper.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import Activity from './model/Activity';
import Address from './model/Address';
import Algorithm from './model/Algorithm';
import BadRequest from './model/BadRequest';
import Cluster from './model/Cluster';
import ClusterConfiguration from './model/ClusterConfiguration';
import ClusterConfigurationClustering from './model/ClusterConfigurationClustering';
import ClusterConfigurationRouting from './model/ClusterConfigurationRouting';
import ClusterCustomer from './model/ClusterCustomer';
import ClusterCustomerAddress from './model/ClusterCustomerAddress';
import ClusterRequest from './model/ClusterRequest';
import ClusterResponse from './model/ClusterResponse';
import Configuration from './model/Configuration';
import CostMatrix from './model/CostMatrix';
import CostMatrixData from './model/CostMatrixData';
import CostMatrixDataInfo from './model/CostMatrixDataInfo';
import Detail from './model/Detail';
import DriveTimeBreak from './model/DriveTimeBreak';
import ErrorMessage from './model/ErrorMessage';
import GHError from './model/GHError';
import GHErrorHintsInner from './model/GHErrorHintsInner';
import GeocodingLocation from './model/GeocodingLocation';
import GeocodingPoint from './model/GeocodingPoint';
import GeocodingResponse from './model/GeocodingResponse';
import GetClusterSolution404Response from './model/GetClusterSolution404Response';
import GroupRelation from './model/GroupRelation';
import InfoResponse from './model/InfoResponse';
import InternalErrorMessage from './model/InternalErrorMessage';
import IsochroneResponse from './model/IsochroneResponse';
import IsochroneResponsePolygon from './model/IsochroneResponsePolygon';
import IsochroneResponsePolygonProperties from './model/IsochroneResponsePolygonProperties';
import JobId from './model/JobId';
import JobRelation from './model/JobRelation';
import LineString from './model/LineString';
import MatrixRequest from './model/MatrixRequest';
import MatrixResponse from './model/MatrixResponse';
import MatrixResponseHintsInner from './model/MatrixResponseHintsInner';
import Objective from './model/Objective';
import Polygon from './model/Polygon';
import PostMatrixRequest from './model/PostMatrixRequest';
import Request from './model/Request';
import RequestRelationsInner from './model/RequestRelationsInner';
import Response from './model/Response';
import ResponseAddress from './model/ResponseAddress';
import ResponseInfo from './model/ResponseInfo';
import Route from './model/Route';
import RoutePoint from './model/RoutePoint';
import RouteRequest from './model/RouteRequest';
import RouteResponse from './model/RouteResponse';
import RouteResponsePath from './model/RouteResponsePath';
import RouteResponsePathInstructionsInner from './model/RouteResponsePathInstructionsInner';
import RouteResponsePathPoints from './model/RouteResponsePathPoints';
import RouteResponsePathSnappedWaypoints from './model/RouteResponsePathSnappedWaypoints';
import Routing from './model/Routing';
import Service from './model/Service';
import Shipment from './model/Shipment';
import SnappedWaypoint from './model/SnappedWaypoint';
import Solution from './model/Solution';
import SolutionUnassigned from './model/SolutionUnassigned';
import Stop from './model/Stop';
import SymmetricalMatrixRequest from './model/SymmetricalMatrixRequest';
import TimeWindow from './model/TimeWindow';
import TimeWindowBreak from './model/TimeWindowBreak';
import Vehicle from './model/Vehicle';
import VehicleBreak from './model/VehicleBreak';
import VehicleProfileId from './model/VehicleProfileId';
import VehicleType from './model/VehicleType';
import ClusterAPIApi from './api/ClusterAPIApi';
import GeocodingAPIApi from './api/GeocodingAPIApi';
import IsochroneAPIApi from './api/IsochroneAPIApi';
import MapMatchingAPIApi from './api/MapMatchingAPIApi';
import MatrixAPIApi from './api/MatrixAPIApi';
import RouteOptimizationAPIApi from './api/RouteOptimizationAPIApi';
import RoutingAPIApi from './api/RoutingAPIApi';


/**
*  With the [GraphHopper Directions API](https://www.graphhopper.com/products/) you can integrate A-to-B route planning, turn-by-turn navigation, route optimization, isochrone calculations and other tools in your application.  The GraphHopper Directions API consists of the following RESTful web services:   * [Routing API](#tag/Routing-API),  * [Route Optimization API](#tag/Route-Optimization-API),  * [Isochrone API](#tag/Isochrone-API),  * [Map Matching API](#tag/Map-Matching-API),  * [Matrix API](#tag/Matrix-API),  * [Geocoding API](#tag/Geocoding-API) and  * [Cluster API](#tag/Cluster-API).  # Explore our APIs  ## Get started  1. [Sign up for GraphHopper](https://support.graphhopper.com/a/solutions/articles/44001976025) 2. [Create an API key](https://support.graphhopper.com/a/solutions/articles/44001976027)  Each API part has its own documentation. Jump to the desired API part and learn about the API through the given examples and tutorials.  In addition, for each API there are specific sample requests that you can send via Insomnia or Postman to see what the requests and responses look like.  ## Insomnia  To explore our APIs with [Insomnia](https://insomnia.rest/), follow these steps:  1. Open Insomnia and Import [our workspace](https://raw.githubusercontent.com/graphhopper/directions-api-doc/master/web/restclients/GraphHopper-Direction-API-Insomnia.json). 2. Specify [your API key](https://graphhopper.com/dashboard/#/register) in your workspace: Manage Environments -&gt; Base Environment -&gt; &#x60;\&quot;api_key\&quot;: your API key&#x60; 3. Start exploring  ![Insomnia](./img/insomnia.png)  ## Postman  To explore our APIs with [Postman](https://www.getpostman.com/), follow these steps:  1. Import our [request collections](https://raw.githubusercontent.com/graphhopper/directions-api-doc/master/web/restclients/graphhopper_directions_api.postman_collection.json) as well as our [environment file](https://raw.githubusercontent.com/graphhopper/directions-api-doc/master/web/restclients/graphhopper_directions_api.postman_environment.json). 2. Specify [your API key](https://graphhopper.com/dashboard/#/register) in your environment: &#x60;\&quot;api_key\&quot;: your API key&#x60; 3. Start exploring  ![Postman](./img/postman.png)  ## API Client Libraries  To speed up development and make coding easier, we offer the following client libraries:   * [JavaScript client](https://github.com/graphhopper/directions-api-js-client) - try the [live examples](https://graphhopper.com/api/1/examples/)  * [Others](https://github.com/graphhopper/directions-api-clients) like C#, Ruby, PHP, Python, ... automatically created for the Route Optimization API  ### Bandwidth reduction  If you create your own client, make sure it supports http/2 and gzipped responses for best speed.  If you use the Matrix, the Route Optimization API or the Cluster API and want to solve large problems, we recommend you to reduce bandwidth by [compressing your POST request](https://gist.github.com/karussell/82851e303ea7b3459b2dea01f18949f4) and specifying the header as follows: &#x60;Content-Encoding: gzip&#x60;. This will also avoid the HTTP 413 error \&quot;Request Entity Too Large\&quot;.  ## Contact Us  If you have problems or questions, please read the following information:  - [FAQ](https://graphhopper.com/api/1/docs/FAQ/) - [Public forum](https://discuss.graphhopper.com/c/directions-api) - [Contact us](https://www.graphhopper.com/contact-form/) - [GraphHopper Status Page](https://status.graphhopper.com/)  To stay informed about the latest developments, you can  - follow us on [twitter](https://twitter.com/graphhopper/), - read [our blog](https://graphhopper.com/blog/), - watch [our documentation repository](https://github.com/graphhopper/directions-api-doc), - sign up for our newsletter or - [our forum](https://discuss.graphhopper.com/c/directions-api).  Select the channel you like the most.   # Map Data and Routing Profiles  Currently, our main data source is [OpenStreetMap](https://www.openstreetmap.org). We also integrated other network data providers. This chapter gives an overview about the options you have.  ## OpenStreetMap  #### Geographical Coverage  [OpenStreetMap](https://www.openstreetmap.org) covers the whole world. If you want to see for yourself if we can provide data suitable for your region, please visit [GraphHopper Maps](https://graphhopper.com/maps/). You can edit and modify OpenStreetMap data if you find that important information is missing, e.g. a weight limit for a bridge. [Here](https://wiki.openstreetmap.org/wiki/Beginners%27_guide) is a beginner&#39;s guide that shows how to add data. If you have edited data, we usually consider your data after 1 week at the latest.  #### Supported Vehicle Profiles  The Routing, Matrix and Route Optimization APIs support the following vehicle profiles:  Name       | Description           | Restrictions              | Icon -----------|:----------------------|:--------------------------|:--------------------------------------------------------- car        | Car mode              | car access                | ![car image](https://graphhopper.com/maps/img/car.png) small_truck| Small truck like a Mercedes Sprinter, Ford Transit or Iveco Daily | height&#x3D;2.7m, width&#x3D;2+0.4m, length&#x3D;5.5m, weight&#x3D;2080+1400 kg | ![small truck image](https://graphhopper.com/maps/img/small_truck.png) truck      | Truck like a MAN or Mercedes-Benz Actros | height&#x3D;3.7m, width&#x3D;2.6+0.5m, length&#x3D;12m, weight&#x3D;13000 + 13000 kg, hgv&#x3D;yes, 3 Axes | ![truck image](https://graphhopper.com/maps/img/truck.png) scooter    | Moped mode | Fast inner city, often used for food delivery, is able to ignore certain bollards, maximum speed of roughly 50km/h | ![scooter image](https://graphhopper.com/maps/img/scooter.png) foot       | Pedestrian or walking without dangerous [SAC-scales](https://wiki.openstreetmap.org/wiki/Key:sac_scale) | foot access         | ![foot image](https://graphhopper.com/maps/img/foot.png) hike       | Pedestrian or walking with priority for more beautiful hiking tours and potentially a bit longer than &#x60;foot&#x60;. Walking duration is influenced by elevation differences.  | foot access         | ![hike image](https://graphhopper.com/maps/img/hike.png) bike       | Trekking bike avoiding hills | bike access  | ![bike image](https://graphhopper.com/maps/img/bike.png) mtb        | Mountainbike          | bike access         | ![Mountainbike image](https://graphhopper.com/maps/img/mtb.png) racingbike| Bike preferring roads | bike access         | ![racingbike image](https://graphhopper.com/maps/img/racingbike.png)  Please note:   * all motor vehicles (&#x60;car&#x60;, &#x60;small_truck&#x60;, &#x60;truck&#x60; and &#x60;scooter&#x60;) support turn restrictions via &#x60;turn_costs&#x3D;true&#x60;  * the free package supports only the vehicle profiles &#x60;car&#x60;, &#x60;bike&#x60; or &#x60;foot&#x60;  * up to 2 different vehicle profiles can be used in a single optimization request. The number of vehicles is unaffected and depends on your subscription.  * we offer custom vehicle profiles with different properties, different speed profiles or different access options. To find out more about custom profiles, please [contact us](https://www.graphhopper.com/contact-form/).  * a sophisticated &#x60;motorcycle&#x60; profile is available up on request. It is powered by the [Kurviger](https://kurviger.de/en) Routing API and favors curves and slopes while avoiding cities and highways.   ## TomTom  If you want to include traffic, you can purchase the TomTom Add-on. This Add-on only uses TomTom&#39;s road network and historical traffic information. Live traffic is not yet considered. If you are interested to learn how we consider traffic information, we recommend that you read [this article](https://www.graphhopper.com/blog/2017/11/06/time-dependent-optimization/).  Please note the following:   * Currently we only offer this for our [Route Optimization API](#tag/Route-Optimization-API).  * In addition to our terms, you need to accept TomTom&#39;s [End User License Aggreement](https://www.graphhopper.com/tomtom-end-user-license-agreement/).  * We do *not* use TomTom&#39;s web services. We only use their data with our software.   [Contact us](https://www.graphhopper.com/contact-form/) for more details.  #### Geographical Coverage  We offer  - Europe including Russia - North, Central and South America - Saudi Arabia - United Arab Emirates - South Africa - Australia  #### Supported Vehicle Profiles  Name       | Description           | Restrictions              | Icon -----------|:----------------------|:--------------------------|:--------------------------------------------------------- car        | Car mode              | car access                | ![car image](https://graphhopper.com/maps/img/car.png) small_truck| Small truck like a Mercedes Sprinter, Ford Transit or Iveco Daily | height&#x3D;2.7m, width&#x3D;2+0.4m, length&#x3D;5.5m, weight&#x3D;2080+1400 kg | ![small truck image](https://graphhopper.com/maps/img/small_truck.png) .<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var GraphHopperDirectionsApi = require('index'); // See note below*.
* var xxxSvc = new GraphHopperDirectionsApi.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new GraphHopperDirectionsApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
* and put the application logic within the callback function.</em>
* </p>
* <p>
* A non-AMD browser application (discouraged) might do something like this:
* <pre>
* var xxxSvc = new GraphHopperDirectionsApi.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new GraphHopperDirectionsApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 1.0.0
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The Activity model constructor.
     * @property {module:model/Activity}
     */
    Activity,

    /**
     * The Address model constructor.
     * @property {module:model/Address}
     */
    Address,

    /**
     * The Algorithm model constructor.
     * @property {module:model/Algorithm}
     */
    Algorithm,

    /**
     * The BadRequest model constructor.
     * @property {module:model/BadRequest}
     */
    BadRequest,

    /**
     * The Cluster model constructor.
     * @property {module:model/Cluster}
     */
    Cluster,

    /**
     * The ClusterConfiguration model constructor.
     * @property {module:model/ClusterConfiguration}
     */
    ClusterConfiguration,

    /**
     * The ClusterConfigurationClustering model constructor.
     * @property {module:model/ClusterConfigurationClustering}
     */
    ClusterConfigurationClustering,

    /**
     * The ClusterConfigurationRouting model constructor.
     * @property {module:model/ClusterConfigurationRouting}
     */
    ClusterConfigurationRouting,

    /**
     * The ClusterCustomer model constructor.
     * @property {module:model/ClusterCustomer}
     */
    ClusterCustomer,

    /**
     * The ClusterCustomerAddress model constructor.
     * @property {module:model/ClusterCustomerAddress}
     */
    ClusterCustomerAddress,

    /**
     * The ClusterRequest model constructor.
     * @property {module:model/ClusterRequest}
     */
    ClusterRequest,

    /**
     * The ClusterResponse model constructor.
     * @property {module:model/ClusterResponse}
     */
    ClusterResponse,

    /**
     * The Configuration model constructor.
     * @property {module:model/Configuration}
     */
    Configuration,

    /**
     * The CostMatrix model constructor.
     * @property {module:model/CostMatrix}
     */
    CostMatrix,

    /**
     * The CostMatrixData model constructor.
     * @property {module:model/CostMatrixData}
     */
    CostMatrixData,

    /**
     * The CostMatrixDataInfo model constructor.
     * @property {module:model/CostMatrixDataInfo}
     */
    CostMatrixDataInfo,

    /**
     * The Detail model constructor.
     * @property {module:model/Detail}
     */
    Detail,

    /**
     * The DriveTimeBreak model constructor.
     * @property {module:model/DriveTimeBreak}
     */
    DriveTimeBreak,

    /**
     * The ErrorMessage model constructor.
     * @property {module:model/ErrorMessage}
     */
    ErrorMessage,

    /**
     * The GHError model constructor.
     * @property {module:model/GHError}
     */
    GHError,

    /**
     * The GHErrorHintsInner model constructor.
     * @property {module:model/GHErrorHintsInner}
     */
    GHErrorHintsInner,

    /**
     * The GeocodingLocation model constructor.
     * @property {module:model/GeocodingLocation}
     */
    GeocodingLocation,

    /**
     * The GeocodingPoint model constructor.
     * @property {module:model/GeocodingPoint}
     */
    GeocodingPoint,

    /**
     * The GeocodingResponse model constructor.
     * @property {module:model/GeocodingResponse}
     */
    GeocodingResponse,

    /**
     * The GetClusterSolution404Response model constructor.
     * @property {module:model/GetClusterSolution404Response}
     */
    GetClusterSolution404Response,

    /**
     * The GroupRelation model constructor.
     * @property {module:model/GroupRelation}
     */
    GroupRelation,

    /**
     * The InfoResponse model constructor.
     * @property {module:model/InfoResponse}
     */
    InfoResponse,

    /**
     * The InternalErrorMessage model constructor.
     * @property {module:model/InternalErrorMessage}
     */
    InternalErrorMessage,

    /**
     * The IsochroneResponse model constructor.
     * @property {module:model/IsochroneResponse}
     */
    IsochroneResponse,

    /**
     * The IsochroneResponsePolygon model constructor.
     * @property {module:model/IsochroneResponsePolygon}
     */
    IsochroneResponsePolygon,

    /**
     * The IsochroneResponsePolygonProperties model constructor.
     * @property {module:model/IsochroneResponsePolygonProperties}
     */
    IsochroneResponsePolygonProperties,

    /**
     * The JobId model constructor.
     * @property {module:model/JobId}
     */
    JobId,

    /**
     * The JobRelation model constructor.
     * @property {module:model/JobRelation}
     */
    JobRelation,

    /**
     * The LineString model constructor.
     * @property {module:model/LineString}
     */
    LineString,

    /**
     * The MatrixRequest model constructor.
     * @property {module:model/MatrixRequest}
     */
    MatrixRequest,

    /**
     * The MatrixResponse model constructor.
     * @property {module:model/MatrixResponse}
     */
    MatrixResponse,

    /**
     * The MatrixResponseHintsInner model constructor.
     * @property {module:model/MatrixResponseHintsInner}
     */
    MatrixResponseHintsInner,

    /**
     * The Objective model constructor.
     * @property {module:model/Objective}
     */
    Objective,

    /**
     * The Polygon model constructor.
     * @property {module:model/Polygon}
     */
    Polygon,

    /**
     * The PostMatrixRequest model constructor.
     * @property {module:model/PostMatrixRequest}
     */
    PostMatrixRequest,

    /**
     * The Request model constructor.
     * @property {module:model/Request}
     */
    Request,

    /**
     * The RequestRelationsInner model constructor.
     * @property {module:model/RequestRelationsInner}
     */
    RequestRelationsInner,

    /**
     * The Response model constructor.
     * @property {module:model/Response}
     */
    Response,

    /**
     * The ResponseAddress model constructor.
     * @property {module:model/ResponseAddress}
     */
    ResponseAddress,

    /**
     * The ResponseInfo model constructor.
     * @property {module:model/ResponseInfo}
     */
    ResponseInfo,

    /**
     * The Route model constructor.
     * @property {module:model/Route}
     */
    Route,

    /**
     * The RoutePoint model constructor.
     * @property {module:model/RoutePoint}
     */
    RoutePoint,

    /**
     * The RouteRequest model constructor.
     * @property {module:model/RouteRequest}
     */
    RouteRequest,

    /**
     * The RouteResponse model constructor.
     * @property {module:model/RouteResponse}
     */
    RouteResponse,

    /**
     * The RouteResponsePath model constructor.
     * @property {module:model/RouteResponsePath}
     */
    RouteResponsePath,

    /**
     * The RouteResponsePathInstructionsInner model constructor.
     * @property {module:model/RouteResponsePathInstructionsInner}
     */
    RouteResponsePathInstructionsInner,

    /**
     * The RouteResponsePathPoints model constructor.
     * @property {module:model/RouteResponsePathPoints}
     */
    RouteResponsePathPoints,

    /**
     * The RouteResponsePathSnappedWaypoints model constructor.
     * @property {module:model/RouteResponsePathSnappedWaypoints}
     */
    RouteResponsePathSnappedWaypoints,

    /**
     * The Routing model constructor.
     * @property {module:model/Routing}
     */
    Routing,

    /**
     * The Service model constructor.
     * @property {module:model/Service}
     */
    Service,

    /**
     * The Shipment model constructor.
     * @property {module:model/Shipment}
     */
    Shipment,

    /**
     * The SnappedWaypoint model constructor.
     * @property {module:model/SnappedWaypoint}
     */
    SnappedWaypoint,

    /**
     * The Solution model constructor.
     * @property {module:model/Solution}
     */
    Solution,

    /**
     * The SolutionUnassigned model constructor.
     * @property {module:model/SolutionUnassigned}
     */
    SolutionUnassigned,

    /**
     * The Stop model constructor.
     * @property {module:model/Stop}
     */
    Stop,

    /**
     * The SymmetricalMatrixRequest model constructor.
     * @property {module:model/SymmetricalMatrixRequest}
     */
    SymmetricalMatrixRequest,

    /**
     * The TimeWindow model constructor.
     * @property {module:model/TimeWindow}
     */
    TimeWindow,

    /**
     * The TimeWindowBreak model constructor.
     * @property {module:model/TimeWindowBreak}
     */
    TimeWindowBreak,

    /**
     * The Vehicle model constructor.
     * @property {module:model/Vehicle}
     */
    Vehicle,

    /**
     * The VehicleBreak model constructor.
     * @property {module:model/VehicleBreak}
     */
    VehicleBreak,

    /**
     * The VehicleProfileId model constructor.
     * @property {module:model/VehicleProfileId}
     */
    VehicleProfileId,

    /**
     * The VehicleType model constructor.
     * @property {module:model/VehicleType}
     */
    VehicleType,

    /**
    * The ClusterAPIApi service constructor.
    * @property {module:api/ClusterAPIApi}
    */
    ClusterAPIApi,

    /**
    * The GeocodingAPIApi service constructor.
    * @property {module:api/GeocodingAPIApi}
    */
    GeocodingAPIApi,

    /**
    * The IsochroneAPIApi service constructor.
    * @property {module:api/IsochroneAPIApi}
    */
    IsochroneAPIApi,

    /**
    * The MapMatchingAPIApi service constructor.
    * @property {module:api/MapMatchingAPIApi}
    */
    MapMatchingAPIApi,

    /**
    * The MatrixAPIApi service constructor.
    * @property {module:api/MatrixAPIApi}
    */
    MatrixAPIApi,

    /**
    * The RouteOptimizationAPIApi service constructor.
    * @property {module:api/RouteOptimizationAPIApi}
    */
    RouteOptimizationAPIApi,

    /**
    * The RoutingAPIApi service constructor.
    * @property {module:api/RoutingAPIApi}
    */
    RoutingAPIApi
};
