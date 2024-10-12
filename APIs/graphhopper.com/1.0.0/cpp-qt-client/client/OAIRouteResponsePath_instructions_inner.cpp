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

#include "OAIRouteResponsePath_instructions_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRouteResponsePath_instructions_inner::OAIRouteResponsePath_instructions_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRouteResponsePath_instructions_inner::OAIRouteResponsePath_instructions_inner() {
    this->initializeModel();
}

OAIRouteResponsePath_instructions_inner::~OAIRouteResponsePath_instructions_inner() {}

void OAIRouteResponsePath_instructions_inner::initializeModel() {

    m_distance_isSet = false;
    m_distance_isValid = false;

    m_exit_number_isSet = false;
    m_exit_number_isValid = false;

    m_interval_isSet = false;
    m_interval_isValid = false;

    m_sign_isSet = false;
    m_sign_isValid = false;

    m_street_name_isSet = false;
    m_street_name_isValid = false;

    m_text_isSet = false;
    m_text_isValid = false;

    m_time_isSet = false;
    m_time_isValid = false;

    m_turn_angle_isSet = false;
    m_turn_angle_isValid = false;
}

void OAIRouteResponsePath_instructions_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRouteResponsePath_instructions_inner::fromJsonObject(QJsonObject json) {

    m_distance_isValid = ::OpenAPI::fromJsonValue(m_distance, json[QString("distance")]);
    m_distance_isSet = !json[QString("distance")].isNull() && m_distance_isValid;

    m_exit_number_isValid = ::OpenAPI::fromJsonValue(m_exit_number, json[QString("exit_number")]);
    m_exit_number_isSet = !json[QString("exit_number")].isNull() && m_exit_number_isValid;

    m_interval_isValid = ::OpenAPI::fromJsonValue(m_interval, json[QString("interval")]);
    m_interval_isSet = !json[QString("interval")].isNull() && m_interval_isValid;

    m_sign_isValid = ::OpenAPI::fromJsonValue(m_sign, json[QString("sign")]);
    m_sign_isSet = !json[QString("sign")].isNull() && m_sign_isValid;

    m_street_name_isValid = ::OpenAPI::fromJsonValue(m_street_name, json[QString("street_name")]);
    m_street_name_isSet = !json[QString("street_name")].isNull() && m_street_name_isValid;

    m_text_isValid = ::OpenAPI::fromJsonValue(m_text, json[QString("text")]);
    m_text_isSet = !json[QString("text")].isNull() && m_text_isValid;

    m_time_isValid = ::OpenAPI::fromJsonValue(m_time, json[QString("time")]);
    m_time_isSet = !json[QString("time")].isNull() && m_time_isValid;

    m_turn_angle_isValid = ::OpenAPI::fromJsonValue(m_turn_angle, json[QString("turn_angle")]);
    m_turn_angle_isSet = !json[QString("turn_angle")].isNull() && m_turn_angle_isValid;
}

QString OAIRouteResponsePath_instructions_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRouteResponsePath_instructions_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_distance_isSet) {
        obj.insert(QString("distance"), ::OpenAPI::toJsonValue(m_distance));
    }
    if (m_exit_number_isSet) {
        obj.insert(QString("exit_number"), ::OpenAPI::toJsonValue(m_exit_number));
    }
    if (m_interval.size() > 0) {
        obj.insert(QString("interval"), ::OpenAPI::toJsonValue(m_interval));
    }
    if (m_sign_isSet) {
        obj.insert(QString("sign"), ::OpenAPI::toJsonValue(m_sign));
    }
    if (m_street_name_isSet) {
        obj.insert(QString("street_name"), ::OpenAPI::toJsonValue(m_street_name));
    }
    if (m_text_isSet) {
        obj.insert(QString("text"), ::OpenAPI::toJsonValue(m_text));
    }
    if (m_time_isSet) {
        obj.insert(QString("time"), ::OpenAPI::toJsonValue(m_time));
    }
    if (m_turn_angle_isSet) {
        obj.insert(QString("turn_angle"), ::OpenAPI::toJsonValue(m_turn_angle));
    }
    return obj;
}

