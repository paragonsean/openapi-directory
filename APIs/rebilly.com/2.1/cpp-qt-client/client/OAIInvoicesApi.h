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

#ifndef OAI_OAIInvoicesApi_H
#define OAI_OAIInvoicesApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIError.h"
#include "OAIInvalidError.h"
#include "OAIInvoice.h"
#include "OAIInvoiceIssue.h"
#include "OAIInvoiceItem.h"
#include "OAIInvoiceReissue.h"
#include "OAIInvoiceTimeline.h"
#include "OAIInvoiceTransaction.h"
#include "OAIInvoiceTransactionAllocation.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIInvoicesApi : public QObject {
    Q_OBJECT

public:
    OAIInvoicesApi(const int timeOut = 0);
    ~OAIInvoicesApi();

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
    * @param[in]  message_id QString [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void deleteInvoiceTimeline(const QString &id, const QString &message_id, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  organization_id QString [optional]
    * @param[in]  expand QString [optional]
    */
    virtual void getCustomerUpcomingInvoiceCollection(const QString &id, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &expand = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  organization_id QString [optional]
    * @param[in]  accept QString [optional]
    * @param[in]  expand QString [optional]
    */
    virtual void getInvoice(const QString &id, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &accept = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &expand = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  organization_id QString [optional]
    * @param[in]  filter QString [optional]
    * @param[in]  sort QList<QString> [optional]
    * @param[in]  limit qint32 [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  q QString [optional]
    * @param[in]  expand QString [optional]
    */
    virtual void getInvoiceCollection(const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &filter = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QList<QString>> &sort = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &q = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &expand = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  organization_id QString [optional]
    * @param[in]  limit qint32 [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  expand QString [optional]
    */
    virtual void getInvoiceItemCollection(const QString &id, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &expand = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  message_id QString [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void getInvoiceTimeline(const QString &id, const QString &message_id, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  organization_id QString [optional]
    * @param[in]  limit qint32 [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  filter QString [optional]
    * @param[in]  sort QList<QString> [optional]
    * @param[in]  q QString [optional]
    */
    virtual void getInvoiceTimelineCollection(const QString &id, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &filter = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QList<QString>> &sort = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<QString> &q = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  organization_id QString [optional]
    * @param[in]  limit qint32 [optional]
    * @param[in]  offset qint32 [optional]
    */
    virtual void getInvoiceTransactionAllocationCollection(const QString &id, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  oai_invoice OAIInvoice [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void postInvoice(const OAIInvoice &oai_invoice, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void postInvoiceAbandonment(const QString &id, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  oai_invoice_issue OAIInvoiceIssue [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void postInvoiceIssuance(const QString &id, const OAIInvoiceIssue &oai_invoice_issue, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  oai_invoice_item OAIInvoiceItem [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void postInvoiceItem(const QString &id, const OAIInvoiceItem &oai_invoice_item, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void postInvoiceRecalculation(const QString &id, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  oai_invoice_reissue OAIInvoiceReissue [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void postInvoiceReissuance(const QString &id, const OAIInvoiceReissue &oai_invoice_reissue, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  oai_invoice_timeline OAIInvoiceTimeline [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void postInvoiceTimeline(const QString &id, const OAIInvoiceTimeline &oai_invoice_timeline, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  oai_invoice_transaction OAIInvoiceTransaction [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void postInvoiceTransaction(const QString &id, const OAIInvoiceTransaction &oai_invoice_transaction, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void postInvoiceVoid(const QString &id, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  oai_invoice OAIInvoice [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void putInvoice(const QString &id, const OAIInvoice &oai_invoice, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());


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

    void deleteInvoiceTimelineCallback(OAIHttpRequestWorker *worker);
    void getCustomerUpcomingInvoiceCollectionCallback(OAIHttpRequestWorker *worker);
    void getInvoiceCallback(OAIHttpRequestWorker *worker);
    void getInvoiceCollectionCallback(OAIHttpRequestWorker *worker);
    void getInvoiceItemCollectionCallback(OAIHttpRequestWorker *worker);
    void getInvoiceTimelineCallback(OAIHttpRequestWorker *worker);
    void getInvoiceTimelineCollectionCallback(OAIHttpRequestWorker *worker);
    void getInvoiceTransactionAllocationCollectionCallback(OAIHttpRequestWorker *worker);
    void postInvoiceCallback(OAIHttpRequestWorker *worker);
    void postInvoiceAbandonmentCallback(OAIHttpRequestWorker *worker);
    void postInvoiceIssuanceCallback(OAIHttpRequestWorker *worker);
    void postInvoiceItemCallback(OAIHttpRequestWorker *worker);
    void postInvoiceRecalculationCallback(OAIHttpRequestWorker *worker);
    void postInvoiceReissuanceCallback(OAIHttpRequestWorker *worker);
    void postInvoiceTimelineCallback(OAIHttpRequestWorker *worker);
    void postInvoiceTransactionCallback(OAIHttpRequestWorker *worker);
    void postInvoiceVoidCallback(OAIHttpRequestWorker *worker);
    void putInvoiceCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void deleteInvoiceTimelineSignal();
    void getCustomerUpcomingInvoiceCollectionSignal(QList<OAIInvoice> summary);
    void getInvoiceSignal(OAIInvoice summary);
    void getInvoiceCollectionSignal(QList<OAIInvoice> summary);
    void getInvoiceItemCollectionSignal(QList<OAIInvoiceItem> summary);
    void getInvoiceTimelineSignal(OAIInvoiceTimeline summary);
    void getInvoiceTimelineCollectionSignal(QList<OAIInvoiceTimeline> summary);
    void getInvoiceTransactionAllocationCollectionSignal(QList<OAIInvoiceTransactionAllocation> summary);
    void postInvoiceSignal(OAIInvoice summary);
    void postInvoiceAbandonmentSignal(OAIInvoice summary);
    void postInvoiceIssuanceSignal(OAIInvoice summary);
    void postInvoiceItemSignal(OAIInvoiceItem summary);
    void postInvoiceRecalculationSignal(OAIInvoice summary);
    void postInvoiceReissuanceSignal(OAIInvoice summary);
    void postInvoiceTimelineSignal(OAIInvoiceTimeline summary);
    void postInvoiceTransactionSignal(OAIInvoice summary);
    void postInvoiceVoidSignal(OAIInvoice summary);
    void putInvoiceSignal(OAIInvoice summary);


    void deleteInvoiceTimelineSignalFull(OAIHttpRequestWorker *worker);
    void getCustomerUpcomingInvoiceCollectionSignalFull(OAIHttpRequestWorker *worker, QList<OAIInvoice> summary);
    void getInvoiceSignalFull(OAIHttpRequestWorker *worker, OAIInvoice summary);
    void getInvoiceCollectionSignalFull(OAIHttpRequestWorker *worker, QList<OAIInvoice> summary);
    void getInvoiceItemCollectionSignalFull(OAIHttpRequestWorker *worker, QList<OAIInvoiceItem> summary);
    void getInvoiceTimelineSignalFull(OAIHttpRequestWorker *worker, OAIInvoiceTimeline summary);
    void getInvoiceTimelineCollectionSignalFull(OAIHttpRequestWorker *worker, QList<OAIInvoiceTimeline> summary);
    void getInvoiceTransactionAllocationCollectionSignalFull(OAIHttpRequestWorker *worker, QList<OAIInvoiceTransactionAllocation> summary);
    void postInvoiceSignalFull(OAIHttpRequestWorker *worker, OAIInvoice summary);
    void postInvoiceAbandonmentSignalFull(OAIHttpRequestWorker *worker, OAIInvoice summary);
    void postInvoiceIssuanceSignalFull(OAIHttpRequestWorker *worker, OAIInvoice summary);
    void postInvoiceItemSignalFull(OAIHttpRequestWorker *worker, OAIInvoiceItem summary);
    void postInvoiceRecalculationSignalFull(OAIHttpRequestWorker *worker, OAIInvoice summary);
    void postInvoiceReissuanceSignalFull(OAIHttpRequestWorker *worker, OAIInvoice summary);
    void postInvoiceTimelineSignalFull(OAIHttpRequestWorker *worker, OAIInvoiceTimeline summary);
    void postInvoiceTransactionSignalFull(OAIHttpRequestWorker *worker, OAIInvoice summary);
    void postInvoiceVoidSignalFull(OAIHttpRequestWorker *worker, OAIInvoice summary);
    void putInvoiceSignalFull(OAIHttpRequestWorker *worker, OAIInvoice summary);

    Q_DECL_DEPRECATED_X("Use deleteInvoiceTimelineSignalError() instead")
    void deleteInvoiceTimelineSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void deleteInvoiceTimelineSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getCustomerUpcomingInvoiceCollectionSignalError() instead")
    void getCustomerUpcomingInvoiceCollectionSignalE(QList<OAIInvoice> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getCustomerUpcomingInvoiceCollectionSignalError(QList<OAIInvoice> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getInvoiceSignalError() instead")
    void getInvoiceSignalE(OAIInvoice summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getInvoiceSignalError(OAIInvoice summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getInvoiceCollectionSignalError() instead")
    void getInvoiceCollectionSignalE(QList<OAIInvoice> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getInvoiceCollectionSignalError(QList<OAIInvoice> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getInvoiceItemCollectionSignalError() instead")
    void getInvoiceItemCollectionSignalE(QList<OAIInvoiceItem> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getInvoiceItemCollectionSignalError(QList<OAIInvoiceItem> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getInvoiceTimelineSignalError() instead")
    void getInvoiceTimelineSignalE(OAIInvoiceTimeline summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getInvoiceTimelineSignalError(OAIInvoiceTimeline summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getInvoiceTimelineCollectionSignalError() instead")
    void getInvoiceTimelineCollectionSignalE(QList<OAIInvoiceTimeline> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getInvoiceTimelineCollectionSignalError(QList<OAIInvoiceTimeline> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getInvoiceTransactionAllocationCollectionSignalError() instead")
    void getInvoiceTransactionAllocationCollectionSignalE(QList<OAIInvoiceTransactionAllocation> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getInvoiceTransactionAllocationCollectionSignalError(QList<OAIInvoiceTransactionAllocation> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postInvoiceSignalError() instead")
    void postInvoiceSignalE(OAIInvoice summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postInvoiceSignalError(OAIInvoice summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postInvoiceAbandonmentSignalError() instead")
    void postInvoiceAbandonmentSignalE(OAIInvoice summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postInvoiceAbandonmentSignalError(OAIInvoice summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postInvoiceIssuanceSignalError() instead")
    void postInvoiceIssuanceSignalE(OAIInvoice summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postInvoiceIssuanceSignalError(OAIInvoice summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postInvoiceItemSignalError() instead")
    void postInvoiceItemSignalE(OAIInvoiceItem summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postInvoiceItemSignalError(OAIInvoiceItem summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postInvoiceRecalculationSignalError() instead")
    void postInvoiceRecalculationSignalE(OAIInvoice summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postInvoiceRecalculationSignalError(OAIInvoice summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postInvoiceReissuanceSignalError() instead")
    void postInvoiceReissuanceSignalE(OAIInvoice summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postInvoiceReissuanceSignalError(OAIInvoice summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postInvoiceTimelineSignalError() instead")
    void postInvoiceTimelineSignalE(OAIInvoiceTimeline summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postInvoiceTimelineSignalError(OAIInvoiceTimeline summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postInvoiceTransactionSignalError() instead")
    void postInvoiceTransactionSignalE(OAIInvoice summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postInvoiceTransactionSignalError(OAIInvoice summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postInvoiceVoidSignalError() instead")
    void postInvoiceVoidSignalE(OAIInvoice summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postInvoiceVoidSignalError(OAIInvoice summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use putInvoiceSignalError() instead")
    void putInvoiceSignalE(OAIInvoice summary, QNetworkReply::NetworkError error_type, QString error_str);
    void putInvoiceSignalError(OAIInvoice summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use deleteInvoiceTimelineSignalErrorFull() instead")
    void deleteInvoiceTimelineSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteInvoiceTimelineSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getCustomerUpcomingInvoiceCollectionSignalErrorFull() instead")
    void getCustomerUpcomingInvoiceCollectionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getCustomerUpcomingInvoiceCollectionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getInvoiceSignalErrorFull() instead")
    void getInvoiceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getInvoiceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getInvoiceCollectionSignalErrorFull() instead")
    void getInvoiceCollectionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getInvoiceCollectionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getInvoiceItemCollectionSignalErrorFull() instead")
    void getInvoiceItemCollectionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getInvoiceItemCollectionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getInvoiceTimelineSignalErrorFull() instead")
    void getInvoiceTimelineSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getInvoiceTimelineSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getInvoiceTimelineCollectionSignalErrorFull() instead")
    void getInvoiceTimelineCollectionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getInvoiceTimelineCollectionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getInvoiceTransactionAllocationCollectionSignalErrorFull() instead")
    void getInvoiceTransactionAllocationCollectionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getInvoiceTransactionAllocationCollectionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postInvoiceSignalErrorFull() instead")
    void postInvoiceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postInvoiceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postInvoiceAbandonmentSignalErrorFull() instead")
    void postInvoiceAbandonmentSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postInvoiceAbandonmentSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postInvoiceIssuanceSignalErrorFull() instead")
    void postInvoiceIssuanceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postInvoiceIssuanceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postInvoiceItemSignalErrorFull() instead")
    void postInvoiceItemSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postInvoiceItemSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postInvoiceRecalculationSignalErrorFull() instead")
    void postInvoiceRecalculationSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postInvoiceRecalculationSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postInvoiceReissuanceSignalErrorFull() instead")
    void postInvoiceReissuanceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postInvoiceReissuanceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postInvoiceTimelineSignalErrorFull() instead")
    void postInvoiceTimelineSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postInvoiceTimelineSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postInvoiceTransactionSignalErrorFull() instead")
    void postInvoiceTransactionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postInvoiceTransactionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postInvoiceVoidSignalErrorFull() instead")
    void postInvoiceVoidSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postInvoiceVoidSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use putInvoiceSignalErrorFull() instead")
    void putInvoiceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void putInvoiceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
