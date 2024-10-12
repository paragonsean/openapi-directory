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
 */

#include "OAIRouteRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRouteRequest::OAIRouteRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRouteRequest::OAIRouteRequest() {
    this->initializeModel();
}

OAIRouteRequest::~OAIRouteRequest() {}

void OAIRouteRequest::initializeModel() {

    m_algorithm_isSet = false;
    m_algorithm_isValid = false;

    m_alternative_route_max_paths_isSet = false;
    m_alternative_route_max_paths_isValid = false;

    m_alternative_route_max_share_factor_isSet = false;
    m_alternative_route_max_share_factor_isValid = false;

    m_alternative_route_max_weight_factor_isSet = false;
    m_alternative_route_max_weight_factor_isValid = false;

    m_avoid_isSet = false;
    m_avoid_isValid = false;

    m_block_area_isSet = false;
    m_block_area_isValid = false;

    m_calc_points_isSet = false;
    m_calc_points_isValid = false;

    m_ch_disable_isSet = false;
    m_ch_disable_isValid = false;

    m_curbsides_isSet = false;
    m_curbsides_isValid = false;

    m_debug_isSet = false;
    m_debug_isValid = false;

    m_details_isSet = false;
    m_details_isValid = false;

    m_elevation_isSet = false;
    m_elevation_isValid = false;

    m_heading_penalty_isSet = false;
    m_heading_penalty_isValid = false;

    m_headings_isSet = false;
    m_headings_isValid = false;

    m_instructions_isSet = false;
    m_instructions_isValid = false;

    m_locale_isSet = false;
    m_locale_isValid = false;

    m_optimize_isSet = false;
    m_optimize_isValid = false;

    m_pass_through_isSet = false;
    m_pass_through_isValid = false;

    m_point_hints_isSet = false;
    m_point_hints_isValid = false;

    m_points_isSet = false;
    m_points_isValid = false;

    m_points_encoded_isSet = false;
    m_points_encoded_isValid = false;

    m_round_trip_distance_isSet = false;
    m_round_trip_distance_isValid = false;

    m_round_trip_seed_isSet = false;
    m_round_trip_seed_isValid = false;

    m_snap_preventions_isSet = false;
    m_snap_preventions_isValid = false;

    m_vehicle_isSet = false;
    m_vehicle_isValid = false;

    m_weighting_isSet = false;
    m_weighting_isValid = false;
}

void OAIRouteRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRouteRequest::fromJsonObject(QJsonObject json) {

    m_algorithm_isValid = ::OpenAPI::fromJsonValue(m_algorithm, json[QString("algorithm")]);
    m_algorithm_isSet = !json[QString("algorithm")].isNull() && m_algorithm_isValid;

    m_alternative_route_max_paths_isValid = ::OpenAPI::fromJsonValue(m_alternative_route_max_paths, json[QString("alternative_route.max_paths")]);
    m_alternative_route_max_paths_isSet = !json[QString("alternative_route.max_paths")].isNull() && m_alternative_route_max_paths_isValid;

    m_alternative_route_max_share_factor_isValid = ::OpenAPI::fromJsonValue(m_alternative_route_max_share_factor, json[QString("alternative_route.max_share_factor")]);
    m_alternative_route_max_share_factor_isSet = !json[QString("alternative_route.max_share_factor")].isNull() && m_alternative_route_max_share_factor_isValid;

    m_alternative_route_max_weight_factor_isValid = ::OpenAPI::fromJsonValue(m_alternative_route_max_weight_factor, json[QString("alternative_route.max_weight_factor")]);
    m_alternative_route_max_weight_factor_isSet = !json[QString("alternative_route.max_weight_factor")].isNull() && m_alternative_route_max_weight_factor_isValid;

    m_avoid_isValid = ::OpenAPI::fromJsonValue(m_avoid, json[QString("avoid")]);
    m_avoid_isSet = !json[QString("avoid")].isNull() && m_avoid_isValid;

    m_block_area_isValid = ::OpenAPI::fromJsonValue(m_block_area, json[QString("block_area")]);
    m_block_area_isSet = !json[QString("block_area")].isNull() && m_block_area_isValid;

    m_calc_points_isValid = ::OpenAPI::fromJsonValue(m_calc_points, json[QString("calc_points")]);
    m_calc_points_isSet = !json[QString("calc_points")].isNull() && m_calc_points_isValid;

    m_ch_disable_isValid = ::OpenAPI::fromJsonValue(m_ch_disable, json[QString("ch.disable")]);
    m_ch_disable_isSet = !json[QString("ch.disable")].isNull() && m_ch_disable_isValid;

    m_curbsides_isValid = ::OpenAPI::fromJsonValue(m_curbsides, json[QString("curbsides")]);
    m_curbsides_isSet = !json[QString("curbsides")].isNull() && m_curbsides_isValid;

    m_debug_isValid = ::OpenAPI::fromJsonValue(m_debug, json[QString("debug")]);
    m_debug_isSet = !json[QString("debug")].isNull() && m_debug_isValid;

    m_details_isValid = ::OpenAPI::fromJsonValue(m_details, json[QString("details")]);
    m_details_isSet = !json[QString("details")].isNull() && m_details_isValid;

    m_elevation_isValid = ::OpenAPI::fromJsonValue(m_elevation, json[QString("elevation")]);
    m_elevation_isSet = !json[QString("elevation")].isNull() && m_elevation_isValid;

    m_heading_penalty_isValid = ::OpenAPI::fromJsonValue(m_heading_penalty, json[QString("heading_penalty")]);
    m_heading_penalty_isSet = !json[QString("heading_penalty")].isNull() && m_heading_penalty_isValid;

    m_headings_isValid = ::OpenAPI::fromJsonValue(m_headings, json[QString("headings")]);
    m_headings_isSet = !json[QString("headings")].isNull() && m_headings_isValid;

    m_instructions_isValid = ::OpenAPI::fromJsonValue(m_instructions, json[QString("instructions")]);
    m_instructions_isSet = !json[QString("instructions")].isNull() && m_instructions_isValid;

    m_locale_isValid = ::OpenAPI::fromJsonValue(m_locale, json[QString("locale")]);
    m_locale_isSet = !json[QString("locale")].isNull() && m_locale_isValid;

    m_optimize_isValid = ::OpenAPI::fromJsonValue(m_optimize, json[QString("optimize")]);
    m_optimize_isSet = !json[QString("optimize")].isNull() && m_optimize_isValid;

    m_pass_through_isValid = ::OpenAPI::fromJsonValue(m_pass_through, json[QString("pass_through")]);
    m_pass_through_isSet = !json[QString("pass_through")].isNull() && m_pass_through_isValid;

    m_point_hints_isValid = ::OpenAPI::fromJsonValue(m_point_hints, json[QString("point_hints")]);
    m_point_hints_isSet = !json[QString("point_hints")].isNull() && m_point_hints_isValid;

    if(json["points"].isArray()){
        auto arr = json["points"].toArray();
        m_points_isValid = true;
        if(arr.count() > 0) {
            for (const QJsonValue jval : arr) {
                QList<double> item;
                m_points_isValid &= ::OpenAPI::fromJsonValue(item, jval);
                m_points_isSet = !jval.isNull() && m_points_isValid;
                m_points.push_back(item);
            }
        }
    }

    m_points_encoded_isValid = ::OpenAPI::fromJsonValue(m_points_encoded, json[QString("points_encoded")]);
    m_points_encoded_isSet = !json[QString("points_encoded")].isNull() && m_points_encoded_isValid;

    m_round_trip_distance_isValid = ::OpenAPI::fromJsonValue(m_round_trip_distance, json[QString("round_trip.distance")]);
    m_round_trip_distance_isSet = !json[QString("round_trip.distance")].isNull() && m_round_trip_distance_isValid;

    m_round_trip_seed_isValid = ::OpenAPI::fromJsonValue(m_round_trip_seed, json[QString("round_trip.seed")]);
    m_round_trip_seed_isSet = !json[QString("round_trip.seed")].isNull() && m_round_trip_seed_isValid;

    m_snap_preventions_isValid = ::OpenAPI::fromJsonValue(m_snap_preventions, json[QString("snap_preventions")]);
    m_snap_preventions_isSet = !json[QString("snap_preventions")].isNull() && m_snap_preventions_isValid;

    m_vehicle_isValid = ::OpenAPI::fromJsonValue(m_vehicle, json[QString("vehicle")]);
    m_vehicle_isSet = !json[QString("vehicle")].isNull() && m_vehicle_isValid;

    m_weighting_isValid = ::OpenAPI::fromJsonValue(m_weighting, json[QString("weighting")]);
    m_weighting_isSet = !json[QString("weighting")].isNull() && m_weighting_isValid;
}

