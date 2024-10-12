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

#include "OAIVehicle.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIVehicle::OAIVehicle(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIVehicle::OAIVehicle() {
    this->initializeModel();
}

OAIVehicle::~OAIVehicle() {}

void OAIVehicle::initializeModel() {

    m_r_break_isSet = false;
    m_r_break_isValid = false;

    m_earliest_start_isSet = false;
    m_earliest_start_isValid = false;

    m_end_address_isSet = false;
    m_end_address_isValid = false;

    m_latest_end_isSet = false;
    m_latest_end_isValid = false;

    m_max_activities_isSet = false;
    m_max_activities_isValid = false;

    m_max_distance_isSet = false;
    m_max_distance_isValid = false;

    m_max_driving_time_isSet = false;
    m_max_driving_time_isValid = false;

    m_max_jobs_isSet = false;
    m_max_jobs_isValid = false;

    m_min_jobs_isSet = false;
    m_min_jobs_isValid = false;

    m_move_to_end_address_isSet = false;
    m_move_to_end_address_isValid = false;

    m_return_to_depot_isSet = false;
    m_return_to_depot_isValid = false;

    m_skills_isSet = false;
    m_skills_isValid = false;

    m_start_address_isSet = false;
    m_start_address_isValid = false;

    m_type_id_isSet = false;
    m_type_id_isValid = false;

    m_vehicle_id_isSet = false;
    m_vehicle_id_isValid = false;
}

void OAIVehicle::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIVehicle::fromJsonObject(QJsonObject json) {

    m_r_break_isValid = ::OpenAPI::fromJsonValue(m_r_break, json[QString("break")]);
    m_r_break_isSet = !json[QString("break")].isNull() && m_r_break_isValid;

    m_earliest_start_isValid = ::OpenAPI::fromJsonValue(m_earliest_start, json[QString("earliest_start")]);
    m_earliest_start_isSet = !json[QString("earliest_start")].isNull() && m_earliest_start_isValid;

    m_end_address_isValid = ::OpenAPI::fromJsonValue(m_end_address, json[QString("end_address")]);
    m_end_address_isSet = !json[QString("end_address")].isNull() && m_end_address_isValid;

    m_latest_end_isValid = ::OpenAPI::fromJsonValue(m_latest_end, json[QString("latest_end")]);
    m_latest_end_isSet = !json[QString("latest_end")].isNull() && m_latest_end_isValid;

    m_max_activities_isValid = ::OpenAPI::fromJsonValue(m_max_activities, json[QString("max_activities")]);
    m_max_activities_isSet = !json[QString("max_activities")].isNull() && m_max_activities_isValid;

    m_max_distance_isValid = ::OpenAPI::fromJsonValue(m_max_distance, json[QString("max_distance")]);
    m_max_distance_isSet = !json[QString("max_distance")].isNull() && m_max_distance_isValid;

    m_max_driving_time_isValid = ::OpenAPI::fromJsonValue(m_max_driving_time, json[QString("max_driving_time")]);
    m_max_driving_time_isSet = !json[QString("max_driving_time")].isNull() && m_max_driving_time_isValid;

    m_max_jobs_isValid = ::OpenAPI::fromJsonValue(m_max_jobs, json[QString("max_jobs")]);
    m_max_jobs_isSet = !json[QString("max_jobs")].isNull() && m_max_jobs_isValid;

    m_min_jobs_isValid = ::OpenAPI::fromJsonValue(m_min_jobs, json[QString("min_jobs")]);
    m_min_jobs_isSet = !json[QString("min_jobs")].isNull() && m_min_jobs_isValid;

    m_move_to_end_address_isValid = ::OpenAPI::fromJsonValue(m_move_to_end_address, json[QString("move_to_end_address")]);
    m_move_to_end_address_isSet = !json[QString("move_to_end_address")].isNull() && m_move_to_end_address_isValid;

    m_return_to_depot_isValid = ::OpenAPI::fromJsonValue(m_return_to_depot, json[QString("return_to_depot")]);
    m_return_to_depot_isSet = !json[QString("return_to_depot")].isNull() && m_return_to_depot_isValid;

    m_skills_isValid = ::OpenAPI::fromJsonValue(m_skills, json[QString("skills")]);
    m_skills_isSet = !json[QString("skills")].isNull() && m_skills_isValid;

    m_start_address_isValid = ::OpenAPI::fromJsonValue(m_start_address, json[QString("start_address")]);
    m_start_address_isSet = !json[QString("start_address")].isNull() && m_start_address_isValid;

    m_type_id_isValid = ::OpenAPI::fromJsonValue(m_type_id, json[QString("type_id")]);
    m_type_id_isSet = !json[QString("type_id")].isNull() && m_type_id_isValid;

    m_vehicle_id_isValid = ::OpenAPI::fromJsonValue(m_vehicle_id, json[QString("vehicle_id")]);
    m_vehicle_id_isSet = !json[QString("vehicle_id")].isNull() && m_vehicle_id_isValid;
}

