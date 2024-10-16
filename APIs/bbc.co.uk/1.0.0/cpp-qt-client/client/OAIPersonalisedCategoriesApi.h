/**
 * Radio & Music Services
 * We encapsulate Radio & Music business logic for iPlayer Radio and BBC Music products on all platforms. We add value by reliably providing the right blend of metadata needed by clients.
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIPersonalisedCategoriesApi_H
#define OAI_OAIPersonalisedCategoriesApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIBody.h"
#include "OAIBody_1.h"
#include "OAIErrorResponse.h"
#include "OAIPersonalisedCategoriesResponse.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIPersonalisedCategoriesApi : public QObject {
    Q_OBJECT

public:
    OAIPersonalisedCategoriesApi(const int timeOut = 0);
    ~OAIPersonalisedCategoriesApi();

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
    * @param[in]  authorization QString [required]
    * @param[in]  x_api_key QString [required]
    * @param[in]  body OAIBody_1 [required]
    */
    virtual void myCategoriesFollowsDelete(const QString &authorization, const QString &x_api_key, const OAIBody_1 &body);

    /**
    * @param[in]  authorization QString [required]
    * @param[in]  x_api_key QString [required]
    * @param[in]  offset qint32 [optional]
    * @param[in]  limit qint32 [optional]
    */
    virtual void myCategoriesFollowsGet(const QString &authorization, const QString &x_api_key, const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  authorization QString [required]
    * @param[in]  x_api_key QString [required]
    * @param[in]  body OAIBody [required]
    */
    virtual void myCategoriesFollowsPost(const QString &authorization, const QString &x_api_key, const OAIBody &body);


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

    void myCategoriesFollowsDeleteCallback(OAIHttpRequestWorker *worker);
    void myCategoriesFollowsGetCallback(OAIHttpRequestWorker *worker);
    void myCategoriesFollowsPostCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void myCategoriesFollowsDeleteSignal();
    void myCategoriesFollowsGetSignal(OAIPersonalisedCategoriesResponse summary);
    void myCategoriesFollowsPostSignal();


    void myCategoriesFollowsDeleteSignalFull(OAIHttpRequestWorker *worker);
    void myCategoriesFollowsGetSignalFull(OAIHttpRequestWorker *worker, OAIPersonalisedCategoriesResponse summary);
    void myCategoriesFollowsPostSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use myCategoriesFollowsDeleteSignalError() instead")
    void myCategoriesFollowsDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void myCategoriesFollowsDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use myCategoriesFollowsGetSignalError() instead")
    void myCategoriesFollowsGetSignalE(OAIPersonalisedCategoriesResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void myCategoriesFollowsGetSignalError(OAIPersonalisedCategoriesResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use myCategoriesFollowsPostSignalError() instead")
    void myCategoriesFollowsPostSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void myCategoriesFollowsPostSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use myCategoriesFollowsDeleteSignalErrorFull() instead")
    void myCategoriesFollowsDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void myCategoriesFollowsDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use myCategoriesFollowsGetSignalErrorFull() instead")
    void myCategoriesFollowsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void myCategoriesFollowsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use myCategoriesFollowsPostSignalErrorFull() instead")
    void myCategoriesFollowsPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void myCategoriesFollowsPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
