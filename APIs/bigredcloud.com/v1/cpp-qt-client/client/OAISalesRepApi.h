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

#ifndef OAI_OAISalesRepApi_H
#define OAI_OAISalesRepApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIBatchItem_SaleRepsDto_.h"
#include "OAIObject.h"
#include "OAIPageResult_SaleRepsDto_.h"
#include "OAISaleRepsDto.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAISalesRepApi : public QObject {
    Q_OBJECT

public:
    OAISalesRepApi(const int timeOut = 0);
    ~OAISalesRepApi();

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
    virtual void salesRepDelete(const qint64 &id, const QString &timestamp);


    virtual void salesRepGet();

    /**
    * @param[in]  oai_sale_reps_dto OAISaleRepsDto [required]
    */
    virtual void salesRepPost(const OAISaleRepsDto &oai_sale_reps_dto);

    /**
    * @param[in]  oai_batch_item_sale_reps_dto_ QList<OAIBatchItem_SaleRepsDto_> [required]
    */
    virtual void salesRepProcessBatch(const QList<OAIBatchItem_SaleRepsDto_> &oai_batch_item_sale_reps_dto_);

    /**
    * @param[in]  id qint64 [required]
    * @param[in]  oai_sale_reps_dto OAISaleRepsDto [required]
    */
    virtual void salesRepPut(const qint64 &id, const OAISaleRepsDto &oai_sale_reps_dto);

    /**
    * @param[in]  id qint64 [required]
    */
    virtual void v1SalesRepsIdGet(const qint64 &id);


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

    void salesRepDeleteCallback(OAIHttpRequestWorker *worker);
    void salesRepGetCallback(OAIHttpRequestWorker *worker);
    void salesRepPostCallback(OAIHttpRequestWorker *worker);
    void salesRepProcessBatchCallback(OAIHttpRequestWorker *worker);
    void salesRepPutCallback(OAIHttpRequestWorker *worker);
    void v1SalesRepsIdGetCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void salesRepDeleteSignal(OAIObject summary);
    void salesRepGetSignal(OAIPageResult_SaleRepsDto_ summary);
    void salesRepPostSignal(OAIObject summary);
    void salesRepProcessBatchSignal(OAIObject summary);
    void salesRepPutSignal(OAIObject summary);
    void v1SalesRepsIdGetSignal(OAISaleRepsDto summary);


    void salesRepDeleteSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void salesRepGetSignalFull(OAIHttpRequestWorker *worker, OAIPageResult_SaleRepsDto_ summary);
    void salesRepPostSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void salesRepProcessBatchSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void salesRepPutSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void v1SalesRepsIdGetSignalFull(OAIHttpRequestWorker *worker, OAISaleRepsDto summary);

    Q_DECL_DEPRECATED_X("Use salesRepDeleteSignalError() instead")
    void salesRepDeleteSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void salesRepDeleteSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use salesRepGetSignalError() instead")
    void salesRepGetSignalE(OAIPageResult_SaleRepsDto_ summary, QNetworkReply::NetworkError error_type, QString error_str);
    void salesRepGetSignalError(OAIPageResult_SaleRepsDto_ summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use salesRepPostSignalError() instead")
    void salesRepPostSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void salesRepPostSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use salesRepProcessBatchSignalError() instead")
    void salesRepProcessBatchSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void salesRepProcessBatchSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use salesRepPutSignalError() instead")
    void salesRepPutSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void salesRepPutSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v1SalesRepsIdGetSignalError() instead")
    void v1SalesRepsIdGetSignalE(OAISaleRepsDto summary, QNetworkReply::NetworkError error_type, QString error_str);
    void v1SalesRepsIdGetSignalError(OAISaleRepsDto summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use salesRepDeleteSignalErrorFull() instead")
    void salesRepDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void salesRepDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use salesRepGetSignalErrorFull() instead")
    void salesRepGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void salesRepGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use salesRepPostSignalErrorFull() instead")
    void salesRepPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void salesRepPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use salesRepProcessBatchSignalErrorFull() instead")
    void salesRepProcessBatchSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void salesRepProcessBatchSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use salesRepPutSignalErrorFull() instead")
    void salesRepPutSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void salesRepPutSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v1SalesRepsIdGetSignalErrorFull() instead")
    void v1SalesRepsIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void v1SalesRepsIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
