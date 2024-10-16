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

#ifndef OAI_OAIBusinessEntitiesApi_H
#define OAI_OAIBusinessEntitiesApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIBusinessEntitiesModel.h"
#include "OAIBusinessEntityModel.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIBusinessEntitiesApi : public QObject {
    Q_OBJECT

public:
    OAIBusinessEntitiesApi(const int timeOut = 0);
    ~OAIBusinessEntitiesApi();

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
    virtual void businessEntitiesGetByIdPlanid(const qint32 &id, const QString &plan_id);

    /**
    * @param[in]  plan_id QString [required]
    */
    virtual void businessEntitiesGetByPlanid(const QString &plan_id);


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

    void businessEntitiesGetByIdPlanidCallback(OAIHttpRequestWorker *worker);
    void businessEntitiesGetByPlanidCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void businessEntitiesGetByIdPlanidSignal(OAIBusinessEntityModel summary);
    void businessEntitiesGetByPlanidSignal(OAIBusinessEntitiesModel summary);


    void businessEntitiesGetByIdPlanidSignalFull(OAIHttpRequestWorker *worker, OAIBusinessEntityModel summary);
    void businessEntitiesGetByPlanidSignalFull(OAIHttpRequestWorker *worker, OAIBusinessEntitiesModel summary);

    Q_DECL_DEPRECATED_X("Use businessEntitiesGetByIdPlanidSignalError() instead")
    void businessEntitiesGetByIdPlanidSignalE(OAIBusinessEntityModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void businessEntitiesGetByIdPlanidSignalError(OAIBusinessEntityModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use businessEntitiesGetByPlanidSignalError() instead")
    void businessEntitiesGetByPlanidSignalE(OAIBusinessEntitiesModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void businessEntitiesGetByPlanidSignalError(OAIBusinessEntitiesModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use businessEntitiesGetByIdPlanidSignalErrorFull() instead")
    void businessEntitiesGetByIdPlanidSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void businessEntitiesGetByIdPlanidSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use businessEntitiesGetByPlanidSignalErrorFull() instead")
    void businessEntitiesGetByPlanidSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void businessEntitiesGetByPlanidSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