QString OAIRouteRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRouteRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_algorithm_isSet) {
        obj.insert(QString("algorithm"), ::OpenAPI::toJsonValue(m_algorithm));
    }
    if (m_alternative_route_max_paths_isSet) {
        obj.insert(QString("alternative_route.max_paths"), ::OpenAPI::toJsonValue(m_alternative_route_max_paths));
    }
    if (m_alternative_route_max_share_factor_isSet) {
        obj.insert(QString("alternative_route.max_share_factor"), ::OpenAPI::toJsonValue(m_alternative_route_max_share_factor));
    }
    if (m_alternative_route_max_weight_factor_isSet) {
        obj.insert(QString("alternative_route.max_weight_factor"), ::OpenAPI::toJsonValue(m_alternative_route_max_weight_factor));
    }
    if (m_avoid_isSet) {
        obj.insert(QString("avoid"), ::OpenAPI::toJsonValue(m_avoid));
    }
    if (m_block_area_isSet) {
        obj.insert(QString("block_area"), ::OpenAPI::toJsonValue(m_block_area));
    }
    if (m_calc_points_isSet) {
        obj.insert(QString("calc_points"), ::OpenAPI::toJsonValue(m_calc_points));
    }
    if (m_ch_disable_isSet) {
        obj.insert(QString("ch.disable"), ::OpenAPI::toJsonValue(m_ch_disable));
    }
    if (m_curbsides.size() > 0) {
        obj.insert(QString("curbsides"), ::OpenAPI::toJsonValue(m_curbsides));
    }
    if (m_debug_isSet) {
        obj.insert(QString("debug"), ::OpenAPI::toJsonValue(m_debug));
    }
    if (m_details.size() > 0) {
        obj.insert(QString("details"), ::OpenAPI::toJsonValue(m_details));
    }
    if (m_elevation_isSet) {
        obj.insert(QString("elevation"), ::OpenAPI::toJsonValue(m_elevation));
    }
    if (m_heading_penalty_isSet) {
        obj.insert(QString("heading_penalty"), ::OpenAPI::toJsonValue(m_heading_penalty));
    }
    if (m_headings.size() > 0) {
        obj.insert(QString("headings"), ::OpenAPI::toJsonValue(m_headings));
    }
    if (m_instructions_isSet) {
        obj.insert(QString("instructions"), ::OpenAPI::toJsonValue(m_instructions));
    }
    if (m_locale_isSet) {
        obj.insert(QString("locale"), ::OpenAPI::toJsonValue(m_locale));
    }
    if (m_optimize_isSet) {
        obj.insert(QString("optimize"), ::OpenAPI::toJsonValue(m_optimize));
    }
    if (m_pass_through_isSet) {
        obj.insert(QString("pass_through"), ::OpenAPI::toJsonValue(m_pass_through));
    }
    if (m_point_hints.size() > 0) {
        obj.insert(QString("point_hints"), ::OpenAPI::toJsonValue(m_point_hints));
    }
    if (m_points.size() > 0) {
        
        obj.insert(QString("points"), toJsonValue(m_points));
    }
    if (m_points_encoded_isSet) {
        obj.insert(QString("points_encoded"), ::OpenAPI::toJsonValue(m_points_encoded));
    }
    if (m_round_trip_distance_isSet) {
        obj.insert(QString("round_trip.distance"), ::OpenAPI::toJsonValue(m_round_trip_distance));
    }
    if (m_round_trip_seed_isSet) {
        obj.insert(QString("round_trip.seed"), ::OpenAPI::toJsonValue(m_round_trip_seed));
    }
    if (m_snap_preventions.size() > 0) {
        obj.insert(QString("snap_preventions"), ::OpenAPI::toJsonValue(m_snap_preventions));
    }
    if (m_vehicle.isSet()) {
        obj.insert(QString("vehicle"), ::OpenAPI::toJsonValue(m_vehicle));
    }
    if (m_weighting_isSet) {
        obj.insert(QString("weighting"), ::OpenAPI::toJsonValue(m_weighting));
    }
    return obj;
}

