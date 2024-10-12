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

#include "OAIRouteResponsePath.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRouteResponsePath::OAIRouteResponsePath(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRouteResponsePath::OAIRouteResponsePath() {
    this->initializeModel();
}

OAIRouteResponsePath::~OAIRouteResponsePath() {}

void OAIRouteResponsePath::initializeModel() {

    m_ascend_isSet = false;
    m_ascend_isValid = false;

    m_bbox_isSet = false;
    m_bbox_isValid = false;

    m_descend_isSet = false;
    m_descend_isValid = false;

    m_details_isSet = false;
    m_details_isValid = false;

    m_distance_isSet = false;
    m_distance_isValid = false;

    m_instructions_isSet = false;
    m_instructions_isValid = false;

    m_points_isSet = false;
    m_points_isValid = false;

    m_points_encoded_isSet = false;
    m_points_encoded_isValid = false;

    m_points_order_isSet = false;
    m_points_order_isValid = false;

    m_snapped_waypoints_isSet = false;
    m_snapped_waypoints_isValid = false;

    m_time_isSet = false;
    m_time_isValid = false;
}

void OAIRouteResponsePath::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRouteResponsePath::fromJsonObject(QJsonObject json) {

    m_ascend_isValid = ::OpenAPI::fromJsonValue(m_ascend, json[QString("ascend")]);
    m_ascend_isSet = !json[QString("ascend")].isNull() && m_ascend_isValid;

    m_bbox_isValid = ::OpenAPI::fromJsonValue(m_bbox, json[QString("bbox")]);
    m_bbox_isSet = !json[QString("bbox")].isNull() && m_bbox_isValid;

    m_descend_isValid = ::OpenAPI::fromJsonValue(m_descend, json[QString("descend")]);
    m_descend_isSet = !json[QString("descend")].isNull() && m_descend_isValid;

    m_details_isValid = ::OpenAPI::fromJsonValue(m_details, json[QString("details")]);
    m_details_isSet = !json[QString("details")].isNull() && m_details_isValid;

    m_distance_isValid = ::OpenAPI::fromJsonValue(m_distance, json[QString("distance")]);
    m_distance_isSet = !json[QString("distance")].isNull() && m_distance_isValid;

    m_instructions_isValid = ::OpenAPI::fromJsonValue(m_instructions, json[QString("instructions")]);
    m_instructions_isSet = !json[QString("instructions")].isNull() && m_instructions_isValid;

    m_points_isValid = ::OpenAPI::fromJsonValue(m_points, json[QString("points")]);
    m_points_isSet = !json[QString("points")].isNull() && m_points_isValid;

    m_points_encoded_isValid = ::OpenAPI::fromJsonValue(m_points_encoded, json[QString("points_encoded")]);
    m_points_encoded_isSet = !json[QString("points_encoded")].isNull() && m_points_encoded_isValid;

    m_points_order_isValid = ::OpenAPI::fromJsonValue(m_points_order, json[QString("points_order")]);
    m_points_order_isSet = !json[QString("points_order")].isNull() && m_points_order_isValid;

    m_snapped_waypoints_isValid = ::OpenAPI::fromJsonValue(m_snapped_waypoints, json[QString("snapped_waypoints")]);
    m_snapped_waypoints_isSet = !json[QString("snapped_waypoints")].isNull() && m_snapped_waypoints_isValid;

    m_time_isValid = ::OpenAPI::fromJsonValue(m_time, json[QString("time")]);
    m_time_isSet = !json[QString("time")].isNull() && m_time_isValid;
}

QString OAIRouteResponsePath::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRouteResponsePath::asJsonObject() const {
    QJsonObject obj;
    if (m_ascend_isSet) {
        obj.insert(QString("ascend"), ::OpenAPI::toJsonValue(m_ascend));
    }
    if (m_bbox.size() > 0) {
        obj.insert(QString("bbox"), ::OpenAPI::toJsonValue(m_bbox));
    }
    if (m_descend_isSet) {
        obj.insert(QString("descend"), ::OpenAPI::toJsonValue(m_descend));
    }
    if (m_details_isSet) {
        obj.insert(QString("details"), ::OpenAPI::toJsonValue(m_details));
    }
    if (m_distance_isSet) {
        obj.insert(QString("distance"), ::OpenAPI::toJsonValue(m_distance));
    }
    if (m_instructions.size() > 0) {
        obj.insert(QString("instructions"), ::OpenAPI::toJsonValue(m_instructions));
    }
    if (m_points.isSet()) {
        obj.insert(QString("points"), ::OpenAPI::toJsonValue(m_points));
    }
    if (m_points_encoded_isSet) {
        obj.insert(QString("points_encoded"), ::OpenAPI::toJsonValue(m_points_encoded));
    }
    if (m_points_order.size() > 0) {
        obj.insert(QString("points_order"), ::OpenAPI::toJsonValue(m_points_order));
    }
    if (m_snapped_waypoints.isSet()) {
        obj.insert(QString("snapped_waypoints"), ::OpenAPI::toJsonValue(m_snapped_waypoints));
    }
    if (m_time_isSet) {
        obj.insert(QString("time"), ::OpenAPI::toJsonValue(m_time));
    }
    return obj;
}