QString OAIVehicle::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIVehicle::asJsonObject() const {
    QJsonObject obj;
    if (m_r_break.isSet()) {
        obj.insert(QString("break"), ::OpenAPI::toJsonValue(m_r_break));
    }
    if (m_earliest_start_isSet) {
        obj.insert(QString("earliest_start"), ::OpenAPI::toJsonValue(m_earliest_start));
    }
    if (m_end_address.isSet()) {
        obj.insert(QString("end_address"), ::OpenAPI::toJsonValue(m_end_address));
    }
    if (m_latest_end_isSet) {
        obj.insert(QString("latest_end"), ::OpenAPI::toJsonValue(m_latest_end));
    }
    if (m_max_activities_isSet) {
        obj.insert(QString("max_activities"), ::OpenAPI::toJsonValue(m_max_activities));
    }
    if (m_max_distance_isSet) {
        obj.insert(QString("max_distance"), ::OpenAPI::toJsonValue(m_max_distance));
    }
    if (m_max_driving_time_isSet) {
        obj.insert(QString("max_driving_time"), ::OpenAPI::toJsonValue(m_max_driving_time));
    }
    if (m_max_jobs_isSet) {
        obj.insert(QString("max_jobs"), ::OpenAPI::toJsonValue(m_max_jobs));
    }
    if (m_min_jobs_isSet) {
        obj.insert(QString("min_jobs"), ::OpenAPI::toJsonValue(m_min_jobs));
    }
    if (m_move_to_end_address_isSet) {
        obj.insert(QString("move_to_end_address"), ::OpenAPI::toJsonValue(m_move_to_end_address));
    }
    if (m_return_to_depot_isSet) {
        obj.insert(QString("return_to_depot"), ::OpenAPI::toJsonValue(m_return_to_depot));
    }
    if (m_skills.size() > 0) {
        obj.insert(QString("skills"), ::OpenAPI::toJsonValue(m_skills));
    }
    if (m_start_address.isSet()) {
        obj.insert(QString("start_address"), ::OpenAPI::toJsonValue(m_start_address));
    }
    if (m_type_id_isSet) {
        obj.insert(QString("type_id"), ::OpenAPI::toJsonValue(m_type_id));
    }
    if (m_vehicle_id_isSet) {
        obj.insert(QString("vehicle_id"), ::OpenAPI::toJsonValue(m_vehicle_id));
    }
    return obj;
}

OAIVehicle_break OAIVehicle::getRBreak() const {
    return m_r_break;
}
void OAIVehicle::setRBreak(const OAIVehicle_break &r_break) {
    m_r_break = r_break;
    m_r_break_isSet = true;
}

bool OAIVehicle::is_r_break_Set() const{
    return m_r_break_isSet;
}

bool OAIVehicle::is_r_break_Valid() const{
    return m_r_break_isValid;
}

qint64 OAIVehicle::getEarliestStart() const {
    return m_earliest_start;
}
void OAIVehicle::setEarliestStart(const qint64 &earliest_start) {
    m_earliest_start = earliest_start;
    m_earliest_start_isSet = true;
}

bool OAIVehicle::is_earliest_start_Set() const{
    return m_earliest_start_isSet;
}

bool OAIVehicle::is_earliest_start_Valid() const{
    return m_earliest_start_isValid;
}

OAIAddress OAIVehicle::getEndAddress() const {
    return m_end_address;
}
void OAIVehicle::setEndAddress(const OAIAddress &end_address) {
    m_end_address = end_address;
    m_end_address_isSet = true;
}

bool OAIVehicle::is_end_address_Set() const{
    return m_end_address_isSet;
}

bool OAIVehicle::is_end_address_Valid() const{
    return m_end_address_isValid;
}

qint64 OAIVehicle::getLatestEnd() const {
    return m_latest_end;
}
void OAIVehicle::setLatestEnd(const qint64 &latest_end) {
    m_latest_end = latest_end;
    m_latest_end_isSet = true;
}

bool OAIVehicle::is_latest_end_Set() const{
    return m_latest_end_isSet;
}

bool OAIVehicle::is_latest_end_Valid() const{
    return m_latest_end_isValid;
}

qint32 OAIVehicle::getMaxActivities() const {
    return m_max_activities;
}
void OAIVehicle::setMaxActivities(const qint32 &max_activities) {
    m_max_activities = max_activities;
    m_max_activities_isSet = true;
}

bool OAIVehicle::is_max_activities_Set() const{
    return m_max_activities_isSet;
}

bool OAIVehicle::is_max_activities_Valid() const{
    return m_max_activities_isValid;
}

