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

#include "OAIShipment.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIShipment::OAIShipment(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIShipment::OAIShipment() {
    this->initializeModel();
}

OAIShipment::~OAIShipment() {}

void OAIShipment::initializeModel() {

    m_allowed_vehicles_isSet = false;
    m_allowed_vehicles_isValid = false;

    m_delivery_isSet = false;
    m_delivery_isValid = false;

    m_disallowed_vehicles_isSet = false;
    m_disallowed_vehicles_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_max_time_in_vehicle_isSet = false;
    m_max_time_in_vehicle_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_pickup_isSet = false;
    m_pickup_isValid = false;

    m_priority_isSet = false;
    m_priority_isValid = false;

    m_required_skills_isSet = false;
    m_required_skills_isValid = false;

    m_size_isSet = false;
    m_size_isValid = false;
}

void OAIShipment::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIShipment::fromJsonObject(QJsonObject json) {

    m_allowed_vehicles_isValid = ::OpenAPI::fromJsonValue(m_allowed_vehicles, json[QString("allowed_vehicles")]);
    m_allowed_vehicles_isSet = !json[QString("allowed_vehicles")].isNull() && m_allowed_vehicles_isValid;

    m_delivery_isValid = ::OpenAPI::fromJsonValue(m_delivery, json[QString("delivery")]);
    m_delivery_isSet = !json[QString("delivery")].isNull() && m_delivery_isValid;

    m_disallowed_vehicles_isValid = ::OpenAPI::fromJsonValue(m_disallowed_vehicles, json[QString("disallowed_vehicles")]);
    m_disallowed_vehicles_isSet = !json[QString("disallowed_vehicles")].isNull() && m_disallowed_vehicles_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_max_time_in_vehicle_isValid = ::OpenAPI::fromJsonValue(m_max_time_in_vehicle, json[QString("max_time_in_vehicle")]);
    m_max_time_in_vehicle_isSet = !json[QString("max_time_in_vehicle")].isNull() && m_max_time_in_vehicle_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_pickup_isValid = ::OpenAPI::fromJsonValue(m_pickup, json[QString("pickup")]);
    m_pickup_isSet = !json[QString("pickup")].isNull() && m_pickup_isValid;

    m_priority_isValid = ::OpenAPI::fromJsonValue(m_priority, json[QString("priority")]);
    m_priority_isSet = !json[QString("priority")].isNull() && m_priority_isValid;

    m_required_skills_isValid = ::OpenAPI::fromJsonValue(m_required_skills, json[QString("required_skills")]);
    m_required_skills_isSet = !json[QString("required_skills")].isNull() && m_required_skills_isValid;

    m_size_isValid = ::OpenAPI::fromJsonValue(m_size, json[QString("size")]);
    m_size_isSet = !json[QString("size")].isNull() && m_size_isValid;
}

QString OAIShipment::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIShipment::asJsonObject() const {
    QJsonObject obj;
    if (m_allowed_vehicles.size() > 0) {
        obj.insert(QString("allowed_vehicles"), ::OpenAPI::toJsonValue(m_allowed_vehicles));
    }
    if (m_delivery.isSet()) {
        obj.insert(QString("delivery"), ::OpenAPI::toJsonValue(m_delivery));
    }
    if (m_disallowed_vehicles.size() > 0) {
        obj.insert(QString("disallowed_vehicles"), ::OpenAPI::toJsonValue(m_disallowed_vehicles));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_max_time_in_vehicle_isSet) {
        obj.insert(QString("max_time_in_vehicle"), ::OpenAPI::toJsonValue(m_max_time_in_vehicle));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_pickup.isSet()) {
        obj.insert(QString("pickup"), ::OpenAPI::toJsonValue(m_pickup));
    }
    if (m_priority_isSet) {
        obj.insert(QString("priority"), ::OpenAPI::toJsonValue(m_priority));
    }
    if (m_required_skills.size() > 0) {
        obj.insert(QString("required_skills"), ::OpenAPI::toJsonValue(m_required_skills));
    }
    if (m_size.size() > 0) {
        obj.insert(QString("size"), ::OpenAPI::toJsonValue(m_size));
    }
    return obj;
}

