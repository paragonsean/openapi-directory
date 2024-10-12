/**
 * Up API
 * The Up API gives you programmatic access to your balances and transaction data. You can request past transactions or set up webhooks to receive real-time events when new transactions hit your account. It’s new, it’s exciting and it’s just the beginning. 
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAITransactionsApi_H
#define OAI_OAITransactionsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIGetTransactionResponse.h"
#include "OAIListTransactionsResponse.h"
#include "OAITransactionStatusEnum.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAITransactionsApi : public QObject {
    Q_OBJECT

public:
    OAITransactionsApi(const int timeOut = 0);
    ~OAITransactionsApi();

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
    * @param[in]  account_id QString [required]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  filter_status OAITransactionStatusEnum [optional]
    * @param[in]  filter_since QDateTime [optional]
    * @param[in]  filter_until QDateTime [optional]
    * @param[in]  filter_category QString [optional]
    * @param[in]  filter_tag QString [optional]
    */
    virtual void accountsAccountIdTransactionsGet(const QString &account_id, const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<OAITransactionStatusEnum> &filter_status = ::OpenAPI::OptionalParam<OAITransactionStatusEnum>(), const ::OpenAPI::OptionalParam<QDateTime> &filter_since = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<QDateTime> &filter_until = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<QString> &filter_category = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &filter_tag = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  page_size qint32 [optional]
    * @param[in]  filter_status OAITransactionStatusEnum [optional]
    * @param[in]  filter_since QDateTime [optional]
    * @param[in]  filter_until QDateTime [optional]
    * @param[in]  filter_category QString [optional]
    * @param[in]  filter_tag QString [optional]
    */
    virtual void transactionsGet(const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<OAITransactionStatusEnum> &filter_status = ::OpenAPI::OptionalParam<OAITransactionStatusEnum>(), const ::OpenAPI::OptionalParam<QDateTime> &filter_since = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<QDateTime> &filter_until = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<QString> &filter_category = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &filter_tag = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    */
    virtual void transactionsIdGet(const QString &id);


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

    void accountsAccountIdTransactionsGetCallback(OAIHttpRequestWorker *worker);
    void transactionsGetCallback(OAIHttpRequestWorker *worker);
    void transactionsIdGetCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void accountsAccountIdTransactionsGetSignal(OAIListTransactionsResponse summary);
    void transactionsGetSignal(OAIListTransactionsResponse summary);
    void transactionsIdGetSignal(OAIGetTransactionResponse summary);


    void accountsAccountIdTransactionsGetSignalFull(OAIHttpRequestWorker *worker, OAIListTransactionsResponse summary);
    void transactionsGetSignalFull(OAIHttpRequestWorker *worker, OAIListTransactionsResponse summary);
    void transactionsIdGetSignalFull(OAIHttpRequestWorker *worker, OAIGetTransactionResponse summary);

    Q_DECL_DEPRECATED_X("Use accountsAccountIdTransactionsGetSignalError() instead")
    void accountsAccountIdTransactionsGetSignalE(OAIListTransactionsResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void accountsAccountIdTransactionsGetSignalError(OAIListTransactionsResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use transactionsGetSignalError() instead")
    void transactionsGetSignalE(OAIListTransactionsResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void transactionsGetSignalError(OAIListTransactionsResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use transactionsIdGetSignalError() instead")
    void transactionsIdGetSignalE(OAIGetTransactionResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void transactionsIdGetSignalError(OAIGetTransactionResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use accountsAccountIdTransactionsGetSignalErrorFull() instead")
    void accountsAccountIdTransactionsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void accountsAccountIdTransactionsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use transactionsGetSignalErrorFull() instead")
    void transactionsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void transactionsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use transactionsIdGetSignalErrorFull() instead")
    void transactionsIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void transactionsIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
