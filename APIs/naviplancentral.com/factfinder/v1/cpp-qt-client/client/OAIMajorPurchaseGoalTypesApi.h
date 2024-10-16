/**
 * Advicent.FactFinderService
 * An API for accessing the NaviPlan Fact Finder.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIMajorPurchaseGoalTypesApi_H
#define OAI_OAIMajorPurchaseGoalTypesApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIMajorPurchaseGoalTypeModel.h"
#include "OAIMajorPurchaseGoalTypesModel.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIMajorPurchaseGoalTypesApi : public QObject {
    Q_OBJECT

public:
    OAIMajorPurchaseGoalTypesApi(const int timeOut = 0);
    ~OAIMajorPurchaseGoalTypesApi();

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
    * @param[in]  country QString [required]
    */
    virtual void majorPurchaseGoalTypesGetByCountry(const QString &country);

    /**
    * @param[in]  id qint32 [required]
    */
    virtual void majorPurchaseGoalTypesGetById(const qint32 &id);


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

    void majorPurchaseGoalTypesGetByCountryCallback(OAIHttpRequestWorker *worker);
    void majorPurchaseGoalTypesGetByIdCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void majorPurchaseGoalTypesGetByCountrySignal(OAIMajorPurchaseGoalTypesModel summary);
    void majorPurchaseGoalTypesGetByIdSignal(OAIMajorPurchaseGoalTypeModel summary);


    void majorPurchaseGoalTypesGetByCountrySignalFull(OAIHttpRequestWorker *worker, OAIMajorPurchaseGoalTypesModel summary);
    void majorPurchaseGoalTypesGetByIdSignalFull(OAIHttpRequestWorker *worker, OAIMajorPurchaseGoalTypeModel summary);

    Q_DECL_DEPRECATED_X("Use majorPurchaseGoalTypesGetByCountrySignalError() instead")
    void majorPurchaseGoalTypesGetByCountrySignalE(OAIMajorPurchaseGoalTypesModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void majorPurchaseGoalTypesGetByCountrySignalError(OAIMajorPurchaseGoalTypesModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use majorPurchaseGoalTypesGetByIdSignalError() instead")
    void majorPurchaseGoalTypesGetByIdSignalE(OAIMajorPurchaseGoalTypeModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void majorPurchaseGoalTypesGetByIdSignalError(OAIMajorPurchaseGoalTypeModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use majorPurchaseGoalTypesGetByCountrySignalErrorFull() instead")
    void majorPurchaseGoalTypesGetByCountrySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void majorPurchaseGoalTypesGetByCountrySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use majorPurchaseGoalTypesGetByIdSignalErrorFull() instead")
    void majorPurchaseGoalTypesGetByIdSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void majorPurchaseGoalTypesGetByIdSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