QString OAIRouteRequest::getAlgorithm() const {
    return m_algorithm;
}
void OAIRouteRequest::setAlgorithm(const QString &algorithm) {
    m_algorithm = algorithm;
    m_algorithm_isSet = true;
}

bool OAIRouteRequest::is_algorithm_Set() const{
    return m_algorithm_isSet;
}

bool OAIRouteRequest::is_algorithm_Valid() const{
    return m_algorithm_isValid;
}

qint32 OAIRouteRequest::getAlternativeRouteMaxPaths() const {
    return m_alternative_route_max_paths;
}
void OAIRouteRequest::setAlternativeRouteMaxPaths(const qint32 &alternative_route_max_paths) {
    m_alternative_route_max_paths = alternative_route_max_paths;
    m_alternative_route_max_paths_isSet = true;
}

bool OAIRouteRequest::is_alternative_route_max_paths_Set() const{
    return m_alternative_route_max_paths_isSet;
}

bool OAIRouteRequest::is_alternative_route_max_paths_Valid() const{
    return m_alternative_route_max_paths_isValid;
}

double OAIRouteRequest::getAlternativeRouteMaxShareFactor() const {
    return m_alternative_route_max_share_factor;
}
void OAIRouteRequest::setAlternativeRouteMaxShareFactor(const double &alternative_route_max_share_factor) {
    m_alternative_route_max_share_factor = alternative_route_max_share_factor;
    m_alternative_route_max_share_factor_isSet = true;
}

bool OAIRouteRequest::is_alternative_route_max_share_factor_Set() const{
    return m_alternative_route_max_share_factor_isSet;
}

bool OAIRouteRequest::is_alternative_route_max_share_factor_Valid() const{
    return m_alternative_route_max_share_factor_isValid;
}

double OAIRouteRequest::getAlternativeRouteMaxWeightFactor() const {
    return m_alternative_route_max_weight_factor;
}
void OAIRouteRequest::setAlternativeRouteMaxWeightFactor(const double &alternative_route_max_weight_factor) {
    m_alternative_route_max_weight_factor = alternative_route_max_weight_factor;
    m_alternative_route_max_weight_factor_isSet = true;
}

bool OAIRouteRequest::is_alternative_route_max_weight_factor_Set() const{
    return m_alternative_route_max_weight_factor_isSet;
}

bool OAIRouteRequest::is_alternative_route_max_weight_factor_Valid() const{
    return m_alternative_route_max_weight_factor_isValid;
}

QString OAIRouteRequest::getAvoid() const {
    return m_avoid;
}
void OAIRouteRequest::setAvoid(const QString &avoid) {
    m_avoid = avoid;
    m_avoid_isSet = true;
}

bool OAIRouteRequest::is_avoid_Set() const{
    return m_avoid_isSet;
}

bool OAIRouteRequest::is_avoid_Valid() const{
    return m_avoid_isValid;
}

QString OAIRouteRequest::getBlockArea() const {
    return m_block_area;
}
void OAIRouteRequest::setBlockArea(const QString &block_area) {
    m_block_area = block_area;
    m_block_area_isSet = true;
}

bool OAIRouteRequest::is_block_area_Set() const{
    return m_block_area_isSet;
}

bool OAIRouteRequest::is_block_area_Valid() const{
    return m_block_area_isValid;
}

bool OAIRouteRequest::isCalcPoints() const {
    return m_calc_points;
}
void OAIRouteRequest::setCalcPoints(const bool &calc_points) {
    m_calc_points = calc_points;
    m_calc_points_isSet = true;
}

bool OAIRouteRequest::is_calc_points_Set() const{
    return m_calc_points_isSet;
}

bool OAIRouteRequest::is_calc_points_Valid() const{
    return m_calc_points_isValid;
}

bool OAIRouteRequest::isChDisable() const {
    return m_ch_disable;
}
void OAIRouteRequest::setChDisable(const bool &ch_disable) {
    m_ch_disable = ch_disable;
    m_ch_disable_isSet = true;
}

bool OAIRouteRequest::is_ch_disable_Set() const{
    return m_ch_disable_isSet;
}

bool OAIRouteRequest::is_ch_disable_Valid() const{
    return m_ch_disable_isValid;
}

