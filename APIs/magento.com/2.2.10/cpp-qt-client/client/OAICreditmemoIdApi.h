/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAICreditmemoIdApi_H
#define OAI_OAICreditmemoIdApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIError_response.h"
#include "OAISales_data_creditmemo_interface.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAICreditmemoIdApi : public QObject {
    Q_OBJECT

public:
    OAICreditmemoIdApi(const int timeOut = 0);
    ~OAICreditmemoIdApi();

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
    */
    virtual void salesCreditmemoManagementV1CancelPut(const qint32 &id);

    /**
    * @param[in]  id qint32 [required]
    */
    virtual void salesCreditmemoRepositoryV1GetGet(const qint32 &id);


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

    void salesCreditmemoManagementV1CancelPutCallback(OAIHttpRequestWorker *worker);
    void salesCreditmemoRepositoryV1GetGetCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void salesCreditmemoManagementV1CancelPutSignal(bool summary);
    void salesCreditmemoRepositoryV1GetGetSignal(OAISales_data_creditmemo_interface summary);


    void salesCreditmemoManagementV1CancelPutSignalFull(OAIHttpRequestWorker *worker, bool summary);
    void salesCreditmemoRepositoryV1GetGetSignalFull(OAIHttpRequestWorker *worker, OAISales_data_creditmemo_interface summary);

    Q_DECL_DEPRECATED_X("Use salesCreditmemoManagementV1CancelPutSignalError() instead")
    void salesCreditmemoManagementV1CancelPutSignalE(bool summary, QNetworkReply::NetworkError error_type, QString error_str);
    void salesCreditmemoManagementV1CancelPutSignalError(bool summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use salesCreditmemoRepositoryV1GetGetSignalError() instead")
    void salesCreditmemoRepositoryV1GetGetSignalE(OAISales_data_creditmemo_interface summary, QNetworkReply::NetworkError error_type, QString error_str);
    void salesCreditmemoRepositoryV1GetGetSignalError(OAISales_data_creditmemo_interface summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use salesCreditmemoManagementV1CancelPutSignalErrorFull() instead")
    void salesCreditmemoManagementV1CancelPutSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void salesCreditmemoManagementV1CancelPutSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use salesCreditmemoRepositoryV1GetGetSignalErrorFull() instead")
    void salesCreditmemoRepositoryV1GetGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void salesCreditmemoRepositoryV1GetGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
