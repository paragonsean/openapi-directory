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

#ifndef OAI_OAIUserFieldsApi_H
#define OAI_OAIUserFieldsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIHTTPStatusVO.h"
#include "OAIProjectHomeUserFieldsListVO.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIUserFieldsApi : public QObject {
    Q_OBJECT

public:
    OAIUserFieldsApi(const int timeOut = 0);
    ~OAIUserFieldsApi();

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
    * @param[in]  client_workgroup_id QString [required]
    */
    virtual void getProjectHomeUserFieldListOfClient(const QString &workgroup_id, const QString &client_workgroup_id);

    /**
    * @param[in]  workgroup_id QString [required]
    */
    virtual void getProjectHomeUserFieldsList(const QString &workgroup_id);


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

    void getProjectHomeUserFieldListOfClientCallback(OAIHttpRequestWorker *worker);
    void getProjectHomeUserFieldsListCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void getProjectHomeUserFieldListOfClientSignal(OAIProjectHomeUserFieldsListVO summary);
    void getProjectHomeUserFieldsListSignal(OAIProjectHomeUserFieldsListVO summary);


    void getProjectHomeUserFieldListOfClientSignalFull(OAIHttpRequestWorker *worker, OAIProjectHomeUserFieldsListVO summary);
    void getProjectHomeUserFieldsListSignalFull(OAIHttpRequestWorker *worker, OAIProjectHomeUserFieldsListVO summary);

    Q_DECL_DEPRECATED_X("Use getProjectHomeUserFieldListOfClientSignalError() instead")
    void getProjectHomeUserFieldListOfClientSignalE(OAIProjectHomeUserFieldsListVO summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getProjectHomeUserFieldListOfClientSignalError(OAIProjectHomeUserFieldsListVO summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getProjectHomeUserFieldsListSignalError() instead")
    void getProjectHomeUserFieldsListSignalE(OAIProjectHomeUserFieldsListVO summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getProjectHomeUserFieldsListSignalError(OAIProjectHomeUserFieldsListVO summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use getProjectHomeUserFieldListOfClientSignalErrorFull() instead")
    void getProjectHomeUserFieldListOfClientSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getProjectHomeUserFieldListOfClientSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getProjectHomeUserFieldsListSignalErrorFull() instead")
    void getProjectHomeUserFieldsListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getProjectHomeUserFieldsListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