QList<QString> OAIRouteRequest::getCurbsides() const {
    return m_curbsides;
}
void OAIRouteRequest::setCurbsides(const QList<QString> &curbsides) {
    m_curbsides = curbsides;
    m_curbsides_isSet = true;
}

bool OAIRouteRequest::is_curbsides_Set() const{
    return m_curbsides_isSet;
}

bool OAIRouteRequest::is_curbsides_Valid() const{
    return m_curbsides_isValid;
}

bool OAIRouteRequest::isDebug() const {
    return m_debug;
}
void OAIRouteRequest::setDebug(const bool &debug) {
    m_debug = debug;
    m_debug_isSet = true;
}

bool OAIRouteRequest::is_debug_Set() const{
    return m_debug_isSet;
}

bool OAIRouteRequest::is_debug_Valid() const{
    return m_debug_isValid;
}

QList<QString> OAIRouteRequest::getDetails() const {
    return m_details;
}
void OAIRouteRequest::setDetails(const QList<QString> &details) {
    m_details = details;
    m_details_isSet = true;
}

bool OAIRouteRequest::is_details_Set() const{
    return m_details_isSet;
}

bool OAIRouteRequest::is_details_Valid() const{
    return m_details_isValid;
}

bool OAIRouteRequest::isElevation() const {
    return m_elevation;
}
void OAIRouteRequest::setElevation(const bool &elevation) {
    m_elevation = elevation;
    m_elevation_isSet = true;
}

bool OAIRouteRequest::is_elevation_Set() const{
    return m_elevation_isSet;
}

bool OAIRouteRequest::is_elevation_Valid() const{
    return m_elevation_isValid;
}

qint32 OAIRouteRequest::getHeadingPenalty() const {
    return m_heading_penalty;
}
void OAIRouteRequest::setHeadingPenalty(const qint32 &heading_penalty) {
    m_heading_penalty = heading_penalty;
    m_heading_penalty_isSet = true;
}

bool OAIRouteRequest::is_heading_penalty_Set() const{
    return m_heading_penalty_isSet;
}

bool OAIRouteRequest::is_heading_penalty_Valid() const{
    return m_heading_penalty_isValid;
}

QList<qint32> OAIRouteRequest::getHeadings() const {
    return m_headings;
}
void OAIRouteRequest::setHeadings(const QList<qint32> &headings) {
    m_headings = headings;
    m_headings_isSet = true;
}

bool OAIRouteRequest::is_headings_Set() const{
    return m_headings_isSet;
}

bool OAIRouteRequest::is_headings_Valid() const{
    return m_headings_isValid;
}

bool OAIRouteRequest::isInstructions() const {
    return m_instructions;
}
void OAIRouteRequest::setInstructions(const bool &instructions) {
    m_instructions = instructions;
    m_instructions_isSet = true;
}

bool OAIRouteRequest::is_instructions_Set() const{
    return m_instructions_isSet;
}

bool OAIRouteRequest::is_instructions_Valid() const{
    return m_instructions_isValid;
}

QString OAIRouteRequest::getLocale() const {
    return m_locale;
}
void OAIRouteRequest::setLocale(const QString &locale) {
    m_locale = locale;
    m_locale_isSet = true;
}

bool OAIRouteRequest::is_locale_Set() const{
    return m_locale_isSet;
}

bool OAIRouteRequest::is_locale_Valid() const{
    return m_locale_isValid;
}

QString OAIRouteRequest::getOptimize() const {
    return m_optimize;
}
void OAIRouteRequest::setOptimize(const QString &optimize) {
    m_optimize = optimize;
    m_optimize_isSet = true;
}

bool OAIRouteRequest::is_optimize_Set() const{
    return m_optimize_isSet;
}

bool OAIRouteRequest::is_optimize_Valid() const{
    return m_optimize_isValid;
}

bool OAIRouteRequest::isPassThrough() const {
    return m_pass_through;
}
void OAIRouteRequest::setPassThrough(const bool &pass_through) {
    m_pass_through = pass_through;
    m_pass_through_isSet = true;
}

bool OAIRouteRequest::is_pass_through_Set() const{
    return m_pass_through_isSet;
}

bool OAIRouteRequest::is_pass_through_Valid() const{
    return m_pass_through_isValid;
}

