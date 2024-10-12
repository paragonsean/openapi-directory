/**
 * Braze Endpoints
 * # Braze API Overview  Braze provides a high performance REST API to allow you to track users, send messages, export data, and more.  A REST API is a way to programmatically transfer information over the web using a predefined schema. Braze has created many different endpoints with specific requirements that will perform various actions and/or return various data. API access is done using HTTPS web requests to your company's REST API endpoint (this will correspond to your Dashboard URL as shown in the table below).  Customers using Braze's EU database should use `https://rest.fra-01.braze.eu/`. For more information on REST API endpoints for customers using Braze's EU database see our [EU/US Implementation Differences documentation](https://www.braze.com/docs/developer_guide/eu01_us3_sdk_implementation_differences/overview/).  ## Braze Instances  Instance    | Dashboard URL   | REST Endpoint ----------- |---------------- | -------------------- US-01 | `https://dashboard.braze.com` or<br> `https://dashboard-01.braze.com` | `https://rest.iad-01.braze.com` US-02 | `https://dashboard-02.braze.com` | `https://rest.iad-02.braze.com` US-03 | `https://dashboard-03.braze.com` | `https://rest.iad-03.braze.com` US-04 | `https://dashboard-04.braze.com` | `https://rest.iad-04.braze.com` US-06 | `https://dashboard-06.braze.com` | `https://rest.iad-06.braze.com` EU-01 | `https://dashboard.braze.eu` or<br> `https://dashboard-01.braze.eu` | `https://rest.fra-01.braze.eu`   # Using Braze's Postman Collection   If you have a Postman account (MacOS, Windows, and Linux versions can be downloaded from their website located [here](https://www.getpostman.com)), you can go to our Postman documentation and click the orange `Run in Postman` button in the top, right corner. This will allow you to [create an environment](#setting-up-your-postman-environment), as well as edit the available `POST` and `GET` requests to suit your own needs.  ## Setting Up Your Postman Environment  The Braze Postman Collection uses a templating variable, `{{instance_url}}`, to substitute the REST API URL of your Braze instance into the pre-built requests. Rather than having to manually edit all requests in the Collection, you can set up this variable in your Postman environment. To do so, please follow the steps below:  1. Click on the gear icon in the top right corner of the Postman app.  2. Select \"Manage Environments\" to open a modal window which displays your active environments. 3. In the bottom right corner of the modal window, click \"Add\" to create a new environment. 4. Give this environment a name (e.g. \"Braze API Requests\") and add keys for `instance_url` and `api_key` with values corresponding to [your Braze instance](https://www.braze.com/docs/api/basics/#endpoints) and [Braze REST API Key](https://www.braze.com/docs/api/basics/#app-group-rest-api-keys), as pictured below.   As of April, 2020 Braze has changed how we read App Group API keys. Instead of passing them in the request body or through url parameters, we now read the App Group Rest`api_key` through the HTTP Authorization header. API keys not passed through the HTTP Authorization Header will coninue to work until they have been sunset.   ## Using the Pre-Built Requests from the Collection  Once you have configured your environment. You can use any of the pre-built requests in the collection as a template for building new API requests. To start using one of the pre-built requests, simply click on it within the 'Collections' menu on the left side of Postman. This will open the request as a new tab in the main window of the Postman app.  In general, there are two types of requests that Braze's API endpoints accept - `GET` and `POST`. Depending on which `HTTP` method the endpoint uses, you'll need to edit the pre-built request differently.  ### Edit a POST Request  When editing a `POST` request, you'll need to open the request and navigate to the `Body` section in the request editor. For readability, select the `raw` radio button to format the `JSON` request body.  ### Edit a GET Request  When editing a `GET` request, you will need to edit the parameters passed in the request URL. To edit these easily, select the `Params` button next to the URL bar and edit the key-value pairs in the fields that will appear below the URL bar.  ## Send Your Request  Once your API request is ready to send, click on the 'Send' button next to the URL bar. The request will be sent and the response data will be populated in a section underneath the request editor. From here, you can view the raw data returned from Braze's API, see the HTTP response code, see how long the request took to process, and view header information.
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIEmailListsAddressesApi_H
#define OAI_OAIEmailListsAddressesApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIEmailListsAddressesApi : public QObject {
    Q_OBJECT

public:
    OAIEmailListsAddressesApi(const int timeOut = 0);
    ~OAIEmailListsAddressesApi();

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
    * @param[in]  start_date QString [optional]
    * @param[in]  end_date QString [optional]
    * @param[in]  limit QString [optional]
    * @param[in]  offset QString [optional]
    * @param[in]  email QString [optional]
    */
    virtual void queryHardBouncedEmails(const ::OpenAPI::OptionalParam<QString> &start_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &end_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &limit = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &offset = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &email = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  start_date QString [optional]
    * @param[in]  end_date QString [optional]
    * @param[in]  limit QString [optional]
    * @param[in]  offset QString [optional]
    * @param[in]  sort_direction QString [optional]
    * @param[in]  email QString [optional]
    */
    virtual void queryListOfUnsubscribedEmailAddresses(const ::OpenAPI::OptionalParam<QString> &start_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &end_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &limit = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &offset = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &sort_direction = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &email = ::OpenAPI::OptionalParam<QString>());


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

    void queryHardBouncedEmailsCallback(OAIHttpRequestWorker *worker);
    void queryListOfUnsubscribedEmailAddressesCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void queryHardBouncedEmailsSignal();
    void queryListOfUnsubscribedEmailAddressesSignal();


    void queryHardBouncedEmailsSignalFull(OAIHttpRequestWorker *worker);
    void queryListOfUnsubscribedEmailAddressesSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use queryHardBouncedEmailsSignalError() instead")
    void queryHardBouncedEmailsSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void queryHardBouncedEmailsSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use queryListOfUnsubscribedEmailAddressesSignalError() instead")
    void queryListOfUnsubscribedEmailAddressesSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void queryListOfUnsubscribedEmailAddressesSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use queryHardBouncedEmailsSignalErrorFull() instead")
    void queryHardBouncedEmailsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void queryHardBouncedEmailsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use queryListOfUnsubscribedEmailAddressesSignalErrorFull() instead")
    void queryListOfUnsubscribedEmailAddressesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void queryListOfUnsubscribedEmailAddressesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
