/**
 * Noosh API application
 * Full description of Noosh API
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIExchangeRateApi_H
#define OAI_OAIExchangeRateApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIHTTPStatusVO.h"
#include "OAIMultiExchangeRateListVO.h"
#include "OAIMultiExchangeRatePersistListVO.h"
#include <QJsonValue>
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIExchangeRateApi : public QObject {
    Q_OBJECT

public:
    OAIExchangeRateApi(const int timeOut = 0);
    ~OAIExchangeRateApi();

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
    * @param[in]  workgroup_id QString [required]
    */
    virtual void getExchangeRateList(const QString &workgroup_id);

    /**
    * @param[in]  workgroup_id QString [required]
    * @param[in]  oai_multi_exchange_rate_persist_list_vo OAIMultiExchangeRatePersistListVO [optional]
    */
    virtual void postExchangeRate(const QString &workgroup_id, const ::OpenAPI::OptionalParam<OAIMultiExchangeRatePersistListVO> &oai_multi_exchange_rate_persist_list_vo = ::OpenAPI::OptionalParam<OAIMultiExchangeRatePersistListVO>());


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

    void getExchangeRateListCallback(OAIHttpRequestWorker *worker);
    void postExchangeRateCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void getExchangeRateListSignal(OAIMultiExchangeRateListVO summary);
    void postExchangeRateSignal(QJsonValue summary);


    void getExchangeRateListSignalFull(OAIHttpRequestWorker *worker, OAIMultiExchangeRateListVO summary);
    void postExchangeRateSignalFull(OAIHttpRequestWorker *worker, QJsonValue summary);

    Q_DECL_DEPRECATED_X("Use getExchangeRateListSignalError() instead")
    void getExchangeRateListSignalE(OAIMultiExchangeRateListVO summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getExchangeRateListSignalError(OAIMultiExchangeRateListVO summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postExchangeRateSignalError() instead")
    void postExchangeRateSignalE(QJsonValue summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postExchangeRateSignalError(QJsonValue summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use getExchangeRateListSignalErrorFull() instead")
    void getExchangeRateListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getExchangeRateListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postExchangeRateSignalErrorFull() instead")
    void postExchangeRateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postExchangeRateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