QList<QString> OAIRouteRequest::getPointHints() const {
    return m_point_hints;
}
void OAIRouteRequest::setPointHints(const QList<QString> &point_hints) {
    m_point_hints = point_hints;
    m_point_hints_isSet = true;
}

bool OAIRouteRequest::is_point_hints_Set() const{
    return m_point_hints_isSet;
}

bool OAIRouteRequest::is_point_hints_Valid() const{
    return m_point_hints_isValid;
}

QList<QList<double>> OAIRouteRequest::getPoints() const {
    return m_points;
}
void OAIRouteRequest::setPoints(const QList<QList<double>> &points) {
    m_points = points;
    m_points_isSet = true;
}

bool OAIRouteRequest::is_points_Set() const{
    return m_points_isSet;
}

bool OAIRouteRequest::is_points_Valid() const{
    return m_points_isValid;
}

bool OAIRouteRequest::isPointsEncoded() const {
    return m_points_encoded;
}
void OAIRouteRequest::setPointsEncoded(const bool &points_encoded) {
    m_points_encoded = points_encoded;
    m_points_encoded_isSet = true;
}

bool OAIRouteRequest::is_points_encoded_Set() const{
    return m_points_encoded_isSet;
}

bool OAIRouteRequest::is_points_encoded_Valid() const{
    return m_points_encoded_isValid;
}

qint32 OAIRouteRequest::getRoundTripDistance() const {
    return m_round_trip_distance;
}
void OAIRouteRequest::setRoundTripDistance(const qint32 &round_trip_distance) {
    m_round_trip_distance = round_trip_distance;
    m_round_trip_distance_isSet = true;
}

bool OAIRouteRequest::is_round_trip_distance_Set() const{
    return m_round_trip_distance_isSet;
}

bool OAIRouteRequest::is_round_trip_distance_Valid() const{
    return m_round_trip_distance_isValid;
}

qint64 OAIRouteRequest::getRoundTripSeed() const {
    return m_round_trip_seed;
}
void OAIRouteRequest::setRoundTripSeed(const qint64 &round_trip_seed) {
    m_round_trip_seed = round_trip_seed;
    m_round_trip_seed_isSet = true;
}

bool OAIRouteRequest::is_round_trip_seed_Set() const{
    return m_round_trip_seed_isSet;
}

bool OAIRouteRequest::is_round_trip_seed_Valid() const{
    return m_round_trip_seed_isValid;
}

QList<QString> OAIRouteRequest::getSnapPreventions() const {
    return m_snap_preventions;
}
void OAIRouteRequest::setSnapPreventions(const QList<QString> &snap_preventions) {
    m_snap_preventions = snap_preventions;
    m_snap_preventions_isSet = true;
}

bool OAIRouteRequest::is_snap_preventions_Set() const{
    return m_snap_preventions_isSet;
}

bool OAIRouteRequest::is_snap_preventions_Valid() const{
    return m_snap_preventions_isValid;
}

OAIVehicleProfileId OAIRouteRequest::getVehicle() const {
    return m_vehicle;
}
void OAIRouteRequest::setVehicle(const OAIVehicleProfileId &vehicle) {
    m_vehicle = vehicle;
    m_vehicle_isSet = true;
}

bool OAIRouteRequest::is_vehicle_Set() const{
    return m_vehicle_isSet;
}

bool OAIRouteRequest::is_vehicle_Valid() const{
    return m_vehicle_isValid;
}

QString OAIRouteRequest::getWeighting() const {
    return m_weighting;
}
void OAIRouteRequest::setWeighting(const QString &weighting) {
    m_weighting = weighting;
    m_weighting_isSet = true;
}

bool OAIRouteRequest::is_weighting_Set() const{
    return m_weighting_isSet;
}

bool OAIRouteRequest::is_weighting_Valid() const{
    return m_weighting_isValid;
}

bool OAIRouteRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_algorithm_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_alternative_route_max_paths_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_alternative_route_max_share_factor_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_alternative_route_max_weight_factor_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_avoid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_block_area_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_calc_points_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ch_disable_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_curbsides.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_debug_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_details.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_elevation_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_heading_penalty_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_headings.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_instructions_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_locale_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_optimize_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pass_through_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_point_hints.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_points.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_points_encoded_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_round_trip_distance_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_round_trip_seed_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_snap_preventions.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_vehicle.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_weighting_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRouteRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
