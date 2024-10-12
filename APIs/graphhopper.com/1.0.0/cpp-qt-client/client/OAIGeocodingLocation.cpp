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

#include "OAIGeocodingLocation.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGeocodingLocation::OAIGeocodingLocation(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGeocodingLocation::OAIGeocodingLocation() {
    this->initializeModel();
}

OAIGeocodingLocation::~OAIGeocodingLocation() {}

void OAIGeocodingLocation::initializeModel() {

    m_city_isSet = false;
    m_city_isValid = false;

    m_country_isSet = false;
    m_country_isValid = false;

    m_housenumber_isSet = false;
    m_housenumber_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_osm_id_isSet = false;
    m_osm_id_isValid = false;

    m_osm_key_isSet = false;
    m_osm_key_isValid = false;

    m_osm_type_isSet = false;
    m_osm_type_isValid = false;

    m_point_isSet = false;
    m_point_isValid = false;

    m_postcode_isSet = false;
    m_postcode_isValid = false;

    m_state_isSet = false;
    m_state_isValid = false;

    m_street_isSet = false;
    m_street_isValid = false;
}

void OAIGeocodingLocation::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGeocodingLocation::fromJsonObject(QJsonObject json) {

    m_city_isValid = ::OpenAPI::fromJsonValue(m_city, json[QString("city")]);
    m_city_isSet = !json[QString("city")].isNull() && m_city_isValid;

    m_country_isValid = ::OpenAPI::fromJsonValue(m_country, json[QString("country")]);
    m_country_isSet = !json[QString("country")].isNull() && m_country_isValid;

    m_housenumber_isValid = ::OpenAPI::fromJsonValue(m_housenumber, json[QString("housenumber")]);
    m_housenumber_isSet = !json[QString("housenumber")].isNull() && m_housenumber_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_osm_id_isValid = ::OpenAPI::fromJsonValue(m_osm_id, json[QString("osm_id")]);
    m_osm_id_isSet = !json[QString("osm_id")].isNull() && m_osm_id_isValid;

    m_osm_key_isValid = ::OpenAPI::fromJsonValue(m_osm_key, json[QString("osm_key")]);
    m_osm_key_isSet = !json[QString("osm_key")].isNull() && m_osm_key_isValid;

    m_osm_type_isValid = ::OpenAPI::fromJsonValue(m_osm_type, json[QString("osm_type")]);
    m_osm_type_isSet = !json[QString("osm_type")].isNull() && m_osm_type_isValid;

    m_point_isValid = ::OpenAPI::fromJsonValue(m_point, json[QString("point")]);
    m_point_isSet = !json[QString("point")].isNull() && m_point_isValid;

    m_postcode_isValid = ::OpenAPI::fromJsonValue(m_postcode, json[QString("postcode")]);
    m_postcode_isSet = !json[QString("postcode")].isNull() && m_postcode_isValid;

    m_state_isValid = ::OpenAPI::fromJsonValue(m_state, json[QString("state")]);
    m_state_isSet = !json[QString("state")].isNull() && m_state_isValid;

    m_street_isValid = ::OpenAPI::fromJsonValue(m_street, json[QString("street")]);
    m_street_isSet = !json[QString("street")].isNull() && m_street_isValid;
}

QString OAIGeocodingLocation::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGeocodingLocation::asJsonObject() const {
    QJsonObject obj;
    if (m_city_isSet) {
        obj.insert(QString("city"), ::OpenAPI::toJsonValue(m_city));
    }
    if (m_country_isSet) {
        obj.insert(QString("country"), ::OpenAPI::toJsonValue(m_country));
    }
    if (m_housenumber_isSet) {
        obj.insert(QString("housenumber"), ::OpenAPI::toJsonValue(m_housenumber));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_osm_id_isSet) {
        obj.insert(QString("osm_id"), ::OpenAPI::toJsonValue(m_osm_id));
    }
    if (m_osm_key_isSet) {
        obj.insert(QString("osm_key"), ::OpenAPI::toJsonValue(m_osm_key));
    }
    if (m_osm_type_isSet) {
        obj.insert(QString("osm_type"), ::OpenAPI::toJsonValue(m_osm_type));
    }
    if (m_point.isSet()) {
        obj.insert(QString("point"), ::OpenAPI::toJsonValue(m_point));
    }
    if (m_postcode_isSet) {
        obj.insert(QString("postcode"), ::OpenAPI::toJsonValue(m_postcode));
    }
    if (m_state_isSet) {
        obj.insert(QString("state"), ::OpenAPI::toJsonValue(m_state));
    }
    if (m_street_isSet) {
        obj.insert(QString("street"), ::OpenAPI::toJsonValue(m_street));
    }
    return obj;
}

