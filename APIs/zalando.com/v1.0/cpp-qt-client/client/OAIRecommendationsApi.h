/**
 * Zalando Shop
 * The shop API empowers developers to build amazing new apps or websites using Zalando shop data and services.
 *
 * The version of the OpenAPI document: v1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIRecommendationsApi_H
#define OAI_OAIRecommendationsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIErrorMessage.h"
#include "OAIRecommendations_Article.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIRecommendationsApi : public QObject {
    Q_OBJECT

public:
    OAIRecommendationsApi(const int timeOut = 0);
    ~OAIRecommendationsApi();

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
    * @param[in]  article_ids QList<QString> [required]
    * @param[in]  max_results QString [optional]
    * @param[in]  accept_language QString [optional]
    * @param[in]  fields QList<QString> [optional]
    */
    virtual void recommendationsArticleIdsGet(const QList<QString> &article_ids, const ::OpenAPI::OptionalParam<QString> &max_results = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &accept_language = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QList<QString>> &fields = ::OpenAPI::OptionalParam<QList<QString>>());


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

    void recommendationsArticleIdsGetCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void recommendationsArticleIdsGetSignal(QList<OAIRecommendations_Article> summary);


    void recommendationsArticleIdsGetSignalFull(OAIHttpRequestWorker *worker, QList<OAIRecommendations_Article> summary);

    Q_DECL_DEPRECATED_X("Use recommendationsArticleIdsGetSignalError() instead")
    void recommendationsArticleIdsGetSignalE(QList<OAIRecommendations_Article> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void recommendationsArticleIdsGetSignalError(QList<OAIRecommendations_Article> summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use recommendationsArticleIdsGetSignalErrorFull() instead")
    void recommendationsArticleIdsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void recommendationsArticleIdsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
