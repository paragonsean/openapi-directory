/**
 * Rudder API
 * Download OpenAPI specification: [openapi.yml](openapi.yml)  # Introduction  Rudder exposes a REST API, enabling the user to interact with Rudder without using the webapp, for example in scripts or cronjobs.  ## Versioning  Each time the API is extended with new features (new functions, new parameters, new responses, ...), it will be assigned a new version number. This will allow you to keep your existing scripts (based on previous behavior). Versions will always be integers (no 2.1 or 3.3, just 2, 3, 4, ...) or `latest`.  You can change the version of the API used by setting it either within the url or in a header:  * the URL: each URL is prefixed by its version id, like `/api/version/function`.  ```bash # Version 10 curl -X GET -H \"X-API-Token: yourToken\" https://rudder.example.com/rudder/api/10/rules # Latest curl -X GET -H \"X-API-Token: yourToken\" https://rudder.example.com/rudder/api/latest/rules # Wrong (not an integer) => 404 not found curl -X GET -H \"X-API-Token: yourToken\" https://rudder.example.com/rudder/api/3.14/rules ```  * the HTTP headers. You can add the **X-API-Version** header to your request. The value needs to be an integer or `latest`.  ```bash # Version 10 curl -X GET -H \"X-API-Token: yourToken\" -H \"X-API-Version: 10\" https://rudder.example.com/rudder/api/rules # Wrong => Error response indicating which versions are available curl -X GET -H \"X-API-Token: yourToken\" -H \"X-API-Version: 3.14\" https://rudder.example.com/rudder/api/rules ```  In the future, we may declare some versions as deprecated, in order to remove them in a later version of Rudder, but we will never remove any versions without warning, or without a safe period of time to allow migration from previous versions.   <h4>Existing versions</h4> <table>   <thead>     <tr>       <th style=\"width: 20%\">Version</th>       <th style=\"width: 20%\">Rudder versions it appeared in</th>       <th style=\"width: 70%\">Description</th>     </tr>   </thead>   <tbody>     <tr>       <td class=\"code\">1</td>       <td class=\"code\">Never released (for internal use only)</td>       <td>Experimental version</td>     </tr>     <tr>       <td class=\"code\">2 to 10 (deprecated)</td>       <td class=\"code\">4.3 and before</td>       <td>These versions provided the core set of API features for rules, directives, nodes global parameters, change requests and compliance, rudder settings and system API</td>     </tr>     <tr>       <td class=\"code\">11</td>       <td class=\"code\">5.0</td>       <td>New system API (replacing old localhost v1 api): status, maintenance operations and server behavior</td>     </tr>     <tr>       <td class=\"code\">12</td>       <td class=\"code\">6.0 and 6.1</td>       <td>Node key management</td>     </tr>     <tr>       <td class=\"code\">13</td>       <td class=\"code\">6.2</td>       <td><ul>         <li>Node status endpoint</li>         <li>System health check</li>         <li>System maintenance job to purge software [that endpoint was back-ported in 6.1]</li>       </ul></td>     </tr>     <tr>       <td class=\"code\">14</td>       <td class=\"code\">7.0</td>       <td><ul>         <li>Secret management</li>         <li>Directive tree</li>         <li>Improve techniques management</li>         <li>Demote a relay</li>       </ul></td>     </tr>     <tr>       <td class=\"code\">15</td>       <td class=\"code\">7.1</td>       <td><ul>         <li>Package updates in nodes</li>       </ul></td>     </tr>     <tr>       <td class=\"code\">16</td>       <td class=\"code\">7.2</td>       <td><ul>         <li>Create node API included from plugin</li>         <li>Configuration archive import/export</li>       </ul></td>     </tr>   </tbody> </table>   ## Response format  All responses from the API are in the JSON format.  ```json {   \"action\": \"The name of the called function\",   \"id\": \"The ID of the element you want, if relevant\",   \"result\": \"The result of your action: success or error\",   \"data\": \"Only present if this is a success and depends on the function, it's usually a JSON object\",   \"errorDetails\": \"Only present if this is an error, it contains the error message\" } ```   * __Success__ responses are sent with the 200 HTTP (Success) code  * __Error__ responses are sent with a HTTP error code (mostly 5xx...)   ## HTTP method  Rudder's REST API is based on the usage of [HTTP methods](http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html). We use them to indicate what action will be done by the request. Currently, we use four of them:   * **GET**: search or retrieve information (get rule details, get a group, ...)  * **PUT**: add new objects (create a directive, clone a Rule, ...)  * **DELETE**: remove objects (delete a node, delete a parameter, ...)  * **POST**: update existing objects (update a directive, reload a group, ...)   ## Parameters  ### General parameters  Some parameters are available for almost all API functions. They will be described in this section. They must be part of the query and can't be submitted in a JSON form.  #### Available for all requests  <table>   <thead>     <tr>       <th style=\"width: 30%\">Field</th>       <th style=\"width: 10%\">Type</th>       <th style=\"width: 70%\">Description</th>     </tr>   </thead>   <tbody>     <tr>       <td class=\"code\">prettify</td>       <td><b>boolean</b><br><i>optional</i></td>       <td>         Determine if the answer should be prettified (human friendly) or not. We recommend using this for debugging purposes, but not for general script usage as this does add some unnecessary load on the server side.         <p class=\"default-value\">Default value: <code>false</code></p>       </td>     </tr>   </tbody> </table>   #### Available for modification requests (PUT/POST/DELETE)  <table>   <thead>     <tr>       <th style=\"width: 25%\">Field</th>       <th style=\"width: 12%\">Type</th>       <th style=\"width: 70%\">Description</th>     </tr>   </thead>   <tbody>     <tr>       <td class=\"code\">reason</td>       <td><b>string</b><br><i>optional</i> or <i>required</i></td>       <td>         Set a message to explain the change. If you set the reason messages to be mandatory in the web interface, failing to supply this value will lead to an error.         <p class=\"default-value\">Default value: <code>\"\"</code></p>       </td>     </tr>     <tr>       <td class=\"code\">changeRequestName</td>       <td><b>string</b><br><i>optional</i></td>       <td>         Set the change request name, is used only if workflows are enabled. The default value depends on the function called         <p class=\"default-value\">Default value: <code>A default string for each function</code></p>       </td>     </tr>     <tr>       <td class=\"code\">changeRequestDescription</td>       <td><b>string</b><br><i>optional</i></td>       <td>         Set the change request description, is used only if workflows are enabled.         <p class=\"default-value\">Default value: <code>\"\"</code></p>       </td>     </tr>   </tbody> </table>   ### Passing parameters  Parameters to the API can be sent:  * As part of the URL for resource identification  * As data for POST/PUT requests    * Directly in JSON format    * As request arguments  #### As part of the URL for resource identification  Parameters in URLs are used to indicate which resource you want to interact with. The function will not work if this resource is missing.  ```bash # Get the Rule of ID \"id\" curl -H \"X-API-Token: yourToken\" https://rudder.example.com/rudder/api/latest/rules/id ```    CAUTION: To avoid surprising behavior, do not put a '/' at the end of an URL: it would be interpreted as '/[empty string parameter]' and redirected to '/index', likely not what you wanted to do.   #### Sending data for POST/PUT requests  ##### Directly in JSON format  JSON format is the preferred way to interact with Rudder API for creating or updating resources. You'll also have to set the *Content-Type* header to **application/json** (without it the JSON content would be ignored). In a `curl` `POST` request, that header can be provided with the `-H` parameter:  ```bash curl -X POST -H \"Content-Type: application/json\" ... ```  The supplied file must contain a valid JSON: strings need quotes, booleans and integers don't, etc.  The (human readable) format is:  ```json {   \"key1\": \"value1\",   \"key2\": false,   \"key3\": 42 } ```   Here is an example with inlined data:  ```bash # Update the Rule 'id' with a new name, disabled, and setting it one directive curl -X POST -H \"X-API-Token: yourToken\" -H  \"Content-Type: application/json\" https://rudder.example.com/rudder/api/rules/latest/{id}   -d '{ \"displayName\": \"new name\", \"enabled\": false, \"directives\": \"directiveId\"}' ```  You can also pass a supply the JSON in a file:  ```bash # Update the Rule 'id' with a new name, disabled, and setting it one directive curl -X POST -H \"X-API-Token: yourToken\" -H \"Content-Type: application/json\" https://rudder.example.com/rudder/api/rules/latest/{id} -d @jsonParam ```  Note that the general parameters view in the previous chapter cannot be passed in a JSON, and you will need to pass them a URL parameters if you want them to be taken into account (you can't mix JSON and request parameters):  ```bash # Update the Rule 'id' with a new name, disabled, and setting it one directive with reason message \"Reason used\" curl -X POST -H \"X-API-Token: yourToken\" -H \"Content-Type: application/json\" \"https://rudder.example.com/rudder/api/rules/latest/{id}?reason=Reason used\" -d @jsonParam -d \"reason=Reason ignored\" ```  ##### Request parameters  In some cases, when you have little, simple data to update, JSON can feel bloated. In such cases, you can use request parameters. You will need to pass one parameter for each data you want to change.  Parameters follow the following schema:  ``` key=value ```  You can pass parameters by two means:  * As query parameters: At the end of your url, put a **?** then your first parameter and then a **&** before next parameters. In that case, parameters need to be https://en.wikipedia.org/wiki/Percent-encoding[URL encoded]  ```bash # Update the Rule 'id' with a new name, disabled, and setting it one directive curl -X POST -H \"X-API-Token: yourToken\"  https://rudder.example.com/rudder/api/rules/latest/{id}?\"displayName=my new name\"&\"enabled=false\"&\"directives=aDirectiveId\" ```  * As request data: You can pass those parameters in the request data, they won't figure in the URL, making it lighter to read, You can pass a file that contains data.  ```bash # Update the Rule 'id' with a new name, disabled, and setting it one directive (in file directive-info.json) curl -X POST -H \"X-API-Token: yourToken\" https://rudder.example.com/rudder/api/rules/latest/{id} -d \"displayName=my new name\" -d \"enabled=false\" -d @directive-info.json ``` 
 *
 * The version of the OpenAPI document: 17
 * Contact: dev@rudder.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAICampaignsApi_H
#define OAI_OAICampaignsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIAllCampaigns_200_response.h"
#include "OAICampaign_details.h"
#include "OAIDeleteCampaignEvent_200_response.h"
#include "OAIDeleteCampaign_200_response.h"
#include "OAIGetAllCampaignEvents_200_response.h"
#include "OAIGetCampaign_200_response.h"
#include "OAIGetEventsCampaign_200_response.h"
#include "OAISaveCampaignEvent_200_response.h"
#include "OAISaveCampaign_200_response.h"
#include "OAIScheduleCampaign_200_response.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAICampaignsApi : public QObject {
    Q_OBJECT

public:
    OAICampaignsApi(const int timeOut = 0);
    ~OAICampaignsApi();

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
    * @param[in]  campaign_type QString [optional]
    * @param[in]  status QString [optional]
    */
    virtual void allCampaigns(const ::OpenAPI::OptionalParam<QString> &campaign_type = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &status = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    */
    virtual void deleteCampaign(const QString &id);

    /**
    * @param[in]  id QString [required]
    */
    virtual void deleteCampaignEvent(const QString &id);

    /**
    * @param[in]  campaign_type QString [optional]
    * @param[in]  state QString [optional]
    * @param[in]  campaign_id QString [optional]
    * @param[in]  limit qint32 [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  before QDate [optional]
    * @param[in]  after QDate [optional]
    * @param[in]  order QString [optional]
    * @param[in]  asc QString [optional]
    */
    virtual void getAllCampaignEvents(const ::OpenAPI::OptionalParam<QString> &campaign_type = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &state = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &campaign_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QDate> &before = ::OpenAPI::OptionalParam<QDate>(), const ::OpenAPI::OptionalParam<QDate> &after = ::OpenAPI::OptionalParam<QDate>(), const ::OpenAPI::OptionalParam<QString> &order = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &asc = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    */
    virtual void getCampaign(const QString &id);

    /**
    * @param[in]  id QString [required]
    */
    virtual void getCampaignEvent(const QString &id);

    /**
    * @param[in]  id QString [required]
    * @param[in]  campaign_type QString [optional]
    * @param[in]  state QString [optional]
    * @param[in]  limit qint32 [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  before QDate [optional]
    * @param[in]  after QDate [optional]
    * @param[in]  order QString [optional]
    * @param[in]  asc QString [optional]
    */
    virtual void getEventsCampaign(const QString &id, const ::OpenAPI::OptionalParam<QString> &campaign_type = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &state = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QDate> &before = ::OpenAPI::OptionalParam<QDate>(), const ::OpenAPI::OptionalParam<QDate> &after = ::OpenAPI::OptionalParam<QDate>(), const ::OpenAPI::OptionalParam<QString> &order = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &asc = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_campaign_details OAICampaign_details [required]
    */
    virtual void saveCampaign(const OAICampaign_details &oai_campaign_details);

    /**
    * @param[in]  id QString [required]
    */
    virtual void saveCampaignEvent(const QString &id);

    /**
    * @param[in]  id QString [required]
    */
    virtual void scheduleCampaign(const QString &id);


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

    void allCampaignsCallback(OAIHttpRequestWorker *worker);
    void deleteCampaignCallback(OAIHttpRequestWorker *worker);
    void deleteCampaignEventCallback(OAIHttpRequestWorker *worker);
    void getAllCampaignEventsCallback(OAIHttpRequestWorker *worker);
    void getCampaignCallback(OAIHttpRequestWorker *worker);
    void getCampaignEventCallback(OAIHttpRequestWorker *worker);
    void getEventsCampaignCallback(OAIHttpRequestWorker *worker);
    void saveCampaignCallback(OAIHttpRequestWorker *worker);
    void saveCampaignEventCallback(OAIHttpRequestWorker *worker);
    void scheduleCampaignCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void allCampaignsSignal(OAIAllCampaigns_200_response summary);
    void deleteCampaignSignal(OAIDeleteCampaign_200_response summary);
    void deleteCampaignEventSignal(OAIDeleteCampaignEvent_200_response summary);
    void getAllCampaignEventsSignal(OAIGetAllCampaignEvents_200_response summary);
    void getCampaignSignal(OAIGetCampaign_200_response summary);
    void getCampaignEventSignal(OAIGetAllCampaignEvents_200_response summary);
    void getEventsCampaignSignal(OAIGetEventsCampaign_200_response summary);
    void saveCampaignSignal(OAISaveCampaign_200_response summary);
    void saveCampaignEventSignal(OAISaveCampaignEvent_200_response summary);
    void scheduleCampaignSignal(OAIScheduleCampaign_200_response summary);


    void allCampaignsSignalFull(OAIHttpRequestWorker *worker, OAIAllCampaigns_200_response summary);
    void deleteCampaignSignalFull(OAIHttpRequestWorker *worker, OAIDeleteCampaign_200_response summary);
    void deleteCampaignEventSignalFull(OAIHttpRequestWorker *worker, OAIDeleteCampaignEvent_200_response summary);
    void getAllCampaignEventsSignalFull(OAIHttpRequestWorker *worker, OAIGetAllCampaignEvents_200_response summary);
    void getCampaignSignalFull(OAIHttpRequestWorker *worker, OAIGetCampaign_200_response summary);
    void getCampaignEventSignalFull(OAIHttpRequestWorker *worker, OAIGetAllCampaignEvents_200_response summary);
    void getEventsCampaignSignalFull(OAIHttpRequestWorker *worker, OAIGetEventsCampaign_200_response summary);
    void saveCampaignSignalFull(OAIHttpRequestWorker *worker, OAISaveCampaign_200_response summary);
    void saveCampaignEventSignalFull(OAIHttpRequestWorker *worker, OAISaveCampaignEvent_200_response summary);
    void scheduleCampaignSignalFull(OAIHttpRequestWorker *worker, OAIScheduleCampaign_200_response summary);

    Q_DECL_DEPRECATED_X("Use allCampaignsSignalError() instead")
    void allCampaignsSignalE(OAIAllCampaigns_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void allCampaignsSignalError(OAIAllCampaigns_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteCampaignSignalError() instead")
    void deleteCampaignSignalE(OAIDeleteCampaign_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteCampaignSignalError(OAIDeleteCampaign_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteCampaignEventSignalError() instead")
    void deleteCampaignEventSignalE(OAIDeleteCampaignEvent_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteCampaignEventSignalError(OAIDeleteCampaignEvent_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getAllCampaignEventsSignalError() instead")
    void getAllCampaignEventsSignalE(OAIGetAllCampaignEvents_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getAllCampaignEventsSignalError(OAIGetAllCampaignEvents_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getCampaignSignalError() instead")
    void getCampaignSignalE(OAIGetCampaign_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getCampaignSignalError(OAIGetCampaign_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getCampaignEventSignalError() instead")
    void getCampaignEventSignalE(OAIGetAllCampaignEvents_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getCampaignEventSignalError(OAIGetAllCampaignEvents_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getEventsCampaignSignalError() instead")
    void getEventsCampaignSignalE(OAIGetEventsCampaign_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getEventsCampaignSignalError(OAIGetEventsCampaign_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use saveCampaignSignalError() instead")
    void saveCampaignSignalE(OAISaveCampaign_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void saveCampaignSignalError(OAISaveCampaign_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use saveCampaignEventSignalError() instead")
    void saveCampaignEventSignalE(OAISaveCampaignEvent_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void saveCampaignEventSignalError(OAISaveCampaignEvent_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use scheduleCampaignSignalError() instead")
    void scheduleCampaignSignalE(OAIScheduleCampaign_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void scheduleCampaignSignalError(OAIScheduleCampaign_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use allCampaignsSignalErrorFull() instead")
    void allCampaignsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void allCampaignsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteCampaignSignalErrorFull() instead")
    void deleteCampaignSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteCampaignSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteCampaignEventSignalErrorFull() instead")
    void deleteCampaignEventSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteCampaignEventSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getAllCampaignEventsSignalErrorFull() instead")
    void getAllCampaignEventsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getAllCampaignEventsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getCampaignSignalErrorFull() instead")
    void getCampaignSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getCampaignSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getCampaignEventSignalErrorFull() instead")
    void getCampaignEventSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getCampaignEventSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getEventsCampaignSignalErrorFull() instead")
    void getEventsCampaignSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getEventsCampaignSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use saveCampaignSignalErrorFull() instead")
    void saveCampaignSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void saveCampaignSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use saveCampaignEventSignalErrorFull() instead")
    void saveCampaignEventSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void saveCampaignEventSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use scheduleCampaignSignalErrorFull() instead")
    void scheduleCampaignSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void scheduleCampaignSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
