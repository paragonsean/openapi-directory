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

#ifndef OAI_OAIRoutingAPIApi_H
#define OAI_OAIRoutingAPIApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIGHError.h"
#include "OAIInfoResponse.h"
#include "OAIRouteRequest.h"
#include "OAIRouteResponse.h"
#include "OAIVehicleProfileId.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIRoutingAPIApi : public QObject {
    Q_OBJECT

public:
    OAIRoutingAPIApi(const int timeOut = 0);
    ~OAIRoutingAPIApi();

    void initializeServerConfigs();
    int setDefaultServerValue(int serverIndex,const QString &operation, const QString &variable,const QString &val);
    void setServerIndex(const QString &operation, int serverIndex);
    void setApiKey(const QString &apiKeyName, const QString &apiKey);
    void setBearerToken(const QString &token);
    void setUsername(const QString &username);
    void setPassword(const QString &password);
    void setTimeOut(const int timeOut);
    void setWorkingDirectory(const QString &path);
    void setNetworkAccessManager(QNetworkAccessManager* manager);
    int addServerConfiguration(const QString &operation, const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables = QMap<QString, OAIServerVariable>());
    void setNewServerForAllOperations(const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables =  QMap<QString, OAIServerVariable>());
    void setNewServer(const QString &operation, const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables =  QMap<QString, OAIServerVariable>());
    void addHeaders(const QString &key, const QString &value);
    void enableRequestCompression();
    void enableResponseCompression();
    void abortRequests();
    QString getParamStylePrefix(const QString &style);
    QString getParamStyleSuffix(const QString &style);
    QString getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode);

    /**
    * @param[in]  point QList<QString> [required]
    * @param[in]  point_hint QList<QString> [optional]
    * @param[in]  snap_prevention QList<QString> [optional]
    * @param[in]  vehicle OAIVehicleProfileId [optional]
    * @param[in]  curbside QList<QString> [optional]
    * @param[in]  turn_costs bool [optional]
    * @param[in]  locale QString [optional]
    * @param[in]  elevation bool [optional]
    * @param[in]  details QList<QString> [optional]
    * @param[in]  optimize QString [optional]
    * @param[in]  instructions bool [optional]
    * @param[in]  calc_points bool [optional]
    * @param[in]  debug bool [optional]
    * @param[in]  points_encoded bool [optional]
    * @param[in]  ch_disable bool [optional]
    * @param[in]  weighting QString [optional]
    * @param[in]  heading QList<qint32> [optional]
    * @param[in]  heading_penalty qint32 [optional]
    * @param[in]  pass_through bool [optional]
    * @param[in]  block_area QString [optional]
    * @param[in]  avoid QString [optional]
    * @param[in]  algorithm QString [optional]
    * @param[in]  round_trip_distance qint32 [optional]
    * @param[in]  round_trip_seed qint64 [optional]
    * @param[in]  alternative_route_max_paths qint32 [optional]
    * @param[in]  alternative_route_max_weight_factor double [optional]
    * @param[in]  alternative_route_max_share_factor double [optional]
    */
    virtual void getRoute(const QList<QString> &point, const ::OpenAPI::OptionalParam<QList<QString>> &point_hint = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<QList<QString>> &snap_prevention = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<OAIVehicleProfileId> &vehicle = ::OpenAPI::OptionalParam<OAIVehicleProfileId>(), const ::OpenAPI::OptionalParam<QList<QString>> &curbside = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<bool> &turn_costs = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &locale = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &elevation = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QList<QString>> &details = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<QString> &optimize = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &instructions = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<bool> &calc_points = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<bool> &debug = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<bool> &points_encoded = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<bool> &ch_disable = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &weighting = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QList<qint32>> &heading = ::OpenAPI::OptionalParam<QList<qint32>>(), const ::OpenAPI::OptionalParam<qint32> &heading_penalty = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<bool> &pass_through = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &block_area = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &avoid = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &round_trip_distance = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint64> &round_trip_seed = ::OpenAPI::OptionalParam<qint64>(), const ::OpenAPI::OptionalParam<qint32> &alternative_route_max_paths = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<double> &alternative_route_max_weight_factor = ::OpenAPI::OptionalParam<double>(), const ::OpenAPI::OptionalParam<double> &alternative_route_max_share_factor = ::OpenAPI::OptionalParam<double>());

    /**
    * @param[in]  oai_route_request OAIRouteRequest [optional]
    */
    virtual void postRoute(const ::OpenAPI::OptionalParam<OAIRouteRequest> &oai_route_request = ::OpenAPI::OptionalParam<OAIRouteRequest>());


    virtual void routeInfoGet();


private:
    QMap<QString,int> _serverIndices;
    QMap<QString,QList<OAIServerConfiguration>> _serverConfigs;
    QMap<QString, QString> _apiKeys;
    QString _bearerToken;
    QString _username;
    QString _password;
    int _timeOut;
    QString _workingDirectory;
    QNetworkAccessManager* _manager;
    QMap<QString, QString> _defaultHeaders;
    bool _isResponseCompressionEnabled;
    bool _isRequestCompressionEnabled;
    OAIHttpRequestInput _latestInput;
    OAIHttpRequestWorker *_latestWorker;
    QStringList _latestScope;
    OauthCode _authFlow;
    OauthImplicit _implicitFlow;
    OauthCredentials _credentialFlow;
    OauthPassword _passwordFlow;
    int _OauthMethod = 0;

    void getRouteCallback(OAIHttpRequestWorker *worker);
    void postRouteCallback(OAIHttpRequestWorker *worker);
    void routeInfoGetCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void getRouteSignal(OAIRouteResponse summary);
    void postRouteSignal(OAIRouteResponse summary);
    void routeInfoGetSignal(OAIInfoResponse summary);


    void getRouteSignalFull(OAIHttpRequestWorker *worker, OAIRouteResponse summary);
    void postRouteSignalFull(OAIHttpRequestWorker *worker, OAIRouteResponse summary);
    void routeInfoGetSignalFull(OAIHttpRequestWorker *worker, OAIInfoResponse summary);

    Q_DECL_DEPRECATED_X("Use getRouteSignalError() instead")
    void getRouteSignalE(OAIRouteResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getRouteSignalError(OAIRouteResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postRouteSignalError() instead")
    void postRouteSignalE(OAIRouteResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postRouteSignalError(OAIRouteResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use routeInfoGetSignalError() instead")
    void routeInfoGetSignalE(OAIInfoResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void routeInfoGetSignalError(OAIInfoResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use getRouteSignalErrorFull() instead")
    void getRouteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getRouteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postRouteSignalErrorFull() instead")
    void postRouteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postRouteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use routeInfoGetSignalErrorFull() instead")
    void routeInfoGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void routeInfoGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