QList<QString> OAIShipment::getAllowedVehicles() const {
    return m_allowed_vehicles;
}
void OAIShipment::setAllowedVehicles(const QList<QString> &allowed_vehicles) {
    m_allowed_vehicles = allowed_vehicles;
    m_allowed_vehicles_isSet = true;
}

bool OAIShipment::is_allowed_vehicles_Set() const{
    return m_allowed_vehicles_isSet;
}

bool OAIShipment::is_allowed_vehicles_Valid() const{
    return m_allowed_vehicles_isValid;
}

OAIStop OAIShipment::getDelivery() const {
    return m_delivery;
}
void OAIShipment::setDelivery(const OAIStop &delivery) {
    m_delivery = delivery;
    m_delivery_isSet = true;
}

bool OAIShipment::is_delivery_Set() const{
    return m_delivery_isSet;
}

bool OAIShipment::is_delivery_Valid() const{
    return m_delivery_isValid;
}

QList<QString> OAIShipment::getDisallowedVehicles() const {
    return m_disallowed_vehicles;
}
void OAIShipment::setDisallowedVehicles(const QList<QString> &disallowed_vehicles) {
    m_disallowed_vehicles = disallowed_vehicles;
    m_disallowed_vehicles_isSet = true;
}

bool OAIShipment::is_disallowed_vehicles_Set() const{
    return m_disallowed_vehicles_isSet;
}

bool OAIShipment::is_disallowed_vehicles_Valid() const{
    return m_disallowed_vehicles_isValid;
}

QString OAIShipment::getId() const {
    return m_id;
}
void OAIShipment::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIShipment::is_id_Set() const{
    return m_id_isSet;
}

bool OAIShipment::is_id_Valid() const{
    return m_id_isValid;
}

qint64 OAIShipment::getMaxTimeInVehicle() const {
    return m_max_time_in_vehicle;
}
void OAIShipment::setMaxTimeInVehicle(const qint64 &max_time_in_vehicle) {
    m_max_time_in_vehicle = max_time_in_vehicle;
    m_max_time_in_vehicle_isSet = true;
}

bool OAIShipment::is_max_time_in_vehicle_Set() const{
    return m_max_time_in_vehicle_isSet;
}

bool OAIShipment::is_max_time_in_vehicle_Valid() const{
    return m_max_time_in_vehicle_isValid;
}

QString OAIShipment::getName() const {
    return m_name;
}
void OAIShipment::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIShipment::is_name_Set() const{
    return m_name_isSet;
}

bool OAIShipment::is_name_Valid() const{
    return m_name_isValid;
}

OAIStop OAIShipment::getPickup() const {
    return m_pickup;
}
void OAIShipment::setPickup(const OAIStop &pickup) {
    m_pickup = pickup;
    m_pickup_isSet = true;
}

bool OAIShipment::is_pickup_Set() const{
    return m_pickup_isSet;
}

bool OAIShipment::is_pickup_Valid() const{
    return m_pickup_isValid;
}

qint32 OAIShipment::getPriority() const {
    return m_priority;
}
void OAIShipment::setPriority(const qint32 &priority) {
    m_priority = priority;
    m_priority_isSet = true;
}

bool OAIShipment::is_priority_Set() const{
    return m_priority_isSet;
}

bool OAIShipment::is_priority_Valid() const{
    return m_priority_isValid;
}

QList<QString> OAIShipment::getRequiredSkills() const {
    return m_required_skills;
}
void OAIShipment::setRequiredSkills(const QList<QString> &required_skills) {
    m_required_skills = required_skills;
    m_required_skills_isSet = true;
}

bool OAIShipment::is_required_skills_Set() const{
    return m_required_skills_isSet;
}

bool OAIShipment::is_required_skills_Valid() const{
    return m_required_skills_isValid;
}

QList<qint32> OAIShipment::getSize() const {
    return m_size;
}
void OAIShipment::setSize(const QList<qint32> &size) {
    m_size = size;
    m_size_isSet = true;
}

bool OAIShipment::is_size_Set() const{
    return m_size_isSet;
}

bool OAIShipment::is_size_Valid() const{
    return m_size_isValid;
}

bool OAIShipment::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_allowed_vehicles.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_delivery.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_disallowed_vehicles.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_max_time_in_vehicle_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pickup.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_priority_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_required_skills.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_size.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIShipment::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_delivery_isValid && m_id_isValid && m_pickup_isValid && true;
}

} // namespace OpenAPI
