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

#ifndef OAI_OAIOrdersApi_H
#define OAI_OAIOrdersApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIError.h"
#include "OAIInvalidError.h"
#include "OAIInvoice.h"
#include "OAIInvoiceIssue.h"
#include "OAIOrderTimeline.h"
#include "OAISubscription.h"
#include "OAISubscriptionCancellation.h"
#include "OAISubscriptionChange.h"
#include "OAISubscriptionInvoice.h"
#include "OAISubscriptionReactivation.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIOrdersApi : public QObject {
    Q_OBJECT

public:
    OAIOrdersApi(const int timeOut = 0);
    ~OAIOrdersApi();

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
    virtual void deleteSubscriptionCancellation(const QString &id, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  message_id QString [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void deleteSubscriptionTimeline(const QString &id, const QString &message_id, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  organization_id QString [optional]
    * @param[in]  expand QString [optional]
    */
    virtual void getSubscription(const QString &id, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &expand = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void getSubscriptionCancellation(const QString &id, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  organization_id QString [optional]
    * @param[in]  limit qint32 [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  filter QString [optional]
    * @param[in]  sort QList<QString> [optional]
    */
    virtual void getSubscriptionCancellationCollection(const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &filter = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QList<QString>> &sort = ::OpenAPI::OptionalParam<QList<QString>>());

    /**
    * @param[in]  organization_id QString [optional]
    * @param[in]  filter QString [optional]
    * @param[in]  sort QList<QString> [optional]
    * @param[in]  limit qint32 [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  q QString [optional]
    * @param[in]  expand QString [optional]
    */
    virtual void getSubscriptionCollection(const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &filter = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QList<QString>> &sort = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &q = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &expand = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void getSubscriptionReactivation(const QString &id, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  organization_id QString [optional]
    * @param[in]  limit qint32 [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  filter QString [optional]
    * @param[in]  sort QList<QString> [optional]
    */
    virtual void getSubscriptionReactivationCollection(const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &filter = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QList<QString>> &sort = ::OpenAPI::OptionalParam<QList<QString>>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  message_id QString [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void getSubscriptionTimeline(const QString &id, const QString &message_id, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  organization_id QString [optional]
    * @param[in]  limit qint32 [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  filter QString [optional]
    * @param[in]  sort QList<QString> [optional]
    * @param[in]  q QString [optional]
    */
    virtual void getSubscriptionTimelineCollection(const QString &id, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &filter = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QList<QString>> &sort = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<QString> &q = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  organization_id QString [optional]
    * @param[in]  expand QString [optional]
    */
    virtual void getSubscriptionUpcomingInvoiceCollection(const QString &id, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &expand = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_subscription OAISubscription [required]
    * @param[in]  organization_id QString [optional]
    * @param[in]  expand QString [optional]
    */
    virtual void postSubscription(const OAISubscription &oai_subscription, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &expand = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_subscription_cancellation OAISubscriptionCancellation [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void postSubscriptionCancellation(const OAISubscriptionCancellation &oai_subscription_cancellation, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  oai_subscription_invoice OAISubscriptionInvoice [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void postSubscriptionInterimInvoice(const QString &id, const OAISubscriptionInvoice &oai_subscription_invoice, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  oai_subscription_change OAISubscriptionChange [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void postSubscriptionItemsChange(const QString &id, const OAISubscriptionChange &oai_subscription_change, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_subscription_reactivation OAISubscriptionReactivation [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void postSubscriptionReactivation(const OAISubscriptionReactivation &oai_subscription_reactivation, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  oai_order_timeline OAIOrderTimeline [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void postSubscriptionTimeline(const QString &id, const OAIOrderTimeline &oai_order_timeline, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  invoice_id QString [required]
    * @param[in]  oai_invoice_issue OAIInvoiceIssue [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void postUpcomingInvoiceIssuance(const QString &id, const QString &invoice_id, const OAIInvoiceIssue &oai_invoice_issue, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  oai_subscription OAISubscription [required]
    * @param[in]  organization_id QString [optional]
    * @param[in]  expand QString [optional]
    */
    virtual void putSubscription(const QString &id, const OAISubscription &oai_subscription, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &expand = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  oai_subscription_cancellation OAISubscriptionCancellation [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void putSubscriptionCancellation(const QString &id, const OAISubscriptionCancellation &oai_subscription_cancellation, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());


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

    void deleteSubscriptionCancellationCallback(OAIHttpRequestWorker *worker);
    void deleteSubscriptionTimelineCallback(OAIHttpRequestWorker *worker);
    void getSubscriptionCallback(OAIHttpRequestWorker *worker);
    void getSubscriptionCancellationCallback(OAIHttpRequestWorker *worker);
    void getSubscriptionCancellationCollectionCallback(OAIHttpRequestWorker *worker);
    void getSubscriptionCollectionCallback(OAIHttpRequestWorker *worker);
    void getSubscriptionReactivationCallback(OAIHttpRequestWorker *worker);
    void getSubscriptionReactivationCollectionCallback(OAIHttpRequestWorker *worker);
    void getSubscriptionTimelineCallback(OAIHttpRequestWorker *worker);
    void getSubscriptionTimelineCollectionCallback(OAIHttpRequestWorker *worker);
    void getSubscriptionUpcomingInvoiceCollectionCallback(OAIHttpRequestWorker *worker);
    void postSubscriptionCallback(OAIHttpRequestWorker *worker);
    void postSubscriptionCancellationCallback(OAIHttpRequestWorker *worker);
    void postSubscriptionInterimInvoiceCallback(OAIHttpRequestWorker *worker);
    void postSubscriptionItemsChangeCallback(OAIHttpRequestWorker *worker);
    void postSubscriptionReactivationCallback(OAIHttpRequestWorker *worker);
    void postSubscriptionTimelineCallback(OAIHttpRequestWorker *worker);
    void postUpcomingInvoiceIssuanceCallback(OAIHttpRequestWorker *worker);
    void putSubscriptionCallback(OAIHttpRequestWorker *worker);
    void putSubscriptionCancellationCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void deleteSubscriptionCancellationSignal();
    void deleteSubscriptionTimelineSignal();
    void getSubscriptionSignal(OAISubscription summary);
    void getSubscriptionCancellationSignal(OAISubscriptionCancellation summary);
    void getSubscriptionCancellationCollectionSignal(QList<OAISubscriptionCancellation> summary);
    void getSubscriptionCollectionSignal(QList<OAISubscription> summary);
    void getSubscriptionReactivationSignal(OAISubscriptionReactivation summary);
    void getSubscriptionReactivationCollectionSignal(QList<OAISubscriptionReactivation> summary);
    void getSubscriptionTimelineSignal(OAIOrderTimeline summary);
    void getSubscriptionTimelineCollectionSignal(QList<OAIOrderTimeline> summary);
    void getSubscriptionUpcomingInvoiceCollectionSignal(QList<OAIInvoice> summary);
    void postSubscriptionSignal(OAISubscription summary);
    void postSubscriptionCancellationSignal(OAISubscriptionCancellation summary);
    void postSubscriptionInterimInvoiceSignal(OAIInvoice summary);
    void postSubscriptionItemsChangeSignal(OAISubscription summary);
    void postSubscriptionReactivationSignal(OAISubscriptionReactivation summary);
    void postSubscriptionTimelineSignal(OAIOrderTimeline summary);
    void postUpcomingInvoiceIssuanceSignal(OAIInvoice summary);
    void putSubscriptionSignal(OAISubscription summary);
    void putSubscriptionCancellationSignal(OAISubscriptionCancellation summary);


    void deleteSubscriptionCancellationSignalFull(OAIHttpRequestWorker *worker);
    void deleteSubscriptionTimelineSignalFull(OAIHttpRequestWorker *worker);
    void getSubscriptionSignalFull(OAIHttpRequestWorker *worker, OAISubscription summary);
    void getSubscriptionCancellationSignalFull(OAIHttpRequestWorker *worker, OAISubscriptionCancellation summary);
    void getSubscriptionCancellationCollectionSignalFull(OAIHttpRequestWorker *worker, QList<OAISubscriptionCancellation> summary);
    void getSubscriptionCollectionSignalFull(OAIHttpRequestWorker *worker, QList<OAISubscription> summary);
    void getSubscriptionReactivationSignalFull(OAIHttpRequestWorker *worker, OAISubscriptionReactivation summary);
    void getSubscriptionReactivationCollectionSignalFull(OAIHttpRequestWorker *worker, QList<OAISubscriptionReactivation> summary);
    void getSubscriptionTimelineSignalFull(OAIHttpRequestWorker *worker, OAIOrderTimeline summary);
    void getSubscriptionTimelineCollectionSignalFull(OAIHttpRequestWorker *worker, QList<OAIOrderTimeline> summary);
    void getSubscriptionUpcomingInvoiceCollectionSignalFull(OAIHttpRequestWorker *worker, QList<OAIInvoice> summary);
    void postSubscriptionSignalFull(OAIHttpRequestWorker *worker, OAISubscription summary);
    void postSubscriptionCancellationSignalFull(OAIHttpRequestWorker *worker, OAISubscriptionCancellation summary);
    void postSubscriptionInterimInvoiceSignalFull(OAIHttpRequestWorker *worker, OAIInvoice summary);
    void postSubscriptionItemsChangeSignalFull(OAIHttpRequestWorker *worker, OAISubscription summary);
    void postSubscriptionReactivationSignalFull(OAIHttpRequestWorker *worker, OAISubscriptionReactivation summary);
    void postSubscriptionTimelineSignalFull(OAIHttpRequestWorker *worker, OAIOrderTimeline summary);
    void postUpcomingInvoiceIssuanceSignalFull(OAIHttpRequestWorker *worker, OAIInvoice summary);
    void putSubscriptionSignalFull(OAIHttpRequestWorker *worker, OAISubscription summary);
    void putSubscriptionCancellationSignalFull(OAIHttpRequestWorker *worker, OAISubscriptionCancellation summary);

    Q_DECL_DEPRECATED_X("Use deleteSubscriptionCancellationSignalError() instead")
    void deleteSubscriptionCancellationSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void deleteSubscriptionCancellationSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteSubscriptionTimelineSignalError() instead")
    void deleteSubscriptionTimelineSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void deleteSubscriptionTimelineSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getSubscriptionSignalError() instead")
    void getSubscriptionSignalE(OAISubscription summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getSubscriptionSignalError(OAISubscription summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getSubscriptionCancellationSignalError() instead")
    void getSubscriptionCancellationSignalE(OAISubscriptionCancellation summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getSubscriptionCancellationSignalError(OAISubscriptionCancellation summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getSubscriptionCancellationCollectionSignalError() instead")
    void getSubscriptionCancellationCollectionSignalE(QList<OAISubscriptionCancellation> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getSubscriptionCancellationCollectionSignalError(QList<OAISubscriptionCancellation> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getSubscriptionCollectionSignalError() instead")
    void getSubscriptionCollectionSignalE(QList<OAISubscription> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getSubscriptionCollectionSignalError(QList<OAISubscription> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getSubscriptionReactivationSignalError() instead")
    void getSubscriptionReactivationSignalE(OAISubscriptionReactivation summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getSubscriptionReactivationSignalError(OAISubscriptionReactivation summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getSubscriptionReactivationCollectionSignalError() instead")
    void getSubscriptionReactivationCollectionSignalE(QList<OAISubscriptionReactivation> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getSubscriptionReactivationCollectionSignalError(QList<OAISubscriptionReactivation> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getSubscriptionTimelineSignalError() instead")
    void getSubscriptionTimelineSignalE(OAIOrderTimeline summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getSubscriptionTimelineSignalError(OAIOrderTimeline summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getSubscriptionTimelineCollectionSignalError() instead")
    void getSubscriptionTimelineCollectionSignalE(QList<OAIOrderTimeline> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getSubscriptionTimelineCollectionSignalError(QList<OAIOrderTimeline> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getSubscriptionUpcomingInvoiceCollectionSignalError() instead")
    void getSubscriptionUpcomingInvoiceCollectionSignalE(QList<OAIInvoice> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getSubscriptionUpcomingInvoiceCollectionSignalError(QList<OAIInvoice> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postSubscriptionSignalError() instead")
    void postSubscriptionSignalE(OAISubscription summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postSubscriptionSignalError(OAISubscription summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postSubscriptionCancellationSignalError() instead")
    void postSubscriptionCancellationSignalE(OAISubscriptionCancellation summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postSubscriptionCancellationSignalError(OAISubscriptionCancellation summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postSubscriptionInterimInvoiceSignalError() instead")
    void postSubscriptionInterimInvoiceSignalE(OAIInvoice summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postSubscriptionInterimInvoiceSignalError(OAIInvoice summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postSubscriptionItemsChangeSignalError() instead")
    void postSubscriptionItemsChangeSignalE(OAISubscription summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postSubscriptionItemsChangeSignalError(OAISubscription summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postSubscriptionReactivationSignalError() instead")
    void postSubscriptionReactivationSignalE(OAISubscriptionReactivation summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postSubscriptionReactivationSignalError(OAISubscriptionReactivation summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postSubscriptionTimelineSignalError() instead")
    void postSubscriptionTimelineSignalE(OAIOrderTimeline summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postSubscriptionTimelineSignalError(OAIOrderTimeline summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postUpcomingInvoiceIssuanceSignalError() instead")
    void postUpcomingInvoiceIssuanceSignalE(OAIInvoice summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postUpcomingInvoiceIssuanceSignalError(OAIInvoice summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use putSubscriptionSignalError() instead")
    void putSubscriptionSignalE(OAISubscription summary, QNetworkReply::NetworkError error_type, QString error_str);
    void putSubscriptionSignalError(OAISubscription summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use putSubscriptionCancellationSignalError() instead")
    void putSubscriptionCancellationSignalE(OAISubscriptionCancellation summary, QNetworkReply::NetworkError error_type, QString error_str);
    void putSubscriptionCancellationSignalError(OAISubscriptionCancellation summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use deleteSubscriptionCancellationSignalErrorFull() instead")
    void deleteSubscriptionCancellationSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteSubscriptionCancellationSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteSubscriptionTimelineSignalErrorFull() instead")
    void deleteSubscriptionTimelineSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteSubscriptionTimelineSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getSubscriptionSignalErrorFull() instead")
    void getSubscriptionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getSubscriptionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getSubscriptionCancellationSignalErrorFull() instead")
    void getSubscriptionCancellationSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getSubscriptionCancellationSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getSubscriptionCancellationCollectionSignalErrorFull() instead")
    void getSubscriptionCancellationCollectionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getSubscriptionCancellationCollectionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getSubscriptionCollectionSignalErrorFull() instead")
    void getSubscriptionCollectionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getSubscriptionCollectionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getSubscriptionReactivationSignalErrorFull() instead")
    void getSubscriptionReactivationSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getSubscriptionReactivationSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getSubscriptionReactivationCollectionSignalErrorFull() instead")
    void getSubscriptionReactivationCollectionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getSubscriptionReactivationCollectionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getSubscriptionTimelineSignalErrorFull() instead")
    void getSubscriptionTimelineSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getSubscriptionTimelineSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getSubscriptionTimelineCollectionSignalErrorFull() instead")
    void getSubscriptionTimelineCollectionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getSubscriptionTimelineCollectionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getSubscriptionUpcomingInvoiceCollectionSignalErrorFull() instead")
    void getSubscriptionUpcomingInvoiceCollectionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getSubscriptionUpcomingInvoiceCollectionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postSubscriptionSignalErrorFull() instead")
    void postSubscriptionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postSubscriptionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postSubscriptionCancellationSignalErrorFull() instead")
    void postSubscriptionCancellationSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postSubscriptionCancellationSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postSubscriptionInterimInvoiceSignalErrorFull() instead")
    void postSubscriptionInterimInvoiceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postSubscriptionInterimInvoiceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postSubscriptionItemsChangeSignalErrorFull() instead")
    void postSubscriptionItemsChangeSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postSubscriptionItemsChangeSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postSubscriptionReactivationSignalErrorFull() instead")
    void postSubscriptionReactivationSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postSubscriptionReactivationSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postSubscriptionTimelineSignalErrorFull() instead")
    void postSubscriptionTimelineSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postSubscriptionTimelineSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postUpcomingInvoiceIssuanceSignalErrorFull() instead")
    void postUpcomingInvoiceIssuanceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postUpcomingInvoiceIssuanceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use putSubscriptionSignalErrorFull() instead")
    void putSubscriptionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void putSubscriptionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use putSubscriptionCancellationSignalErrorFull() instead")
    void putSubscriptionCancellationSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void putSubscriptionCancellationSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
