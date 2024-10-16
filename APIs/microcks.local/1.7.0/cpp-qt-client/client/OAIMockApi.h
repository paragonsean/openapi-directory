/**
 * Microcks API v1.7
 * API offered by Microcks, the Kubernetes native tools for API and microservices mocking and testing (microcks.io)
 *
 * The version of the OpenAPI document: 1.7.0
 * Contact: laurent@microcks.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIMockApi_H
#define OAI_OAIMockApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAICounter.h"
#include "OAIGetService_200_response.h"
#include "OAIHttpFileElement.h"
#include "OAIMetadata.h"
#include "OAIOperationOverrideDTO.h"
#include "OAIService.h"
#include <QMap>
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIMockApi : public QObject {
    Q_OBJECT

public:
    OAIMockApi(const int timeOut = 0);
    ~OAIMockApi();

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
    virtual void deleteService(const QString &id);

    /**
    * @param[in]  service_ids QList<QString> [required]
    */
    virtual void exportSnapshot(const QList<QString> &service_ids);

    /**
    * @param[in]  id QString [required]
    * @param[in]  messages bool [optional]
    */
    virtual void getService(const QString &id, const ::OpenAPI::OptionalParam<bool> &messages = ::OpenAPI::OptionalParam<bool>());

    /**
    * @param[in]  page qint32 [optional]
    * @param[in]  size qint32 [optional]
    */
    virtual void getServices(const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &size = ::OpenAPI::OptionalParam<qint32>());


    virtual void getServicesCounter();


    virtual void getServicesLabels();

    /**
    * @param[in]  file OAIHttpFileElement [required]
    */
    virtual void importSnapshot(const OAIHttpFileElement &file);

    /**
    * @param[in]  id QString [required]
    * @param[in]  operation_name QString [required]
    * @param[in]  oai_operation_override_dto OAIOperationOverrideDTO [required]
    */
    virtual void overrideServiceOperation(const QString &id, const QString &operation_name, const OAIOperationOverrideDTO &oai_operation_override_dto);

    /**
    * @param[in]  query_map QMap<QString, QString> [required]
    */
    virtual void searchServices(const QMap<QString, QString> &query_map);

    /**
    * @param[in]  id QString [required]
    * @param[in]  oai_metadata OAIMetadata [required]
    */
    virtual void updateServiceMetadata(const QString &id, const OAIMetadata &oai_metadata);


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

    void deleteServiceCallback(OAIHttpRequestWorker *worker);
    void exportSnapshotCallback(OAIHttpRequestWorker *worker);
    void getServiceCallback(OAIHttpRequestWorker *worker);
    void getServicesCallback(OAIHttpRequestWorker *worker);
    void getServicesCounterCallback(OAIHttpRequestWorker *worker);
    void getServicesLabelsCallback(OAIHttpRequestWorker *worker);
    void importSnapshotCallback(OAIHttpRequestWorker *worker);
    void overrideServiceOperationCallback(OAIHttpRequestWorker *worker);
    void searchServicesCallback(OAIHttpRequestWorker *worker);
    void updateServiceMetadataCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void deleteServiceSignal();
    void exportSnapshotSignal(OAIHttpFileElement summary);
    void getServiceSignal(OAIGetService_200_response summary);
    void getServicesSignal(OAIService summary);
    void getServicesCounterSignal(OAICounter summary);
    void getServicesLabelsSignal(QMap<QString, QList> summary);
    void importSnapshotSignal();
    void overrideServiceOperationSignal();
    void searchServicesSignal(QList<OAIService> summary);
    void updateServiceMetadataSignal();


    void deleteServiceSignalFull(OAIHttpRequestWorker *worker);
    void exportSnapshotSignalFull(OAIHttpRequestWorker *worker, OAIHttpFileElement summary);
    void getServiceSignalFull(OAIHttpRequestWorker *worker, OAIGetService_200_response summary);
    void getServicesSignalFull(OAIHttpRequestWorker *worker, OAIService summary);
    void getServicesCounterSignalFull(OAIHttpRequestWorker *worker, OAICounter summary);
    void getServicesLabelsSignalFull(OAIHttpRequestWorker *worker, QMap<QString, QList> summary);
    void importSnapshotSignalFull(OAIHttpRequestWorker *worker);
    void overrideServiceOperationSignalFull(OAIHttpRequestWorker *worker);
    void searchServicesSignalFull(OAIHttpRequestWorker *worker, QList<OAIService> summary);
    void updateServiceMetadataSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use deleteServiceSignalError() instead")
    void deleteServiceSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void deleteServiceSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use exportSnapshotSignalError() instead")
    void exportSnapshotSignalE(OAIHttpFileElement summary, QNetworkReply::NetworkError error_type, QString error_str);
    void exportSnapshotSignalError(OAIHttpFileElement summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getServiceSignalError() instead")
    void getServiceSignalE(OAIGetService_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getServiceSignalError(OAIGetService_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getServicesSignalError() instead")
    void getServicesSignalE(OAIService summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getServicesSignalError(OAIService summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getServicesCounterSignalError() instead")
    void getServicesCounterSignalE(OAICounter summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getServicesCounterSignalError(OAICounter summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getServicesLabelsSignalError() instead")
    void getServicesLabelsSignalE(QMap<QString, QList> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getServicesLabelsSignalError(QMap<QString, QList> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use importSnapshotSignalError() instead")
    void importSnapshotSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void importSnapshotSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use overrideServiceOperationSignalError() instead")
    void overrideServiceOperationSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void overrideServiceOperationSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use searchServicesSignalError() instead")
    void searchServicesSignalE(QList<OAIService> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void searchServicesSignalError(QList<OAIService> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateServiceMetadataSignalError() instead")
    void updateServiceMetadataSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void updateServiceMetadataSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use deleteServiceSignalErrorFull() instead")
    void deleteServiceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteServiceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use exportSnapshotSignalErrorFull() instead")
    void exportSnapshotSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void exportSnapshotSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getServiceSignalErrorFull() instead")
    void getServiceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getServiceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getServicesSignalErrorFull() instead")
    void getServicesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getServicesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getServicesCounterSignalErrorFull() instead")
    void getServicesCounterSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getServicesCounterSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getServicesLabelsSignalErrorFull() instead")
    void getServicesLabelsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getServicesLabelsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use importSnapshotSignalErrorFull() instead")
    void importSnapshotSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void importSnapshotSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use overrideServiceOperationSignalErrorFull() instead")
    void overrideServiceOperationSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void overrideServiceOperationSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use searchServicesSignalErrorFull() instead")
    void searchServicesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void searchServicesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateServiceMetadataSignalErrorFull() instead")
    void updateServiceMetadataSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateServiceMetadataSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
