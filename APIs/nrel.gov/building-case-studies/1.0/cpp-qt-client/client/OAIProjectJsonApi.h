/**
 * High Performance Building Database
 * The Buildings Database is a shared resource for the building industry. The Database, developed by the U.S. Department of Energy and the National Renewable Energy Laboratory (NREL), is a unique central repository of in-depth information and data on high-performance, green building projects across the United States and abroad.  
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIProjectJsonApi_H
#define OAI_OAIProjectJsonApi_H

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

class OAIProjectJsonApi : public QObject {
    Q_OBJECT

public:
    OAIProjectJsonApi(const int timeOut = 0);
    ~OAIProjectJsonApi();

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
    * @param[in]  output_format QString [required]
    * @param[in]  api_key QString [required]
    * @param[in]  project_id qint32 [required]
    */
    virtual void document(const QString &output_format, const QString &api_key, const qint32 &project_id);

    /**
    * @param[in]  output_format QString [required]
    * @param[in]  api_key QString [required]
    * @param[in]  search QString [optional]
    * @param[in]  portal QString [optional]
    * @param[in]  page qint32 [optional]
    * @param[in]  city QString [optional]
    * @param[in]  province QString [optional]
    * @param[in]  region QString [optional]
    */
    virtual void project(const QString &output_format, const QString &api_key, const ::OpenAPI::OptionalParam<QString> &search = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &portal = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &city = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &province = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &region = ::OpenAPI::OptionalParam<QString>());


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

    void documentCallback(OAIHttpRequestWorker *worker);
    void projectCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void documentSignal();
    void projectSignal();


    void documentSignalFull(OAIHttpRequestWorker *worker);
    void projectSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use documentSignalError() instead")
    void documentSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void documentSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectSignalError() instead")
    void projectSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void projectSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use documentSignalErrorFull() instead")
    void documentSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void documentSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectSignalErrorFull() instead")
    void projectSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void projectSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
