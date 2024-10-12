/**
 * Otoroshi Admin API
 * Admin API of the Otoroshi reverse proxy
 *
 * The version of the OpenAPI document: 1.5.0-dev
 * Contact: oss@maif.fr
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIGroupsApi_H
#define OAI_OAIGroupsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIDeleted.h"
#include "OAIGroup.h"
#include "OAIPatch_inner.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIGroupsApi : public QObject {
    Q_OBJECT

public:
    OAIGroupsApi(const int timeOut = 0);
    ~OAIGroupsApi();

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


    virtual void allServiceGroups();

    /**
    * @param[in]  oai_group OAIGroup [optional]
    */
    virtual void createGroup(const ::OpenAPI::OptionalParam<OAIGroup> &oai_group = ::OpenAPI::OptionalParam<OAIGroup>());

    /**
    * @param[in]  service_group_id QString [required]
    */
    virtual void deleteGroup(const QString &service_group_id);

    /**
    * @param[in]  service_group_id QString [required]
    * @param[in]  oai_patch_inner QList<OAIPatch_inner> [optional]
    */
    virtual void patchGroup(const QString &service_group_id, const ::OpenAPI::OptionalParam<QList<OAIPatch_inner>> &oai_patch_inner = ::OpenAPI::OptionalParam<QList<OAIPatch_inner>>());

    /**
    * @param[in]  service_group_id QString [required]
    */
    virtual void serviceGroup(const QString &service_group_id);

    /**
    * @param[in]  service_group_id QString [required]
    * @param[in]  oai_group OAIGroup [optional]
    */
    virtual void updateGroup(const QString &service_group_id, const ::OpenAPI::OptionalParam<OAIGroup> &oai_group = ::OpenAPI::OptionalParam<OAIGroup>());


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

    void allServiceGroupsCallback(OAIHttpRequestWorker *worker);
    void createGroupCallback(OAIHttpRequestWorker *worker);
    void deleteGroupCallback(OAIHttpRequestWorker *worker);
    void patchGroupCallback(OAIHttpRequestWorker *worker);
    void serviceGroupCallback(OAIHttpRequestWorker *worker);
    void updateGroupCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void allServiceGroupsSignal(QList<OAIGroup> summary);
    void createGroupSignal(OAIGroup summary);
    void deleteGroupSignal(OAIDeleted summary);
    void patchGroupSignal(OAIGroup summary);
    void serviceGroupSignal(OAIGroup summary);
    void updateGroupSignal(OAIGroup summary);


    void allServiceGroupsSignalFull(OAIHttpRequestWorker *worker, QList<OAIGroup> summary);
    void createGroupSignalFull(OAIHttpRequestWorker *worker, OAIGroup summary);
    void deleteGroupSignalFull(OAIHttpRequestWorker *worker, OAIDeleted summary);
    void patchGroupSignalFull(OAIHttpRequestWorker *worker, OAIGroup summary);
    void serviceGroupSignalFull(OAIHttpRequestWorker *worker, OAIGroup summary);
    void updateGroupSignalFull(OAIHttpRequestWorker *worker, OAIGroup summary);

    Q_DECL_DEPRECATED_X("Use allServiceGroupsSignalError() instead")
    void allServiceGroupsSignalE(QList<OAIGroup> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void allServiceGroupsSignalError(QList<OAIGroup> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createGroupSignalError() instead")
    void createGroupSignalE(OAIGroup summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createGroupSignalError(OAIGroup summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteGroupSignalError() instead")
    void deleteGroupSignalE(OAIDeleted summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteGroupSignalError(OAIDeleted summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patchGroupSignalError() instead")
    void patchGroupSignalE(OAIGroup summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patchGroupSignalError(OAIGroup summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serviceGroupSignalError() instead")
    void serviceGroupSignalE(OAIGroup summary, QNetworkReply::NetworkError error_type, QString error_str);
    void serviceGroupSignalError(OAIGroup summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateGroupSignalError() instead")
    void updateGroupSignalE(OAIGroup summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateGroupSignalError(OAIGroup summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use allServiceGroupsSignalErrorFull() instead")
    void allServiceGroupsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void allServiceGroupsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createGroupSignalErrorFull() instead")
    void createGroupSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createGroupSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteGroupSignalErrorFull() instead")
    void deleteGroupSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteGroupSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patchGroupSignalErrorFull() instead")
    void patchGroupSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patchGroupSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serviceGroupSignalErrorFull() instead")
    void serviceGroupSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void serviceGroupSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateGroupSignalErrorFull() instead")
    void updateGroupSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateGroupSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
