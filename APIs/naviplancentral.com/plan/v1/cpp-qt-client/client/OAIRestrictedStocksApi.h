/**
 * NaviPlan API
 * An API for accessing NaviPlan plan data for a client.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIRestrictedStocksApi_H
#define OAI_OAIRestrictedStocksApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIRestrictedStockModel.h"
#include "OAIRestrictedStocksModel.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIRestrictedStocksApi : public QObject {
    Q_OBJECT

public:
    OAIRestrictedStocksApi(const int timeOut = 0);
    ~OAIRestrictedStocksApi();

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
    * @param[in]  id qint32 [required]
    * @param[in]  plan_id QString [required]
    */
    virtual void restrictedStocksGetByIdPlanid(const qint32 &id, const QString &plan_id);

    /**
    * @param[in]  plan_id QString [required]
    */
    virtual void restrictedStocksGetByPlanid(const QString &plan_id);


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

    void restrictedStocksGetByIdPlanidCallback(OAIHttpRequestWorker *worker);
    void restrictedStocksGetByPlanidCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void restrictedStocksGetByIdPlanidSignal(OAIRestrictedStockModel summary);
    void restrictedStocksGetByPlanidSignal(OAIRestrictedStocksModel summary);


    void restrictedStocksGetByIdPlanidSignalFull(OAIHttpRequestWorker *worker, OAIRestrictedStockModel summary);
    void restrictedStocksGetByPlanidSignalFull(OAIHttpRequestWorker *worker, OAIRestrictedStocksModel summary);

    Q_DECL_DEPRECATED_X("Use restrictedStocksGetByIdPlanidSignalError() instead")
    void restrictedStocksGetByIdPlanidSignalE(OAIRestrictedStockModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void restrictedStocksGetByIdPlanidSignalError(OAIRestrictedStockModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use restrictedStocksGetByPlanidSignalError() instead")
    void restrictedStocksGetByPlanidSignalE(OAIRestrictedStocksModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void restrictedStocksGetByPlanidSignalError(OAIRestrictedStocksModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use restrictedStocksGetByIdPlanidSignalErrorFull() instead")
    void restrictedStocksGetByIdPlanidSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void restrictedStocksGetByIdPlanidSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use restrictedStocksGetByPlanidSignalErrorFull() instead")
    void restrictedStocksGetByPlanidSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void restrictedStocksGetByPlanidSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
