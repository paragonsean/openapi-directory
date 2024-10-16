/**
 * Blazemeter API Explorer
 * Live API Documentation
 *
 * The version of the OpenAPI document: 4
 * Contact: support@blazemeter.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIUserApi_H
#define OAI_OAIUserApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIObject.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIUserApi : public QObject {
    Q_OBJECT

public:
    OAIUserApi(const int timeOut = 0);
    ~OAIUserApi();

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


    virtual void activeSessions();

    /**
    * @param[in]  blazemeter_routing_v4_user_model5 OAIObject [optional]
    */
    virtual void panicTerminate(const ::OpenAPI::OptionalParam<OAIObject> &blazemeter_routing_v4_user_model5 = ::OpenAPI::OptionalParam<OAIObject>());

    /**
    * @param[in]  blazemeter_routing_v4_user_model4 OAIObject [required]
    */
    virtual void r_register(const OAIObject &blazemeter_routing_v4_user_model4);

    /**
    * @param[in]  email QString [required]
    * @param[in]  password QString [required]
    * @param[in]  first_name QString [optional]
    * @param[in]  last_name QString [optional]
    */
    virtual void registerRetrieve(const QString &email, const QString &password, const ::OpenAPI::OptionalParam<QString> &first_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &last_name = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  skip QString [optional]
    * @param[in]  limit QString [optional]
    */
    virtual void retrieveCollections(const ::OpenAPI::OptionalParam<QString> &skip = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &limit = ::OpenAPI::OptionalParam<QString>());


    virtual void retrieveInvites();


    virtual void retrieveLocations();

    /**
    * @param[in]  skip qint64 [optional]
    * @param[in]  limit qint64 [optional]
    */
    virtual void retrieveMasters(const ::OpenAPI::OptionalParam<qint64> &skip = ::OpenAPI::OptionalParam<qint64>(), const ::OpenAPI::OptionalParam<qint64> &limit = ::OpenAPI::OptionalParam<qint64>());


    virtual void retrieveProjects();

    /**
    * @param[in]  skip QString [optional]
    * @param[in]  limit QString [optional]
    */
    virtual void retrieveTests(const ::OpenAPI::OptionalParam<QString> &skip = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &limit = ::OpenAPI::OptionalParam<QString>());


    virtual void top();

    /**
    * @param[in]  blazemeter_routing_v4_user_model1 OAIObject [required]
    */
    virtual void userPasswordPatch(const OAIObject &blazemeter_routing_v4_user_model1);

    /**
    * @param[in]  blazemeter_routing_v4_user_model3 OAIObject [required]
    */
    virtual void userPasswordPost(const OAIObject &blazemeter_routing_v4_user_model3);

    /**
    * @param[in]  blazemeter_routing_v4_user_model2 OAIObject [required]
    */
    virtual void userPasswordPut(const OAIObject &blazemeter_routing_v4_user_model2);


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

    void activeSessionsCallback(OAIHttpRequestWorker *worker);
    void panicTerminateCallback(OAIHttpRequestWorker *worker);
    void r_registerCallback(OAIHttpRequestWorker *worker);
    void registerRetrieveCallback(OAIHttpRequestWorker *worker);
    void retrieveCollectionsCallback(OAIHttpRequestWorker *worker);
    void retrieveInvitesCallback(OAIHttpRequestWorker *worker);
    void retrieveLocationsCallback(OAIHttpRequestWorker *worker);
    void retrieveMastersCallback(OAIHttpRequestWorker *worker);
    void retrieveProjectsCallback(OAIHttpRequestWorker *worker);
    void retrieveTestsCallback(OAIHttpRequestWorker *worker);
    void topCallback(OAIHttpRequestWorker *worker);
    void userPasswordPatchCallback(OAIHttpRequestWorker *worker);
    void userPasswordPostCallback(OAIHttpRequestWorker *worker);
    void userPasswordPutCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void activeSessionsSignal(OAIObject summary);
    void panicTerminateSignal(OAIObject summary);
    void r_registerSignal(OAIObject summary);
    void registerRetrieveSignal(OAIObject summary);
    void retrieveCollectionsSignal(OAIObject summary);
    void retrieveInvitesSignal(QList<QString> summary);
    void retrieveLocationsSignal(OAIObject summary);
    void retrieveMastersSignal(OAIObject summary);
    void retrieveProjectsSignal(OAIObject summary);
    void retrieveTestsSignal(OAIObject summary);
    void topSignal(QList<QString> summary);
    void userPasswordPatchSignal(OAIObject summary);
    void userPasswordPostSignal(OAIObject summary);
    void userPasswordPutSignal(OAIObject summary);


    void activeSessionsSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void panicTerminateSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void r_registerSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void registerRetrieveSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void retrieveCollectionsSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void retrieveInvitesSignalFull(OAIHttpRequestWorker *worker, QList<QString> summary);
    void retrieveLocationsSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void retrieveMastersSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void retrieveProjectsSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void retrieveTestsSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void topSignalFull(OAIHttpRequestWorker *worker, QList<QString> summary);
    void userPasswordPatchSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void userPasswordPostSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void userPasswordPutSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);

    Q_DECL_DEPRECATED_X("Use activeSessionsSignalError() instead")
    void activeSessionsSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void activeSessionsSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use panicTerminateSignalError() instead")
    void panicTerminateSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void panicTerminateSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use r_registerSignalError() instead")
    void r_registerSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void r_registerSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use registerRetrieveSignalError() instead")
    void registerRetrieveSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void registerRetrieveSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use retrieveCollectionsSignalError() instead")
    void retrieveCollectionsSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void retrieveCollectionsSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use retrieveInvitesSignalError() instead")
    void retrieveInvitesSignalE(QList<QString> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void retrieveInvitesSignalError(QList<QString> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use retrieveLocationsSignalError() instead")
    void retrieveLocationsSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void retrieveLocationsSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use retrieveMastersSignalError() instead")
    void retrieveMastersSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void retrieveMastersSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use retrieveProjectsSignalError() instead")
    void retrieveProjectsSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void retrieveProjectsSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use retrieveTestsSignalError() instead")
    void retrieveTestsSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void retrieveTestsSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use topSignalError() instead")
    void topSignalE(QList<QString> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void topSignalError(QList<QString> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use userPasswordPatchSignalError() instead")
    void userPasswordPatchSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void userPasswordPatchSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use userPasswordPostSignalError() instead")
    void userPasswordPostSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void userPasswordPostSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use userPasswordPutSignalError() instead")
    void userPasswordPutSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void userPasswordPutSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use activeSessionsSignalErrorFull() instead")
    void activeSessionsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void activeSessionsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use panicTerminateSignalErrorFull() instead")
    void panicTerminateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void panicTerminateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use r_registerSignalErrorFull() instead")
    void r_registerSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void r_registerSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use registerRetrieveSignalErrorFull() instead")
    void registerRetrieveSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void registerRetrieveSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use retrieveCollectionsSignalErrorFull() instead")
    void retrieveCollectionsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void retrieveCollectionsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use retrieveInvitesSignalErrorFull() instead")
    void retrieveInvitesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void retrieveInvitesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use retrieveLocationsSignalErrorFull() instead")
    void retrieveLocationsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void retrieveLocationsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use retrieveMastersSignalErrorFull() instead")
    void retrieveMastersSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void retrieveMastersSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use retrieveProjectsSignalErrorFull() instead")
    void retrieveProjectsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void retrieveProjectsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use retrieveTestsSignalErrorFull() instead")
    void retrieveTestsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void retrieveTestsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use topSignalErrorFull() instead")
    void topSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void topSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use userPasswordPatchSignalErrorFull() instead")
    void userPasswordPatchSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void userPasswordPatchSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use userPasswordPostSignalErrorFull() instead")
    void userPasswordPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void userPasswordPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use userPasswordPutSignalErrorFull() instead")
    void userPasswordPutSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void userPasswordPutSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
