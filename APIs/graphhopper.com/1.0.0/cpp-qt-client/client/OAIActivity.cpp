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

#include "OAIActivity.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIActivity::OAIActivity(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIActivity::OAIActivity() {
    this->initializeModel();
}

OAIActivity::~OAIActivity() {}

void OAIActivity::initializeModel() {

    m_address_isSet = false;
    m_address_isValid = false;

    m_arr_date_time_isSet = false;
    m_arr_date_time_isValid = false;

    m_arr_time_isSet = false;
    m_arr_time_isValid = false;

    m_distance_isSet = false;
    m_distance_isValid = false;

    m_driving_time_isSet = false;
    m_driving_time_isValid = false;

    m_end_date_time_isSet = false;
    m_end_date_time_isValid = false;

    m_end_time_isSet = false;
    m_end_time_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_load_after_isSet = false;
    m_load_after_isValid = false;

    m_load_before_isSet = false;
    m_load_before_isValid = false;

    m_location_id_isSet = false;
    m_location_id_isValid = false;

    m_preparation_time_isSet = false;
    m_preparation_time_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_waiting_time_isSet = false;
    m_waiting_time_isValid = false;
}

void OAIActivity::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIActivity::fromJsonObject(QJsonObject json) {

    m_address_isValid = ::OpenAPI::fromJsonValue(m_address, json[QString("address")]);
    m_address_isSet = !json[QString("address")].isNull() && m_address_isValid;

    m_arr_date_time_isValid = ::OpenAPI::fromJsonValue(m_arr_date_time, json[QString("arr_date_time")]);
    m_arr_date_time_isSet = !json[QString("arr_date_time")].isNull() && m_arr_date_time_isValid;

    m_arr_time_isValid = ::OpenAPI::fromJsonValue(m_arr_time, json[QString("arr_time")]);
    m_arr_time_isSet = !json[QString("arr_time")].isNull() && m_arr_time_isValid;

    m_distance_isValid = ::OpenAPI::fromJsonValue(m_distance, json[QString("distance")]);
    m_distance_isSet = !json[QString("distance")].isNull() && m_distance_isValid;

    m_driving_time_isValid = ::OpenAPI::fromJsonValue(m_driving_time, json[QString("driving_time")]);
    m_driving_time_isSet = !json[QString("driving_time")].isNull() && m_driving_time_isValid;

    m_end_date_time_isValid = ::OpenAPI::fromJsonValue(m_end_date_time, json[QString("end_date_time")]);
    m_end_date_time_isSet = !json[QString("end_date_time")].isNull() && m_end_date_time_isValid;

    m_end_time_isValid = ::OpenAPI::fromJsonValue(m_end_time, json[QString("end_time")]);
    m_end_time_isSet = !json[QString("end_time")].isNull() && m_end_time_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_load_after_isValid = ::OpenAPI::fromJsonValue(m_load_after, json[QString("load_after")]);
    m_load_after_isSet = !json[QString("load_after")].isNull() && m_load_after_isValid;

    m_load_before_isValid = ::OpenAPI::fromJsonValue(m_load_before, json[QString("load_before")]);
    m_load_before_isSet = !json[QString("load_before")].isNull() && m_load_before_isValid;

    m_location_id_isValid = ::OpenAPI::fromJsonValue(m_location_id, json[QString("location_id")]);
    m_location_id_isSet = !json[QString("location_id")].isNull() && m_location_id_isValid;

    m_preparation_time_isValid = ::OpenAPI::fromJsonValue(m_preparation_time, json[QString("preparation_time")]);
    m_preparation_time_isSet = !json[QString("preparation_time")].isNull() && m_preparation_time_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_waiting_time_isValid = ::OpenAPI::fromJsonValue(m_waiting_time, json[QString("waiting_time")]);
    m_waiting_time_isSet = !json[QString("waiting_time")].isNull() && m_waiting_time_isValid;
}

QString OAIActivity::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIActivity::asJsonObject() const {
    QJsonObject obj;
    if (m_address.isSet()) {
        obj.insert(QString("address"), ::OpenAPI::toJsonValue(m_address));
    }
    if (m_arr_date_time_isSet) {
        obj.insert(QString("arr_date_time"), ::OpenAPI::toJsonValue(m_arr_date_time));
    }
    if (m_arr_time_isSet) {
        obj.insert(QString("arr_time"), ::OpenAPI::toJsonValue(m_arr_time));
    }
    if (m_distance_isSet) {
        obj.insert(QString("distance"), ::OpenAPI::toJsonValue(m_distance));
    }
    if (m_driving_time_isSet) {
        obj.insert(QString("driving_time"), ::OpenAPI::toJsonValue(m_driving_time));
    }
    if (m_end_date_time_isSet) {
        obj.insert(QString("end_date_time"), ::OpenAPI::toJsonValue(m_end_date_time));
    }
    if (m_end_time_isSet) {
        obj.insert(QString("end_time"), ::OpenAPI::toJsonValue(m_end_time));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_load_after.size() > 0) {
        obj.insert(QString("load_after"), ::OpenAPI::toJsonValue(m_load_after));
    }
    if (m_load_before.size() > 0) {
        obj.insert(QString("load_before"), ::OpenAPI::toJsonValue(m_load_before));
    }
    if (m_location_id_isSet) {
        obj.insert(QString("location_id"), ::OpenAPI::toJsonValue(m_location_id));
    }
    if (m_preparation_time_isSet) {
        obj.insert(QString("preparation_time"), ::OpenAPI::toJsonValue(m_preparation_time));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_waiting_time_isSet) {
        obj.insert(QString("waiting_time"), ::OpenAPI::toJsonValue(m_waiting_time));
    }
    return obj;
}

