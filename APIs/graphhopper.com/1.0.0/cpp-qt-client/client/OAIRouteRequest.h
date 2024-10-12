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
 * OAIRouteRequest.h
 *
 * 
 */

#ifndef OAIRouteRequest_H
#define OAIRouteRequest_H

#include <QJsonObject>

#include "OAIVehicleProfileId.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIRouteRequest : public OAIObject {
public:
    OAIRouteRequest();
    OAIRouteRequest(QString json);
    ~OAIRouteRequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAlgorithm() const;
    void setAlgorithm(const QString &algorithm);
    bool is_algorithm_Set() const;
    bool is_algorithm_Valid() const;

    qint32 getAlternativeRouteMaxPaths() const;
    void setAlternativeRouteMaxPaths(const qint32 &alternative_route_max_paths);
    bool is_alternative_route_max_paths_Set() const;
    bool is_alternative_route_max_paths_Valid() const;

    double getAlternativeRouteMaxShareFactor() const;
    void setAlternativeRouteMaxShareFactor(const double &alternative_route_max_share_factor);
    bool is_alternative_route_max_share_factor_Set() const;
    bool is_alternative_route_max_share_factor_Valid() const;

    double getAlternativeRouteMaxWeightFactor() const;
    void setAlternativeRouteMaxWeightFactor(const double &alternative_route_max_weight_factor);
    bool is_alternative_route_max_weight_factor_Set() const;
    bool is_alternative_route_max_weight_factor_Valid() const;

    QString getAvoid() const;
    void setAvoid(const QString &avoid);
    bool is_avoid_Set() const;
    bool is_avoid_Valid() const;

    QString getBlockArea() const;
    void setBlockArea(const QString &block_area);
    bool is_block_area_Set() const;
    bool is_block_area_Valid() const;

    bool isCalcPoints() const;
    void setCalcPoints(const bool &calc_points);
    bool is_calc_points_Set() const;
    bool is_calc_points_Valid() const;

    bool isChDisable() const;
    void setChDisable(const bool &ch_disable);
    bool is_ch_disable_Set() const;
    bool is_ch_disable_Valid() const;

    QList<QString> getCurbsides() const;
    void setCurbsides(const QList<QString> &curbsides);
    bool is_curbsides_Set() const;
    bool is_curbsides_Valid() const;

    bool isDebug() const;
    void setDebug(const bool &debug);
    bool is_debug_Set() const;
    bool is_debug_Valid() const;

    QList<QString> getDetails() const;
    void setDetails(const QList<QString> &details);
    bool is_details_Set() const;
    bool is_details_Valid() const;

    bool isElevation() const;
    void setElevation(const bool &elevation);
    bool is_elevation_Set() const;
    bool is_elevation_Valid() const;

    qint32 getHeadingPenalty() const;
    void setHeadingPenalty(const qint32 &heading_penalty);
    bool is_heading_penalty_Set() const;
    bool is_heading_penalty_Valid() const;

    QList<qint32> getHeadings() const;
    void setHeadings(const QList<qint32> &headings);
    bool is_headings_Set() const;
    bool is_headings_Valid() const;

    bool isInstructions() const;
    void setInstructions(const bool &instructions);
    bool is_instructions_Set() const;
    bool is_instructions_Valid() const;

    QString getLocale() const;
    void setLocale(const QString &locale);
    bool is_locale_Set() const;
    bool is_locale_Valid() const;

    QString getOptimize() const;
    void setOptimize(const QString &optimize);
    bool is_optimize_Set() const;
    bool is_optimize_Valid() const;

    bool isPassThrough() const;
    void setPassThrough(const bool &pass_through);
    bool is_pass_through_Set() const;
    bool is_pass_through_Valid() const;

    QList<QString> getPointHints() const;
    void setPointHints(const QList<QString> &point_hints);
    bool is_point_hints_Set() const;
    bool is_point_hints_Valid() const;

    QList<QList<double>> getPoints() const;
    void setPoints(const QList<QList<double>> &points);
    bool is_points_Set() const;
    bool is_points_Valid() const;

    bool isPointsEncoded() const;
    void setPointsEncoded(const bool &points_encoded);
    bool is_points_encoded_Set() const;
    bool is_points_encoded_Valid() const;

    qint32 getRoundTripDistance() const;
    void setRoundTripDistance(const qint32 &round_trip_distance);
    bool is_round_trip_distance_Set() const;
    bool is_round_trip_distance_Valid() const;

    qint64 getRoundTripSeed() const;
    void setRoundTripSeed(const qint64 &round_trip_seed);
    bool is_round_trip_seed_Set() const;
    bool is_round_trip_seed_Valid() const;

    QList<QString> getSnapPreventions() const;
    void setSnapPreventions(const QList<QString> &snap_preventions);
    bool is_snap_preventions_Set() const;
    bool is_snap_preventions_Valid() const;

    OAIVehicleProfileId getVehicle() const;
    void setVehicle(const OAIVehicleProfileId &vehicle);
    bool is_vehicle_Set() const;
    bool is_vehicle_Valid() const;

    QString getWeighting() const;
    void setWeighting(const QString &weighting);
    bool is_weighting_Set() const;
    bool is_weighting_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_algorithm;
    bool m_algorithm_isSet;
    bool m_algorithm_isValid;

    qint32 m_alternative_route_max_paths;
    bool m_alternative_route_max_paths_isSet;
    bool m_alternative_route_max_paths_isValid;

    double m_alternative_route_max_share_factor;
    bool m_alternative_route_max_share_factor_isSet;
    bool m_alternative_route_max_share_factor_isValid;

    double m_alternative_route_max_weight_factor;
    bool m_alternative_route_max_weight_factor_isSet;
    bool m_alternative_route_max_weight_factor_isValid;

    QString m_avoid;
    bool m_avoid_isSet;
    bool m_avoid_isValid;

    QString m_block_area;
    bool m_block_area_isSet;
    bool m_block_area_isValid;

    bool m_calc_points;
    bool m_calc_points_isSet;
    bool m_calc_points_isValid;

    bool m_ch_disable;
    bool m_ch_disable_isSet;
    bool m_ch_disable_isValid;

    QList<QString> m_curbsides;
    bool m_curbsides_isSet;
    bool m_curbsides_isValid;

    bool m_debug;
    bool m_debug_isSet;
    bool m_debug_isValid;

    QList<QString> m_details;
    bool m_details_isSet;
    bool m_details_isValid;

    bool m_elevation;
    bool m_elevation_isSet;
    bool m_elevation_isValid;

    qint32 m_heading_penalty;
    bool m_heading_penalty_isSet;
    bool m_heading_penalty_isValid;

    QList<qint32> m_headings;
    bool m_headings_isSet;
    bool m_headings_isValid;

    bool m_instructions;
    bool m_instructions_isSet;
    bool m_instructions_isValid;

    QString m_locale;
    bool m_locale_isSet;
    bool m_locale_isValid;

    QString m_optimize;
    bool m_optimize_isSet;
    bool m_optimize_isValid;

    bool m_pass_through;
    bool m_pass_through_isSet;
    bool m_pass_through_isValid;

    QList<QString> m_point_hints;
    bool m_point_hints_isSet;
    bool m_point_hints_isValid;

    QList<QList<double>> m_points;
    bool m_points_isSet;
    bool m_points_isValid;

    bool m_points_encoded;
    bool m_points_encoded_isSet;
    bool m_points_encoded_isValid;

    qint32 m_round_trip_distance;
    bool m_round_trip_distance_isSet;
    bool m_round_trip_distance_isValid;

    qint64 m_round_trip_seed;
    bool m_round_trip_seed_isSet;
    bool m_round_trip_seed_isValid;

    QList<QString> m_snap_preventions;
    bool m_snap_preventions_isSet;
    bool m_snap_preventions_isValid;

    OAIVehicleProfileId m_vehicle;
    bool m_vehicle_isSet;
    bool m_vehicle_isValid;

    QString m_weighting;
    bool m_weighting_isSet;
    bool m_weighting_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIRouteRequest)

#endif // OAIRouteRequest_H