QString OAIGeocodingLocation::getCity() const {
    return m_city;
}
void OAIGeocodingLocation::setCity(const QString &city) {
    m_city = city;
    m_city_isSet = true;
}

bool OAIGeocodingLocation::is_city_Set() const{
    return m_city_isSet;
}

bool OAIGeocodingLocation::is_city_Valid() const{
    return m_city_isValid;
}

QString OAIGeocodingLocation::getCountry() const {
    return m_country;
}
void OAIGeocodingLocation::setCountry(const QString &country) {
    m_country = country;
    m_country_isSet = true;
}

bool OAIGeocodingLocation::is_country_Set() const{
    return m_country_isSet;
}

bool OAIGeocodingLocation::is_country_Valid() const{
    return m_country_isValid;
}

QString OAIGeocodingLocation::getHousenumber() const {
    return m_housenumber;
}
void OAIGeocodingLocation::setHousenumber(const QString &housenumber) {
    m_housenumber = housenumber;
    m_housenumber_isSet = true;
}

bool OAIGeocodingLocation::is_housenumber_Set() const{
    return m_housenumber_isSet;
}

bool OAIGeocodingLocation::is_housenumber_Valid() const{
    return m_housenumber_isValid;
}

QString OAIGeocodingLocation::getName() const {
    return m_name;
}
void OAIGeocodingLocation::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIGeocodingLocation::is_name_Set() const{
    return m_name_isSet;
}

bool OAIGeocodingLocation::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIGeocodingLocation::getOsmId() const {
    return m_osm_id;
}
void OAIGeocodingLocation::setOsmId(const QString &osm_id) {
    m_osm_id = osm_id;
    m_osm_id_isSet = true;
}

bool OAIGeocodingLocation::is_osm_id_Set() const{
    return m_osm_id_isSet;
}

bool OAIGeocodingLocation::is_osm_id_Valid() const{
    return m_osm_id_isValid;
}

QString OAIGeocodingLocation::getOsmKey() const {
    return m_osm_key;
}
void OAIGeocodingLocation::setOsmKey(const QString &osm_key) {
    m_osm_key = osm_key;
    m_osm_key_isSet = true;
}

bool OAIGeocodingLocation::is_osm_key_Set() const{
    return m_osm_key_isSet;
}

bool OAIGeocodingLocation::is_osm_key_Valid() const{
    return m_osm_key_isValid;
}

QString OAIGeocodingLocation::getOsmType() const {
    return m_osm_type;
}
void OAIGeocodingLocation::setOsmType(const QString &osm_type) {
    m_osm_type = osm_type;
    m_osm_type_isSet = true;
}

bool OAIGeocodingLocation::is_osm_type_Set() const{
    return m_osm_type_isSet;
}

bool OAIGeocodingLocation::is_osm_type_Valid() const{
    return m_osm_type_isValid;
}

OAIGeocodingPoint OAIGeocodingLocation::getPoint() const {
    return m_point;
}
void OAIGeocodingLocation::setPoint(const OAIGeocodingPoint &point) {
    m_point = point;
    m_point_isSet = true;
}

bool OAIGeocodingLocation::is_point_Set() const{
    return m_point_isSet;
}

bool OAIGeocodingLocation::is_point_Valid() const{
    return m_point_isValid;
}

QString OAIGeocodingLocation::getPostcode() const {
    return m_postcode;
}
void OAIGeocodingLocation::setPostcode(const QString &postcode) {
    m_postcode = postcode;
    m_postcode_isSet = true;
}

bool OAIGeocodingLocation::is_postcode_Set() const{
    return m_postcode_isSet;
}

bool OAIGeocodingLocation::is_postcode_Valid() const{
    return m_postcode_isValid;
}

QString OAIGeocodingLocation::getState() const {
    return m_state;
}
void OAIGeocodingLocation::setState(const QString &state) {
    m_state = state;
    m_state_isSet = true;
}

bool OAIGeocodingLocation::is_state_Set() const{
    return m_state_isSet;
}

bool OAIGeocodingLocation::is_state_Valid() const{
    return m_state_isValid;
}

QString OAIGeocodingLocation::getStreet() const {
    return m_street;
}
void OAIGeocodingLocation::setStreet(const QString &street) {
    m_street = street;
    m_street_isSet = true;
}

bool OAIGeocodingLocation::is_street_Set() const{
    return m_street_isSet;
}

bool OAIGeocodingLocation::is_street_Valid() const{
    return m_street_isValid;
}

bool OAIGeocodingLocation::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_city_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_country_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_housenumber_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_osm_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_osm_key_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_osm_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_point.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_postcode_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_state_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_street_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGeocodingLocation::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
