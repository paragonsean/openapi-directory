/**
 * Wowza Streaming Cloud REST API Reference Documentation
 *  # About the REST API  The Wowza Streaming Cloud<sup>TM</sup> REST API (application programming interface) offers complete programmatic control over live streams, transcoders, stream sources, and stream targets. Anything you can do in the Wowza Streaming Cloud UI can also be achieved by making HTTP-based requests to cloud-based servers through the REST API.  The Wowza Streaming Cloud REST API features *cross-origin resource sharing*, or CORS. CORS is a [W3C specification](https://www.w3.org/TR/cors/) that provides headers in HTTP requests to enable a web server to safely make a network request to another domain.  In order to protect shared resources, the Wowza Streaming Cloud REST API is subject to limits. For details, see [Wowza Streaming Cloud REST API limits](https://www.wowza.com/docs/wowza-streaming-cloud-rest-api-limits). # About this documentation This reference documentation is based on the open-source [Swagger framework](http://swagger.io/specification/). It allows you to view the operations, parameters, and request and reponse schemas for every resource. Request samples are presented in cURL (Shell) and JavaScript; some samples also include just the JSON object. Response samples are all JSON.  For more information and examples on using the Wowza Streaming Cloud REST API, see our [library of Wowza Streaming Cloud REST API technical articles](https://www.wowza.com/docs/wowza-streaming-cloud-rest-api).  # Query requirements The Wowza Streaming Cloud REST API uses HTTP requests to retrieve data from cloud-based servers. Requests must contain proper JSON, two authentication keys, and the correct version number in the base path.  ## JSON The Wowza Streaming Cloud REST API uses the [JSON API specification](http://jsonapi.org/format/) to request and return data. This means requests must include the header `Content-Type: application/json` and must include a single resource object in JSON format as primary data.  Responses include HTTP status codes that indicate whether the query was successful. If there was an error, a description explains the problem so that you can fix it and try again.  ## Authentication Requests to the Wowza Streaming Cloud REST API must be authenticated with two keys: an API key and an access key. Each key is a 64-character alphanumeric string that you can find on the **API Access** page in Wowza Streaming Cloud.  Use the `wsc-api-key` and `wsc-access-key` headers to authenticate requests, like this (in cURL):  ```bash curl -H 'wsc-api-key: [64-character-api-key-goes-here]' -H 'wsc-access-key: [64-character-access-key-goes-here]' ```  <!-- ReDoc-Inject: <security-definitions> -->  ## Version The Wowza Streaming Cloud API is currently at version 1.0.0. Use `v1` in your base path in every request, like this path to the live_streams endpoint: ``` https://api.cloud.wowza.com/api/v1/live_streams ``` ## Example query Here is a complete example POST request, in cURL, with proper JSON syntax, headers, authentication, and version information: ```bash curl -H 'wsc-api-key: [64-character-api-key-goes-here]' -H 'wsc-access-key: [64-character-access-key-goes-here]'   -H 'Content-Type: application/json' -X POST -d '{     \"live_stream\": {       \"name\": \"My live Stream\",       \"...\": \"...\"     }   }' https://api.cloud.wowza.com/api/v1/live_streams ``` 
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIStreamTargetsApi_H
#define OAI_OAIStreamTargetsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAICreateStreamTargetProperty_200_response.h"
#include "OAICreateStreamTarget_200_response.h"
#include "OAIError401.h"
#include "OAIError403.h"
#include "OAIError404.h"
#include "OAIError410.h"
#include "OAIError422.h"
#include "OAIGeoblock_create_input.h"
#include "OAIGeoblock_update_input.h"
#include "OAIRegenerateConnectionCodeStreamTarget_200_response.h"
#include "OAIShowStreamTargetGeoblock_200_response.h"
#include "OAIShowStreamTargetMetricsCurrent_200_response.h"
#include "OAIShowStreamTargetMetricsHistoric_200_response.h"
#include "OAIShowStreamTargetTokenAuth_200_response.h"
#include "OAIStream_target_create_input.h"
#include "OAIStream_target_properties.h"
#include "OAIStream_target_property_create_input.h"
#include "OAIStream_target_update_input.h"
#include "OAIStream_targets.h"
#include "OAIToken_auth_create_input.h"
#include "OAIToken_auth_update_input.h"
#include "OAIWowza_stream_target_input.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIStreamTargetsApi : public QObject {
    Q_OBJECT

public:
    OAIStreamTargetsApi(const int timeOut = 0);
    ~OAIStreamTargetsApi();

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
    * @param[in]  stream_target OAIWowza_stream_target_input [required]
    */
    Q_DECL_DEPRECATED virtual void addStreamTarget(const OAIWowza_stream_target_input &stream_target);

    /**
    * @param[in]  stream_target OAIStream_target_create_input [required]
    */
    virtual void createStreamTarget(const OAIStream_target_create_input &stream_target);

    /**
    * @param[in]  stream_target_id QString [required]
    * @param[in]  geoblock OAIGeoblock_create_input [required]
    */
    virtual void createStreamTargetGeoblock(const QString &stream_target_id, const OAIGeoblock_create_input &geoblock);

    /**
    * @param[in]  stream_target_id QString [required]
    * @param[in]  property OAIStream_target_property_create_input [required]
    */
    virtual void createStreamTargetProperty(const QString &stream_target_id, const OAIStream_target_property_create_input &property);

    /**
    * @param[in]  stream_target_id QString [required]
    * @param[in]  token_auth OAIToken_auth_create_input [required]
    */
    virtual void createStreamTargetTokenAuth(const QString &stream_target_id, const OAIToken_auth_create_input &token_auth);

    /**
    * @param[in]  id QString [required]
    */
    virtual void deleteStreamTarget(const QString &id);

    /**
    * @param[in]  stream_target_id QString [required]
    * @param[in]  id QString [required]
    */
    virtual void deleteStreamTargetProperty(const QString &stream_target_id, const QString &id);

    /**
    * @param[in]  stream_target_id QString [required]
    */
    virtual void listStreamTargetProperties(const QString &stream_target_id);

    /**
    * @param[in]  page qint32 [optional]
    * @param[in]  per_page qint32 [optional]
    */
    virtual void listStreamTargets(const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &per_page = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    */
    virtual void regenerateConnectionCodeStreamTarget(const QString &id);

    /**
    * @param[in]  id QString [required]
    */
    virtual void showStreamTarget(const QString &id);

    /**
    * @param[in]  stream_target_id QString [required]
    */
    virtual void showStreamTargetGeoblock(const QString &stream_target_id);

    /**
    * @param[in]  id QString [required]
    */
    virtual void showStreamTargetMetricsCurrent(const QString &id);

    /**
    * @param[in]  id QString [required]
    * @param[in]  from QString [optional]
    * @param[in]  to QString [optional]
    * @param[in]  interval QString [optional]
    */
    virtual void showStreamTargetMetricsHistoric(const QString &id, const ::OpenAPI::OptionalParam<QString> &from = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &to = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &interval = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  stream_target_id QString [required]
    * @param[in]  id QString [required]
    */
    virtual void showStreamTargetProperty(const QString &stream_target_id, const QString &id);

    /**
    * @param[in]  stream_target_id QString [required]
    */
    virtual void showStreamTargetTokenAuth(const QString &stream_target_id);

    /**
    * @param[in]  id QString [required]
    * @param[in]  stream_target OAIStream_target_update_input [required]
    */
    virtual void updateStreamTarget(const QString &id, const OAIStream_target_update_input &stream_target);

    /**
    * @param[in]  stream_target_id QString [required]
    * @param[in]  geoblock OAIGeoblock_update_input [required]
    */
    virtual void updateStreamTargetGeoblock(const QString &stream_target_id, const OAIGeoblock_update_input &geoblock);

    /**
    * @param[in]  stream_target_id QString [required]
    * @param[in]  token_auth OAIToken_auth_update_input [required]
    */
    virtual void updateStreamTargetTokenAuth(const QString &stream_target_id, const OAIToken_auth_update_input &token_auth);


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

    void addStreamTargetCallback(OAIHttpRequestWorker *worker);
    void createStreamTargetCallback(OAIHttpRequestWorker *worker);
    void createStreamTargetGeoblockCallback(OAIHttpRequestWorker *worker);
    void createStreamTargetPropertyCallback(OAIHttpRequestWorker *worker);
    void createStreamTargetTokenAuthCallback(OAIHttpRequestWorker *worker);
    void deleteStreamTargetCallback(OAIHttpRequestWorker *worker);
    void deleteStreamTargetPropertyCallback(OAIHttpRequestWorker *worker);
    void listStreamTargetPropertiesCallback(OAIHttpRequestWorker *worker);
    void listStreamTargetsCallback(OAIHttpRequestWorker *worker);
    void regenerateConnectionCodeStreamTargetCallback(OAIHttpRequestWorker *worker);
    void showStreamTargetCallback(OAIHttpRequestWorker *worker);
    void showStreamTargetGeoblockCallback(OAIHttpRequestWorker *worker);
    void showStreamTargetMetricsCurrentCallback(OAIHttpRequestWorker *worker);
    void showStreamTargetMetricsHistoricCallback(OAIHttpRequestWorker *worker);
    void showStreamTargetPropertyCallback(OAIHttpRequestWorker *worker);
    void showStreamTargetTokenAuthCallback(OAIHttpRequestWorker *worker);
    void updateStreamTargetCallback(OAIHttpRequestWorker *worker);
    void updateStreamTargetGeoblockCallback(OAIHttpRequestWorker *worker);
    void updateStreamTargetTokenAuthCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void addStreamTargetSignal(OAICreateStreamTarget_200_response summary);
    void createStreamTargetSignal(OAICreateStreamTarget_200_response summary);
    void createStreamTargetGeoblockSignal(OAIShowStreamTargetGeoblock_200_response summary);
    void createStreamTargetPropertySignal(OAICreateStreamTargetProperty_200_response summary);
    void createStreamTargetTokenAuthSignal(OAIShowStreamTargetTokenAuth_200_response summary);
    void deleteStreamTargetSignal();
    void deleteStreamTargetPropertySignal();
    void listStreamTargetPropertiesSignal(OAIStream_target_properties summary);
    void listStreamTargetsSignal(OAIStream_targets summary);
    void regenerateConnectionCodeStreamTargetSignal(OAIRegenerateConnectionCodeStreamTarget_200_response summary);
    void showStreamTargetSignal(OAICreateStreamTarget_200_response summary);
    void showStreamTargetGeoblockSignal(OAIShowStreamTargetGeoblock_200_response summary);
    void showStreamTargetMetricsCurrentSignal(OAIShowStreamTargetMetricsCurrent_200_response summary);
    void showStreamTargetMetricsHistoricSignal(OAIShowStreamTargetMetricsHistoric_200_response summary);
    void showStreamTargetPropertySignal(OAICreateStreamTargetProperty_200_response summary);
    void showStreamTargetTokenAuthSignal(OAIShowStreamTargetTokenAuth_200_response summary);
    void updateStreamTargetSignal(OAICreateStreamTarget_200_response summary);
    void updateStreamTargetGeoblockSignal(OAIShowStreamTargetGeoblock_200_response summary);
    void updateStreamTargetTokenAuthSignal(OAIShowStreamTargetTokenAuth_200_response summary);


    void addStreamTargetSignalFull(OAIHttpRequestWorker *worker, OAICreateStreamTarget_200_response summary);
    void createStreamTargetSignalFull(OAIHttpRequestWorker *worker, OAICreateStreamTarget_200_response summary);
    void createStreamTargetGeoblockSignalFull(OAIHttpRequestWorker *worker, OAIShowStreamTargetGeoblock_200_response summary);
    void createStreamTargetPropertySignalFull(OAIHttpRequestWorker *worker, OAICreateStreamTargetProperty_200_response summary);
    void createStreamTargetTokenAuthSignalFull(OAIHttpRequestWorker *worker, OAIShowStreamTargetTokenAuth_200_response summary);
    void deleteStreamTargetSignalFull(OAIHttpRequestWorker *worker);
    void deleteStreamTargetPropertySignalFull(OAIHttpRequestWorker *worker);
    void listStreamTargetPropertiesSignalFull(OAIHttpRequestWorker *worker, OAIStream_target_properties summary);
    void listStreamTargetsSignalFull(OAIHttpRequestWorker *worker, OAIStream_targets summary);
    void regenerateConnectionCodeStreamTargetSignalFull(OAIHttpRequestWorker *worker, OAIRegenerateConnectionCodeStreamTarget_200_response summary);
    void showStreamTargetSignalFull(OAIHttpRequestWorker *worker, OAICreateStreamTarget_200_response summary);
    void showStreamTargetGeoblockSignalFull(OAIHttpRequestWorker *worker, OAIShowStreamTargetGeoblock_200_response summary);
    void showStreamTargetMetricsCurrentSignalFull(OAIHttpRequestWorker *worker, OAIShowStreamTargetMetricsCurrent_200_response summary);
    void showStreamTargetMetricsHistoricSignalFull(OAIHttpRequestWorker *worker, OAIShowStreamTargetMetricsHistoric_200_response summary);
    void showStreamTargetPropertySignalFull(OAIHttpRequestWorker *worker, OAICreateStreamTargetProperty_200_response summary);
    void showStreamTargetTokenAuthSignalFull(OAIHttpRequestWorker *worker, OAIShowStreamTargetTokenAuth_200_response summary);
    void updateStreamTargetSignalFull(OAIHttpRequestWorker *worker, OAICreateStreamTarget_200_response summary);
    void updateStreamTargetGeoblockSignalFull(OAIHttpRequestWorker *worker, OAIShowStreamTargetGeoblock_200_response summary);
    void updateStreamTargetTokenAuthSignalFull(OAIHttpRequestWorker *worker, OAIShowStreamTargetTokenAuth_200_response summary);

    Q_DECL_DEPRECATED_X("Use addStreamTargetSignalError() instead")
    void addStreamTargetSignalE(OAICreateStreamTarget_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void addStreamTargetSignalError(OAICreateStreamTarget_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createStreamTargetSignalError() instead")
    void createStreamTargetSignalE(OAICreateStreamTarget_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createStreamTargetSignalError(OAICreateStreamTarget_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createStreamTargetGeoblockSignalError() instead")
    void createStreamTargetGeoblockSignalE(OAIShowStreamTargetGeoblock_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createStreamTargetGeoblockSignalError(OAIShowStreamTargetGeoblock_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createStreamTargetPropertySignalError() instead")
    void createStreamTargetPropertySignalE(OAICreateStreamTargetProperty_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createStreamTargetPropertySignalError(OAICreateStreamTargetProperty_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createStreamTargetTokenAuthSignalError() instead")
    void createStreamTargetTokenAuthSignalE(OAIShowStreamTargetTokenAuth_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createStreamTargetTokenAuthSignalError(OAIShowStreamTargetTokenAuth_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteStreamTargetSignalError() instead")
    void deleteStreamTargetSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void deleteStreamTargetSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteStreamTargetPropertySignalError() instead")
    void deleteStreamTargetPropertySignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void deleteStreamTargetPropertySignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listStreamTargetPropertiesSignalError() instead")
    void listStreamTargetPropertiesSignalE(OAIStream_target_properties summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listStreamTargetPropertiesSignalError(OAIStream_target_properties summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listStreamTargetsSignalError() instead")
    void listStreamTargetsSignalE(OAIStream_targets summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listStreamTargetsSignalError(OAIStream_targets summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use regenerateConnectionCodeStreamTargetSignalError() instead")
    void regenerateConnectionCodeStreamTargetSignalE(OAIRegenerateConnectionCodeStreamTarget_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void regenerateConnectionCodeStreamTargetSignalError(OAIRegenerateConnectionCodeStreamTarget_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use showStreamTargetSignalError() instead")
    void showStreamTargetSignalE(OAICreateStreamTarget_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void showStreamTargetSignalError(OAICreateStreamTarget_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use showStreamTargetGeoblockSignalError() instead")
    void showStreamTargetGeoblockSignalE(OAIShowStreamTargetGeoblock_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void showStreamTargetGeoblockSignalError(OAIShowStreamTargetGeoblock_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use showStreamTargetMetricsCurrentSignalError() instead")
    void showStreamTargetMetricsCurrentSignalE(OAIShowStreamTargetMetricsCurrent_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void showStreamTargetMetricsCurrentSignalError(OAIShowStreamTargetMetricsCurrent_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use showStreamTargetMetricsHistoricSignalError() instead")
    void showStreamTargetMetricsHistoricSignalE(OAIShowStreamTargetMetricsHistoric_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void showStreamTargetMetricsHistoricSignalError(OAIShowStreamTargetMetricsHistoric_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use showStreamTargetPropertySignalError() instead")
    void showStreamTargetPropertySignalE(OAICreateStreamTargetProperty_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void showStreamTargetPropertySignalError(OAICreateStreamTargetProperty_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use showStreamTargetTokenAuthSignalError() instead")
    void showStreamTargetTokenAuthSignalE(OAIShowStreamTargetTokenAuth_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void showStreamTargetTokenAuthSignalError(OAIShowStreamTargetTokenAuth_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateStreamTargetSignalError() instead")
    void updateStreamTargetSignalE(OAICreateStreamTarget_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateStreamTargetSignalError(OAICreateStreamTarget_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateStreamTargetGeoblockSignalError() instead")
    void updateStreamTargetGeoblockSignalE(OAIShowStreamTargetGeoblock_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateStreamTargetGeoblockSignalError(OAIShowStreamTargetGeoblock_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateStreamTargetTokenAuthSignalError() instead")
    void updateStreamTargetTokenAuthSignalE(OAIShowStreamTargetTokenAuth_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateStreamTargetTokenAuthSignalError(OAIShowStreamTargetTokenAuth_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use addStreamTargetSignalErrorFull() instead")
    void addStreamTargetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void addStreamTargetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createStreamTargetSignalErrorFull() instead")
    void createStreamTargetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createStreamTargetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createStreamTargetGeoblockSignalErrorFull() instead")
    void createStreamTargetGeoblockSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createStreamTargetGeoblockSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createStreamTargetPropertySignalErrorFull() instead")
    void createStreamTargetPropertySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createStreamTargetPropertySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createStreamTargetTokenAuthSignalErrorFull() instead")
    void createStreamTargetTokenAuthSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createStreamTargetTokenAuthSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteStreamTargetSignalErrorFull() instead")
    void deleteStreamTargetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteStreamTargetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteStreamTargetPropertySignalErrorFull() instead")
    void deleteStreamTargetPropertySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteStreamTargetPropertySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listStreamTargetPropertiesSignalErrorFull() instead")
    void listStreamTargetPropertiesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listStreamTargetPropertiesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listStreamTargetsSignalErrorFull() instead")
    void listStreamTargetsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listStreamTargetsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use regenerateConnectionCodeStreamTargetSignalErrorFull() instead")
    void regenerateConnectionCodeStreamTargetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void regenerateConnectionCodeStreamTargetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use showStreamTargetSignalErrorFull() instead")
    void showStreamTargetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void showStreamTargetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use showStreamTargetGeoblockSignalErrorFull() instead")
    void showStreamTargetGeoblockSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void showStreamTargetGeoblockSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use showStreamTargetMetricsCurrentSignalErrorFull() instead")
    void showStreamTargetMetricsCurrentSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void showStreamTargetMetricsCurrentSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use showStreamTargetMetricsHistoricSignalErrorFull() instead")
    void showStreamTargetMetricsHistoricSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void showStreamTargetMetricsHistoricSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use showStreamTargetPropertySignalErrorFull() instead")
    void showStreamTargetPropertySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void showStreamTargetPropertySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use showStreamTargetTokenAuthSignalErrorFull() instead")
    void showStreamTargetTokenAuthSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void showStreamTargetTokenAuthSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateStreamTargetSignalErrorFull() instead")
    void updateStreamTargetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateStreamTargetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateStreamTargetGeoblockSignalErrorFull() instead")
    void updateStreamTargetGeoblockSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateStreamTargetGeoblockSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateStreamTargetTokenAuthSignalErrorFull() instead")
    void updateStreamTargetTokenAuthSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateStreamTargetTokenAuthSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
