/**
 * Fitbit Plus API
 * # Overview The Fitbit Plus API is a RESTful API. The requests and responses are formated according to the [JSON API](http://jsonapi.org/format/1.0/) specification.  In addition to this documentation, we also provide an [OpenAPI](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md) \"yaml\" file describing the API: [Fitbit Plus API Specification](swagger.yaml).  # Authentication Authentication for the Fitbit Plus API is based on the [OAuth 2.0 Authorization Framework](https://tools.ietf.org/html/rfc6749). Fitbit Plus currently supports grant types of **client_credentials** and **refresh_token**.  See [POST /oauth/token](#operation/createToken) for details on the request and response formats. <!-- ReDoc-Inject: <security-definitions> -->  ## Building Integrations We will provide customers with unique client credentials for each application/integration they build, allowing us to enforce appropriate access controls and monitor API usage. The client credentials will be scoped to the organization, and allow full access to all patients and related data within that organization.  These credentials are appropriate for creating an integration that does one of the following:  - background reporting/analysis  - synchronizing data with another system (such as an EMR)  The API credentials and oauth flows we currently support are **not** well suited for creating a user-facing application that allows a user (patient, coach, or admin) to login and have access to data which is appropriate to that specific user. It is possible to build such an application, but it is not possible to use Fitbit Plus as a federated identity provider. You would need to have a separate means of verifying a user's identity. We do not currently support the required password-based oauth flow to make this possible.  # Paging The Fitbit Plus API supports two different pagination strategies for GET collection endpoints.  #### Skip-based paging  Skip-based paging uses the query parameters `page[size]` and `page[number]` to specify the max number of resources returned and the page number. We default to skip-based paging if there are no page parameters. The response will include a `links` object containing links to the first, last, prev, and next pages of data.  If the contents of the collection change while you are iterating through the collection, you will see duplicate or missing documents. For example, if you are iterating through the `calender_event` resource via `GET /pub/calendar_event?sort=start_at&page[size]=50&page[number]=1`, and a new `calendar_event` is created that has a `start_at` value before the first `calendar_event`, when you fetch the next page at `GET /pub/calendar_event?sort=start_at&page[size]=50&page[number]=2`, the first entry in the second response will be a duplicate of the last entry in the first response.  #### Cursor-based paging Cursor-based paging uses the query parameters `page[limit]` and `page[after]` to specify the max number of entries returned and identify where to begin the next page. Add `page[limit]` to the parameters to use cursor-based paging. The response will include a `links` object containing a link to the next page of data, if the next page exists.  Cursor-based paging is not subject to duplication if new resources are added to the collection. For example, if you are iterating through the `calender_event` resource via `GET /pub/calendar_event?sort=start_at&page[limit]=50`, and a new `calendar_event` is created that has a `start_at` value before the first `calendar_event`, you will not see a duplicate entry when you fetch the next page at `GET /pub/calendar_event?sort=start_at&page[limit]=50&page[after]=<cursor>`.  We encourage the use of cursor-based paging for performance reasons.  In either form of paging, you can determine whether any resources were missed by comparing the number of fetched resources against `meta.count`. Set `page[size]` or `page[limit]` to 0 to get only the count.  It is not valid to mix the two strategies. 
 *
 * The version of the OpenAPI document: v7.78.1
 * Contact: apiteam@twinehealth.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIOrganizationApi_H
#define OAI_OAIOrganizationApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIFetchErrorResponse.h"
#include "OAIFetchOrganizationResponse.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIOrganizationApi : public QObject {
    Q_OBJECT

public:
    OAIOrganizationApi(const int timeOut = 0);
    ~OAIOrganizationApi();

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
    * @param[in]  id QString [required]
    */
    virtual void fetchOrganization(const QString &id);


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

    void fetchOrganizationCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void fetchOrganizationSignal(OAIFetchOrganizationResponse summary);


    void fetchOrganizationSignalFull(OAIHttpRequestWorker *worker, OAIFetchOrganizationResponse summary);

    Q_DECL_DEPRECATED_X("Use fetchOrganizationSignalError() instead")
    void fetchOrganizationSignalE(OAIFetchOrganizationResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void fetchOrganizationSignalError(OAIFetchOrganizationResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use fetchOrganizationSignalErrorFull() instead")
    void fetchOrganizationSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void fetchOrganizationSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
