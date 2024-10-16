/**
 * OnSched Consumer API
 * Build secure and scalable custom apps for Online Booking. Our flexible API provides many options for availability and booking.  <br><br>  Take the API for a test drive. Just click on the Authorize button below and authenticate.   You can access our demo company profile if you are not a customer, or your own profile by using your assigned ClientId and Secret.  <br><br>  The API has two interfaces, consumer and setup.   <ul>  <li>  The consumer interface provides all the endpoints required for implementing consumer booking flows.  </li>  <li>  The setup interface provides endpoints for profile configuration and setup.  </li>  </ul>  Toggle freely between the two interfaces using the swagger tool bar option labelled 'Select a definition'.  
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIResourceGroupsApi_H
#define OAI_OAIResourceGroupsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIResourceGroupListViewModel.h"
#include "OAIResourceGroupViewModel.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIResourceGroupsApi : public QObject {
    Q_OBJECT

public:
    OAIResourceGroupsApi(const int timeOut = 0);
    ~OAIResourceGroupsApi();

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
    * @param[in]  location_id QString [optional]
    * @param[in]  deleted bool [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  limit qint32 [optional]
    */
    virtual void consumerV1ResourcegroupsGet(const ::OpenAPI::OptionalParam<QString> &location_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &deleted = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    */
    virtual void consumerV1ResourcegroupsIdGet(const QString &id);


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

    void consumerV1ResourcegroupsGetCallback(OAIHttpRequestWorker *worker);
    void consumerV1ResourcegroupsIdGetCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void consumerV1ResourcegroupsGetSignal(OAIResourceGroupListViewModel summary);
    void consumerV1ResourcegroupsIdGetSignal(OAIResourceGroupViewModel summary);


    void consumerV1ResourcegroupsGetSignalFull(OAIHttpRequestWorker *worker, OAIResourceGroupListViewModel summary);
    void consumerV1ResourcegroupsIdGetSignalFull(OAIHttpRequestWorker *worker, OAIResourceGroupViewModel summary);

    Q_DECL_DEPRECATED_X("Use consumerV1ResourcegroupsGetSignalError() instead")
    void consumerV1ResourcegroupsGetSignalE(OAIResourceGroupListViewModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void consumerV1ResourcegroupsGetSignalError(OAIResourceGroupListViewModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use consumerV1ResourcegroupsIdGetSignalError() instead")
    void consumerV1ResourcegroupsIdGetSignalE(OAIResourceGroupViewModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void consumerV1ResourcegroupsIdGetSignalError(OAIResourceGroupViewModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use consumerV1ResourcegroupsGetSignalErrorFull() instead")
    void consumerV1ResourcegroupsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void consumerV1ResourcegroupsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use consumerV1ResourcegroupsIdGetSignalErrorFull() instead")
    void consumerV1ResourcegroupsIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void consumerV1ResourcegroupsIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
