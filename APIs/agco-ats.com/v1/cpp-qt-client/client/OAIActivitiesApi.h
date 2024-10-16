/**
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIActivitiesApi_H
#define OAI_OAIActivitiesApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIAPI_Models_ApiError.h"
#include "OAIAPI_PagedResponse_BuildSystem_Shared_DTO_Activity_.h"
#include "OAIBuildSystem_Shared_DTO_Activity.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIActivitiesApi : public QObject {
    Q_OBJECT

public:
    OAIActivitiesApi(const int timeOut = 0);
    ~OAIActivitiesApi();

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
    * @param[in]  activity_id qint32 [required]
    */
    virtual void activitiesDeleteActivity(const qint32 &activity_id);

    /**
    * @param[in]  limit qint32 [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  is_include_deleted bool [optional]
    */
    virtual void activitiesGetActivities(const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<bool> &is_include_deleted = ::OpenAPI::OptionalParam<bool>());

    /**
    * @param[in]  activity_id qint32 [required]
    * @param[in]  is_include_deleted bool [optional]
    */
    virtual void activitiesGetActivity(const qint32 &activity_id, const ::OpenAPI::OptionalParam<bool> &is_include_deleted = ::OpenAPI::OptionalParam<bool>());

    /**
    * @param[in]  oai_build_system_shared_dto_activity OAIBuildSystem_Shared_DTO_Activity [required]
    */
    virtual void activitiesPostActivity(const OAIBuildSystem_Shared_DTO_Activity &oai_build_system_shared_dto_activity);

    /**
    * @param[in]  activity_id qint32 [required]
    * @param[in]  oai_build_system_shared_dto_activity OAIBuildSystem_Shared_DTO_Activity [required]
    */
    virtual void activitiesPutActivity(const qint32 &activity_id, const OAIBuildSystem_Shared_DTO_Activity &oai_build_system_shared_dto_activity);


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

    void activitiesDeleteActivityCallback(OAIHttpRequestWorker *worker);
    void activitiesGetActivitiesCallback(OAIHttpRequestWorker *worker);
    void activitiesGetActivityCallback(OAIHttpRequestWorker *worker);
    void activitiesPostActivityCallback(OAIHttpRequestWorker *worker);
    void activitiesPutActivityCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void activitiesDeleteActivitySignal();
    void activitiesGetActivitiesSignal(OAIAPI_PagedResponse_BuildSystem_Shared_DTO_Activity_ summary);
    void activitiesGetActivitySignal(OAIBuildSystem_Shared_DTO_Activity summary);
    void activitiesPostActivitySignal(qint32 summary);
    void activitiesPutActivitySignal();


    void activitiesDeleteActivitySignalFull(OAIHttpRequestWorker *worker);
    void activitiesGetActivitiesSignalFull(OAIHttpRequestWorker *worker, OAIAPI_PagedResponse_BuildSystem_Shared_DTO_Activity_ summary);
    void activitiesGetActivitySignalFull(OAIHttpRequestWorker *worker, OAIBuildSystem_Shared_DTO_Activity summary);
    void activitiesPostActivitySignalFull(OAIHttpRequestWorker *worker, qint32 summary);
    void activitiesPutActivitySignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use activitiesDeleteActivitySignalError() instead")
    void activitiesDeleteActivitySignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void activitiesDeleteActivitySignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use activitiesGetActivitiesSignalError() instead")
    void activitiesGetActivitiesSignalE(OAIAPI_PagedResponse_BuildSystem_Shared_DTO_Activity_ summary, QNetworkReply::NetworkError error_type, QString error_str);
    void activitiesGetActivitiesSignalError(OAIAPI_PagedResponse_BuildSystem_Shared_DTO_Activity_ summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use activitiesGetActivitySignalError() instead")
    void activitiesGetActivitySignalE(OAIBuildSystem_Shared_DTO_Activity summary, QNetworkReply::NetworkError error_type, QString error_str);
    void activitiesGetActivitySignalError(OAIBuildSystem_Shared_DTO_Activity summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use activitiesPostActivitySignalError() instead")
    void activitiesPostActivitySignalE(qint32 summary, QNetworkReply::NetworkError error_type, QString error_str);
    void activitiesPostActivitySignalError(qint32 summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use activitiesPutActivitySignalError() instead")
    void activitiesPutActivitySignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void activitiesPutActivitySignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use activitiesDeleteActivitySignalErrorFull() instead")
    void activitiesDeleteActivitySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void activitiesDeleteActivitySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use activitiesGetActivitiesSignalErrorFull() instead")
    void activitiesGetActivitiesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void activitiesGetActivitiesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use activitiesGetActivitySignalErrorFull() instead")
    void activitiesGetActivitySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void activitiesGetActivitySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use activitiesPostActivitySignalErrorFull() instead")
    void activitiesPostActivitySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void activitiesPostActivitySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use activitiesPutActivitySignalErrorFull() instead")
    void activitiesPutActivitySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void activitiesPutActivitySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
