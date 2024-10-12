/**
 * Rebilly REST API
 * # Introduction The Rebilly API is built on HTTP.  Our API is RESTful.  It has predictable resource URLs.  It returns HTTP response codes to indicate errors.  It also accepts and returns JSON in the HTTP body.  You can use your favorite HTTP/REST library for your programming language to use Rebilly's API, or you can use one of our SDKs (currently available in [PHP](https://github.com/Rebilly/rebilly-php) and [Javascript](https://github.com/Rebilly/rebilly-js-sdk)).  We have other APIs that are also available.  Every action from our [app](https://app.rebilly.com) is supported by an API which is documented and available for use so that you may automate any workflows necessary.  This document contains the most commonly integrated resources.  # Authentication  When you sign up for an account, you are given your first secret API key. You can generate additional API keys, and delete API keys (as you may need to rotate your keys in the future). You authenticate to the Rebilly API by providing your secret key in the request header.  Rebilly offers three forms of authentication:  secret key, publishable key, JSON Web Tokens, and public signature key. - [Secret API key](#section/Authentication/SecretApiKey): used for requests made   from the server side. Never share these keys. Keep them guarded and secure. - [Publishable API key](#section/Authentication/PublishableApiKey): used for    requests from the client side. For now can only be used to create    a [Payment Token](#operation/PostToken) and    a [File token](#operation/PostFile). - [JWT](#section/Authentication/JWT): short lifetime tokens that can be assigned a specific expiration time.  Never share your secret keys. Keep them guarded and secure.  &lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt;  # Errors Rebilly follow's the error response format proposed in [RFC 7807](https://tools.ietf.org/html/rfc7807) also known as Problem Details for HTTP APIs.  As with our normal API responses, your client must be prepared to gracefully handle additional members of the response.  ## Forbidden &lt;RedocResponse pointer={\"#/components/responses/Forbidden\"} /&gt;  ## Conflict &lt;RedocResponse pointer={\"#/components/responses/Conflict\"} /&gt;  ## NotFound &lt;RedocResponse pointer={\"#/components/responses/NotFound\"} /&gt;  ## Unauthorized &lt;RedocResponse pointer={\"#/components/responses/Unauthorized\"} /&gt;  ## ValidationError &lt;RedocResponse pointer={\"#/components/responses/ValidationError\"} /&gt;  # SDKs  Rebilly offers a Javascript SDK and a PHP SDK to help interact with the API.  However, no SDK is required to use the API.  Rebilly also offers [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/),  a client-side iFrame-based solution to help create payment tokens while minimizing PCI DSS compliance burdens and maximizing the customizability. [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/) is interacting with the [payment tokens creation operation](#operation/PostToken).  ## Javascript SDK  Installation and usage instructions can be found [here](https://docs.rebilly.com/docs/developer-docs/sdks). SDK code examples are included in these docs.  ## PHP SDK For all PHP SDK examples provided in these docs you will need to configure the `$client`. You may do it like this:  ```php $client = new Rebilly\\Client([     'apiKey' =&gt; 'YourApiKeyHere',     'baseUrl' =&gt; 'https://api.rebilly.com', ]); ```  # Using filter with collections Rebilly provides collections filtering. You can use `?filter` param on collections to define which records should be shown in the response.  Here is filter format description:  - Fields and values in filter are separated with `:`: `?filter=firstName:John`.  - Sub-fields are separated with `.`: `?filter=billingAddress.country:US`.  - Multiple filters are separated with `;`: `?filter=firstName:John;lastName:Doe`. They will be joined with `AND` logic. In this example: `firstName:John` AND `lastName:Doe`.  - You can use multiple values using `,` as values separator: `?filter=firstName:John,Bob`. Multiple values specified for a field will be joined with `OR` logic. In this example: `firstName:John` OR `firstName:Bob`.  - To negate the filter use `!`: `?filter=firstName:!John`. Note that you can negate multiple values like this: `?filter=firstName:!John,!Bob`. This filter rule will exclude all Johns and Bobs from the response.  - You can use range filters like this: `?filter=amount:1..10`.  - You can use gte (greater than or equals) filter like this: `?filter=amount:1..`, or lte (less than or equals) than filter like this: `?filter=amount:..10`. This also works for datetime-based fields.  - You can create some [predefined values lists](https://user-api-docs.rebilly.com/#tag/Lists) and use them in filter: `?filter=firstName:@yourListName`. You can also exclude list values: `?filter=firstName:!@yourListName`.  - Datetime-based fields accept values formatted using RFC 3339 like this: `?filter=createdTime:2021-02-14T13:30:00Z`.   # Expand to include embedded objects Rebilly provides the ability to pre-load additional  objects with a request.   You can use `?expand` param on most requests to expand and include embedded objects within the `_embedded` property of the response.  The `_embedded` property contains an array of  objects keyed by the expand parameter value(s).  You may expand multiple objects by passing them as comma-separated to the expand value like so:  ``` ?expand=recentInvoice,customer ```  And in the response, you would see:  ``` \"_embedded\": [     \"recentInvoice\": {...},     \"customer\": {...} ] ``` Expand may be utilitized not only on `GET` requests but also on `PATCH`, `POST`, `PUT` requests too.   # Getting started guide  Rebilly's API has over 300 operations.  That's more than you'll  need to implement your use cases.  If you have a use  case you would like to implement, please consult us for feedback on the best API operations for the task.  Our getting started guide will demonstrate a basic order form use case.  It will allow us to highlight core resources in Rebilly that will be helpful for many other use cases too.  Within 25 minutes, you'll have sent API requests (via our console) to create a subscription order. 
 *
 * The version of the OpenAPI document: 2.1
 * Contact: integrations@rebilly.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAICouponsApi_H
#define OAI_OAICouponsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAICoupon.h"
#include "OAICouponExpiration.h"
#include "OAICouponRedemption.h"
#include "OAIError.h"
#include "OAIInvalidError.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAICouponsApi : public QObject {
    Q_OBJECT

public:
    OAICouponsApi(const int timeOut = 0);
    ~OAICouponsApi();

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
    * @param[in]  organization_id QString [optional]
    */
    virtual void getCoupon(const QString &id, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  organization_id QString [optional]
    * @param[in]  limit qint32 [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  filter QString [optional]
    * @param[in]  q QString [optional]
    * @param[in]  sort QList<QString> [optional]
    */
    virtual void getCouponCollection(const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &filter = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &q = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QList<QString>> &sort = ::OpenAPI::OptionalParam<QList<QString>>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void getCouponRedemption(const QString &id, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  organization_id QString [optional]
    * @param[in]  limit qint32 [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  filter QString [optional]
    * @param[in]  q QString [optional]
    * @param[in]  sort QList<QString> [optional]
    */
    virtual void getCouponRedemptionCollection(const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &filter = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &q = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QList<QString>> &sort = ::OpenAPI::OptionalParam<QList<QString>>());

    /**
    * @param[in]  oai_coupon OAICoupon [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void postCoupon(const OAICoupon &oai_coupon, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  organization_id QString [optional]
    * @param[in]  oai_coupon_expiration OAICouponExpiration [optional]
    */
    virtual void postCouponExpiration(const QString &id, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<OAICouponExpiration> &oai_coupon_expiration = ::OpenAPI::OptionalParam<OAICouponExpiration>());

    /**
    * @param[in]  oai_coupon_redemption OAICouponRedemption [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void postCouponRedemption(const OAICouponRedemption &oai_coupon_redemption, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void postCouponRedemptionCancellation(const QString &id, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  oai_coupon OAICoupon [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void putCoupon(const QString &id, const OAICoupon &oai_coupon, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());


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

    void getCouponCallback(OAIHttpRequestWorker *worker);
    void getCouponCollectionCallback(OAIHttpRequestWorker *worker);
    void getCouponRedemptionCallback(OAIHttpRequestWorker *worker);
    void getCouponRedemptionCollectionCallback(OAIHttpRequestWorker *worker);
    void postCouponCallback(OAIHttpRequestWorker *worker);
    void postCouponExpirationCallback(OAIHttpRequestWorker *worker);
    void postCouponRedemptionCallback(OAIHttpRequestWorker *worker);
    void postCouponRedemptionCancellationCallback(OAIHttpRequestWorker *worker);
    void putCouponCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void getCouponSignal(OAICoupon summary);
    void getCouponCollectionSignal(QList<OAICoupon> summary);
    void getCouponRedemptionSignal(OAICouponRedemption summary);
    void getCouponRedemptionCollectionSignal(QList<OAICouponRedemption> summary);
    void postCouponSignal(OAICoupon summary);
    void postCouponExpirationSignal(OAICoupon summary);
    void postCouponRedemptionSignal(OAICouponRedemption summary);
    void postCouponRedemptionCancellationSignal();
    void putCouponSignal(OAICoupon summary);


    void getCouponSignalFull(OAIHttpRequestWorker *worker, OAICoupon summary);
    void getCouponCollectionSignalFull(OAIHttpRequestWorker *worker, QList<OAICoupon> summary);
    void getCouponRedemptionSignalFull(OAIHttpRequestWorker *worker, OAICouponRedemption summary);
    void getCouponRedemptionCollectionSignalFull(OAIHttpRequestWorker *worker, QList<OAICouponRedemption> summary);
    void postCouponSignalFull(OAIHttpRequestWorker *worker, OAICoupon summary);
    void postCouponExpirationSignalFull(OAIHttpRequestWorker *worker, OAICoupon summary);
    void postCouponRedemptionSignalFull(OAIHttpRequestWorker *worker, OAICouponRedemption summary);
    void postCouponRedemptionCancellationSignalFull(OAIHttpRequestWorker *worker);
    void putCouponSignalFull(OAIHttpRequestWorker *worker, OAICoupon summary);

    Q_DECL_DEPRECATED_X("Use getCouponSignalError() instead")
    void getCouponSignalE(OAICoupon summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getCouponSignalError(OAICoupon summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getCouponCollectionSignalError() instead")
    void getCouponCollectionSignalE(QList<OAICoupon> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getCouponCollectionSignalError(QList<OAICoupon> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getCouponRedemptionSignalError() instead")
    void getCouponRedemptionSignalE(OAICouponRedemption summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getCouponRedemptionSignalError(OAICouponRedemption summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getCouponRedemptionCollectionSignalError() instead")
    void getCouponRedemptionCollectionSignalE(QList<OAICouponRedemption> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getCouponRedemptionCollectionSignalError(QList<OAICouponRedemption> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postCouponSignalError() instead")
    void postCouponSignalE(OAICoupon summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postCouponSignalError(OAICoupon summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postCouponExpirationSignalError() instead")
    void postCouponExpirationSignalE(OAICoupon summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postCouponExpirationSignalError(OAICoupon summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postCouponRedemptionSignalError() instead")
    void postCouponRedemptionSignalE(OAICouponRedemption summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postCouponRedemptionSignalError(OAICouponRedemption summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postCouponRedemptionCancellationSignalError() instead")
    void postCouponRedemptionCancellationSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void postCouponRedemptionCancellationSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use putCouponSignalError() instead")
    void putCouponSignalE(OAICoupon summary, QNetworkReply::NetworkError error_type, QString error_str);
    void putCouponSignalError(OAICoupon summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use getCouponSignalErrorFull() instead")
    void getCouponSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getCouponSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getCouponCollectionSignalErrorFull() instead")
    void getCouponCollectionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getCouponCollectionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getCouponRedemptionSignalErrorFull() instead")
    void getCouponRedemptionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getCouponRedemptionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getCouponRedemptionCollectionSignalErrorFull() instead")
    void getCouponRedemptionCollectionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getCouponRedemptionCollectionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postCouponSignalErrorFull() instead")
    void postCouponSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postCouponSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postCouponExpirationSignalErrorFull() instead")
    void postCouponExpirationSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postCouponExpirationSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postCouponRedemptionSignalErrorFull() instead")
    void postCouponRedemptionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postCouponRedemptionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postCouponRedemptionCancellationSignalErrorFull() instead")
    void postCouponRedemptionCancellationSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postCouponRedemptionCancellationSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use putCouponSignalErrorFull() instead")
    void putCouponSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void putCouponSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
