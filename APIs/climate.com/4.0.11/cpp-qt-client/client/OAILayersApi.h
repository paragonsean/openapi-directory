/**
 * Climate FieldView Platform APIs
 * **Last Modified**: Wed Jan  4 12:47:29 UTC 2023   All endpoints are only accessible via HTTPS.  * All API endpoints are located at `https://platform.climate.com` (e.g. `https://platform.climate.com/v4/fields`).  * The authorization token endpoint is located at `https://api.climate.com/api/oauth/token`.  ## Troubleshooting  `X-Http-Request-Id` response header will be returned on every call, successful or not. If you experience an issue with our api and need to contact technical support, please supply the value of the `X-Http-Request-Id` header along with an approximate time of when the request was made.  ## Request Limits  When you’re onboarded to Climate’s API platform, your `x-api-key` is assigned a custom usage plan. Usage plans are unique to each partner and have the following key attributes:   1. Throttling information     * burstLimit: Maximum rate limit over a period ranging from 1 second to a few seconds     * rateLimit: A steady-state rate limit  2. Quota information     * Limit: The maximum number of requests that can be made in a given month  When the request rate threshold is exceeded, a `429` response code is returned. Optionally, the [`Retry-After`](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.37) header may be returned:   Following are examples of rate limit errors:  1. Rate limit exceeded:  <br>HTTP/1.1 429  <br>Content-Type: application/json <br>Content-Length: 32     {\"message\":\"Too Many Requests\"}  2. Quota exhausted: <br>HTTP/1.1 429  <br>Content-Type: application/json <br>Content-Length: 29      {\"message\":\"Limit Exceeded\"}  ## Pagination  Pagination is performed via headers. Any request which returns a `\"results\"` array may be paginated. The following figure shows how query results are laid out with X-Limit=4 and no filter applied.  <img style=\"width:70%;height:auto;\" src=\"https://s3-us-west-2.amazonaws.com/climate-com/images/svg_upload_tests/paging.png\">  * If there are no results, a response code of `304` will be returned.  * If the response is the last set of results, a response code of `200` or `206` will be returned.  * If there are more results, a response code of `206` will be returned.  * If `X-Next-Token` is provided in the request headers but the token has expired, a response code of `409` will be returned. This is only applicable for some endpoints; see specific endpoint documentation below.  #### X-Limit  The page size can be controlled with the `X-Limit` header. Valid values are `1-100` and defaults to `100`.  #### X-Next-Token  If the results are paginated, a response header of `X-Next-Token` will be returned. Use the associated value in the subsequent request (via the `X-Next-Token` request header) to retrieve the next page. The following sequence diagram shows how to use `X-Next-Token` to fetch all the records.  <img src=\"https://s3-us-west-2.amazonaws.com/climate-com/images/svg_upload_tests/x-next-token.svg\">   ## Chunked Uploads  Uploads larger than `5MiB` (`5242880 bytes`) must be done in `5MiB` chunks (with the exception of the final chunk). Each chunk request MUST contain a `Content-Range` header specifying the portion of the upload, and a `Content-Type` header specifying binary content type (`application/octet-stream`). Range uploads must be contiguous. The maximum upload size is capped at `500MiB` (`524288000 bytes`).  ## Chunked Downloads  Downloads larger than `5MiB` (`5242880 bytes`) must be done in `1-5MiB` chunks (with the exception of the final chunk, which may be less than `1MiB`). Each chunk request MUST contain a `Range` header specifying the requested portion of the download, and an `Accept` header specifying binary and json content types  (`application/octet-stream,application/json`) or all content types (`*_/_*`).  ## Drivers  If you need drivers to process agronomic data, download the ADAPT plugin below. We only support the plugin in the Windows environment, minimum is Windows 7 SP1.  For asPlanted, asHarvested and asApplied data: * [ADAPT Plugin](https://dev.fieldview.com/drivers/ClimateADAPTPlugin_latest.exe) <br>Release notes can be found [here](https://dev.fieldview.com/drivers/adapt-release-notes.txt). <br>Download and use of the ADAPT plugin means that you agree to the EULA for use of the ADAPT plugin.  <br>Please review the [EULA](https://dev.fieldview.com/EULA/ADAPT%20Plugin%20EULA-06-19.pdf) (last updated on June 6th, 2019) before download and use of the ADAPT plugin. <br>For more information, please refer to:   * [ADAPT Resources](https://adaptframework.org/)   * [ADAPT Overview](https://aggateway.atlassian.net/wiki/spaces/ADM/overview)   * [ADAPT FAQ](https://aggateway.atlassian.net/wiki/spaces/ADM/pages/165942474/ADAPT+Frequently-Asked+Questions+FAQ)   * [ADAPT Videos](https://adaptframework.org/adapt-videos/)  ## Sample Test Data  Sample agronomic data: * [asPlanted and asHarvested data](https://dev.fieldview.com/sample-agronomic-data/Planting_Harvesting_data_04_18_2018_21_46_18.zip) * [asApplied data set 1](https://dev.fieldview.com/sample-agronomic-data/as-applied-data1.zip) * [asApplied data set 2](https://dev.fieldview.com/sample-agronomic-data/as-applied-data2.zip) <br>To upload the sample data to your account, please follow the instructions in this [link](https://support.climate.com/kt#/kA02A000000AaxzSAC/en_US).  Sample soil data: * [Sample soil data](https://dev.fieldview.com/sample-soil-data/soil-sample.xml) --- 
 *
 * The version of the OpenAPI document: 4.0.11
 * Contact: developer@climate.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAILayersApi_H
#define OAI_OAILayersApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIApplicationActivities.h"
#include "OAIApplicationActivityContents.h"
#include "OAIError.h"
#include "OAIHarvestActivities.h"
#include "OAIHarvestActivityContents.h"
#include "OAIObject.h"
#include "OAIPlantingActivities.h"
#include "OAIPlantingActivityContents.h"
#include "OAIScoutingObservation.h"
#include "OAIScoutingObservationAttachmentContents.h"
#include "OAIScoutingObservationAttachments.h"
#include "OAIScoutingObservations.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAILayersApi : public QObject {
    Q_OBJECT

public:
    OAILayersApi(const int timeOut = 0);
    ~OAILayersApi();

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
    * @param[in]  accept QString [required]
    * @param[in]  activity_id QString [required]
    * @param[in]  range QString [required]
    */
    virtual void v4LayersAsAppliedActivityIdContentsGet(const QString &accept, const QString &activity_id, const QString &range);

    /**
    * @param[in]  accept QString [required]
    * @param[in]  x_next_token QString [optional]
    * @param[in]  x_limit qint32 [optional]
    * @param[in]  resource_owner_id QString [optional]
    * @param[in]  occurred_after QDateTime [optional]
    * @param[in]  occurred_before QDateTime [optional]
    * @param[in]  updated_after QDateTime [optional]
    */
    virtual void v4LayersAsAppliedGet(const QString &accept, const ::OpenAPI::OptionalParam<QString> &x_next_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &x_limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &resource_owner_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QDateTime> &occurred_after = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<QDateTime> &occurred_before = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<QDateTime> &updated_after = ::OpenAPI::OptionalParam<QDateTime>());

    /**
    * @param[in]  accept QString [required]
    * @param[in]  activity_id QString [required]
    * @param[in]  range QString [required]
    */
    virtual void v4LayersAsHarvestedActivityIdContentsGet(const QString &accept, const QString &activity_id, const QString &range);

    /**
    * @param[in]  accept QString [required]
    * @param[in]  x_next_token QString [optional]
    * @param[in]  x_limit qint32 [optional]
    * @param[in]  resource_owner_id QString [optional]
    * @param[in]  occurred_after QDateTime [optional]
    * @param[in]  occurred_before QDateTime [optional]
    * @param[in]  updated_after QDateTime [optional]
    */
    virtual void v4LayersAsHarvestedGet(const QString &accept, const ::OpenAPI::OptionalParam<QString> &x_next_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &x_limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &resource_owner_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QDateTime> &occurred_after = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<QDateTime> &occurred_before = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<QDateTime> &updated_after = ::OpenAPI::OptionalParam<QDateTime>());

    /**
    * @param[in]  accept QString [required]
    * @param[in]  activity_id QString [required]
    * @param[in]  range QString [required]
    */
    virtual void v4LayersAsPlantedActivityIdContentsGet(const QString &accept, const QString &activity_id, const QString &range);

    /**
    * @param[in]  accept QString [required]
    * @param[in]  x_next_token QString [optional]
    * @param[in]  x_limit qint32 [optional]
    * @param[in]  resource_owner_id QString [optional]
    * @param[in]  occurred_after QDateTime [optional]
    * @param[in]  occurred_before QDateTime [optional]
    * @param[in]  updated_after QDateTime [optional]
    */
    virtual void v4LayersAsPlantedGet(const QString &accept, const ::OpenAPI::OptionalParam<QString> &x_next_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &x_limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &resource_owner_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QDateTime> &occurred_after = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<QDateTime> &occurred_before = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<QDateTime> &updated_after = ::OpenAPI::OptionalParam<QDateTime>());

    /**
    * @param[in]  x_next_token QString [optional]
    * @param[in]  x_limit qint32 [optional]
    * @param[in]  occurred_after QDateTime [optional]
    * @param[in]  occurred_before QDateTime [optional]
    */
    virtual void v4LayersScoutingObservationsGet(const ::OpenAPI::OptionalParam<QString> &x_next_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &x_limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QDateTime> &occurred_after = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<QDateTime> &occurred_before = ::OpenAPI::OptionalParam<QDateTime>());

    /**
    * @param[in]  accept QString [required]
    * @param[in]  scouting_observation_id QString [required]
    * @param[in]  attachment_id QString [required]
    * @param[in]  range QString [required]
    */
    virtual void v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGet(const QString &accept, const QString &scouting_observation_id, const QString &attachment_id, const QString &range);

    /**
    * @param[in]  scouting_observation_id QString [required]
    * @param[in]  x_next_token QString [optional]
    * @param[in]  x_limit qint32 [optional]
    */
    virtual void v4LayersScoutingObservationsScoutingObservationIdAttachmentsGet(const QString &scouting_observation_id, const ::OpenAPI::OptionalParam<QString> &x_next_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &x_limit = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  scouting_observation_id QString [required]
    */
    virtual void v4LayersScoutingObservationsScoutingObservationIdGet(const QString &scouting_observation_id);


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

    void v4LayersAsAppliedActivityIdContentsGetCallback(OAIHttpRequestWorker *worker);
    void v4LayersAsAppliedGetCallback(OAIHttpRequestWorker *worker);
    void v4LayersAsHarvestedActivityIdContentsGetCallback(OAIHttpRequestWorker *worker);
    void v4LayersAsHarvestedGetCallback(OAIHttpRequestWorker *worker);
    void v4LayersAsPlantedActivityIdContentsGetCallback(OAIHttpRequestWorker *worker);
    void v4LayersAsPlantedGetCallback(OAIHttpRequestWorker *worker);
    void v4LayersScoutingObservationsGetCallback(OAIHttpRequestWorker *worker);
    void v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGetCallback(OAIHttpRequestWorker *worker);
    void v4LayersScoutingObservationsScoutingObservationIdAttachmentsGetCallback(OAIHttpRequestWorker *worker);
    void v4LayersScoutingObservationsScoutingObservationIdGetCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void v4LayersAsAppliedActivityIdContentsGetSignal(OAIApplicationActivityContents summary);
    void v4LayersAsAppliedGetSignal(OAIApplicationActivities summary);
    void v4LayersAsHarvestedActivityIdContentsGetSignal(OAIHarvestActivityContents summary);
    void v4LayersAsHarvestedGetSignal(OAIHarvestActivities summary);
    void v4LayersAsPlantedActivityIdContentsGetSignal(OAIPlantingActivityContents summary);
    void v4LayersAsPlantedGetSignal(OAIPlantingActivities summary);
    void v4LayersScoutingObservationsGetSignal(OAIScoutingObservations summary);
    void v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGetSignal(OAIScoutingObservationAttachmentContents summary);
    void v4LayersScoutingObservationsScoutingObservationIdAttachmentsGetSignal(OAIScoutingObservationAttachments summary);
    void v4LayersScoutingObservationsScoutingObservationIdGetSignal(OAIScoutingObservation summary);


    void v4LayersAsAppliedActivityIdContentsGetSignalFull(OAIHttpRequestWorker *worker, OAIApplicationActivityContents summary);
    void v4LayersAsAppliedGetSignalFull(OAIHttpRequestWorker *worker, OAIApplicationActivities summary);
    void v4LayersAsHarvestedActivityIdContentsGetSignalFull(OAIHttpRequestWorker *worker, OAIHarvestActivityContents summary);
    void v4LayersAsHarvestedGetSignalFull(OAIHttpRequestWorker *worker, OAIHarvestActivities summary);
    void v4LayersAsPlantedActivityIdContentsGetSignalFull(OAIHttpRequestWorker *worker, OAIPlantingActivityContents summary);
    void v4LayersAsPlantedGetSignalFull(OAIHttpRequestWorker *worker, OAIPlantingActivities summary);
    void v4LayersScoutingObservationsGetSignalFull(OAIHttpRequestWorker *worker, OAIScoutingObservations summary);
    void v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGetSignalFull(OAIHttpRequestWorker *worker, OAIScoutingObservationAttachmentContents summary);
    void v4LayersScoutingObservationsScoutingObservationIdAttachmentsGetSignalFull(OAIHttpRequestWorker *worker, OAIScoutingObservationAttachments summary);
    void v4LayersScoutingObservationsScoutingObservationIdGetSignalFull(OAIHttpRequestWorker *worker, OAIScoutingObservation summary);

    Q_DECL_DEPRECATED_X("Use v4LayersAsAppliedActivityIdContentsGetSignalError() instead")
    void v4LayersAsAppliedActivityIdContentsGetSignalE(OAIApplicationActivityContents summary, QNetworkReply::NetworkError error_type, QString error_str);
    void v4LayersAsAppliedActivityIdContentsGetSignalError(OAIApplicationActivityContents summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v4LayersAsAppliedGetSignalError() instead")
    void v4LayersAsAppliedGetSignalE(OAIApplicationActivities summary, QNetworkReply::NetworkError error_type, QString error_str);
    void v4LayersAsAppliedGetSignalError(OAIApplicationActivities summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v4LayersAsHarvestedActivityIdContentsGetSignalError() instead")
    void v4LayersAsHarvestedActivityIdContentsGetSignalE(OAIHarvestActivityContents summary, QNetworkReply::NetworkError error_type, QString error_str);
    void v4LayersAsHarvestedActivityIdContentsGetSignalError(OAIHarvestActivityContents summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v4LayersAsHarvestedGetSignalError() instead")
    void v4LayersAsHarvestedGetSignalE(OAIHarvestActivities summary, QNetworkReply::NetworkError error_type, QString error_str);
    void v4LayersAsHarvestedGetSignalError(OAIHarvestActivities summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v4LayersAsPlantedActivityIdContentsGetSignalError() instead")
    void v4LayersAsPlantedActivityIdContentsGetSignalE(OAIPlantingActivityContents summary, QNetworkReply::NetworkError error_type, QString error_str);
    void v4LayersAsPlantedActivityIdContentsGetSignalError(OAIPlantingActivityContents summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v4LayersAsPlantedGetSignalError() instead")
    void v4LayersAsPlantedGetSignalE(OAIPlantingActivities summary, QNetworkReply::NetworkError error_type, QString error_str);
    void v4LayersAsPlantedGetSignalError(OAIPlantingActivities summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v4LayersScoutingObservationsGetSignalError() instead")
    void v4LayersScoutingObservationsGetSignalE(OAIScoutingObservations summary, QNetworkReply::NetworkError error_type, QString error_str);
    void v4LayersScoutingObservationsGetSignalError(OAIScoutingObservations summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGetSignalError() instead")
    void v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGetSignalE(OAIScoutingObservationAttachmentContents summary, QNetworkReply::NetworkError error_type, QString error_str);
    void v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGetSignalError(OAIScoutingObservationAttachmentContents summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v4LayersScoutingObservationsScoutingObservationIdAttachmentsGetSignalError() instead")
    void v4LayersScoutingObservationsScoutingObservationIdAttachmentsGetSignalE(OAIScoutingObservationAttachments summary, QNetworkReply::NetworkError error_type, QString error_str);
    void v4LayersScoutingObservationsScoutingObservationIdAttachmentsGetSignalError(OAIScoutingObservationAttachments summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v4LayersScoutingObservationsScoutingObservationIdGetSignalError() instead")
    void v4LayersScoutingObservationsScoutingObservationIdGetSignalE(OAIScoutingObservation summary, QNetworkReply::NetworkError error_type, QString error_str);
    void v4LayersScoutingObservationsScoutingObservationIdGetSignalError(OAIScoutingObservation summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use v4LayersAsAppliedActivityIdContentsGetSignalErrorFull() instead")
    void v4LayersAsAppliedActivityIdContentsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void v4LayersAsAppliedActivityIdContentsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v4LayersAsAppliedGetSignalErrorFull() instead")
    void v4LayersAsAppliedGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void v4LayersAsAppliedGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v4LayersAsHarvestedActivityIdContentsGetSignalErrorFull() instead")
    void v4LayersAsHarvestedActivityIdContentsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void v4LayersAsHarvestedActivityIdContentsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v4LayersAsHarvestedGetSignalErrorFull() instead")
    void v4LayersAsHarvestedGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void v4LayersAsHarvestedGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v4LayersAsPlantedActivityIdContentsGetSignalErrorFull() instead")
    void v4LayersAsPlantedActivityIdContentsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void v4LayersAsPlantedActivityIdContentsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v4LayersAsPlantedGetSignalErrorFull() instead")
    void v4LayersAsPlantedGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void v4LayersAsPlantedGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v4LayersScoutingObservationsGetSignalErrorFull() instead")
    void v4LayersScoutingObservationsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void v4LayersScoutingObservationsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGetSignalErrorFull() instead")
    void v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v4LayersScoutingObservationsScoutingObservationIdAttachmentsGetSignalErrorFull() instead")
    void v4LayersScoutingObservationsScoutingObservationIdAttachmentsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void v4LayersScoutingObservationsScoutingObservationIdAttachmentsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v4LayersScoutingObservationsScoutingObservationIdGetSignalErrorFull() instead")
    void v4LayersScoutingObservationsScoutingObservationIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void v4LayersScoutingObservationsScoutingObservationIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
