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

#ifndef OAI_OAIProductsApi_H
#define OAI_OAIProductsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAICount.h"
#include "OAINotFound.h"
#include "OAIProduct.h"
#include "OAIProductEdit.h"
#include "OAIStatusInvalid.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIProductsApi : public QObject {
    Q_OBJECT

public:
    OAIProductsApi(const int timeOut = 0);
    ~OAIProductsApi();

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
    * @param[in]  locale QString [optional]
    */
    virtual void productsAfterIdJsonGet(const QString &login, const QString &authtoken, const qint32 &id, const ::OpenAPI::OptionalParam<QString> &locale = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  login QString [required]
    * @param[in]  authtoken QString [required]
    * @param[in]  category_id qint32 [required]
    * @param[in]  locale QString [optional]
    */
    virtual void productsCategoryCategoryIdCountJsonGet(const QString &login, const QString &authtoken, const qint32 &category_id, const ::OpenAPI::OptionalParam<QString> &locale = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  login QString [required]
    * @param[in]  authtoken QString [required]
    * @param[in]  category_id qint32 [required]
    * @param[in]  locale QString [optional]
    */
    virtual void productsCategoryCategoryIdJsonGet(const QString &login, const QString &authtoken, const qint32 &category_id, const ::OpenAPI::OptionalParam<QString> &locale = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  login QString [required]
    * @param[in]  authtoken QString [required]
    */
    virtual void productsCountJsonGet(const QString &login, const QString &authtoken);

    /**
    * @param[in]  login QString [required]
    * @param[in]  authtoken QString [required]
    * @param[in]  id qint32 [required]
    */
    virtual void productsIdJsonDelete(const QString &login, const QString &authtoken, const qint32 &id);

    /**
    * @param[in]  login QString [required]
    * @param[in]  authtoken QString [required]
    * @param[in]  id qint32 [required]
    * @param[in]  locale QString [optional]
    */
    virtual void productsIdJsonGet(const QString &login, const QString &authtoken, const qint32 &id, const ::OpenAPI::OptionalParam<QString> &locale = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  login QString [required]
    * @param[in]  authtoken QString [required]
    * @param[in]  id qint32 [required]
    * @param[in]  oai_product_edit OAIProductEdit [required]
    * @param[in]  locale QString [optional]
    */
    virtual void productsIdJsonPut(const QString &login, const QString &authtoken, const qint32 &id, const OAIProductEdit &oai_product_edit, const ::OpenAPI::OptionalParam<QString> &locale = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  login QString [required]
    * @param[in]  authtoken QString [required]
    * @param[in]  limit qint32 [optional]
    * @param[in]  page qint32 [optional]
    * @param[in]  locale QString [optional]
    */
    virtual void productsJsonGet(const QString &login, const QString &authtoken, const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &locale = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  login QString [required]
    * @param[in]  authtoken QString [required]
    * @param[in]  oai_product_edit OAIProductEdit [required]
    * @param[in]  locale QString [optional]
    */
    virtual void productsJsonPost(const QString &login, const QString &authtoken, const OAIProductEdit &oai_product_edit, const ::OpenAPI::OptionalParam<QString> &locale = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  login QString [required]
    * @param[in]  authtoken QString [required]
    * @param[in]  query QString [required]
    * @param[in]  locale QString [optional]
    * @param[in]  fields QString [optional]
    */
    virtual void productsSearchJsonGet(const QString &login, const QString &authtoken, const QString &query, const ::OpenAPI::OptionalParam<QString> &locale = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &fields = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  login QString [required]
    * @param[in]  authtoken QString [required]
    * @param[in]  status QString [required]
    * @param[in]  locale QString [optional]
    */
    virtual void productsStatusStatusCountJsonGet(const QString &login, const QString &authtoken, const QString &status, const ::OpenAPI::OptionalParam<QString> &locale = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  login QString [required]
    * @param[in]  authtoken QString [required]
    * @param[in]  status QString [required]
    * @param[in]  locale QString [optional]
    */
    virtual void productsStatusStatusJsonGet(const QString &login, const QString &authtoken, const QString &status, const ::OpenAPI::OptionalParam<QString> &locale = ::OpenAPI::OptionalParam<QString>());


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

    void productsAfterIdJsonGetCallback(OAIHttpRequestWorker *worker);
    void productsCategoryCategoryIdCountJsonGetCallback(OAIHttpRequestWorker *worker);
    void productsCategoryCategoryIdJsonGetCallback(OAIHttpRequestWorker *worker);
    void productsCountJsonGetCallback(OAIHttpRequestWorker *worker);
    void productsIdJsonDeleteCallback(OAIHttpRequestWorker *worker);
    void productsIdJsonGetCallback(OAIHttpRequestWorker *worker);
    void productsIdJsonPutCallback(OAIHttpRequestWorker *worker);
    void productsJsonGetCallback(OAIHttpRequestWorker *worker);
    void productsJsonPostCallback(OAIHttpRequestWorker *worker);
    void productsSearchJsonGetCallback(OAIHttpRequestWorker *worker);
    void productsStatusStatusCountJsonGetCallback(OAIHttpRequestWorker *worker);
    void productsStatusStatusJsonGetCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void productsAfterIdJsonGetSignal(QList<OAIProduct> summary);
    void productsCategoryCategoryIdCountJsonGetSignal(OAICount summary);
    void productsCategoryCategoryIdJsonGetSignal(QList<OAIProduct> summary);
    void productsCountJsonGetSignal(OAICount summary);
    void productsIdJsonDeleteSignal(QString summary);
    void productsIdJsonGetSignal(OAIProduct summary);
    void productsIdJsonPutSignal(OAIProduct summary);
    void productsJsonGetSignal(QList<OAIProduct> summary);
    void productsJsonPostSignal(OAIProduct summary);
    void productsSearchJsonGetSignal(QList<OAIProduct> summary);
    void productsStatusStatusCountJsonGetSignal(OAICount summary);
    void productsStatusStatusJsonGetSignal(QList<OAIProduct> summary);


    void productsAfterIdJsonGetSignalFull(OAIHttpRequestWorker *worker, QList<OAIProduct> summary);
    void productsCategoryCategoryIdCountJsonGetSignalFull(OAIHttpRequestWorker *worker, OAICount summary);
    void productsCategoryCategoryIdJsonGetSignalFull(OAIHttpRequestWorker *worker, QList<OAIProduct> summary);
    void productsCountJsonGetSignalFull(OAIHttpRequestWorker *worker, OAICount summary);
    void productsIdJsonDeleteSignalFull(OAIHttpRequestWorker *worker, QString summary);
    void productsIdJsonGetSignalFull(OAIHttpRequestWorker *worker, OAIProduct summary);
    void productsIdJsonPutSignalFull(OAIHttpRequestWorker *worker, OAIProduct summary);
    void productsJsonGetSignalFull(OAIHttpRequestWorker *worker, QList<OAIProduct> summary);
    void productsJsonPostSignalFull(OAIHttpRequestWorker *worker, OAIProduct summary);
    void productsSearchJsonGetSignalFull(OAIHttpRequestWorker *worker, QList<OAIProduct> summary);
    void productsStatusStatusCountJsonGetSignalFull(OAIHttpRequestWorker *worker, OAICount summary);
    void productsStatusStatusJsonGetSignalFull(OAIHttpRequestWorker *worker, QList<OAIProduct> summary);

    Q_DECL_DEPRECATED_X("Use productsAfterIdJsonGetSignalError() instead")
    void productsAfterIdJsonGetSignalE(QList<OAIProduct> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void productsAfterIdJsonGetSignalError(QList<OAIProduct> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use productsCategoryCategoryIdCountJsonGetSignalError() instead")
    void productsCategoryCategoryIdCountJsonGetSignalE(OAICount summary, QNetworkReply::NetworkError error_type, QString error_str);
    void productsCategoryCategoryIdCountJsonGetSignalError(OAICount summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use productsCategoryCategoryIdJsonGetSignalError() instead")
    void productsCategoryCategoryIdJsonGetSignalE(QList<OAIProduct> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void productsCategoryCategoryIdJsonGetSignalError(QList<OAIProduct> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use productsCountJsonGetSignalError() instead")
    void productsCountJsonGetSignalE(OAICount summary, QNetworkReply::NetworkError error_type, QString error_str);
    void productsCountJsonGetSignalError(OAICount summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use productsIdJsonDeleteSignalError() instead")
    void productsIdJsonDeleteSignalE(QString summary, QNetworkReply::NetworkError error_type, QString error_str);
    void productsIdJsonDeleteSignalError(QString summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use productsIdJsonGetSignalError() instead")
    void productsIdJsonGetSignalE(OAIProduct summary, QNetworkReply::NetworkError error_type, QString error_str);
    void productsIdJsonGetSignalError(OAIProduct summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use productsIdJsonPutSignalError() instead")
    void productsIdJsonPutSignalE(OAIProduct summary, QNetworkReply::NetworkError error_type, QString error_str);
    void productsIdJsonPutSignalError(OAIProduct summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use productsJsonGetSignalError() instead")
    void productsJsonGetSignalE(QList<OAIProduct> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void productsJsonGetSignalError(QList<OAIProduct> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use productsJsonPostSignalError() instead")
    void productsJsonPostSignalE(OAIProduct summary, QNetworkReply::NetworkError error_type, QString error_str);
    void productsJsonPostSignalError(OAIProduct summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use productsSearchJsonGetSignalError() instead")
    void productsSearchJsonGetSignalE(QList<OAIProduct> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void productsSearchJsonGetSignalError(QList<OAIProduct> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use productsStatusStatusCountJsonGetSignalError() instead")
    void productsStatusStatusCountJsonGetSignalE(OAICount summary, QNetworkReply::NetworkError error_type, QString error_str);
    void productsStatusStatusCountJsonGetSignalError(OAICount summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use productsStatusStatusJsonGetSignalError() instead")
    void productsStatusStatusJsonGetSignalE(QList<OAIProduct> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void productsStatusStatusJsonGetSignalError(QList<OAIProduct> summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use productsAfterIdJsonGetSignalErrorFull() instead")
    void productsAfterIdJsonGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void productsAfterIdJsonGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use productsCategoryCategoryIdCountJsonGetSignalErrorFull() instead")
    void productsCategoryCategoryIdCountJsonGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void productsCategoryCategoryIdCountJsonGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use productsCategoryCategoryIdJsonGetSignalErrorFull() instead")
    void productsCategoryCategoryIdJsonGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void productsCategoryCategoryIdJsonGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use productsCountJsonGetSignalErrorFull() instead")
    void productsCountJsonGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void productsCountJsonGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use productsIdJsonDeleteSignalErrorFull() instead")
    void productsIdJsonDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void productsIdJsonDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use productsIdJsonGetSignalErrorFull() instead")
    void productsIdJsonGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void productsIdJsonGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use productsIdJsonPutSignalErrorFull() instead")
    void productsIdJsonPutSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void productsIdJsonPutSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use productsJsonGetSignalErrorFull() instead")
    void productsJsonGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void productsJsonGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use productsJsonPostSignalErrorFull() instead")
    void productsJsonPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void productsJsonPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use productsSearchJsonGetSignalErrorFull() instead")
    void productsSearchJsonGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void productsSearchJsonGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use productsStatusStatusCountJsonGetSignalErrorFull() instead")
    void productsStatusStatusCountJsonGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void productsStatusStatusCountJsonGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use productsStatusStatusJsonGetSignalErrorFull() instead")
    void productsStatusStatusJsonGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void productsStatusStatusJsonGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
