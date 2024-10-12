/**
 * Dados Abertos - API
 * API de Dados Abertos com dados processados pelo grupo de monitoramento de Queimadas do INPE.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIFocosApi_H
#define OAI_OAIFocosApi_H

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

class OAIFocosApi : public QObject {
    Q_OBJECT

public:
    OAIFocosApi(const int timeOut = 0);
    ~OAIFocosApi();

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
    * @param[in]  pais_id qint32 [optional]
    * @param[in]  estado_id qint32 [optional]
    * @param[in]  municipio_id qint32 [optional]
    * @param[in]  satelite QList<QString> [optional]
    */
    virtual void getFocosCountResource(const ::OpenAPI::OptionalParam<qint32> &pais_id = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &estado_id = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &municipio_id = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QList<QString>> &satelite = ::OpenAPI::OptionalParam<QList<QString>>());

    /**
    * @param[in]  pais_id qint32 [optional]
    * @param[in]  estado_id qint32 [optional]
    * @param[in]  municipio_id qint32 [optional]
    * @param[in]  satelite QList<QString> [optional]
    * @param[in]  x_fields QString [optional]
    */
    virtual void getFocosResource(const ::OpenAPI::OptionalParam<qint32> &pais_id = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &estado_id = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &municipio_id = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QList<QString>> &satelite = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<QString> &x_fields = ::OpenAPI::OptionalParam<QString>());


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

    void getFocosCountResourceCallback(OAIHttpRequestWorker *worker);
    void getFocosResourceCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void getFocosCountResourceSignal();
    void getFocosResourceSignal();


    void getFocosCountResourceSignalFull(OAIHttpRequestWorker *worker);
    void getFocosResourceSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use getFocosCountResourceSignalError() instead")
    void getFocosCountResourceSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void getFocosCountResourceSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getFocosResourceSignalError() instead")
    void getFocosResourceSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void getFocosResourceSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use getFocosCountResourceSignalErrorFull() instead")
    void getFocosCountResourceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getFocosCountResourceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getFocosResourceSignalErrorFull() instead")
    void getFocosResourceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getFocosResourceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
