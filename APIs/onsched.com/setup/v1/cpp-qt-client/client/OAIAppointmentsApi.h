/**
 * OnSched Setup API
 * Build secure and scalable custom apps for onboarding and setup. Our flexible API provides many options for configuration.  <br><br>  Take the API for a test drive. Just click on the Authorize button below and authenticate.   You can access our demo company profile if you are not a customer, or your own profile by using your assigned ClientId and Secret.  <br><br>  The API has two interfaces, consumer and setup.   <ul>  <li>  The consumer interface provides all the endpoints required for implementing consumer booking flows.  </li>  <li>  The setup interface provides endpoints for profile configuration and setup.  </li>  </ul>  Toggle freely between the two interfaces using the swagger tool bar option labelled 'Select a definition'.  
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIAppointmentsApi_H
#define OAI_OAIAppointmentsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIAppointmentListViewModel.h"
#include "OAIAppointmentViewModel.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIAppointmentsApi : public QObject {
    Q_OBJECT

public:
    OAIAppointmentsApi(const int timeOut = 0);
    ~OAIAppointmentsApi();

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
    * @param[in]  email QString [optional]
    * @param[in]  lastname QString [optional]
    * @param[in]  service_id QString [optional]
    * @param[in]  calendar_id QString [optional]
    * @param[in]  resource_id QString [optional]
    * @param[in]  customer_id QString [optional]
    * @param[in]  service_allocation_id QString [optional]
    * @param[in]  start_date QDateTime [optional]
    * @param[in]  end_date QDateTime [optional]
    * @param[in]  status QString [optional]
    * @param[in]  booked_by QString [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  limit qint32 [optional]
    */
    virtual void setupV1AppointmentsGet(const ::OpenAPI::OptionalParam<QString> &location_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &email = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &lastname = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &service_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &calendar_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &resource_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &customer_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &service_allocation_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QDateTime> &start_date = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<QDateTime> &end_date = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<QString> &status = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &booked_by = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    */
    virtual void setupV1AppointmentsIdGet(const QString &id);

    /**
    * @param[in]  id QString [required]
    * @param[in]  resource_id QString [required]
    */
    virtual void setupV1AppointmentsIdReassignResourceResourceIdPut(const QString &id, const QString &resource_id);


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

    void setupV1AppointmentsGetCallback(OAIHttpRequestWorker *worker);
    void setupV1AppointmentsIdGetCallback(OAIHttpRequestWorker *worker);
    void setupV1AppointmentsIdReassignResourceResourceIdPutCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void setupV1AppointmentsGetSignal(OAIAppointmentListViewModel summary);
    void setupV1AppointmentsIdGetSignal(OAIAppointmentViewModel summary);
    void setupV1AppointmentsIdReassignResourceResourceIdPutSignal(OAIAppointmentViewModel summary);


    void setupV1AppointmentsGetSignalFull(OAIHttpRequestWorker *worker, OAIAppointmentListViewModel summary);
    void setupV1AppointmentsIdGetSignalFull(OAIHttpRequestWorker *worker, OAIAppointmentViewModel summary);
    void setupV1AppointmentsIdReassignResourceResourceIdPutSignalFull(OAIHttpRequestWorker *worker, OAIAppointmentViewModel summary);

    Q_DECL_DEPRECATED_X("Use setupV1AppointmentsGetSignalError() instead")
    void setupV1AppointmentsGetSignalE(OAIAppointmentListViewModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1AppointmentsGetSignalError(OAIAppointmentListViewModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1AppointmentsIdGetSignalError() instead")
    void setupV1AppointmentsIdGetSignalE(OAIAppointmentViewModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1AppointmentsIdGetSignalError(OAIAppointmentViewModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1AppointmentsIdReassignResourceResourceIdPutSignalError() instead")
    void setupV1AppointmentsIdReassignResourceResourceIdPutSignalE(OAIAppointmentViewModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1AppointmentsIdReassignResourceResourceIdPutSignalError(OAIAppointmentViewModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use setupV1AppointmentsGetSignalErrorFull() instead")
    void setupV1AppointmentsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1AppointmentsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1AppointmentsIdGetSignalErrorFull() instead")
    void setupV1AppointmentsIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1AppointmentsIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1AppointmentsIdReassignResourceResourceIdPutSignalErrorFull() instead")
    void setupV1AppointmentsIdReassignResourceResourceIdPutSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1AppointmentsIdReassignResourceResourceIdPutSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