qint64 OAIVehicle::getMaxDistance() const {
    return m_max_distance;
}
void OAIVehicle::setMaxDistance(const qint64 &max_distance) {
    m_max_distance = max_distance;
    m_max_distance_isSet = true;
}

bool OAIVehicle::is_max_distance_Set() const{
    return m_max_distance_isSet;
}

bool OAIVehicle::is_max_distance_Valid() const{
    return m_max_distance_isValid;
}

qint64 OAIVehicle::getMaxDrivingTime() const {
    return m_max_driving_time;
}
void OAIVehicle::setMaxDrivingTime(const qint64 &max_driving_time) {
    m_max_driving_time = max_driving_time;
    m_max_driving_time_isSet = true;
}

bool OAIVehicle::is_max_driving_time_Set() const{
    return m_max_driving_time_isSet;
}

bool OAIVehicle::is_max_driving_time_Valid() const{
    return m_max_driving_time_isValid;
}

qint32 OAIVehicle::getMaxJobs() const {
    return m_max_jobs;
}
void OAIVehicle::setMaxJobs(const qint32 &max_jobs) {
    m_max_jobs = max_jobs;
    m_max_jobs_isSet = true;
}

bool OAIVehicle::is_max_jobs_Set() const{
    return m_max_jobs_isSet;
}

bool OAIVehicle::is_max_jobs_Valid() const{
    return m_max_jobs_isValid;
}

qint32 OAIVehicle::getMinJobs() const {
    return m_min_jobs;
}
void OAIVehicle::setMinJobs(const qint32 &min_jobs) {
    m_min_jobs = min_jobs;
    m_min_jobs_isSet = true;
}

bool OAIVehicle::is_min_jobs_Set() const{
    return m_min_jobs_isSet;
}

bool OAIVehicle::is_min_jobs_Valid() const{
    return m_min_jobs_isValid;
}

bool OAIVehicle::isMoveToEndAddress() const {
    return m_move_to_end_address;
}
void OAIVehicle::setMoveToEndAddress(const bool &move_to_end_address) {
    m_move_to_end_address = move_to_end_address;
    m_move_to_end_address_isSet = true;
}

bool OAIVehicle::is_move_to_end_address_Set() const{
    return m_move_to_end_address_isSet;
}

bool OAIVehicle::is_move_to_end_address_Valid() const{
    return m_move_to_end_address_isValid;
}

bool OAIVehicle::isReturnToDepot() const {
    return m_return_to_depot;
}
void OAIVehicle::setReturnToDepot(const bool &return_to_depot) {
    m_return_to_depot = return_to_depot;
    m_return_to_depot_isSet = true;
}

bool OAIVehicle::is_return_to_depot_Set() const{
    return m_return_to_depot_isSet;
}

bool OAIVehicle::is_return_to_depot_Valid() const{
    return m_return_to_depot_isValid;
}

QList<QString> OAIVehicle::getSkills() const {
    return m_skills;
}
void OAIVehicle::setSkills(const QList<QString> &skills) {
    m_skills = skills;
    m_skills_isSet = true;
}

bool OAIVehicle::is_skills_Set() const{
    return m_skills_isSet;
}

bool OAIVehicle::is_skills_Valid() const{
    return m_skills_isValid;
}

OAIAddress OAIVehicle::getStartAddress() const {
    return m_start_address;
}
void OAIVehicle::setStartAddress(const OAIAddress &start_address) {
    m_start_address = start_address;
    m_start_address_isSet = true;
}

bool OAIVehicle::is_start_address_Set() const{
    return m_start_address_isSet;
}

bool OAIVehicle::is_start_address_Valid() const{
    return m_start_address_isValid;
}

QString OAIVehicle::getTypeId() const {
    return m_type_id;
}
void OAIVehicle::setTypeId(const QString &type_id) {
    m_type_id = type_id;
    m_type_id_isSet = true;
}

bool OAIVehicle::is_type_id_Set() const{
    return m_type_id_isSet;
}

bool OAIVehicle::is_type_id_Valid() const{
    return m_type_id_isValid;
}

QString OAIVehicle::getVehicleId() const {
    return m_vehicle_id;
}
void OAIVehicle::setVehicleId(const QString &vehicle_id) {
    m_vehicle_id = vehicle_id;
    m_vehicle_id_isSet = true;
}

bool OAIVehicle::is_vehicle_id_Set() const{
    return m_vehicle_id_isSet;
}

bool OAIVehicle::is_vehicle_id_Valid() const{
    return m_vehicle_id_isValid;
}

bool OAIVehicle::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_r_break.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_earliest_start_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_end_address.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_latest_end_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_max_activities_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_max_distance_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_max_driving_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_max_jobs_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_min_jobs_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_move_to_end_address_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_return_to_depot_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_skills.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_start_address.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_vehicle_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIVehicle::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_start_address_isValid && m_vehicle_id_isValid && true;
}

} // namespace OpenAPI