double OAIRouteResponsePath_instructions_inner::getDistance() const {
    return m_distance;
}
void OAIRouteResponsePath_instructions_inner::setDistance(const double &distance) {
    m_distance = distance;
    m_distance_isSet = true;
}

bool OAIRouteResponsePath_instructions_inner::is_distance_Set() const{
    return m_distance_isSet;
}

bool OAIRouteResponsePath_instructions_inner::is_distance_Valid() const{
    return m_distance_isValid;
}

qint32 OAIRouteResponsePath_instructions_inner::getExitNumber() const {
    return m_exit_number;
}
void OAIRouteResponsePath_instructions_inner::setExitNumber(const qint32 &exit_number) {
    m_exit_number = exit_number;
    m_exit_number_isSet = true;
}

bool OAIRouteResponsePath_instructions_inner::is_exit_number_Set() const{
    return m_exit_number_isSet;
}

bool OAIRouteResponsePath_instructions_inner::is_exit_number_Valid() const{
    return m_exit_number_isValid;
}

QList<qint32> OAIRouteResponsePath_instructions_inner::getInterval() const {
    return m_interval;
}
void OAIRouteResponsePath_instructions_inner::setInterval(const QList<qint32> &interval) {
    m_interval = interval;
    m_interval_isSet = true;
}

bool OAIRouteResponsePath_instructions_inner::is_interval_Set() const{
    return m_interval_isSet;
}

bool OAIRouteResponsePath_instructions_inner::is_interval_Valid() const{
    return m_interval_isValid;
}

qint32 OAIRouteResponsePath_instructions_inner::getSign() const {
    return m_sign;
}
void OAIRouteResponsePath_instructions_inner::setSign(const qint32 &sign) {
    m_sign = sign;
    m_sign_isSet = true;
}

bool OAIRouteResponsePath_instructions_inner::is_sign_Set() const{
    return m_sign_isSet;
}

bool OAIRouteResponsePath_instructions_inner::is_sign_Valid() const{
    return m_sign_isValid;
}

QString OAIRouteResponsePath_instructions_inner::getStreetName() const {
    return m_street_name;
}
void OAIRouteResponsePath_instructions_inner::setStreetName(const QString &street_name) {
    m_street_name = street_name;
    m_street_name_isSet = true;
}

bool OAIRouteResponsePath_instructions_inner::is_street_name_Set() const{
    return m_street_name_isSet;
}

bool OAIRouteResponsePath_instructions_inner::is_street_name_Valid() const{
    return m_street_name_isValid;
}

QString OAIRouteResponsePath_instructions_inner::getText() const {
    return m_text;
}
void OAIRouteResponsePath_instructions_inner::setText(const QString &text) {
    m_text = text;
    m_text_isSet = true;
}

bool OAIRouteResponsePath_instructions_inner::is_text_Set() const{
    return m_text_isSet;
}

bool OAIRouteResponsePath_instructions_inner::is_text_Valid() const{
    return m_text_isValid;
}

qint32 OAIRouteResponsePath_instructions_inner::getTime() const {
    return m_time;
}
void OAIRouteResponsePath_instructions_inner::setTime(const qint32 &time) {
    m_time = time;
    m_time_isSet = true;
}

bool OAIRouteResponsePath_instructions_inner::is_time_Set() const{
    return m_time_isSet;
}

bool OAIRouteResponsePath_instructions_inner::is_time_Valid() const{
    return m_time_isValid;
}

double OAIRouteResponsePath_instructions_inner::getTurnAngle() const {
    return m_turn_angle;
}
void OAIRouteResponsePath_instructions_inner::setTurnAngle(const double &turn_angle) {
    m_turn_angle = turn_angle;
    m_turn_angle_isSet = true;
}

bool OAIRouteResponsePath_instructions_inner::is_turn_angle_Set() const{
    return m_turn_angle_isSet;
}

bool OAIRouteResponsePath_instructions_inner::is_turn_angle_Valid() const{
    return m_turn_angle_isValid;
}

bool OAIRouteResponsePath_instructions_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_distance_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_exit_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_interval.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_sign_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_street_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_text_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_turn_angle_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRouteResponsePath_instructions_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
