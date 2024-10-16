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

#ifndef OAI_OAIStringDefinitionsApi_H
#define OAI_OAIStringDefinitionsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIAPI_IPagedResponse_GlobalResources_Shared_Models_StringDefinition_.h"
#include "OAIAPI_Models_ApiError.h"
#include "OAIGlobalResources_Shared_Models_StringDefinition.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIStringDefinitionsApi : public QObject {
    Q_OBJECT

public:
    OAIStringDefinitionsApi(const int timeOut = 0);
    ~OAIStringDefinitionsApi();

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
    * @param[in]  include_translations bool [optional]
    * @param[in]  include_deleted_languages bool [optional]
    * @param[in]  language_ids QString [optional]
    */
    virtual void stringDefinitionsGetDefinition(const QString &id, const ::OpenAPI::OptionalParam<bool> &include_translations = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<bool> &include_deleted_languages = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &language_ids = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  limit qint32 [optional]
    * @param[in]  modified_after_timestamp QString [optional]
    * @param[in]  include_translations bool [optional]
    * @param[in]  string_text QString [optional]
    * @param[in]  description_text QString [optional]
    * @param[in]  use_full_text bool [optional]
    * @param[in]  include_deleted_languages bool [optional]
    * @param[in]  language_ids QString [optional]
    * @param[in]  string_ids QString [optional]
    * @param[in]  matching_translations_only bool [optional]
    */
    virtual void stringDefinitionsGetDefinitions(const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &modified_after_timestamp = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &include_translations = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &string_text = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &description_text = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &use_full_text = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<bool> &include_deleted_languages = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &language_ids = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &string_ids = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &matching_translations_only = ::OpenAPI::OptionalParam<bool>());

    /**
    * @param[in]  oai_global_resources_shared_models_string_definition QList<OAIGlobalResources_Shared_Models_StringDefinition> [required]
    */
    virtual void stringDefinitionsPostDefinition(const QList<OAIGlobalResources_Shared_Models_StringDefinition> &oai_global_resources_shared_models_string_definition);

    /**
    * @param[in]  oai_global_resources_shared_models_string_definition QList<OAIGlobalResources_Shared_Models_StringDefinition> [required]
    */
    virtual void stringDefinitionsUpdateDefinitions(const QList<OAIGlobalResources_Shared_Models_StringDefinition> &oai_global_resources_shared_models_string_definition);


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

    void stringDefinitionsGetDefinitionCallback(OAIHttpRequestWorker *worker);
    void stringDefinitionsGetDefinitionsCallback(OAIHttpRequestWorker *worker);
    void stringDefinitionsPostDefinitionCallback(OAIHttpRequestWorker *worker);
    void stringDefinitionsUpdateDefinitionsCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void stringDefinitionsGetDefinitionSignal(OAIGlobalResources_Shared_Models_StringDefinition summary);
    void stringDefinitionsGetDefinitionsSignal(OAIAPI_IPagedResponse_GlobalResources_Shared_Models_StringDefinition_ summary);
    void stringDefinitionsPostDefinitionSignal();
    void stringDefinitionsUpdateDefinitionsSignal();


    void stringDefinitionsGetDefinitionSignalFull(OAIHttpRequestWorker *worker, OAIGlobalResources_Shared_Models_StringDefinition summary);
    void stringDefinitionsGetDefinitionsSignalFull(OAIHttpRequestWorker *worker, OAIAPI_IPagedResponse_GlobalResources_Shared_Models_StringDefinition_ summary);
    void stringDefinitionsPostDefinitionSignalFull(OAIHttpRequestWorker *worker);
    void stringDefinitionsUpdateDefinitionsSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use stringDefinitionsGetDefinitionSignalError() instead")
    void stringDefinitionsGetDefinitionSignalE(OAIGlobalResources_Shared_Models_StringDefinition summary, QNetworkReply::NetworkError error_type, QString error_str);
    void stringDefinitionsGetDefinitionSignalError(OAIGlobalResources_Shared_Models_StringDefinition summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use stringDefinitionsGetDefinitionsSignalError() instead")
    void stringDefinitionsGetDefinitionsSignalE(OAIAPI_IPagedResponse_GlobalResources_Shared_Models_StringDefinition_ summary, QNetworkReply::NetworkError error_type, QString error_str);
    void stringDefinitionsGetDefinitionsSignalError(OAIAPI_IPagedResponse_GlobalResources_Shared_Models_StringDefinition_ summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use stringDefinitionsPostDefinitionSignalError() instead")
    void stringDefinitionsPostDefinitionSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void stringDefinitionsPostDefinitionSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use stringDefinitionsUpdateDefinitionsSignalError() instead")
    void stringDefinitionsUpdateDefinitionsSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void stringDefinitionsUpdateDefinitionsSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use stringDefinitionsGetDefinitionSignalErrorFull() instead")
    void stringDefinitionsGetDefinitionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void stringDefinitionsGetDefinitionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use stringDefinitionsGetDefinitionsSignalErrorFull() instead")
    void stringDefinitionsGetDefinitionsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void stringDefinitionsGetDefinitionsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use stringDefinitionsPostDefinitionSignalErrorFull() instead")
    void stringDefinitionsPostDefinitionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void stringDefinitionsPostDefinitionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use stringDefinitionsUpdateDefinitionsSignalErrorFull() instead")
    void stringDefinitionsUpdateDefinitionsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void stringDefinitionsUpdateDefinitionsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
