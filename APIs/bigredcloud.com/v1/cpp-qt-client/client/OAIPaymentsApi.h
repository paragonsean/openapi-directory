/**
 * Big Red Cloud API
 *   <div style='line-height: 30px;'>      <strong>Welcome to the Big Red Cloud API</strong><br/>      This API enables programmatic access to Big Red Cloud data.<br/>      We have used Swagger to auto generate the API documentation on this page, and it also enables direct interaction with the API in this page. <br/>      To get started, you will require an API Key - check out our guide at <a target='_blank' href='https://www.bigredcloud.com/support/generating-api-key-guide/'>https://www.bigredcloud.com/support/generating-api-key-guide/</a> for information on how to get one. <br/>      Use the  'Enter API Key' button below to enter your API key and start interacting with your Big Red Cloud data right on this page. <br/>      The API key will be stored in your browsers local storage for convenience, but you will be able to delete it at any time if you wish. <br/>      For additional information on the API, check out our support article at <a target='_blank' href='https://www.bigredcloud.com/support/api/'>https://www.bigredcloud.com/support/api/</a><br/>  </div>
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIPaymentsApi_H
#define OAI_OAIPaymentsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIBatchItem_PaymentDto_.h"
#include "OAIObject.h"
#include "OAIPageResult_PaymentQueryDto_.h"
#include "OAIPaymentDto.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIPaymentsApi : public QObject {
    Q_OBJECT

public:
    OAIPaymentsApi(const int timeOut = 0);
    ~OAIPaymentsApi();

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
    * @param[in]  id qint64 [required]
    * @param[in]  timestamp QString [required]
    */
    virtual void paymentsDelete(const qint64 &id, const QString &timestamp);


    virtual void paymentsGet();

    /**
    * @param[in]  oai_payment_dto OAIPaymentDto [required]
    */
    virtual void paymentsPost(const OAIPaymentDto &oai_payment_dto);

    /**
    * @param[in]  oai_batch_item_payment_dto_ QList<OAIBatchItem_PaymentDto_> [required]
    */
    virtual void paymentsProcessBatch(const QList<OAIBatchItem_PaymentDto_> &oai_batch_item_payment_dto_);

    /**
    * @param[in]  id qint64 [required]
    * @param[in]  oai_payment_dto OAIPaymentDto [required]
    */
    virtual void paymentsPut(const qint64 &id, const OAIPaymentDto &oai_payment_dto);

    /**
    * @param[in]  id qint64 [required]
    */
    virtual void v1PaymentsIdGet(const qint64 &id);


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

    void paymentsDeleteCallback(OAIHttpRequestWorker *worker);
    void paymentsGetCallback(OAIHttpRequestWorker *worker);
    void paymentsPostCallback(OAIHttpRequestWorker *worker);
    void paymentsProcessBatchCallback(OAIHttpRequestWorker *worker);
    void paymentsPutCallback(OAIHttpRequestWorker *worker);
    void v1PaymentsIdGetCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void paymentsDeleteSignal(OAIObject summary);
    void paymentsGetSignal(OAIPageResult_PaymentQueryDto_ summary);
    void paymentsPostSignal(OAIObject summary);
    void paymentsProcessBatchSignal(OAIObject summary);
    void paymentsPutSignal(OAIObject summary);
    void v1PaymentsIdGetSignal(OAIPaymentDto summary);


    void paymentsDeleteSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void paymentsGetSignalFull(OAIHttpRequestWorker *worker, OAIPageResult_PaymentQueryDto_ summary);
    void paymentsPostSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void paymentsProcessBatchSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void paymentsPutSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void v1PaymentsIdGetSignalFull(OAIHttpRequestWorker *worker, OAIPaymentDto summary);

    Q_DECL_DEPRECATED_X("Use paymentsDeleteSignalError() instead")
    void paymentsDeleteSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void paymentsDeleteSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use paymentsGetSignalError() instead")
    void paymentsGetSignalE(OAIPageResult_PaymentQueryDto_ summary, QNetworkReply::NetworkError error_type, QString error_str);
    void paymentsGetSignalError(OAIPageResult_PaymentQueryDto_ summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use paymentsPostSignalError() instead")
    void paymentsPostSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void paymentsPostSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use paymentsProcessBatchSignalError() instead")
    void paymentsProcessBatchSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void paymentsProcessBatchSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use paymentsPutSignalError() instead")
    void paymentsPutSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void paymentsPutSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v1PaymentsIdGetSignalError() instead")
    void v1PaymentsIdGetSignalE(OAIPaymentDto summary, QNetworkReply::NetworkError error_type, QString error_str);
    void v1PaymentsIdGetSignalError(OAIPaymentDto summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use paymentsDeleteSignalErrorFull() instead")
    void paymentsDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void paymentsDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use paymentsGetSignalErrorFull() instead")
    void paymentsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void paymentsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use paymentsPostSignalErrorFull() instead")
    void paymentsPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void paymentsPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use paymentsProcessBatchSignalErrorFull() instead")
    void paymentsProcessBatchSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void paymentsProcessBatchSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use paymentsPutSignalErrorFull() instead")
    void paymentsPutSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void paymentsPutSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v1PaymentsIdGetSignalErrorFull() instead")
    void v1PaymentsIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void v1PaymentsIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