OAIResponseAddress OAIActivity::getAddress() const {
    return m_address;
}
void OAIActivity::setAddress(const OAIResponseAddress &address) {
    m_address = address;
    m_address_isSet = true;
}

bool OAIActivity::is_address_Set() const{
    return m_address_isSet;
}

bool OAIActivity::is_address_Valid() const{
    return m_address_isValid;
}

QDateTime OAIActivity::getArrDateTime() const {
    return m_arr_date_time;
}
void OAIActivity::setArrDateTime(const QDateTime &arr_date_time) {
    m_arr_date_time = arr_date_time;
    m_arr_date_time_isSet = true;
}

bool OAIActivity::is_arr_date_time_Set() const{
    return m_arr_date_time_isSet;
}

bool OAIActivity::is_arr_date_time_Valid() const{
    return m_arr_date_time_isValid;
}

qint64 OAIActivity::getArrTime() const {
    return m_arr_time;
}
void OAIActivity::setArrTime(const qint64 &arr_time) {
    m_arr_time = arr_time;
    m_arr_time_isSet = true;
}

bool OAIActivity::is_arr_time_Set() const{
    return m_arr_time_isSet;
}

bool OAIActivity::is_arr_time_Valid() const{
    return m_arr_time_isValid;
}

qint64 OAIActivity::getDistance() const {
    return m_distance;
}
void OAIActivity::setDistance(const qint64 &distance) {
    m_distance = distance;
    m_distance_isSet = true;
}

bool OAIActivity::is_distance_Set() const{
    return m_distance_isSet;
}

bool OAIActivity::is_distance_Valid() const{
    return m_distance_isValid;
}

qint64 OAIActivity::getDrivingTime() const {
    return m_driving_time;
}
void OAIActivity::setDrivingTime(const qint64 &driving_time) {
    m_driving_time = driving_time;
    m_driving_time_isSet = true;
}

bool OAIActivity::is_driving_time_Set() const{
    return m_driving_time_isSet;
}

bool OAIActivity::is_driving_time_Valid() const{
    return m_driving_time_isValid;
}

QDateTime OAIActivity::getEndDateTime() const {
    return m_end_date_time;
}
void OAIActivity::setEndDateTime(const QDateTime &end_date_time) {
    m_end_date_time = end_date_time;
    m_end_date_time_isSet = true;
}

bool OAIActivity::is_end_date_time_Set() const{
    return m_end_date_time_isSet;
}

bool OAIActivity::is_end_date_time_Valid() const{
    return m_end_date_time_isValid;
}

qint64 OAIActivity::getEndTime() const {
    return m_end_time;
}
void OAIActivity::setEndTime(const qint64 &end_time) {
    m_end_time = end_time;
    m_end_time_isSet = true;
}

bool OAIActivity::is_end_time_Set() const{
    return m_end_time_isSet;
}

bool OAIActivity::is_end_time_Valid() const{
    return m_end_time_isValid;
}

QString OAIActivity::getId() const {
    return m_id;
}
void OAIActivity::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIActivity::is_id_Set() const{
    return m_id_isSet;
}

bool OAIActivity::is_id_Valid() const{
    return m_id_isValid;
}

QList<qint32> OAIActivity::getLoadAfter() const {
    return m_load_after;
}
void OAIActivity::setLoadAfter(const QList<qint32> &load_after) {
    m_load_after = load_after;
    m_load_after_isSet = true;
}

bool OAIActivity::is_load_after_Set() const{
    return m_load_after_isSet;
}

bool OAIActivity::is_load_after_Valid() const{
    return m_load_after_isValid;
}

QList<qint32> OAIActivity::getLoadBefore() const {
    return m_load_before;
}
void OAIActivity::setLoadBefore(const QList<qint32> &load_before) {
    m_load_before = load_before;
    m_load_before_isSet = true;
}

bool OAIActivity::is_load_before_Set() const{
    return m_load_before_isSet;
}

bool OAIActivity::is_load_before_Valid() const{
    return m_load_before_isValid;
}

QString OAIActivity::getLocationId() const {
    return m_location_id;
}
void OAIActivity::setLocationId(const QString &location_id) {
    m_location_id = location_id;
    m_location_id_isSet = true;
}

bool OAIActivity::is_location_id_Set() const{
    return m_location_id_isSet;
}

bool OAIActivity::is_location_id_Valid() const{
    return m_location_id_isValid;
}

qint64 OAIActivity::getPreparationTime() const {
    return m_preparation_time;
}
void OAIActivity::setPreparationTime(const qint64 &preparation_time) {
    m_preparation_time = preparation_time;
    m_preparation_time_isSet = true;
}

bool OAIActivity::is_preparation_time_Set() const{
    return m_preparation_time_isSet;
}

bool OAIActivity::is_preparation_time_Valid() const{
    return m_preparation_time_isValid;
}

QString OAIActivity::getType() const {
    return m_type;
}
void OAIActivity::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIActivity::is_type_Set() const{
    return m_type_isSet;
}

bool OAIActivity::is_type_Valid() const{
    return m_type_isValid;
}

qint64 OAIActivity::getWaitingTime() const {
    return m_waiting_time;
}
void OAIActivity::setWaitingTime(const qint64 &waiting_time) {
    m_waiting_time = waiting_time;
    m_waiting_time_isSet = true;
}

bool OAIActivity::is_waiting_time_Set() const{
    return m_waiting_time_isSet;
}

bool OAIActivity::is_waiting_time_Valid() const{
    return m_waiting_time_isValid;
}

bool OAIActivity::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_address.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_arr_date_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_arr_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_distance_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_driving_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_end_date_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_end_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_load_after.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_load_before.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_location_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_preparation_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_waiting_time_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIActivity::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
