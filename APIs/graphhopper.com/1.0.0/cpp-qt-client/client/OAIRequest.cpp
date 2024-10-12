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

#include "OAIRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRequest::OAIRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRequest::OAIRequest() {
    this->initializeModel();
}

OAIRequest::~OAIRequest() {}

void OAIRequest::initializeModel() {

    m_algorithm_isSet = false;
    m_algorithm_isValid = false;

    m_configuration_isSet = false;
    m_configuration_isValid = false;

    m_cost_matrices_isSet = false;
    m_cost_matrices_isValid = false;

    m_objectives_isSet = false;
    m_objectives_isValid = false;

    m_relations_isSet = false;
    m_relations_isValid = false;

    m_services_isSet = false;
    m_services_isValid = false;

    m_shipments_isSet = false;
    m_shipments_isValid = false;

    m_vehicle_types_isSet = false;
    m_vehicle_types_isValid = false;

    m_vehicles_isSet = false;
    m_vehicles_isValid = false;
}

void OAIRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRequest::fromJsonObject(QJsonObject json) {

    m_algorithm_isValid = ::OpenAPI::fromJsonValue(m_algorithm, json[QString("algorithm")]);
    m_algorithm_isSet = !json[QString("algorithm")].isNull() && m_algorithm_isValid;

    m_configuration_isValid = ::OpenAPI::fromJsonValue(m_configuration, json[QString("configuration")]);
    m_configuration_isSet = !json[QString("configuration")].isNull() && m_configuration_isValid;

    m_cost_matrices_isValid = ::OpenAPI::fromJsonValue(m_cost_matrices, json[QString("cost_matrices")]);
    m_cost_matrices_isSet = !json[QString("cost_matrices")].isNull() && m_cost_matrices_isValid;

    m_objectives_isValid = ::OpenAPI::fromJsonValue(m_objectives, json[QString("objectives")]);
    m_objectives_isSet = !json[QString("objectives")].isNull() && m_objectives_isValid;

    m_relations_isValid = ::OpenAPI::fromJsonValue(m_relations, json[QString("relations")]);
    m_relations_isSet = !json[QString("relations")].isNull() && m_relations_isValid;

    m_services_isValid = ::OpenAPI::fromJsonValue(m_services, json[QString("services")]);
    m_services_isSet = !json[QString("services")].isNull() && m_services_isValid;

    m_shipments_isValid = ::OpenAPI::fromJsonValue(m_shipments, json[QString("shipments")]);
    m_shipments_isSet = !json[QString("shipments")].isNull() && m_shipments_isValid;

    m_vehicle_types_isValid = ::OpenAPI::fromJsonValue(m_vehicle_types, json[QString("vehicle_types")]);
    m_vehicle_types_isSet = !json[QString("vehicle_types")].isNull() && m_vehicle_types_isValid;

    m_vehicles_isValid = ::OpenAPI::fromJsonValue(m_vehicles, json[QString("vehicles")]);
    m_vehicles_isSet = !json[QString("vehicles")].isNull() && m_vehicles_isValid;
}

QString OAIRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_algorithm.isSet()) {
        obj.insert(QString("algorithm"), ::OpenAPI::toJsonValue(m_algorithm));
    }
    if (m_configuration.isSet()) {
        obj.insert(QString("configuration"), ::OpenAPI::toJsonValue(m_configuration));
    }
    if (m_cost_matrices.size() > 0) {
        obj.insert(QString("cost_matrices"), ::OpenAPI::toJsonValue(m_cost_matrices));
    }
    if (m_objectives.size() > 0) {
        obj.insert(QString("objectives"), ::OpenAPI::toJsonValue(m_objectives));
    }
    if (m_relations.size() > 0) {
        obj.insert(QString("relations"), ::OpenAPI::toJsonValue(m_relations));
    }
    if (m_services.size() > 0) {
        obj.insert(QString("services"), ::OpenAPI::toJsonValue(m_services));
    }
    if (m_shipments.size() > 0) {
        obj.insert(QString("shipments"), ::OpenAPI::toJsonValue(m_shipments));
    }
    if (m_vehicle_types.size() > 0) {
        obj.insert(QString("vehicle_types"), ::OpenAPI::toJsonValue(m_vehicle_types));
    }
    if (m_vehicles.size() > 0) {
        obj.insert(QString("vehicles"), ::OpenAPI::toJsonValue(m_vehicles));
    }
    return obj;
}

