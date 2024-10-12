/**
 * Cambase.io
 * Cambase.io is a project by Evercam.io in order to make it easier for software developers to have a reliable, up to date source of model hardware information available via a public API.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIVendorsApi_H
#define OAI_OAIVendorsApi_H

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

class OAIVendorsApi : public QObject {
    Q_OBJECT

public:
    OAIVendorsApi(const int timeOut = 0);
    ~OAIVendorsApi();

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
    * @param[in]  vendor_name QString [required]
    * @param[in]  vendor_info QString [optional]
    * @param[in]  vendor_url QString [optional]
    * @param[in]  vendor_mac QString [optional]
    */
    virtual void apiV1VendorsCreate(const QString &vendor_name, const ::OpenAPI::OptionalParam<QString> &vendor_info = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &vendor_url = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &vendor_mac = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  vendor_name QString [optional]
    * @param[in]  vendor_info QString [optional]
    * @param[in]  vendor_url QString [optional]
    * @param[in]  vendor_mac QString [optional]
    */
    virtual void apiV1VendorsIdJsonPatch(const QString &id, const ::OpenAPI::OptionalParam<QString> &vendor_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &vendor_info = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &vendor_url = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &vendor_mac = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  vendor_name QString [optional]
    * @param[in]  vendor_info QString [optional]
    * @param[in]  vendor_url QString [optional]
    * @param[in]  vendor_mac QString [optional]
    */
    virtual void apiV1VendorsIdJsonPut(const QString &id, const ::OpenAPI::OptionalParam<QString> &vendor_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &vendor_info = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &vendor_url = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &vendor_mac = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  page qint32 [optional]
    * @param[in]  order QString [optional]
    */
    virtual void apiV1VendorsIndex(const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &order = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  order QString [optional]
    */
    virtual void apiV1VendorsShow(const QString &id, const ::OpenAPI::OptionalParam<QString> &order = ::OpenAPI::OptionalParam<QString>());


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

    void apiV1VendorsCreateCallback(OAIHttpRequestWorker *worker);
    void apiV1VendorsIdJsonPatchCallback(OAIHttpRequestWorker *worker);
    void apiV1VendorsIdJsonPutCallback(OAIHttpRequestWorker *worker);
    void apiV1VendorsIndexCallback(OAIHttpRequestWorker *worker);
    void apiV1VendorsShowCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void apiV1VendorsCreateSignal();
    void apiV1VendorsIdJsonPatchSignal();
    void apiV1VendorsIdJsonPutSignal();
    void apiV1VendorsIndexSignal();
    void apiV1VendorsShowSignal();


    void apiV1VendorsCreateSignalFull(OAIHttpRequestWorker *worker);
    void apiV1VendorsIdJsonPatchSignalFull(OAIHttpRequestWorker *worker);
    void apiV1VendorsIdJsonPutSignalFull(OAIHttpRequestWorker *worker);
    void apiV1VendorsIndexSignalFull(OAIHttpRequestWorker *worker);
    void apiV1VendorsShowSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use apiV1VendorsCreateSignalError() instead")
    void apiV1VendorsCreateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1VendorsCreateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1VendorsIdJsonPatchSignalError() instead")
    void apiV1VendorsIdJsonPatchSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1VendorsIdJsonPatchSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1VendorsIdJsonPutSignalError() instead")
    void apiV1VendorsIdJsonPutSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1VendorsIdJsonPutSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1VendorsIndexSignalError() instead")
    void apiV1VendorsIndexSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1VendorsIndexSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1VendorsShowSignalError() instead")
    void apiV1VendorsShowSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1VendorsShowSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use apiV1VendorsCreateSignalErrorFull() instead")
    void apiV1VendorsCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1VendorsCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1VendorsIdJsonPatchSignalErrorFull() instead")
    void apiV1VendorsIdJsonPatchSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1VendorsIdJsonPatchSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1VendorsIdJsonPutSignalErrorFull() instead")
    void apiV1VendorsIdJsonPutSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1VendorsIdJsonPutSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1VendorsIndexSignalErrorFull() instead")
    void apiV1VendorsIndexSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1VendorsIndexSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1VendorsShowSignalErrorFull() instead")
    void apiV1VendorsShowSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1VendorsShowSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
