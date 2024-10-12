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

#include "OAIRouting.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRouting::OAIRouting(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRouting::OAIRouting() {
    this->initializeModel();
}

OAIRouting::~OAIRouting() {}

void OAIRouting::initializeModel() {

    m_calc_points_isSet = false;
    m_calc_points_isValid = false;

    m_consider_traffic_isSet = false;
    m_consider_traffic_isValid = false;

    m_curbside_strictness_isSet = false;
    m_curbside_strictness_isValid = false;

    m_fail_fast_isSet = false;
    m_fail_fast_isValid = false;

    m_network_data_provider_isSet = false;
    m_network_data_provider_isValid = false;

    m_return_snapped_waypoints_isSet = false;
    m_return_snapped_waypoints_isValid = false;

    m_snap_preventions_isSet = false;
    m_snap_preventions_isValid = false;
}

void OAIRouting::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRouting::fromJsonObject(QJsonObject json) {

    m_calc_points_isValid = ::OpenAPI::fromJsonValue(m_calc_points, json[QString("calc_points")]);
    m_calc_points_isSet = !json[QString("calc_points")].isNull() && m_calc_points_isValid;

    m_consider_traffic_isValid = ::OpenAPI::fromJsonValue(m_consider_traffic, json[QString("consider_traffic")]);
    m_consider_traffic_isSet = !json[QString("consider_traffic")].isNull() && m_consider_traffic_isValid;

    m_curbside_strictness_isValid = ::OpenAPI::fromJsonValue(m_curbside_strictness, json[QString("curbside_strictness")]);
    m_curbside_strictness_isSet = !json[QString("curbside_strictness")].isNull() && m_curbside_strictness_isValid;

    m_fail_fast_isValid = ::OpenAPI::fromJsonValue(m_fail_fast, json[QString("fail_fast")]);
    m_fail_fast_isSet = !json[QString("fail_fast")].isNull() && m_fail_fast_isValid;

    m_network_data_provider_isValid = ::OpenAPI::fromJsonValue(m_network_data_provider, json[QString("network_data_provider")]);
    m_network_data_provider_isSet = !json[QString("network_data_provider")].isNull() && m_network_data_provider_isValid;

    m_return_snapped_waypoints_isValid = ::OpenAPI::fromJsonValue(m_return_snapped_waypoints, json[QString("return_snapped_waypoints")]);
    m_return_snapped_waypoints_isSet = !json[QString("return_snapped_waypoints")].isNull() && m_return_snapped_waypoints_isValid;

    m_snap_preventions_isValid = ::OpenAPI::fromJsonValue(m_snap_preventions, json[QString("snap_preventions")]);
    m_snap_preventions_isSet = !json[QString("snap_preventions")].isNull() && m_snap_preventions_isValid;
}

QString OAIRouting::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRouting::asJsonObject() const {
    QJsonObject obj;
    if (m_calc_points_isSet) {
        obj.insert(QString("calc_points"), ::OpenAPI::toJsonValue(m_calc_points));
    }
    if (m_consider_traffic_isSet) {
        obj.insert(QString("consider_traffic"), ::OpenAPI::toJsonValue(m_consider_traffic));
    }
    if (m_curbside_strictness_isSet) {
        obj.insert(QString("curbside_strictness"), ::OpenAPI::toJsonValue(m_curbside_strictness));
    }
    if (m_fail_fast_isSet) {
        obj.insert(QString("fail_fast"), ::OpenAPI::toJsonValue(m_fail_fast));
    }
    if (m_network_data_provider_isSet) {
        obj.insert(QString("network_data_provider"), ::OpenAPI::toJsonValue(m_network_data_provider));
    }
    if (m_return_snapped_waypoints_isSet) {
        obj.insert(QString("return_snapped_waypoints"), ::OpenAPI::toJsonValue(m_return_snapped_waypoints));
    }
    if (m_snap_preventions.size() > 0) {
        obj.insert(QString("snap_preventions"), ::OpenAPI::toJsonValue(m_snap_preventions));
    }
    return obj;
}

bool OAIRouting::isCalcPoints() const {
    return m_calc_points;
}
void OAIRouting::setCalcPoints(const bool &calc_points) {
    m_calc_points = calc_points;
    m_calc_points_isSet = true;
}

bool OAIRouting::is_calc_points_Set() const{
    return m_calc_points_isSet;
}

bool OAIRouting::is_calc_points_Valid() const{
    return m_calc_points_isValid;
}

bool OAIRouting::isConsiderTraffic() const {
    return m_consider_traffic;
}
void OAIRouting::setConsiderTraffic(const bool &consider_traffic) {
    m_consider_traffic = consider_traffic;
    m_consider_traffic_isSet = true;
}

bool OAIRouting::is_consider_traffic_Set() const{
    return m_consider_traffic_isSet;
}

bool OAIRouting::is_consider_traffic_Valid() const{
    return m_consider_traffic_isValid;
}

QString OAIRouting::getCurbsideStrictness() const {
    return m_curbside_strictness;
}
void OAIRouting::setCurbsideStrictness(const QString &curbside_strictness) {
    m_curbside_strictness = curbside_strictness;
    m_curbside_strictness_isSet = true;
}

bool OAIRouting::is_curbside_strictness_Set() const{
    return m_curbside_strictness_isSet;
}

bool OAIRouting::is_curbside_strictness_Valid() const{
    return m_curbside_strictness_isValid;
}

bool OAIRouting::isFailFast() const {
    return m_fail_fast;
}
void OAIRouting::setFailFast(const bool &fail_fast) {
    m_fail_fast = fail_fast;
    m_fail_fast_isSet = true;
}

bool OAIRouting::is_fail_fast_Set() const{
    return m_fail_fast_isSet;
}

bool OAIRouting::is_fail_fast_Valid() const{
    return m_fail_fast_isValid;
}

QString OAIRouting::getNetworkDataProvider() const {
    return m_network_data_provider;
}
void OAIRouting::setNetworkDataProvider(const QString &network_data_provider) {
    m_network_data_provider = network_data_provider;
    m_network_data_provider_isSet = true;
}

bool OAIRouting::is_network_data_provider_Set() const{
    return m_network_data_provider_isSet;
}

bool OAIRouting::is_network_data_provider_Valid() const{
    return m_network_data_provider_isValid;
}

bool OAIRouting::isReturnSnappedWaypoints() const {
    return m_return_snapped_waypoints;
}
void OAIRouting::setReturnSnappedWaypoints(const bool &return_snapped_waypoints) {
    m_return_snapped_waypoints = return_snapped_waypoints;
    m_return_snapped_waypoints_isSet = true;
}

bool OAIRouting::is_return_snapped_waypoints_Set() const{
    return m_return_snapped_waypoints_isSet;
}

bool OAIRouting::is_return_snapped_waypoints_Valid() const{
    return m_return_snapped_waypoints_isValid;
}

QList<QString> OAIRouting::getSnapPreventions() const {
    return m_snap_preventions;
}
void OAIRouting::setSnapPreventions(const QList<QString> &snap_preventions) {
    m_snap_preventions = snap_preventions;
    m_snap_preventions_isSet = true;
}

bool OAIRouting::is_snap_preventions_Set() const{
    return m_snap_preventions_isSet;
}

bool OAIRouting::is_snap_preventions_Valid() const{
    return m_snap_preventions_isValid;
}

bool OAIRouting::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_calc_points_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_consider_traffic_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_curbside_strictness_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fail_fast_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_network_data_provider_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_return_snapped_waypoints_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_snap_preventions.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRouting::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
