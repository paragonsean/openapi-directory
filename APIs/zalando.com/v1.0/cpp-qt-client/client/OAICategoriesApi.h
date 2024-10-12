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

#ifndef OAI_OAICategoriesApi_H
#define OAI_OAICategoriesApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAICategories.h"
#include "OAICategory.h"
#include "OAIErrorMessage.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAICategoriesApi : public QObject {
    Q_OBJECT

public:
    OAICategoriesApi(const int timeOut = 0);
    ~OAICategoriesApi();

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
    * @param[in]  name QList<QString> [optional]
    * @param[in]  type QString [optional]
    * @param[in]  outlet QString [optional]
    * @param[in]  hidden QString [optional]
    * @param[in]  target_group QString [optional]
    * @param[in]  key QList<QString> [optional]
    * @param[in]  parent_key QList<QString> [optional]
    * @param[in]  child_key QList<QString> [optional]
    * @param[in]  suggested_filter QList<QString> [optional]
    * @param[in]  page QString [optional]
    * @param[in]  page_size QString [optional]
    * @param[in]  accept_language QString [optional]
    * @param[in]  fields QList<QString> [optional]
    */
    virtual void categoriesGet(const ::OpenAPI::OptionalParam<QList<QString>> &name = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<QString> &type = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &outlet = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &hidden = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &target_group = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QList<QString>> &key = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<QList<QString>> &parent_key = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<QList<QString>> &child_key = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<QList<QString>> &suggested_filter = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<QString> &page = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &page_size = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &accept_language = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QList<QString>> &fields = ::OpenAPI::OptionalParam<QList<QString>>());

    /**
    * @param[in]  key QList<QString> [required]
    * @param[in]  accept_language QString [optional]
    * @param[in]  fields QList<QString> [optional]
    */
    virtual void categoriesKeyGet(const QList<QString> &key, const ::OpenAPI::OptionalParam<QString> &accept_language = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QList<QString>> &fields = ::OpenAPI::OptionalParam<QList<QString>>());


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

    void categoriesGetCallback(OAIHttpRequestWorker *worker);
    void categoriesKeyGetCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void categoriesGetSignal(OAICategories summary);
    void categoriesKeyGetSignal(OAICategory summary);


    void categoriesGetSignalFull(OAIHttpRequestWorker *worker, OAICategories summary);
    void categoriesKeyGetSignalFull(OAIHttpRequestWorker *worker, OAICategory summary);

    Q_DECL_DEPRECATED_X("Use categoriesGetSignalError() instead")
    void categoriesGetSignalE(OAICategories summary, QNetworkReply::NetworkError error_type, QString error_str);
    void categoriesGetSignalError(OAICategories summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use categoriesKeyGetSignalError() instead")
    void categoriesKeyGetSignalE(OAICategory summary, QNetworkReply::NetworkError error_type, QString error_str);
    void categoriesKeyGetSignalError(OAICategory summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use categoriesGetSignalErrorFull() instead")
    void categoriesGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void categoriesGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use categoriesKeyGetSignalErrorFull() instead")
    void categoriesKeyGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void categoriesKeyGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
