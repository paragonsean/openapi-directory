/**
 * ApplicationInsightsManagementClient
 * Azure Application Insights client for favorites.
 *
 * The version of the OpenAPI document: 2015-05-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIDefaultApi_H
#define OAI_OAIDefaultApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIApplicationInsightsComponentFavorite.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIDefaultApi : public QObject {
    Q_OBJECT

public:
    OAIDefaultApi(const int timeOut = 0);
    ~OAIDefaultApi();

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
    * @param[in]  resource_group_name QString [required]
    * @param[in]  api_version QString [required]
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_name QString [required]
    * @param[in]  favorite_id QString [required]
    * @param[in]  favorite_properties OAIApplicationInsightsComponentFavorite [required]
    */
    virtual void favoritesAdd(const QString &resource_group_name, const QString &api_version, const QString &subscription_id, const QString &resource_name, const QString &favorite_id, const OAIApplicationInsightsComponentFavorite &favorite_properties);

    /**
    * @param[in]  resource_group_name QString [required]
    * @param[in]  api_version QString [required]
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_name QString [required]
    * @param[in]  favorite_id QString [required]
    */
    virtual void favoritesDelete(const QString &resource_group_name, const QString &api_version, const QString &subscription_id, const QString &resource_name, const QString &favorite_id);

    /**
    * @param[in]  resource_group_name QString [required]
    * @param[in]  api_version QString [required]
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_name QString [required]
    * @param[in]  favorite_id QString [required]
    */
    virtual void favoritesGet(const QString &resource_group_name, const QString &api_version, const QString &subscription_id, const QString &resource_name, const QString &favorite_id);

    /**
    * @param[in]  resource_group_name QString [required]
    * @param[in]  api_version QString [required]
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_name QString [required]
    * @param[in]  favorite_type QString [optional]
    * @param[in]  source_type QString [optional]
    * @param[in]  can_fetch_content bool [optional]
    * @param[in]  tags QList<QString> [optional]
    */
    virtual void favoritesList(const QString &resource_group_name, const QString &api_version, const QString &subscription_id, const QString &resource_name, const ::OpenAPI::OptionalParam<QString> &favorite_type = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &source_type = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &can_fetch_content = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QList<QString>> &tags = ::OpenAPI::OptionalParam<QList<QString>>());

    /**
    * @param[in]  resource_group_name QString [required]
    * @param[in]  api_version QString [required]
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_name QString [required]
    * @param[in]  favorite_id QString [required]
    * @param[in]  favorite_properties OAIApplicationInsightsComponentFavorite [required]
    */
    virtual void favoritesUpdate(const QString &resource_group_name, const QString &api_version, const QString &subscription_id, const QString &resource_name, const QString &favorite_id, const OAIApplicationInsightsComponentFavorite &favorite_properties);


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

    void favoritesAddCallback(OAIHttpRequestWorker *worker);
    void favoritesDeleteCallback(OAIHttpRequestWorker *worker);
    void favoritesGetCallback(OAIHttpRequestWorker *worker);
    void favoritesListCallback(OAIHttpRequestWorker *worker);
    void favoritesUpdateCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void favoritesAddSignal(OAIApplicationInsightsComponentFavorite summary);
    void favoritesDeleteSignal();
    void favoritesGetSignal(OAIApplicationInsightsComponentFavorite summary);
    void favoritesListSignal(QList<OAIApplicationInsightsComponentFavorite> summary);
    void favoritesUpdateSignal(OAIApplicationInsightsComponentFavorite summary);


    void favoritesAddSignalFull(OAIHttpRequestWorker *worker, OAIApplicationInsightsComponentFavorite summary);
    void favoritesDeleteSignalFull(OAIHttpRequestWorker *worker);
    void favoritesGetSignalFull(OAIHttpRequestWorker *worker, OAIApplicationInsightsComponentFavorite summary);
    void favoritesListSignalFull(OAIHttpRequestWorker *worker, QList<OAIApplicationInsightsComponentFavorite> summary);
    void favoritesUpdateSignalFull(OAIHttpRequestWorker *worker, OAIApplicationInsightsComponentFavorite summary);

    Q_DECL_DEPRECATED_X("Use favoritesAddSignalError() instead")
    void favoritesAddSignalE(OAIApplicationInsightsComponentFavorite summary, QNetworkReply::NetworkError error_type, QString error_str);
    void favoritesAddSignalError(OAIApplicationInsightsComponentFavorite summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use favoritesDeleteSignalError() instead")
    void favoritesDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void favoritesDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use favoritesGetSignalError() instead")
    void favoritesGetSignalE(OAIApplicationInsightsComponentFavorite summary, QNetworkReply::NetworkError error_type, QString error_str);
    void favoritesGetSignalError(OAIApplicationInsightsComponentFavorite summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use favoritesListSignalError() instead")
    void favoritesListSignalE(QList<OAIApplicationInsightsComponentFavorite> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void favoritesListSignalError(QList<OAIApplicationInsightsComponentFavorite> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use favoritesUpdateSignalError() instead")
    void favoritesUpdateSignalE(OAIApplicationInsightsComponentFavorite summary, QNetworkReply::NetworkError error_type, QString error_str);
    void favoritesUpdateSignalError(OAIApplicationInsightsComponentFavorite summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use favoritesAddSignalErrorFull() instead")
    void favoritesAddSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void favoritesAddSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use favoritesDeleteSignalErrorFull() instead")
    void favoritesDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void favoritesDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use favoritesGetSignalErrorFull() instead")
    void favoritesGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void favoritesGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use favoritesListSignalErrorFull() instead")
    void favoritesListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void favoritesListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use favoritesUpdateSignalErrorFull() instead")
    void favoritesUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void favoritesUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
