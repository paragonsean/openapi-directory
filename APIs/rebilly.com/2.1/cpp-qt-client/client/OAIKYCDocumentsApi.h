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

#ifndef OAI_OAIKYCDocumentsApi_H
#define OAI_OAIKYCDocumentsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIError.h"
#include "OAIInvalidError.h"
#include "OAIKycDocumentRejection.h"
#include "OAIKycDocument_2.h"
#include "OAIKycRequest.h"
#include "OAIPatchKycRequest_request.h"
#include "OAIPostKycDocumentMatches_request.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIKYCDocumentsApi : public QObject {
    Q_OBJECT

public:
    OAIKYCDocumentsApi(const int timeOut = 0);
    ~OAIKYCDocumentsApi();

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
    virtual void deleteKycRequest(const QString &id, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void getKycDocument(const QString &id, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  organization_id QString [optional]
    * @param[in]  limit qint32 [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  filter QString [optional]
    * @param[in]  sort QList<QString> [optional]
    */
    virtual void getKycDocumentCollection(const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &filter = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QList<QString>> &sort = ::OpenAPI::OptionalParam<QList<QString>>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void getKycRequest(const QString &id, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  organization_id QString [optional]
    * @param[in]  limit qint32 [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  filter QString [optional]
    * @param[in]  sort QList<QString> [optional]
    */
    virtual void getKycRequestCollection(const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &filter = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QList<QString>> &sort = ::OpenAPI::OptionalParam<QList<QString>>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  organization_id QString [optional]
    * @param[in]  oai_patch_kyc_request_request OAIPatchKycRequest_request [optional]
    */
    virtual void patchKycRequest(const QString &id, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<OAIPatchKycRequest_request> &oai_patch_kyc_request_request = ::OpenAPI::OptionalParam<OAIPatchKycRequest_request>());

    /**
    * @param[in]  oai_kyc_document_2 OAIKycDocument_2 [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void postKycDocument(const OAIKycDocument_2 &oai_kyc_document_2, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void postKycDocumentAcceptance(const QString &id, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  oai_post_kyc_document_matches_request OAIPostKycDocumentMatches_request [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void postKycDocumentMatches(const QString &id, const OAIPostKycDocumentMatches_request &oai_post_kyc_document_matches_request, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  oai_kyc_document_rejection OAIKycDocumentRejection [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void postKycDocumentRejection(const QString &id, const OAIKycDocumentRejection &oai_kyc_document_rejection, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void postKycDocumentReview(const QString &id, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_kyc_request OAIKycRequest [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void postKycRequest(const OAIKycRequest &oai_kyc_request, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  oai_kyc_document_2 OAIKycDocument_2 [required]
    * @param[in]  organization_id QString [optional]
    */
    virtual void putKycDocument(const QString &id, const OAIKycDocument_2 &oai_kyc_document_2, const ::OpenAPI::OptionalParam<QString> &organization_id = ::OpenAPI::OptionalParam<QString>());


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

    void deleteKycRequestCallback(OAIHttpRequestWorker *worker);
    void getKycDocumentCallback(OAIHttpRequestWorker *worker);
    void getKycDocumentCollectionCallback(OAIHttpRequestWorker *worker);
    void getKycRequestCallback(OAIHttpRequestWorker *worker);
    void getKycRequestCollectionCallback(OAIHttpRequestWorker *worker);
    void patchKycRequestCallback(OAIHttpRequestWorker *worker);
    void postKycDocumentCallback(OAIHttpRequestWorker *worker);
    void postKycDocumentAcceptanceCallback(OAIHttpRequestWorker *worker);
    void postKycDocumentMatchesCallback(OAIHttpRequestWorker *worker);
    void postKycDocumentRejectionCallback(OAIHttpRequestWorker *worker);
    void postKycDocumentReviewCallback(OAIHttpRequestWorker *worker);
    void postKycRequestCallback(OAIHttpRequestWorker *worker);
    void putKycDocumentCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void deleteKycRequestSignal();
    void getKycDocumentSignal(OAIKycDocument_2 summary);
    void getKycDocumentCollectionSignal(QList<OAIKycDocument_2> summary);
    void getKycRequestSignal(OAIKycRequest summary);
    void getKycRequestCollectionSignal(QList<OAIKycRequest> summary);
    void patchKycRequestSignal(OAIKycRequest summary);
    void postKycDocumentSignal(OAIKycDocument_2 summary);
    void postKycDocumentAcceptanceSignal(OAIKycDocument_2 summary);
    void postKycDocumentMatchesSignal();
    void postKycDocumentRejectionSignal(OAIKycDocument_2 summary);
    void postKycDocumentReviewSignal(OAIKycDocument_2 summary);
    void postKycRequestSignal(OAIKycRequest summary);
    void putKycDocumentSignal(OAIKycDocument_2 summary);


    void deleteKycRequestSignalFull(OAIHttpRequestWorker *worker);
    void getKycDocumentSignalFull(OAIHttpRequestWorker *worker, OAIKycDocument_2 summary);
    void getKycDocumentCollectionSignalFull(OAIHttpRequestWorker *worker, QList<OAIKycDocument_2> summary);
    void getKycRequestSignalFull(OAIHttpRequestWorker *worker, OAIKycRequest summary);
    void getKycRequestCollectionSignalFull(OAIHttpRequestWorker *worker, QList<OAIKycRequest> summary);
    void patchKycRequestSignalFull(OAIHttpRequestWorker *worker, OAIKycRequest summary);
    void postKycDocumentSignalFull(OAIHttpRequestWorker *worker, OAIKycDocument_2 summary);
    void postKycDocumentAcceptanceSignalFull(OAIHttpRequestWorker *worker, OAIKycDocument_2 summary);
    void postKycDocumentMatchesSignalFull(OAIHttpRequestWorker *worker);
    void postKycDocumentRejectionSignalFull(OAIHttpRequestWorker *worker, OAIKycDocument_2 summary);
    void postKycDocumentReviewSignalFull(OAIHttpRequestWorker *worker, OAIKycDocument_2 summary);
    void postKycRequestSignalFull(OAIHttpRequestWorker *worker, OAIKycRequest summary);
    void putKycDocumentSignalFull(OAIHttpRequestWorker *worker, OAIKycDocument_2 summary);

    Q_DECL_DEPRECATED_X("Use deleteKycRequestSignalError() instead")
    void deleteKycRequestSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void deleteKycRequestSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getKycDocumentSignalError() instead")
    void getKycDocumentSignalE(OAIKycDocument_2 summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getKycDocumentSignalError(OAIKycDocument_2 summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getKycDocumentCollectionSignalError() instead")
    void getKycDocumentCollectionSignalE(QList<OAIKycDocument_2> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getKycDocumentCollectionSignalError(QList<OAIKycDocument_2> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getKycRequestSignalError() instead")
    void getKycRequestSignalE(OAIKycRequest summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getKycRequestSignalError(OAIKycRequest summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getKycRequestCollectionSignalError() instead")
    void getKycRequestCollectionSignalE(QList<OAIKycRequest> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getKycRequestCollectionSignalError(QList<OAIKycRequest> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patchKycRequestSignalError() instead")
    void patchKycRequestSignalE(OAIKycRequest summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patchKycRequestSignalError(OAIKycRequest summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postKycDocumentSignalError() instead")
    void postKycDocumentSignalE(OAIKycDocument_2 summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postKycDocumentSignalError(OAIKycDocument_2 summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postKycDocumentAcceptanceSignalError() instead")
    void postKycDocumentAcceptanceSignalE(OAIKycDocument_2 summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postKycDocumentAcceptanceSignalError(OAIKycDocument_2 summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postKycDocumentMatchesSignalError() instead")
    void postKycDocumentMatchesSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void postKycDocumentMatchesSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postKycDocumentRejectionSignalError() instead")
    void postKycDocumentRejectionSignalE(OAIKycDocument_2 summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postKycDocumentRejectionSignalError(OAIKycDocument_2 summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postKycDocumentReviewSignalError() instead")
    void postKycDocumentReviewSignalE(OAIKycDocument_2 summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postKycDocumentReviewSignalError(OAIKycDocument_2 summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postKycRequestSignalError() instead")
    void postKycRequestSignalE(OAIKycRequest summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postKycRequestSignalError(OAIKycRequest summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use putKycDocumentSignalError() instead")
    void putKycDocumentSignalE(OAIKycDocument_2 summary, QNetworkReply::NetworkError error_type, QString error_str);
    void putKycDocumentSignalError(OAIKycDocument_2 summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use deleteKycRequestSignalErrorFull() instead")
    void deleteKycRequestSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteKycRequestSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getKycDocumentSignalErrorFull() instead")
    void getKycDocumentSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getKycDocumentSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getKycDocumentCollectionSignalErrorFull() instead")
    void getKycDocumentCollectionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getKycDocumentCollectionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getKycRequestSignalErrorFull() instead")
    void getKycRequestSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getKycRequestSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getKycRequestCollectionSignalErrorFull() instead")
    void getKycRequestCollectionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getKycRequestCollectionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patchKycRequestSignalErrorFull() instead")
    void patchKycRequestSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patchKycRequestSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postKycDocumentSignalErrorFull() instead")
    void postKycDocumentSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postKycDocumentSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postKycDocumentAcceptanceSignalErrorFull() instead")
    void postKycDocumentAcceptanceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postKycDocumentAcceptanceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postKycDocumentMatchesSignalErrorFull() instead")
    void postKycDocumentMatchesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postKycDocumentMatchesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postKycDocumentRejectionSignalErrorFull() instead")
    void postKycDocumentRejectionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postKycDocumentRejectionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postKycDocumentReviewSignalErrorFull() instead")
    void postKycDocumentReviewSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postKycDocumentReviewSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postKycRequestSignalErrorFull() instead")
    void postKycRequestSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postKycRequestSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use putKycDocumentSignalErrorFull() instead")
    void putKycDocumentSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void putKycDocumentSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