OAIAlgorithm OAIRequest::getAlgorithm() const {
    return m_algorithm;
}
void OAIRequest::setAlgorithm(const OAIAlgorithm &algorithm) {
    m_algorithm = algorithm;
    m_algorithm_isSet = true;
}

bool OAIRequest::is_algorithm_Set() const{
    return m_algorithm_isSet;
}

bool OAIRequest::is_algorithm_Valid() const{
    return m_algorithm_isValid;
}

OAIConfiguration OAIRequest::getConfiguration() const {
    return m_configuration;
}
void OAIRequest::setConfiguration(const OAIConfiguration &configuration) {
    m_configuration = configuration;
    m_configuration_isSet = true;
}

bool OAIRequest::is_configuration_Set() const{
    return m_configuration_isSet;
}

bool OAIRequest::is_configuration_Valid() const{
    return m_configuration_isValid;
}

QList<OAICostMatrix> OAIRequest::getCostMatrices() const {
    return m_cost_matrices;
}
void OAIRequest::setCostMatrices(const QList<OAICostMatrix> &cost_matrices) {
    m_cost_matrices = cost_matrices;
    m_cost_matrices_isSet = true;
}

bool OAIRequest::is_cost_matrices_Set() const{
    return m_cost_matrices_isSet;
}

bool OAIRequest::is_cost_matrices_Valid() const{
    return m_cost_matrices_isValid;
}

QList<OAIObjective> OAIRequest::getObjectives() const {
    return m_objectives;
}
void OAIRequest::setObjectives(const QList<OAIObjective> &objectives) {
    m_objectives = objectives;
    m_objectives_isSet = true;
}

bool OAIRequest::is_objectives_Set() const{
    return m_objectives_isSet;
}

bool OAIRequest::is_objectives_Valid() const{
    return m_objectives_isValid;
}

QList<OAIRequest_relations_inner> OAIRequest::getRelations() const {
    return m_relations;
}
void OAIRequest::setRelations(const QList<OAIRequest_relations_inner> &relations) {
    m_relations = relations;
    m_relations_isSet = true;
}

bool OAIRequest::is_relations_Set() const{
    return m_relations_isSet;
}

bool OAIRequest::is_relations_Valid() const{
    return m_relations_isValid;
}

QList<OAIService> OAIRequest::getServices() const {
    return m_services;
}
void OAIRequest::setServices(const QList<OAIService> &services) {
    m_services = services;
    m_services_isSet = true;
}

bool OAIRequest::is_services_Set() const{
    return m_services_isSet;
}

bool OAIRequest::is_services_Valid() const{
    return m_services_isValid;
}

QList<OAIShipment> OAIRequest::getShipments() const {
    return m_shipments;
}
void OAIRequest::setShipments(const QList<OAIShipment> &shipments) {
    m_shipments = shipments;
    m_shipments_isSet = true;
}

bool OAIRequest::is_shipments_Set() const{
    return m_shipments_isSet;
}

bool OAIRequest::is_shipments_Valid() const{
    return m_shipments_isValid;
}

QList<OAIVehicleType> OAIRequest::getVehicleTypes() const {
    return m_vehicle_types;
}
void OAIRequest::setVehicleTypes(const QList<OAIVehicleType> &vehicle_types) {
    m_vehicle_types = vehicle_types;
    m_vehicle_types_isSet = true;
}

bool OAIRequest::is_vehicle_types_Set() const{
    return m_vehicle_types_isSet;
}

bool OAIRequest::is_vehicle_types_Valid() const{
    return m_vehicle_types_isValid;
}

QList<OAIVehicle> OAIRequest::getVehicles() const {
    return m_vehicles;
}
void OAIRequest::setVehicles(const QList<OAIVehicle> &vehicles) {
    m_vehicles = vehicles;
    m_vehicles_isSet = true;
}

bool OAIRequest::is_vehicles_Set() const{
    return m_vehicles_isSet;
}

bool OAIRequest::is_vehicles_Valid() const{
    return m_vehicles_isValid;
}

bool OAIRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_algorithm.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_configuration.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_cost_matrices.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_objectives.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_relations.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_services.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_shipments.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_vehicle_types.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_vehicles.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
