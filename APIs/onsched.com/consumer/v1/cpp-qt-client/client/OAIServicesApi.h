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

#ifndef OAI_OAIServicesApi_H
#define OAI_OAIServicesApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIResourceListViewModel.h"
#include "OAIServiceAllocationListViewModel.h"
#include "OAIServiceAllocationViewModel.h"
#include "OAIServiceListViewModel.h"
#include "OAIServiceSortOrder.h"
#include "OAIServiceViewModel.h"
#include "OAIServicesScope.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIServicesApi : public QObject {
    Q_OBJECT

public:
    OAIServicesApi(const int timeOut = 0);
    ~OAIServicesApi();

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
    virtual void consumerV1ServicesAllocationsIdGet(const QString &id);

    /**
    * @param[in]  location_id QString [optional]
    * @param[in]  service_group_id qint32 [optional]
    * @param[in]  default_service bool [optional]
    * @param[in]  all_locations bool [optional]
    * @param[in]  scope OAIServicesScope [optional]
    * @param[in]  name QString [optional]
    * @param[in]  service_id QString [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  limit qint32 [optional]
    * @param[in]  sort_order OAIServiceSortOrder [optional]
    * @param[in]  sort_descending bool [optional]
    */
    virtual void consumerV1ServicesGet(const ::OpenAPI::OptionalParam<QString> &location_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &service_group_id = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<bool> &default_service = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<bool> &all_locations = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<OAIServicesScope> &scope = ::OpenAPI::OptionalParam<OAIServicesScope>(), const ::OpenAPI::OptionalParam<QString> &name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &service_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<OAIServiceSortOrder> &sort_order = ::OpenAPI::OptionalParam<OAIServiceSortOrder>(), const ::OpenAPI::OptionalParam<bool> &sort_descending = ::OpenAPI::OptionalParam<bool>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  location_id QString [optional]
    * @param[in]  resource_id QString [optional]
    * @param[in]  start_date QDateTime [optional]
    * @param[in]  end_date QDateTime [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  limit qint32 [optional]
    */
    virtual void consumerV1ServicesIdAllocationsGet(const QString &id, const ::OpenAPI::OptionalParam<QString> &location_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &resource_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QDateTime> &start_date = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<QDateTime> &end_date = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id qint32 [required]
    */
    virtual void consumerV1ServicesIdGet(const qint32 &id);

    /**
    * @param[in]  id QString [required]
    * @param[in]  location_id QString [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  limit qint32 [optional]
    */
    virtual void consumerV1ServicesIdResourcesGet(const QString &id, const ::OpenAPI::OptionalParam<QString> &location_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>());


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

    void consumerV1ServicesAllocationsIdGetCallback(OAIHttpRequestWorker *worker);
    void consumerV1ServicesGetCallback(OAIHttpRequestWorker *worker);
    void consumerV1ServicesIdAllocationsGetCallback(OAIHttpRequestWorker *worker);
    void consumerV1ServicesIdGetCallback(OAIHttpRequestWorker *worker);
    void consumerV1ServicesIdResourcesGetCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void consumerV1ServicesAllocationsIdGetSignal(OAIServiceAllocationViewModel summary);
    void consumerV1ServicesGetSignal(OAIServiceListViewModel summary);
    void consumerV1ServicesIdAllocationsGetSignal(OAIServiceAllocationListViewModel summary);
    void consumerV1ServicesIdGetSignal(OAIServiceViewModel summary);
    void consumerV1ServicesIdResourcesGetSignal(OAIResourceListViewModel summary);


    void consumerV1ServicesAllocationsIdGetSignalFull(OAIHttpRequestWorker *worker, OAIServiceAllocationViewModel summary);
    void consumerV1ServicesGetSignalFull(OAIHttpRequestWorker *worker, OAIServiceListViewModel summary);
    void consumerV1ServicesIdAllocationsGetSignalFull(OAIHttpRequestWorker *worker, OAIServiceAllocationListViewModel summary);
    void consumerV1ServicesIdGetSignalFull(OAIHttpRequestWorker *worker, OAIServiceViewModel summary);
    void consumerV1ServicesIdResourcesGetSignalFull(OAIHttpRequestWorker *worker, OAIResourceListViewModel summary);

    Q_DECL_DEPRECATED_X("Use consumerV1ServicesAllocationsIdGetSignalError() instead")
    void consumerV1ServicesAllocationsIdGetSignalE(OAIServiceAllocationViewModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void consumerV1ServicesAllocationsIdGetSignalError(OAIServiceAllocationViewModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use consumerV1ServicesGetSignalError() instead")
    void consumerV1ServicesGetSignalE(OAIServiceListViewModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void consumerV1ServicesGetSignalError(OAIServiceListViewModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use consumerV1ServicesIdAllocationsGetSignalError() instead")
    void consumerV1ServicesIdAllocationsGetSignalE(OAIServiceAllocationListViewModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void consumerV1ServicesIdAllocationsGetSignalError(OAIServiceAllocationListViewModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use consumerV1ServicesIdGetSignalError() instead")
    void consumerV1ServicesIdGetSignalE(OAIServiceViewModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void consumerV1ServicesIdGetSignalError(OAIServiceViewModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use consumerV1ServicesIdResourcesGetSignalError() instead")
    void consumerV1ServicesIdResourcesGetSignalE(OAIResourceListViewModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void consumerV1ServicesIdResourcesGetSignalError(OAIResourceListViewModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use consumerV1ServicesAllocationsIdGetSignalErrorFull() instead")
    void consumerV1ServicesAllocationsIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void consumerV1ServicesAllocationsIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use consumerV1ServicesGetSignalErrorFull() instead")
    void consumerV1ServicesGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void consumerV1ServicesGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use consumerV1ServicesIdAllocationsGetSignalErrorFull() instead")
    void consumerV1ServicesIdAllocationsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void consumerV1ServicesIdAllocationsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use consumerV1ServicesIdGetSignalErrorFull() instead")
    void consumerV1ServicesIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void consumerV1ServicesIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use consumerV1ServicesIdResourcesGetSignalErrorFull() instead")
    void consumerV1ServicesIdResourcesGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void consumerV1ServicesIdResourcesGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
