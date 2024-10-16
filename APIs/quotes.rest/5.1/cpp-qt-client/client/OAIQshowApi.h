/**
 * They Said So Quotes API
 *  They Said So Quotes API offers a complete feature rich REST API access to its quotes platform.  This is the documentation for the world famous [quotes API](https://theysaidso.com/api).  If you are a subscriber and you are trying this from a console you can use Bearer token with your api key as the token. You can test and play with the API right here on this web page. Please note recently we closed downs public access without api key to prevent abuse. The public routes are still available to use free of charge but requires a api token. You can get one for free at our website. For using the private end points and subscribing to the API please visit [https://theysaidso.com/api](https://theysaidso.com/api).
 *
 * The version of the OpenAPI document: 5.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIQshowApi_H
#define OAI_OAIQshowApi_H

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

class OAIQshowApi : public QObject {
    Q_OBJECT

public:
    OAIQshowApi(const int timeOut = 0);
    ~OAIQshowApi();

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
    * @param[in]  id QString [required]
    */
    virtual void qshowDelete(const QString &id);

    /**
    * @param[in]  id QString [required]
    */
    virtual void qshowGet(const QString &id);

    /**
    * @param[in]  start qint32 [optional]
    * @param[in]  r_public bool [optional]
    */
    virtual void qshowListGet(const ::OpenAPI::OptionalParam<qint32> &start = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<bool> &r_public = ::OpenAPI::OptionalParam<bool>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  title QString [optional]
    * @param[in]  description QString [optional]
    * @param[in]  tags QList<QString> [optional]
    */
    virtual void qshowPatch(const QString &id, const ::OpenAPI::OptionalParam<QString> &title = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &description = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QList<QString>> &tags = ::OpenAPI::OptionalParam<QList<QString>>());

    /**
    * @param[in]  title QString [required]
    * @param[in]  description QString [optional]
    * @param[in]  tags QList<QString> [optional]
    */
    virtual void qshowPut(const QString &title, const ::OpenAPI::OptionalParam<QString> &description = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QList<QString>> &tags = ::OpenAPI::OptionalParam<QList<QString>>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  quoteid QString [required]
    */
    virtual void qshowQuotesAddPost(const QString &id, const QString &quoteid);

    /**
    * @param[in]  id QString [required]
    */
    virtual void qshowQuotesGet(const QString &id);

    /**
    * @param[in]  id QString [required]
    * @param[in]  quoteid QString [required]
    */
    virtual void qshowQuotesRemovePost(const QString &id, const QString &quoteid);


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

    void qshowDeleteCallback(OAIHttpRequestWorker *worker);
    void qshowGetCallback(OAIHttpRequestWorker *worker);
    void qshowListGetCallback(OAIHttpRequestWorker *worker);
    void qshowPatchCallback(OAIHttpRequestWorker *worker);
    void qshowPutCallback(OAIHttpRequestWorker *worker);
    void qshowQuotesAddPostCallback(OAIHttpRequestWorker *worker);
    void qshowQuotesGetCallback(OAIHttpRequestWorker *worker);
    void qshowQuotesRemovePostCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void qshowDeleteSignal();
    void qshowGetSignal();
    void qshowListGetSignal();
    void qshowPatchSignal();
    void qshowPutSignal();
    void qshowQuotesAddPostSignal();
    void qshowQuotesGetSignal();
    void qshowQuotesRemovePostSignal();


    void qshowDeleteSignalFull(OAIHttpRequestWorker *worker);
    void qshowGetSignalFull(OAIHttpRequestWorker *worker);
    void qshowListGetSignalFull(OAIHttpRequestWorker *worker);
    void qshowPatchSignalFull(OAIHttpRequestWorker *worker);
    void qshowPutSignalFull(OAIHttpRequestWorker *worker);
    void qshowQuotesAddPostSignalFull(OAIHttpRequestWorker *worker);
    void qshowQuotesGetSignalFull(OAIHttpRequestWorker *worker);
    void qshowQuotesRemovePostSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use qshowDeleteSignalError() instead")
    void qshowDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void qshowDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use qshowGetSignalError() instead")
    void qshowGetSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void qshowGetSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use qshowListGetSignalError() instead")
    void qshowListGetSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void qshowListGetSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use qshowPatchSignalError() instead")
    void qshowPatchSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void qshowPatchSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use qshowPutSignalError() instead")
    void qshowPutSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void qshowPutSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use qshowQuotesAddPostSignalError() instead")
    void qshowQuotesAddPostSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void qshowQuotesAddPostSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use qshowQuotesGetSignalError() instead")
    void qshowQuotesGetSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void qshowQuotesGetSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use qshowQuotesRemovePostSignalError() instead")
    void qshowQuotesRemovePostSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void qshowQuotesRemovePostSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use qshowDeleteSignalErrorFull() instead")
    void qshowDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void qshowDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use qshowGetSignalErrorFull() instead")
    void qshowGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void qshowGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use qshowListGetSignalErrorFull() instead")
    void qshowListGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void qshowListGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use qshowPatchSignalErrorFull() instead")
    void qshowPatchSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void qshowPatchSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use qshowPutSignalErrorFull() instead")
    void qshowPutSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void qshowPutSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use qshowQuotesAddPostSignalErrorFull() instead")
    void qshowQuotesAddPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void qshowQuotesAddPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use qshowQuotesGetSignalErrorFull() instead")
    void qshowQuotesGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void qshowQuotesGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use qshowQuotesRemovePostSignalErrorFull() instead")
    void qshowQuotesRemovePostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void qshowQuotesRemovePostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
