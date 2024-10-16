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

#ifndef OAI_OAIUserContentDefinitionsApi_H
#define OAI_OAIUserContentDefinitionsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIAPI_Models_ApiError.h"
#include "OAIAPI_PagedResponse_ContentSubmission_Shared_BusinessEntities_UserContentDefinition_.h"
#include "OAIContentSubmission_Shared_BusinessEntities_UserContentDefinition.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIUserContentDefinitionsApi : public QObject {
    Q_OBJECT

public:
    OAIUserContentDefinitionsApi(const int timeOut = 0);
    ~OAIUserContentDefinitionsApi();

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
    * @param[in]  user_content_definition_id qint32 [required]
    */
    virtual void userContentDefinitionsDeleteUserContentDefinition(const qint32 &user_content_definition_id);

    /**
    * @param[in]  user_content_definition_id qint32 [required]
    */
    virtual void userContentDefinitionsGetUserContentDefinition(const qint32 &user_content_definition_id);

    /**
    * @param[in]  limit qint32 [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  user_id qint32 [optional]
    * @param[in]  content_definition_id qint32 [optional]
    */
    virtual void userContentDefinitionsGetUserContentDefinitions(const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &user_id = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &content_definition_id = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  oai_content_submission_shared_business_entities_user_content_definition OAIContentSubmission_Shared_BusinessEntities_UserContentDefinition [required]
    */
    virtual void userContentDefinitionsPostUserContentDefinition(const OAIContentSubmission_Shared_BusinessEntities_UserContentDefinition &oai_content_submission_shared_business_entities_user_content_definition);


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

    void userContentDefinitionsDeleteUserContentDefinitionCallback(OAIHttpRequestWorker *worker);
    void userContentDefinitionsGetUserContentDefinitionCallback(OAIHttpRequestWorker *worker);
    void userContentDefinitionsGetUserContentDefinitionsCallback(OAIHttpRequestWorker *worker);
    void userContentDefinitionsPostUserContentDefinitionCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void userContentDefinitionsDeleteUserContentDefinitionSignal();
    void userContentDefinitionsGetUserContentDefinitionSignal(OAIContentSubmission_Shared_BusinessEntities_UserContentDefinition summary);
    void userContentDefinitionsGetUserContentDefinitionsSignal(OAIAPI_PagedResponse_ContentSubmission_Shared_BusinessEntities_UserContentDefinition_ summary);
    void userContentDefinitionsPostUserContentDefinitionSignal(qint32 summary);


    void userContentDefinitionsDeleteUserContentDefinitionSignalFull(OAIHttpRequestWorker *worker);
    void userContentDefinitionsGetUserContentDefinitionSignalFull(OAIHttpRequestWorker *worker, OAIContentSubmission_Shared_BusinessEntities_UserContentDefinition summary);
    void userContentDefinitionsGetUserContentDefinitionsSignalFull(OAIHttpRequestWorker *worker, OAIAPI_PagedResponse_ContentSubmission_Shared_BusinessEntities_UserContentDefinition_ summary);
    void userContentDefinitionsPostUserContentDefinitionSignalFull(OAIHttpRequestWorker *worker, qint32 summary);

    Q_DECL_DEPRECATED_X("Use userContentDefinitionsDeleteUserContentDefinitionSignalError() instead")
    void userContentDefinitionsDeleteUserContentDefinitionSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void userContentDefinitionsDeleteUserContentDefinitionSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use userContentDefinitionsGetUserContentDefinitionSignalError() instead")
    void userContentDefinitionsGetUserContentDefinitionSignalE(OAIContentSubmission_Shared_BusinessEntities_UserContentDefinition summary, QNetworkReply::NetworkError error_type, QString error_str);
    void userContentDefinitionsGetUserContentDefinitionSignalError(OAIContentSubmission_Shared_BusinessEntities_UserContentDefinition summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use userContentDefinitionsGetUserContentDefinitionsSignalError() instead")
    void userContentDefinitionsGetUserContentDefinitionsSignalE(OAIAPI_PagedResponse_ContentSubmission_Shared_BusinessEntities_UserContentDefinition_ summary, QNetworkReply::NetworkError error_type, QString error_str);
    void userContentDefinitionsGetUserContentDefinitionsSignalError(OAIAPI_PagedResponse_ContentSubmission_Shared_BusinessEntities_UserContentDefinition_ summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use userContentDefinitionsPostUserContentDefinitionSignalError() instead")
    void userContentDefinitionsPostUserContentDefinitionSignalE(qint32 summary, QNetworkReply::NetworkError error_type, QString error_str);
    void userContentDefinitionsPostUserContentDefinitionSignalError(qint32 summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use userContentDefinitionsDeleteUserContentDefinitionSignalErrorFull() instead")
    void userContentDefinitionsDeleteUserContentDefinitionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void userContentDefinitionsDeleteUserContentDefinitionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use userContentDefinitionsGetUserContentDefinitionSignalErrorFull() instead")
    void userContentDefinitionsGetUserContentDefinitionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void userContentDefinitionsGetUserContentDefinitionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use userContentDefinitionsGetUserContentDefinitionsSignalErrorFull() instead")
    void userContentDefinitionsGetUserContentDefinitionsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void userContentDefinitionsGetUserContentDefinitionsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use userContentDefinitionsPostUserContentDefinitionSignalErrorFull() instead")
    void userContentDefinitionsPostUserContentDefinitionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void userContentDefinitionsPostUserContentDefinitionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
