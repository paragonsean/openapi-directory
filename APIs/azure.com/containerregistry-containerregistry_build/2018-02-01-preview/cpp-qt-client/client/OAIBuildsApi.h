/**
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIBuildsApi_H
#define OAI_OAIBuildsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIBuild.h"
#include "OAIBuildGetLogResult.h"
#include "OAIBuildListResult.h"
#include "OAIBuildUpdateParameters.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIBuildsApi : public QObject {
    Q_OBJECT

public:
    OAIBuildsApi(const int timeOut = 0);
    ~OAIBuildsApi();

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
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group_name QString [required]
    * @param[in]  registry_name QString [required]
    * @param[in]  api_version QString [required]
    * @param[in]  build_id QString [required]
    */
    virtual void buildsCancel(const QString &subscription_id, const QString &resource_group_name, const QString &registry_name, const QString &api_version, const QString &build_id);

    /**
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group_name QString [required]
    * @param[in]  registry_name QString [required]
    * @param[in]  api_version QString [required]
    * @param[in]  build_id QString [required]
    */
    virtual void buildsGet(const QString &subscription_id, const QString &resource_group_name, const QString &registry_name, const QString &api_version, const QString &build_id);

    /**
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group_name QString [required]
    * @param[in]  registry_name QString [required]
    * @param[in]  api_version QString [required]
    * @param[in]  build_id QString [required]
    */
    virtual void buildsGetLogLink(const QString &subscription_id, const QString &resource_group_name, const QString &registry_name, const QString &api_version, const QString &build_id);

    /**
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group_name QString [required]
    * @param[in]  registry_name QString [required]
    * @param[in]  api_version QString [required]
    * @param[in]  filter QString [optional]
    * @param[in]  top qint32 [optional]
    * @param[in]  skip_token QString [optional]
    */
    virtual void buildsList(const QString &subscription_id, const QString &resource_group_name, const QString &registry_name, const QString &api_version, const ::OpenAPI::OptionalParam<QString> &filter = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &top = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &skip_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group_name QString [required]
    * @param[in]  registry_name QString [required]
    * @param[in]  api_version QString [required]
    * @param[in]  build_id QString [required]
    * @param[in]  build_update_parameters OAIBuildUpdateParameters [required]
    */
    virtual void buildsUpdate(const QString &subscription_id, const QString &resource_group_name, const QString &registry_name, const QString &api_version, const QString &build_id, const OAIBuildUpdateParameters &build_update_parameters);


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

    void buildsCancelCallback(OAIHttpRequestWorker *worker);
    void buildsGetCallback(OAIHttpRequestWorker *worker);
    void buildsGetLogLinkCallback(OAIHttpRequestWorker *worker);
    void buildsListCallback(OAIHttpRequestWorker *worker);
    void buildsUpdateCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void buildsCancelSignal();
    void buildsGetSignal(OAIBuild summary);
    void buildsGetLogLinkSignal(OAIBuildGetLogResult summary);
    void buildsListSignal(OAIBuildListResult summary);
    void buildsUpdateSignal(OAIBuild summary);


    void buildsCancelSignalFull(OAIHttpRequestWorker *worker);
    void buildsGetSignalFull(OAIHttpRequestWorker *worker, OAIBuild summary);
    void buildsGetLogLinkSignalFull(OAIHttpRequestWorker *worker, OAIBuildGetLogResult summary);
    void buildsListSignalFull(OAIHttpRequestWorker *worker, OAIBuildListResult summary);
    void buildsUpdateSignalFull(OAIHttpRequestWorker *worker, OAIBuild summary);

    Q_DECL_DEPRECATED_X("Use buildsCancelSignalError() instead")
    void buildsCancelSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void buildsCancelSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use buildsGetSignalError() instead")
    void buildsGetSignalE(OAIBuild summary, QNetworkReply::NetworkError error_type, QString error_str);
    void buildsGetSignalError(OAIBuild summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use buildsGetLogLinkSignalError() instead")
    void buildsGetLogLinkSignalE(OAIBuildGetLogResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void buildsGetLogLinkSignalError(OAIBuildGetLogResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use buildsListSignalError() instead")
    void buildsListSignalE(OAIBuildListResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void buildsListSignalError(OAIBuildListResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use buildsUpdateSignalError() instead")
    void buildsUpdateSignalE(OAIBuild summary, QNetworkReply::NetworkError error_type, QString error_str);
    void buildsUpdateSignalError(OAIBuild summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use buildsCancelSignalErrorFull() instead")
    void buildsCancelSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void buildsCancelSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use buildsGetSignalErrorFull() instead")
    void buildsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void buildsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use buildsGetLogLinkSignalErrorFull() instead")
    void buildsGetLogLinkSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void buildsGetLogLinkSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use buildsListSignalErrorFull() instead")
    void buildsListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void buildsListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use buildsUpdateSignalErrorFull() instead")
    void buildsUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void buildsUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