double OAIRouteResponsePath::getAscend() const {
    return m_ascend;
}
void OAIRouteResponsePath::setAscend(const double &ascend) {
    m_ascend = ascend;
    m_ascend_isSet = true;
}

bool OAIRouteResponsePath::is_ascend_Set() const{
    return m_ascend_isSet;
}

bool OAIRouteResponsePath::is_ascend_Valid() const{
    return m_ascend_isValid;
}

QList<double> OAIRouteResponsePath::getBbox() const {
    return m_bbox;
}
void OAIRouteResponsePath::setBbox(const QList<double> &bbox) {
    m_bbox = bbox;
    m_bbox_isSet = true;
}

bool OAIRouteResponsePath::is_bbox_Set() const{
    return m_bbox_isSet;
}

bool OAIRouteResponsePath::is_bbox_Valid() const{
    return m_bbox_isValid;
}

double OAIRouteResponsePath::getDescend() const {
    return m_descend;
}
void OAIRouteResponsePath::setDescend(const double &descend) {
    m_descend = descend;
    m_descend_isSet = true;
}

bool OAIRouteResponsePath::is_descend_Set() const{
    return m_descend_isSet;
}

bool OAIRouteResponsePath::is_descend_Valid() const{
    return m_descend_isValid;
}

OAIObject OAIRouteResponsePath::getDetails() const {
    return m_details;
}
void OAIRouteResponsePath::setDetails(const OAIObject &details) {
    m_details = details;
    m_details_isSet = true;
}

bool OAIRouteResponsePath::is_details_Set() const{
    return m_details_isSet;
}

bool OAIRouteResponsePath::is_details_Valid() const{
    return m_details_isValid;
}

double OAIRouteResponsePath::getDistance() const {
    return m_distance;
}
void OAIRouteResponsePath::setDistance(const double &distance) {
    m_distance = distance;
    m_distance_isSet = true;
}

bool OAIRouteResponsePath::is_distance_Set() const{
    return m_distance_isSet;
}

bool OAIRouteResponsePath::is_distance_Valid() const{
    return m_distance_isValid;
}

QList<OAIRouteResponsePath_instructions_inner> OAIRouteResponsePath::getInstructions() const {
    return m_instructions;
}
void OAIRouteResponsePath::setInstructions(const QList<OAIRouteResponsePath_instructions_inner> &instructions) {
    m_instructions = instructions;
    m_instructions_isSet = true;
}

bool OAIRouteResponsePath::is_instructions_Set() const{
    return m_instructions_isSet;
}

bool OAIRouteResponsePath::is_instructions_Valid() const{
    return m_instructions_isValid;
}

OAIRouteResponsePath_points OAIRouteResponsePath::getPoints() const {
    return m_points;
}
void OAIRouteResponsePath::setPoints(const OAIRouteResponsePath_points &points) {
    m_points = points;
    m_points_isSet = true;
}

bool OAIRouteResponsePath::is_points_Set() const{
    return m_points_isSet;
}

bool OAIRouteResponsePath::is_points_Valid() const{
    return m_points_isValid;
}

bool OAIRouteResponsePath::isPointsEncoded() const {
    return m_points_encoded;
}
void OAIRouteResponsePath::setPointsEncoded(const bool &points_encoded) {
    m_points_encoded = points_encoded;
    m_points_encoded_isSet = true;
}

bool OAIRouteResponsePath::is_points_encoded_Set() const{
    return m_points_encoded_isSet;
}

bool OAIRouteResponsePath::is_points_encoded_Valid() const{
    return m_points_encoded_isValid;
}

QList<qint32> OAIRouteResponsePath::getPointsOrder() const {
    return m_points_order;
}
void OAIRouteResponsePath::setPointsOrder(const QList<qint32> &points_order) {
    m_points_order = points_order;
    m_points_order_isSet = true;
}

bool OAIRouteResponsePath::is_points_order_Set() const{
    return m_points_order_isSet;
}

bool OAIRouteResponsePath::is_points_order_Valid() const{
    return m_points_order_isValid;
}

OAIRouteResponsePath_snapped_waypoints OAIRouteResponsePath::getSnappedWaypoints() const {
    return m_snapped_waypoints;
}
void OAIRouteResponsePath::setSnappedWaypoints(const OAIRouteResponsePath_snapped_waypoints &snapped_waypoints) {
    m_snapped_waypoints = snapped_waypoints;
    m_snapped_waypoints_isSet = true;
}

bool OAIRouteResponsePath::is_snapped_waypoints_Set() const{
    return m_snapped_waypoints_isSet;
}

bool OAIRouteResponsePath::is_snapped_waypoints_Valid() const{
    return m_snapped_waypoints_isValid;
}

qint64 OAIRouteResponsePath::getTime() const {
    return m_time;
}
void OAIRouteResponsePath::setTime(const qint64 &time) {
    m_time = time;
    m_time_isSet = true;
}

bool OAIRouteResponsePath::is_time_Set() const{
    return m_time_isSet;
}

bool OAIRouteResponsePath::is_time_Valid() const{
    return m_time_isValid;
}

bool OAIRouteResponsePath::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_ascend_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_bbox.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_descend_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_details_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_distance_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_instructions.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_points.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_points_encoded_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_points_order.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_snapped_waypoints.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_time_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRouteResponsePath::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
