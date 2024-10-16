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

#ifndef OAI_OAIContentReleaseApi_H
#define OAI_OAIContentReleaseApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIAPI_Models_ApiError.h"
#include "OAIAPI_PagedResponse_ContentSubmission_Shared_BusinessEntities_ContentReleaseVersion_.h"
#include "OAIContentSubmission_Shared_BusinessEntities_ContentReleaseVersion.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIContentReleaseApi : public QObject {
    Q_OBJECT

public:
    OAIContentReleaseApi(const int timeOut = 0);
    ~OAIContentReleaseApi();

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
    * @param[in]  content_release_id qint32 [required]
    */
    virtual void apiV2ContentReleasesContentReleaseIdGet(const qint32 &content_release_id);

    /**
    * @param[in]  content_release_id qint32 [required]
    */
    virtual void contentReleaseDeleteContentReleaseVersionn(const qint32 &content_release_id);

    /**
    * @param[in]  limit qint32 [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  deleted bool [optional]
    * @param[in]  release_id qint32 [optional]
    * @param[in]  user_id qint32 [optional]
    * @param[in]  content_definition_id qint32 [optional]
    * @param[in]  version qint32 [optional]
    */
    virtual void contentReleaseGetContentReleaseVersion(const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<bool> &deleted = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<qint32> &release_id = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &user_id = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &content_definition_id = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &version = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  oai_content_submission_shared_business_entities_content_release_version OAIContentSubmission_Shared_BusinessEntities_ContentReleaseVersion [required]
    */
    virtual void contentReleasePostContentRelease(const OAIContentSubmission_Shared_BusinessEntities_ContentReleaseVersion &oai_content_submission_shared_business_entities_content_release_version);

    /**
    * @param[in]  content_release_id qint32 [required]
    * @param[in]  oai_content_submission_shared_business_entities_content_release_version OAIContentSubmission_Shared_BusinessEntities_ContentReleaseVersion [required]
    */
    virtual void contentReleasePutContentDefinition(const qint32 &content_release_id, const OAIContentSubmission_Shared_BusinessEntities_ContentReleaseVersion &oai_content_submission_shared_business_entities_content_release_version);


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

    void apiV2ContentReleasesContentReleaseIdGetCallback(OAIHttpRequestWorker *worker);
    void contentReleaseDeleteContentReleaseVersionnCallback(OAIHttpRequestWorker *worker);
    void contentReleaseGetContentReleaseVersionCallback(OAIHttpRequestWorker *worker);
    void contentReleasePostContentReleaseCallback(OAIHttpRequestWorker *worker);
    void contentReleasePutContentDefinitionCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void apiV2ContentReleasesContentReleaseIdGetSignal(OAIContentSubmission_Shared_BusinessEntities_ContentReleaseVersion summary);
    void contentReleaseDeleteContentReleaseVersionnSignal();
    void contentReleaseGetContentReleaseVersionSignal(OAIAPI_PagedResponse_ContentSubmission_Shared_BusinessEntities_ContentReleaseVersion_ summary);
    void contentReleasePostContentReleaseSignal(qint32 summary);
    void contentReleasePutContentDefinitionSignal();


    void apiV2ContentReleasesContentReleaseIdGetSignalFull(OAIHttpRequestWorker *worker, OAIContentSubmission_Shared_BusinessEntities_ContentReleaseVersion summary);
    void contentReleaseDeleteContentReleaseVersionnSignalFull(OAIHttpRequestWorker *worker);
    void contentReleaseGetContentReleaseVersionSignalFull(OAIHttpRequestWorker *worker, OAIAPI_PagedResponse_ContentSubmission_Shared_BusinessEntities_ContentReleaseVersion_ summary);
    void contentReleasePostContentReleaseSignalFull(OAIHttpRequestWorker *worker, qint32 summary);
    void contentReleasePutContentDefinitionSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use apiV2ContentReleasesContentReleaseIdGetSignalError() instead")
    void apiV2ContentReleasesContentReleaseIdGetSignalE(OAIContentSubmission_Shared_BusinessEntities_ContentReleaseVersion summary, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV2ContentReleasesContentReleaseIdGetSignalError(OAIContentSubmission_Shared_BusinessEntities_ContentReleaseVersion summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use contentReleaseDeleteContentReleaseVersionnSignalError() instead")
    void contentReleaseDeleteContentReleaseVersionnSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void contentReleaseDeleteContentReleaseVersionnSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use contentReleaseGetContentReleaseVersionSignalError() instead")
    void contentReleaseGetContentReleaseVersionSignalE(OAIAPI_PagedResponse_ContentSubmission_Shared_BusinessEntities_ContentReleaseVersion_ summary, QNetworkReply::NetworkError error_type, QString error_str);
    void contentReleaseGetContentReleaseVersionSignalError(OAIAPI_PagedResponse_ContentSubmission_Shared_BusinessEntities_ContentReleaseVersion_ summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use contentReleasePostContentReleaseSignalError() instead")
    void contentReleasePostContentReleaseSignalE(qint32 summary, QNetworkReply::NetworkError error_type, QString error_str);
    void contentReleasePostContentReleaseSignalError(qint32 summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use contentReleasePutContentDefinitionSignalError() instead")
    void contentReleasePutContentDefinitionSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void contentReleasePutContentDefinitionSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use apiV2ContentReleasesContentReleaseIdGetSignalErrorFull() instead")
    void apiV2ContentReleasesContentReleaseIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV2ContentReleasesContentReleaseIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use contentReleaseDeleteContentReleaseVersionnSignalErrorFull() instead")
    void contentReleaseDeleteContentReleaseVersionnSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void contentReleaseDeleteContentReleaseVersionnSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use contentReleaseGetContentReleaseVersionSignalErrorFull() instead")
    void contentReleaseGetContentReleaseVersionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void contentReleaseGetContentReleaseVersionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use contentReleasePostContentReleaseSignalErrorFull() instead")
    void contentReleasePostContentReleaseSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void contentReleasePostContentReleaseSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use contentReleasePutContentDefinitionSignalErrorFull() instead")
    void contentReleasePutContentDefinitionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void contentReleasePutContentDefinitionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
