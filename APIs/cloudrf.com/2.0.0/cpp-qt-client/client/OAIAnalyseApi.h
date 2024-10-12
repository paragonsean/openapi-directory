/**
 * Cloud-RF API
 * Use this JSON API to build and test radio links for any radio, anywhere. Authenticate with your API2.0 key in the request header as key
 *
 * The version of the OpenAPI document: 2.0.0
 * Contact: support@cloudrf.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIAnalyseApi_H
#define OAI_OAIAnalyseApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIAnalyseApi : public QObject {
    Q_OBJECT

public:
    OAIAnalyseApi(const int timeOut = 0);
    ~OAIAnalyseApi();

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
    * @param[in]  network QString [required]
    * @param[in]  name QString [required]
    */
    virtual void interference(const QString &network, const QString &name);

    /**
    * @param[in]  network QString [required]
    * @param[in]  name QString [required]
    */
    virtual void mesh(const QString &network, const QString &name);

    /**
    * @param[in]  net QString [required]
    * @param[in]  nam QString [required]
    * @param[in]  lat float [required]
    * @param[in]  lon float [required]
    * @param[in]  alt qint32 [required]
    * @param[in]  rxg float [optional]
    */
    virtual void network(const QString &net, const QString &nam, const float &lat, const float &lon, const qint32 &alt, const ::OpenAPI::OptionalParam<float> &rxg = ::OpenAPI::OptionalParam<float>());


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

    void interferenceCallback(OAIHttpRequestWorker *worker);
    void meshCallback(OAIHttpRequestWorker *worker);
    void networkCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void interferenceSignal();
    void meshSignal();
    void networkSignal();


    void interferenceSignalFull(OAIHttpRequestWorker *worker);
    void meshSignalFull(OAIHttpRequestWorker *worker);
    void networkSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use interferenceSignalError() instead")
    void interferenceSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void interferenceSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use meshSignalError() instead")
    void meshSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void meshSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use networkSignalError() instead")
    void networkSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void networkSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use interferenceSignalErrorFull() instead")
    void interferenceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void interferenceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use meshSignalErrorFull() instead")
    void meshSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void meshSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use networkSignalErrorFull() instead")
    void networkSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void networkSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
