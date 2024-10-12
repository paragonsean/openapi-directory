/**
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIGenericobjectApi_H
#define OAI_OAIGenericobjectApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIGenericObject.h"
#include "OAIGenericObjectListResponse.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIGenericobjectApi : public QObject {
    Q_OBJECT

public:
    OAIGenericobjectApi(const int timeOut = 0);
    ~OAIGenericobjectApi();

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
    * @param[in]  resource_id QString [required]
    * @param[in]  _xgafv QString [optional]
    * @param[in]  access_token QString [optional]
    * @param[in]  alt QString [optional]
    * @param[in]  callback QString [optional]
    * @param[in]  fields QString [optional]
    * @param[in]  key QString [optional]
    * @param[in]  oauth_token QString [optional]
    * @param[in]  pretty_print bool [optional]
    * @param[in]  quota_user QString [optional]
    * @param[in]  upload_protocol QString [optional]
    * @param[in]  upload_type QString [optional]
    */
    virtual void walletobjects_genericobject_get(const QString &resource_id, const ::OpenAPI::OptionalParam<QString> &_xgafv = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &access_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &alt = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &callback = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &fields = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &key = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &oauth_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &pretty_print = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &quota_user = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &upload_protocol = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &upload_type = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  _xgafv QString [optional]
    * @param[in]  access_token QString [optional]
    * @param[in]  alt QString [optional]
    * @param[in]  callback QString [optional]
    * @param[in]  fields QString [optional]
    * @param[in]  key QString [optional]
    * @param[in]  oauth_token QString [optional]
    * @param[in]  pretty_print bool [optional]
    * @param[in]  quota_user QString [optional]
    * @param[in]  upload_protocol QString [optional]
    * @param[in]  upload_type QString [optional]
    * @param[in]  oai_generic_object OAIGenericObject [optional]
    */
    virtual void walletobjects_genericobject_insert(const ::OpenAPI::OptionalParam<QString> &_xgafv = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &access_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &alt = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &callback = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &fields = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &key = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &oauth_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &pretty_print = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &quota_user = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &upload_protocol = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &upload_type = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<OAIGenericObject> &oai_generic_object = ::OpenAPI::OptionalParam<OAIGenericObject>());

    /**
    * @param[in]  _xgafv QString [optional]
    * @param[in]  access_token QString [optional]
    * @param[in]  alt QString [optional]
    * @param[in]  callback QString [optional]
    * @param[in]  fields QString [optional]
    * @param[in]  key QString [optional]
    * @param[in]  oauth_token QString [optional]
    * @param[in]  pretty_print bool [optional]
    * @param[in]  quota_user QString [optional]
    * @param[in]  upload_protocol QString [optional]
    * @param[in]  upload_type QString [optional]
    * @param[in]  class_id QString [optional]
    * @param[in]  max_results qint32 [optional]
    * @param[in]  token QString [optional]
    */
    virtual void walletobjects_genericobject_list(const ::OpenAPI::OptionalParam<QString> &_xgafv = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &access_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &alt = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &callback = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &fields = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &key = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &oauth_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &pretty_print = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &quota_user = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &upload_protocol = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &upload_type = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &class_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &max_results = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  resource_id QString [required]
    * @param[in]  _xgafv QString [optional]
    * @param[in]  access_token QString [optional]
    * @param[in]  alt QString [optional]
    * @param[in]  callback QString [optional]
    * @param[in]  fields QString [optional]
    * @param[in]  key QString [optional]
    * @param[in]  oauth_token QString [optional]
    * @param[in]  pretty_print bool [optional]
    * @param[in]  quota_user QString [optional]
    * @param[in]  upload_protocol QString [optional]
    * @param[in]  upload_type QString [optional]
    * @param[in]  oai_generic_object OAIGenericObject [optional]
    */
    virtual void walletobjects_genericobject_patch(const QString &resource_id, const ::OpenAPI::OptionalParam<QString> &_xgafv = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &access_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &alt = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &callback = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &fields = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &key = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &oauth_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &pretty_print = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &quota_user = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &upload_protocol = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &upload_type = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<OAIGenericObject> &oai_generic_object = ::OpenAPI::OptionalParam<OAIGenericObject>());

    /**
    * @param[in]  resource_id QString [required]
    * @param[in]  _xgafv QString [optional]
    * @param[in]  access_token QString [optional]
    * @param[in]  alt QString [optional]
    * @param[in]  callback QString [optional]
    * @param[in]  fields QString [optional]
    * @param[in]  key QString [optional]
    * @param[in]  oauth_token QString [optional]
    * @param[in]  pretty_print bool [optional]
    * @param[in]  quota_user QString [optional]
    * @param[in]  upload_protocol QString [optional]
    * @param[in]  upload_type QString [optional]
    * @param[in]  oai_generic_object OAIGenericObject [optional]
    */
    virtual void walletobjects_genericobject_update(const QString &resource_id, const ::OpenAPI::OptionalParam<QString> &_xgafv = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &access_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &alt = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &callback = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &fields = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &key = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &oauth_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &pretty_print = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &quota_user = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &upload_protocol = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &upload_type = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<OAIGenericObject> &oai_generic_object = ::OpenAPI::OptionalParam<OAIGenericObject>());


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

    void walletobjects_genericobject_getCallback(OAIHttpRequestWorker *worker);
    void walletobjects_genericobject_insertCallback(OAIHttpRequestWorker *worker);
    void walletobjects_genericobject_listCallback(OAIHttpRequestWorker *worker);
    void walletobjects_genericobject_patchCallback(OAIHttpRequestWorker *worker);
    void walletobjects_genericobject_updateCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void walletobjects_genericobject_getSignal(OAIGenericObject summary);
    void walletobjects_genericobject_insertSignal(OAIGenericObject summary);
    void walletobjects_genericobject_listSignal(OAIGenericObjectListResponse summary);
    void walletobjects_genericobject_patchSignal(OAIGenericObject summary);
    void walletobjects_genericobject_updateSignal(OAIGenericObject summary);


    void walletobjects_genericobject_getSignalFull(OAIHttpRequestWorker *worker, OAIGenericObject summary);
    void walletobjects_genericobject_insertSignalFull(OAIHttpRequestWorker *worker, OAIGenericObject summary);
    void walletobjects_genericobject_listSignalFull(OAIHttpRequestWorker *worker, OAIGenericObjectListResponse summary);
    void walletobjects_genericobject_patchSignalFull(OAIHttpRequestWorker *worker, OAIGenericObject summary);
    void walletobjects_genericobject_updateSignalFull(OAIHttpRequestWorker *worker, OAIGenericObject summary);

    Q_DECL_DEPRECATED_X("Use walletobjects_genericobject_getSignalError() instead")
    void walletobjects_genericobject_getSignalE(OAIGenericObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void walletobjects_genericobject_getSignalError(OAIGenericObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use walletobjects_genericobject_insertSignalError() instead")
    void walletobjects_genericobject_insertSignalE(OAIGenericObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void walletobjects_genericobject_insertSignalError(OAIGenericObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use walletobjects_genericobject_listSignalError() instead")
    void walletobjects_genericobject_listSignalE(OAIGenericObjectListResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void walletobjects_genericobject_listSignalError(OAIGenericObjectListResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use walletobjects_genericobject_patchSignalError() instead")
    void walletobjects_genericobject_patchSignalE(OAIGenericObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void walletobjects_genericobject_patchSignalError(OAIGenericObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use walletobjects_genericobject_updateSignalError() instead")
    void walletobjects_genericobject_updateSignalE(OAIGenericObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void walletobjects_genericobject_updateSignalError(OAIGenericObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use walletobjects_genericobject_getSignalErrorFull() instead")
    void walletobjects_genericobject_getSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void walletobjects_genericobject_getSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use walletobjects_genericobject_insertSignalErrorFull() instead")
    void walletobjects_genericobject_insertSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void walletobjects_genericobject_insertSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use walletobjects_genericobject_listSignalErrorFull() instead")
    void walletobjects_genericobject_listSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void walletobjects_genericobject_listSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use walletobjects_genericobject_patchSignalErrorFull() instead")
    void walletobjects_genericobject_patchSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void walletobjects_genericobject_patchSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use walletobjects_genericobject_updateSignalErrorFull() instead")
    void walletobjects_genericobject_updateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void walletobjects_genericobject_updateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
