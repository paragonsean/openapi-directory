/**
 * PeerTube
 * The PeerTube API is built on HTTP(S) and is RESTful. You can use your favorite HTTP/REST library for your programming language to use PeerTube. The spec API is fully compatible with [openapi-generator](https://github.com/OpenAPITools/openapi-generator/wiki/API-client-generator-HOWTO) which generates a client SDK in the language of your choice - we generate some client SDKs automatically:  - [Python](https://framagit.org/framasoft/peertube/clients/python) - [Go](https://framagit.org/framasoft/peertube/clients/go) - [Kotlin](https://framagit.org/framasoft/peertube/clients/kotlin)  See the [REST API quick start](https://docs.joinpeertube.org/api/rest-getting-started) for a few examples of using the PeerTube API.  # Authentication  When you sign up for an account on a PeerTube instance, you are given the possibility to generate sessions on it, and authenticate there using an access token. Only __one access token can currently be used at a time__.  ## Roles  Accounts are given permissions based on their role. There are three roles on PeerTube: Administrator, Moderator, and User. See the [roles guide](https://docs.joinpeertube.org/admin/managing-users#roles) for a detail of their permissions.  # Errors  The API uses standard HTTP status codes to indicate the success or failure of the API call, completed by a [RFC7807-compliant](https://tools.ietf.org/html/rfc7807) response body.  ``` HTTP 1.1 404 Not Found Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Video not found\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"status\": 404,   \"title\": \"Not Found\",   \"type\": \"about:blank\" } ```  We provide error `type` values for [a growing number of cases](https://github.com/Chocobozzz/PeerTube/blob/develop/shared/models/server/server-error-code.enum.ts), but it is still optional. Types are used to disambiguate errors that bear the same status code and are non-obvious:  ``` HTTP 1.1 403 Forbidden Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Cannot get this video regarding follow constraints\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"status\": 403,   \"title\": \"Forbidden\",   \"type\": \"https://docs.joinpeertube.org/api/rest-reference.html#section/Errors/does_not_respect_follow_constraints\" } ```  Here a 403 error could otherwise mean that the video is private or blocklisted.  ### Validation errors  Each parameter is evaluated on its own against a set of rules before the route validator proceeds with potential testing involving parameter combinations. Errors coming from validation errors appear earlier and benefit from a more detailed error description:  ``` HTTP 1.1 400 Bad Request Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Incorrect request parameters: id\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"instance\": \"/api/v1/videos/9c9de5e8-0a1e-484a-b099-e80766180\",   \"invalid-params\": {     \"id\": {       \"location\": \"params\",       \"msg\": \"Invalid value\",       \"param\": \"id\",       \"value\": \"9c9de5e8-0a1e-484a-b099-e80766180\"     }   },   \"status\": 400,   \"title\": \"Bad Request\",   \"type\": \"about:blank\" } ```  Where `id` is the name of the field concerned by the error, within the route definition. `invalid-params.<field>.location` can be either 'params', 'body', 'header', 'query' or 'cookies', and `invalid-params.<field>.value` reports the value that didn't pass validation whose `invalid-params.<field>.msg` is about.  ### Deprecated error fields  Some fields could be included with previous versions. They are still included but their use is deprecated: - `error`: superseded by `detail` - `code`: superseded by `type` (which is now an URI)  # Rate limits  We are rate-limiting all endpoints of PeerTube's API. Custom values can be set by administrators:  | Endpoint (prefix: `/api/v1`) | Calls         | Time frame   | |------------------------------|---------------|--------------| | `/_*`                         | 50            | 10 seconds   | | `POST /users/token`          | 15            | 5 minutes    | | `POST /users/register`       | 2<sup>*</sup> | 5 minutes    | | `POST /users/ask-send-verify-email` | 3      | 5 minutes    |  Depending on the endpoint, <sup>*</sup>failed requests are not taken into account. A service limit is announced by a `429 Too Many Requests` status code.  You can get details about the current state of your rate limit by reading the following headers:  | Header                  | Description                                                | |-------------------------|------------------------------------------------------------| | `X-RateLimit-Limit`     | Number of max requests allowed in the current time period  | | `X-RateLimit-Remaining` | Number of remaining requests in the current time period    | | `X-RateLimit-Reset`     | Timestamp of end of current time period as UNIX timestamp  | | `Retry-After`           | Seconds to delay after the first `429` is received         |  # CORS  This API features [Cross-Origin Resource Sharing (CORS)](https://fetch.spec.whatwg.org/), allowing cross-domain communication from the browser for some routes:  | Endpoint                    | |------------------------- ---| | `/api/_*`                    | | `/download/_*`               | | `/lazy-static/_*`            | | `/.well-known/webfinger`    |  In addition, all routes serving ActivityPub are CORS-enabled for all origins. 
 *
 * The version of the OpenAPI document: 5.1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIPluginsApi_H
#define OAI_OAIPluginsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIAddPlugin_request.h"
#include "OAIPlugin.h"
#include "OAIPluginResponse.h"
#include "OAIUninstallPlugin_request.h"
#include "OAI_api_v1_plugins__npmName__settings_put_request.h"
#include <QJsonValue>
#include <QMap>
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIPluginsApi : public QObject {
    Q_OBJECT

public:
    OAIPluginsApi(const int timeOut = 0);
    ~OAIPluginsApi();

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
    * @param[in]  oai_add_plugin_request OAIAddPlugin_request [optional]
    */
    virtual void addPlugin(const ::OpenAPI::OptionalParam<OAIAddPlugin_request> &oai_add_plugin_request = ::OpenAPI::OptionalParam<OAIAddPlugin_request>());

    /**
    * @param[in]  npm_name QString [required]
    */
    virtual void apiV1PluginsNpmNamePublicSettingsGet(const QString &npm_name);

    /**
    * @param[in]  npm_name QString [required]
    */
    virtual void apiV1PluginsNpmNameRegisteredSettingsGet(const QString &npm_name);

    /**
    * @param[in]  npm_name QString [required]
    * @param[in]  oai_api_v1_plugins__npm_name__settings_put_request OAI_api_v1_plugins__npmName__settings_put_request [optional]
    */
    virtual void apiV1PluginsNpmNameSettingsPut(const QString &npm_name, const ::OpenAPI::OptionalParam<OAI_api_v1_plugins__npmName__settings_put_request> &oai_api_v1_plugins__npm_name__settings_put_request = ::OpenAPI::OptionalParam<OAI_api_v1_plugins__npmName__settings_put_request>());

    /**
    * @param[in]  search QString [optional]
    * @param[in]  plugin_type qint32 [optional]
    * @param[in]  current_peer_tube_engine QString [optional]
    * @param[in]  start qint32 [optional]
    * @param[in]  count qint32 [optional]
    * @param[in]  sort QString [optional]
    */
    virtual void getAvailablePlugins(const ::OpenAPI::OptionalParam<QString> &search = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &plugin_type = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &current_peer_tube_engine = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &start = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &count = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &sort = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  npm_name QString [required]
    */
    virtual void getPlugin(const QString &npm_name);

    /**
    * @param[in]  plugin_type qint32 [optional]
    * @param[in]  uninstalled bool [optional]
    * @param[in]  start qint32 [optional]
    * @param[in]  count qint32 [optional]
    * @param[in]  sort QString [optional]
    */
    virtual void getPlugins(const ::OpenAPI::OptionalParam<qint32> &plugin_type = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<bool> &uninstalled = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<qint32> &start = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &count = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &sort = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_uninstall_plugin_request OAIUninstallPlugin_request [optional]
    */
    virtual void uninstallPlugin(const ::OpenAPI::OptionalParam<OAIUninstallPlugin_request> &oai_uninstall_plugin_request = ::OpenAPI::OptionalParam<OAIUninstallPlugin_request>());

    /**
    * @param[in]  oai_add_plugin_request OAIAddPlugin_request [optional]
    */
    virtual void updatePlugin(const ::OpenAPI::OptionalParam<OAIAddPlugin_request> &oai_add_plugin_request = ::OpenAPI::OptionalParam<OAIAddPlugin_request>());


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

    void addPluginCallback(OAIHttpRequestWorker *worker);
    void apiV1PluginsNpmNamePublicSettingsGetCallback(OAIHttpRequestWorker *worker);
    void apiV1PluginsNpmNameRegisteredSettingsGetCallback(OAIHttpRequestWorker *worker);
    void apiV1PluginsNpmNameSettingsPutCallback(OAIHttpRequestWorker *worker);
    void getAvailablePluginsCallback(OAIHttpRequestWorker *worker);
    void getPluginCallback(OAIHttpRequestWorker *worker);
    void getPluginsCallback(OAIHttpRequestWorker *worker);
    void uninstallPluginCallback(OAIHttpRequestWorker *worker);
    void updatePluginCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void addPluginSignal();
    void apiV1PluginsNpmNamePublicSettingsGetSignal(QMap<QString, QJsonValue> summary);
    void apiV1PluginsNpmNameRegisteredSettingsGetSignal(QMap<QString, QJsonValue> summary);
    void apiV1PluginsNpmNameSettingsPutSignal();
    void getAvailablePluginsSignal(OAIPluginResponse summary);
    void getPluginSignal(OAIPlugin summary);
    void getPluginsSignal(OAIPluginResponse summary);
    void uninstallPluginSignal();
    void updatePluginSignal();


    void addPluginSignalFull(OAIHttpRequestWorker *worker);
    void apiV1PluginsNpmNamePublicSettingsGetSignalFull(OAIHttpRequestWorker *worker, QMap<QString, QJsonValue> summary);
    void apiV1PluginsNpmNameRegisteredSettingsGetSignalFull(OAIHttpRequestWorker *worker, QMap<QString, QJsonValue> summary);
    void apiV1PluginsNpmNameSettingsPutSignalFull(OAIHttpRequestWorker *worker);
    void getAvailablePluginsSignalFull(OAIHttpRequestWorker *worker, OAIPluginResponse summary);
    void getPluginSignalFull(OAIHttpRequestWorker *worker, OAIPlugin summary);
    void getPluginsSignalFull(OAIHttpRequestWorker *worker, OAIPluginResponse summary);
    void uninstallPluginSignalFull(OAIHttpRequestWorker *worker);
    void updatePluginSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use addPluginSignalError() instead")
    void addPluginSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void addPluginSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1PluginsNpmNamePublicSettingsGetSignalError() instead")
    void apiV1PluginsNpmNamePublicSettingsGetSignalE(QMap<QString, QJsonValue> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1PluginsNpmNamePublicSettingsGetSignalError(QMap<QString, QJsonValue> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1PluginsNpmNameRegisteredSettingsGetSignalError() instead")
    void apiV1PluginsNpmNameRegisteredSettingsGetSignalE(QMap<QString, QJsonValue> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1PluginsNpmNameRegisteredSettingsGetSignalError(QMap<QString, QJsonValue> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1PluginsNpmNameSettingsPutSignalError() instead")
    void apiV1PluginsNpmNameSettingsPutSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1PluginsNpmNameSettingsPutSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getAvailablePluginsSignalError() instead")
    void getAvailablePluginsSignalE(OAIPluginResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getAvailablePluginsSignalError(OAIPluginResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getPluginSignalError() instead")
    void getPluginSignalE(OAIPlugin summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getPluginSignalError(OAIPlugin summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getPluginsSignalError() instead")
    void getPluginsSignalE(OAIPluginResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getPluginsSignalError(OAIPluginResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use uninstallPluginSignalError() instead")
    void uninstallPluginSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void uninstallPluginSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updatePluginSignalError() instead")
    void updatePluginSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void updatePluginSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use addPluginSignalErrorFull() instead")
    void addPluginSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void addPluginSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1PluginsNpmNamePublicSettingsGetSignalErrorFull() instead")
    void apiV1PluginsNpmNamePublicSettingsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1PluginsNpmNamePublicSettingsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1PluginsNpmNameRegisteredSettingsGetSignalErrorFull() instead")
    void apiV1PluginsNpmNameRegisteredSettingsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1PluginsNpmNameRegisteredSettingsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1PluginsNpmNameSettingsPutSignalErrorFull() instead")
    void apiV1PluginsNpmNameSettingsPutSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1PluginsNpmNameSettingsPutSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getAvailablePluginsSignalErrorFull() instead")
    void getAvailablePluginsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getAvailablePluginsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getPluginSignalErrorFull() instead")
    void getPluginSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getPluginSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getPluginsSignalErrorFull() instead")
    void getPluginsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getPluginsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use uninstallPluginSignalErrorFull() instead")
    void uninstallPluginSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void uninstallPluginSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updatePluginSignalErrorFull() instead")
    void updatePluginSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updatePluginSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
