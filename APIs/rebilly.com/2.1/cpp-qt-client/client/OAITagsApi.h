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

#ifndef OAI_OAITagsApi_H
#define OAI_OAITagsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIError.h"
#include "OAIInvalidError.h"
#include "OAIPostTagCustomerCollection_request.h"
#include "OAITag.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAITagsApi : public QObject {
    Q_OBJECT

public:
    OAITagsApi(const int timeOut = 0);
    ~OAITagsApi();

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
    * @param[in]  tag QString [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void deleteTag(const QString &tag, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  tag QString [required]
    * @param[in]  customer_id QString [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void deleteTagCustomer(const QString &tag, const QString &customer_id, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  tag QString [required]
    * @param[in]  oai_post_tag_customer_collection_request OAIPostTagCustomerCollection_request [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void deleteTagCustomerCollection(const QString &tag, const OAIPostTagCustomerCollection_request &oai_post_tag_customer_collection_request, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  tag QString [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void getTag(const QString &tag, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  organization_id QString [optional]
    * @param[in]  limit qint32 [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  filter QString [optional]
    * @param[in]  q QString [optional]
    * @param[in]  sort QList<QString> [optional]
    */
    virtual void getTagCollection(const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &filter = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &q = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QList<QString>> &sort = ::OpenAPI::OptionalParam<QList<QString>>());

    /**
    * @param[in]  tag QString [required]
    * @param[in]  oai_tag OAITag [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void patchTag(const QString &tag, const OAITag &oai_tag, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_tag OAITag [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void postTag(const OAITag &oai_tag, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  tag QString [required]
    * @param[in]  customer_id QString [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void postTagCustomer(const QString &tag, const QString &customer_id, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  tag QString [required]
    * @param[in]  oai_post_tag_customer_collection_request OAIPostTagCustomerCollection_request [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void postTagCustomerCollection(const QString &tag, const OAIPostTagCustomerCollection_request &oai_post_tag_customer_collection_request, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());


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

    void deleteTagCallback(OAIHttpRequestWorker *worker);
    void deleteTagCustomerCallback(OAIHttpRequestWorker *worker);
    void deleteTagCustomerCollectionCallback(OAIHttpRequestWorker *worker);
    void getTagCallback(OAIHttpRequestWorker *worker);
    void getTagCollectionCallback(OAIHttpRequestWorker *worker);
    void patchTagCallback(OAIHttpRequestWorker *worker);
    void postTagCallback(OAIHttpRequestWorker *worker);
    void postTagCustomerCallback(OAIHttpRequestWorker *worker);
    void postTagCustomerCollectionCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void deleteTagSignal();
    void deleteTagCustomerSignal();
    void deleteTagCustomerCollectionSignal();
    void getTagSignal(OAITag summary);
    void getTagCollectionSignal(QList<OAITag> summary);
    void patchTagSignal(OAITag summary);
    void postTagSignal(OAITag summary);
    void postTagCustomerSignal();
    void postTagCustomerCollectionSignal();


    void deleteTagSignalFull(OAIHttpRequestWorker *worker);
    void deleteTagCustomerSignalFull(OAIHttpRequestWorker *worker);
    void deleteTagCustomerCollectionSignalFull(OAIHttpRequestWorker *worker);
    void getTagSignalFull(OAIHttpRequestWorker *worker, OAITag summary);
    void getTagCollectionSignalFull(OAIHttpRequestWorker *worker, QList<OAITag> summary);
    void patchTagSignalFull(OAIHttpRequestWorker *worker, OAITag summary);
    void postTagSignalFull(OAIHttpRequestWorker *worker, OAITag summary);
    void postTagCustomerSignalFull(OAIHttpRequestWorker *worker);
    void postTagCustomerCollectionSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use deleteTagSignalError() instead")
    void deleteTagSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void deleteTagSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteTagCustomerSignalError() instead")
    void deleteTagCustomerSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void deleteTagCustomerSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteTagCustomerCollectionSignalError() instead")
    void deleteTagCustomerCollectionSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void deleteTagCustomerCollectionSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getTagSignalError() instead")
    void getTagSignalE(OAITag summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getTagSignalError(OAITag summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getTagCollectionSignalError() instead")
    void getTagCollectionSignalE(QList<OAITag> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getTagCollectionSignalError(QList<OAITag> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patchTagSignalError() instead")
    void patchTagSignalE(OAITag summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patchTagSignalError(OAITag summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postTagSignalError() instead")
    void postTagSignalE(OAITag summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postTagSignalError(OAITag summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postTagCustomerSignalError() instead")
    void postTagCustomerSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void postTagCustomerSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postTagCustomerCollectionSignalError() instead")
    void postTagCustomerCollectionSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void postTagCustomerCollectionSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use deleteTagSignalErrorFull() instead")
    void deleteTagSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteTagSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteTagCustomerSignalErrorFull() instead")
    void deleteTagCustomerSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteTagCustomerSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteTagCustomerCollectionSignalErrorFull() instead")
    void deleteTagCustomerCollectionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteTagCustomerCollectionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getTagSignalErrorFull() instead")
    void getTagSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getTagSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getTagCollectionSignalErrorFull() instead")
    void getTagCollectionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getTagCollectionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patchTagSignalErrorFull() instead")
    void patchTagSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patchTagSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postTagSignalErrorFull() instead")
    void postTagSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postTagSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postTagCustomerSignalErrorFull() instead")
    void postTagCustomerSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postTagCustomerSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postTagCustomerCollectionSignalErrorFull() instead")
    void postTagCustomerCollectionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postTagCustomerCollectionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
