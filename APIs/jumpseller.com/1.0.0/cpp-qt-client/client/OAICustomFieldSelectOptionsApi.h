/**
 * Jumpseller API
 * # Endpoint Structure  All URLs are in the format:   ```text https://api.jumpseller.com/v1/path.json?login=XXXXXX&authtoken=storetoken   ```  The path is prefixed by the API version and the URL takes as parameters the login (your store specific API login) and your authentication token. <br/><br/> ***  # Version  The current version of the API is **v1**.   If we change the API in backward-incompatible ways, we'll increase the version number and maintain stable support for the old urls. <br/><br/> ***  # Authentication  The API uses a token-based authentication with a combination of a login key and an auth token. **Both parameters can be found on the left sidebar of the Account section, accessed from the main menu of your Admin Panel**. The auth token of the user can be reset on the same page.  ![Store Login](/images/support/api/apilogin.png)  The auth token is a **32 characters** string.  If you are developing a Jumpseller App, the authentication should be done using [OAuth-2](/support/oauth-2). Please read the article [Build an App](/support/apps) for more information. <br/><br/> ***  # Curl Examples  To request all the products at your store, you would append the products index path to the base url to create an URL with the format:    ```text https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX ```  In curl, you can invoque that URL with:    ```text curl -X GET \"https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX\" ```  To create a product, you will include the JSON data and specify the MIME Type:    ```text curl -X POST -d '{ \"product\" : {\"name\": \"My new Product!\", \"price\": 100} }' \"https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\" ```  and to update the product identified with 123:    ```text curl -X PUT -d '{ \"product\" : {\"name\": \"My updated Product!\", \"price\": 99} }' \"https://api.jumpseller.com/v1/products/123.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\" ```  or delete it:    ```text curl -X DELETE \"https://api.jumpseller.com/v1/products/123.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\" ``` <br/><br/> ***  # PHP Examples  Create a new Product (POST method)  ```php $url = 'https://api.jumpseller.com/v1/products.json?login=XXXXX&authtoken=XXXXX; $ch = curl_init($url); curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));  curl_setopt($ch, CURLOPT_CUSTOMREQUEST, \"POST\"); //post method curl_setopt($ch, CURLOPT_POSTFIELDS, '{ \"product\" : {\"name\": \"My updated Product!\", \"price\": 99} }');  $result = curl_exec($ch); print_r($result); curl_close($ch); ``` <br/><br/> ***  # Plain JSON only. No XML.  * We only support JSON for data serialization. * Our node format has no root element.   * We use snake_case to describe attribute keys (like \"created_at\").   * All empty value are replaced with **null** strings. * All API URLs end in .json to indicate that they accept and return JSON. * POST and PUT methods require you to explicitly state the MIME type of your request's body content as **\"application/json\"**. <br/><br/> ***  # Rate Limit You can perform a maximum of:  + 240 (two hundred forty) requests per minute and + 8 (eight) requests per second   If you exceed this limit, you'll get a 403 Forbidden (Rate Limit Exceeded) response for subsequent requests.    The rate limits apply by IP address and by store. This means that multiple requests on different stores are not counted towards the same rate limit.  This limits are necessary to ensure resources are correctly used. Your application should be aware of this limits and retry any unsuccessful request, check the following Ruby stub:  ```ruby tries = 0; max_tries = 3; begin   HTTParty.send(method, uri) # perform an API call.   sleep 0.5   tries += 1 rescue   unless tries >= max_tries     sleep 1.0 # wait the necessary time before retrying the call again.     retry   end end ```  Finally, you can review the Response Headers of each request:  ```text Jumpseller-PerMinuteRateLimit-Limit: 60   Jumpseller-PerMinuteRateLimit-Remaining: 59 # requests available on the per-second interval   Jumpseller-PerSecondRateLimit-Limit: 2   Jumpseller-PerSecondRateLimit-Remaining: 1 # requests available on the per-second interval ```   to better model your application requests intervals.  In the event of getting your IP banned, the Response Header `Jumpseller-BannedByRateLimit-Reset` informs you the time when will your ban be reseted. <br/><br/> ***  # Pagination  By default we will return 50 objects (products, orders, etc) per page. There is a maximum of 100, using a query string `&limit=100`. If the result set gets paginated it is your responsibility to check the next page for more objects -- you do this by using query strings `&page=2`, `&page=3` and so on.  ```text https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX&page=3&limit=100 ``` <br/><br/> ***  # More * [Jumpseller API wrapper](https://gitlab.com/jumpseller-api/ruby) provides a public Ruby abstraction over our API; * [Apps Page](/apps) showcases external integrations with Jumpseller done by technical experts; * [Imgbb API](https://api.imgbb.com/) provides an easy way to upload and temporaly host for images and files. <br/><br/> *** <br/><br/> 
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAICustomFieldSelectOptionsApi_H
#define OAI_OAICustomFieldSelectOptionsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAICustomFieldSelectOption.h"
#include "OAICustomFieldSelectOptionEdit.h"
#include "OAINotFound.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAICustomFieldSelectOptionsApi : public QObject {
    Q_OBJECT

public:
    OAICustomFieldSelectOptionsApi(const int timeOut = 0);
    ~OAICustomFieldSelectOptionsApi();

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
    * @param[in]  login QString [required]
    * @param[in]  authtoken QString [required]
    * @param[in]  id qint32 [required]
    * @param[in]  custom_field_select_option_id qint32 [required]
    */
    virtual void customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonGet(const QString &login, const QString &authtoken, const qint32 &id, const qint32 &custom_field_select_option_id);

    /**
    * @param[in]  login QString [required]
    * @param[in]  authtoken QString [required]
    * @param[in]  id qint32 [required]
    * @param[in]  custom_field_select_option_id qint32 [required]
    * @param[in]  oai_custom_field_select_option_edit OAICustomFieldSelectOptionEdit [required]
    */
    virtual void customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonPut(const QString &login, const QString &authtoken, const qint32 &id, const qint32 &custom_field_select_option_id, const OAICustomFieldSelectOptionEdit &oai_custom_field_select_option_edit);

    /**
    * @param[in]  login QString [required]
    * @param[in]  authtoken QString [required]
    * @param[in]  id qint32 [required]
    */
    virtual void customFieldsIdSelectOptionsJsonGet(const QString &login, const QString &authtoken, const qint32 &id);

    /**
    * @param[in]  login QString [required]
    * @param[in]  authtoken QString [required]
    * @param[in]  id QString [required]
    * @param[in]  oai_custom_field_select_option_edit OAICustomFieldSelectOptionEdit [required]
    */
    virtual void customFieldsIdSelectOptionsJsonPost(const QString &login, const QString &authtoken, const QString &id, const OAICustomFieldSelectOptionEdit &oai_custom_field_select_option_edit);


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

    void customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonGetCallback(OAIHttpRequestWorker *worker);
    void customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonPutCallback(OAIHttpRequestWorker *worker);
    void customFieldsIdSelectOptionsJsonGetCallback(OAIHttpRequestWorker *worker);
    void customFieldsIdSelectOptionsJsonPostCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonGetSignal(OAICustomFieldSelectOption summary);
    void customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonPutSignal(OAICustomFieldSelectOption summary);
    void customFieldsIdSelectOptionsJsonGetSignal(QList<OAICustomFieldSelectOption> summary);
    void customFieldsIdSelectOptionsJsonPostSignal(OAICustomFieldSelectOption summary);


    void customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonGetSignalFull(OAIHttpRequestWorker *worker, OAICustomFieldSelectOption summary);
    void customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonPutSignalFull(OAIHttpRequestWorker *worker, OAICustomFieldSelectOption summary);
    void customFieldsIdSelectOptionsJsonGetSignalFull(OAIHttpRequestWorker *worker, QList<OAICustomFieldSelectOption> summary);
    void customFieldsIdSelectOptionsJsonPostSignalFull(OAIHttpRequestWorker *worker, OAICustomFieldSelectOption summary);

    Q_DECL_DEPRECATED_X("Use customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonGetSignalError() instead")
    void customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonGetSignalE(OAICustomFieldSelectOption summary, QNetworkReply::NetworkError error_type, QString error_str);
    void customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonGetSignalError(OAICustomFieldSelectOption summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonPutSignalError() instead")
    void customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonPutSignalE(OAICustomFieldSelectOption summary, QNetworkReply::NetworkError error_type, QString error_str);
    void customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonPutSignalError(OAICustomFieldSelectOption summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use customFieldsIdSelectOptionsJsonGetSignalError() instead")
    void customFieldsIdSelectOptionsJsonGetSignalE(QList<OAICustomFieldSelectOption> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void customFieldsIdSelectOptionsJsonGetSignalError(QList<OAICustomFieldSelectOption> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use customFieldsIdSelectOptionsJsonPostSignalError() instead")
    void customFieldsIdSelectOptionsJsonPostSignalE(OAICustomFieldSelectOption summary, QNetworkReply::NetworkError error_type, QString error_str);
    void customFieldsIdSelectOptionsJsonPostSignalError(OAICustomFieldSelectOption summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonGetSignalErrorFull() instead")
    void customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonPutSignalErrorFull() instead")
    void customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonPutSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonPutSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use customFieldsIdSelectOptionsJsonGetSignalErrorFull() instead")
    void customFieldsIdSelectOptionsJsonGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void customFieldsIdSelectOptionsJsonGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use customFieldsIdSelectOptionsJsonPostSignalErrorFull() instead")
    void customFieldsIdSelectOptionsJsonPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void customFieldsIdSelectOptionsJsonPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
