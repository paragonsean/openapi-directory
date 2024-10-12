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

/*
 * OAIVehicle.h
 *
 * 
 */

#ifndef OAIVehicle_H
#define OAIVehicle_H

#include <QJsonObject>

#include "OAIAddress.h"
#include "OAIVehicle_break.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIVehicle_break;
class OAIAddress;

class OAIVehicle : public OAIObject {
public:
    OAIVehicle();
    OAIVehicle(QString json);
    ~OAIVehicle() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIVehicle_break getRBreak() const;
    void setRBreak(const OAIVehicle_break &r_break);
    bool is_r_break_Set() const;
    bool is_r_break_Valid() const;

    qint64 getEarliestStart() const;
    void setEarliestStart(const qint64 &earliest_start);
    bool is_earliest_start_Set() const;
    bool is_earliest_start_Valid() const;

    OAIAddress getEndAddress() const;
    void setEndAddress(const OAIAddress &end_address);
    bool is_end_address_Set() const;
    bool is_end_address_Valid() const;

    qint64 getLatestEnd() const;
    void setLatestEnd(const qint64 &latest_end);
    bool is_latest_end_Set() const;
    bool is_latest_end_Valid() const;

    qint32 getMaxActivities() const;
    void setMaxActivities(const qint32 &max_activities);
    bool is_max_activities_Set() const;
    bool is_max_activities_Valid() const;

    qint64 getMaxDistance() const;
    void setMaxDistance(const qint64 &max_distance);
    bool is_max_distance_Set() const;
    bool is_max_distance_Valid() const;

    qint64 getMaxDrivingTime() const;
    void setMaxDrivingTime(const qint64 &max_driving_time);
    bool is_max_driving_time_Set() const;
    bool is_max_driving_time_Valid() const;

    qint32 getMaxJobs() const;
    void setMaxJobs(const qint32 &max_jobs);
    bool is_max_jobs_Set() const;
    bool is_max_jobs_Valid() const;

    qint32 getMinJobs() const;
    void setMinJobs(const qint32 &min_jobs);
    bool is_min_jobs_Set() const;
    bool is_min_jobs_Valid() const;

    bool isMoveToEndAddress() const;
    void setMoveToEndAddress(const bool &move_to_end_address);
    bool is_move_to_end_address_Set() const;
    bool is_move_to_end_address_Valid() const;

    bool isReturnToDepot() const;
    void setReturnToDepot(const bool &return_to_depot);
    bool is_return_to_depot_Set() const;
    bool is_return_to_depot_Valid() const;

    QList<QString> getSkills() const;
    void setSkills(const QList<QString> &skills);
    bool is_skills_Set() const;
    bool is_skills_Valid() const;

    OAIAddress getStartAddress() const;
    void setStartAddress(const OAIAddress &start_address);
    bool is_start_address_Set() const;
    bool is_start_address_Valid() const;

    QString getTypeId() const;
    void setTypeId(const QString &type_id);
    bool is_type_id_Set() const;
    bool is_type_id_Valid() const;

    QString getVehicleId() const;
    void setVehicleId(const QString &vehicle_id);
    bool is_vehicle_id_Set() const;
    bool is_vehicle_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIVehicle_break m_r_break;
    bool m_r_break_isSet;
    bool m_r_break_isValid;

    qint64 m_earliest_start;
    bool m_earliest_start_isSet;
    bool m_earliest_start_isValid;

    OAIAddress m_end_address;
    bool m_end_address_isSet;
    bool m_end_address_isValid;

    qint64 m_latest_end;
    bool m_latest_end_isSet;
    bool m_latest_end_isValid;

    qint32 m_max_activities;
    bool m_max_activities_isSet;
    bool m_max_activities_isValid;

    qint64 m_max_distance;
    bool m_max_distance_isSet;
    bool m_max_distance_isValid;

    qint64 m_max_driving_time;
    bool m_max_driving_time_isSet;
    bool m_max_driving_time_isValid;

    qint32 m_max_jobs;
    bool m_max_jobs_isSet;
    bool m_max_jobs_isValid;

    qint32 m_min_jobs;
    bool m_min_jobs_isSet;
    bool m_min_jobs_isValid;

    bool m_move_to_end_address;
    bool m_move_to_end_address_isSet;
    bool m_move_to_end_address_isValid;

    bool m_return_to_depot;
    bool m_return_to_depot_isSet;
    bool m_return_to_depot_isValid;

    QList<QString> m_skills;
    bool m_skills_isSet;
    bool m_skills_isValid;

    OAIAddress m_start_address;
    bool m_start_address_isSet;
    bool m_start_address_isValid;

    QString m_type_id;
    bool m_type_id_isSet;
    bool m_type_id_isValid;

    QString m_vehicle_id;
    bool m_vehicle_id_isSet;
    bool m_vehicle_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIVehicle)

#endif // OAIVehicle_H
