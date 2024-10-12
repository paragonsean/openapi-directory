/**
 * ConfigCat Public Management API
 * **Base API URL**: https://api.configcat.com  If you prefer the swagger documentation, you can find it here: [Swagger UI](https://api.configcat.com/swagger).  The purpose of this API is to access the ConfigCat platform programmatically.  You can **Create**, **Read**, **Update** and **Delete** any entities like **Feature Flags, Configs, Environments** or **Products** within ConfigCat.   The API is based on HTTP REST, uses resource-oriented URLs, status codes and supports JSON  and JSON+HAL format. Do not use this API for accessing and evaluating feature flag values. Use the [SDKs instead](https://configcat.com/docs/sdk-reference/overview).   # OpenAPI Specification  The complete specification is publicly available here: [swagger.json](v1/swagger.json).  You can use it to generate client libraries in various languages with [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator) or [Swagger Codegen](https://swagger.io/tools/swagger-codegen/) to interact with this API.  # Authentication This API uses the [Basic HTTP Authentication Scheme](https://en.wikipedia.org/wiki/Basic_access_authentication).   <!-- ReDoc-Inject: <security-definitions> -->  # Throttling and rate limits All the rate limited API calls are returning information about the current rate limit period in the following HTTP headers:  | Header | Description | | :- | :- | | X-Rate-Limit-Remaining | The maximum number of requests remaining in the current rate limit period. | | X-Rate-Limit-Reset     | The time when the current rate limit period resets.        |  When the rate limit is exceeded by a request, the API returns with a `HTTP 429 - Too many requests` status along with a `Retry-After` HTTP header. 
 *
 * The version of the OpenAPI document: v1
 * Contact: support@configcat.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIFeatureFlagSettingValuesApi_H
#define OAI_OAIFeatureFlagSettingValuesApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIConfigSettingValuesModel.h"
#include "OAIJsonPatch.h"
#include "OAISettingValueModel.h"
#include "OAISettingValueModel_haljson.h"
#include "OAIUpdateSettingValueModel.h"
#include "OAIUpdateSettingValuesWithIdModel.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIFeatureFlagSettingValuesApi : public QObject {
    Q_OBJECT

public:
    OAIFeatureFlagSettingValuesApi(const int timeOut = 0);
    ~OAIFeatureFlagSettingValuesApi();

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
    * @param[in]  environment_id QString [required]
    * @param[in]  setting_id qint32 [required]
    */
    virtual void getSettingValue(const QString &environment_id, const qint32 &setting_id);

    /**
    * @param[in]  config_id QString [required]
    * @param[in]  environment_id QString [required]
    */
    virtual void getSettingValues(const QString &config_id, const QString &environment_id);

    /**
    * @param[in]  config_id QString [required]
    * @param[in]  environment_id QString [required]
    * @param[in]  oai_update_setting_values_with_id_model OAIUpdateSettingValuesWithIdModel [required]
    * @param[in]  reason QString [optional]
    */
    virtual void postSettingValues(const QString &config_id, const QString &environment_id, const OAIUpdateSettingValuesWithIdModel &oai_update_setting_values_with_id_model, const ::OpenAPI::OptionalParam<QString> &reason = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  environment_id QString [required]
    * @param[in]  setting_id qint32 [required]
    * @param[in]  oai_update_setting_value_model OAIUpdateSettingValueModel [required]
    * @param[in]  reason QString [optional]
    */
    virtual void replaceSettingValue(const QString &environment_id, const qint32 &setting_id, const OAIUpdateSettingValueModel &oai_update_setting_value_model, const ::OpenAPI::OptionalParam<QString> &reason = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  environment_id QString [required]
    * @param[in]  setting_id qint32 [required]
    * @param[in]  oai_json_patch OAIJsonPatch [required]
    * @param[in]  reason QString [optional]
    */
    virtual void updateSettingValue(const QString &environment_id, const qint32 &setting_id, const OAIJsonPatch &oai_json_patch, const ::OpenAPI::OptionalParam<QString> &reason = ::OpenAPI::OptionalParam<QString>());


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

    void getSettingValueCallback(OAIHttpRequestWorker *worker);
    void getSettingValuesCallback(OAIHttpRequestWorker *worker);
    void postSettingValuesCallback(OAIHttpRequestWorker *worker);
    void replaceSettingValueCallback(OAIHttpRequestWorker *worker);
    void updateSettingValueCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void getSettingValueSignal(OAISettingValueModel_haljson summary);
    void getSettingValuesSignal(OAIConfigSettingValuesModel summary);
    void postSettingValuesSignal(OAIConfigSettingValuesModel summary);
    void replaceSettingValueSignal(OAISettingValueModel_haljson summary);
    void updateSettingValueSignal(OAISettingValueModel_haljson summary);


    void getSettingValueSignalFull(OAIHttpRequestWorker *worker, OAISettingValueModel_haljson summary);
    void getSettingValuesSignalFull(OAIHttpRequestWorker *worker, OAIConfigSettingValuesModel summary);
    void postSettingValuesSignalFull(OAIHttpRequestWorker *worker, OAIConfigSettingValuesModel summary);
    void replaceSettingValueSignalFull(OAIHttpRequestWorker *worker, OAISettingValueModel_haljson summary);
    void updateSettingValueSignalFull(OAIHttpRequestWorker *worker, OAISettingValueModel_haljson summary);

    Q_DECL_DEPRECATED_X("Use getSettingValueSignalError() instead")
    void getSettingValueSignalE(OAISettingValueModel_haljson summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getSettingValueSignalError(OAISettingValueModel_haljson summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getSettingValuesSignalError() instead")
    void getSettingValuesSignalE(OAIConfigSettingValuesModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getSettingValuesSignalError(OAIConfigSettingValuesModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postSettingValuesSignalError() instead")
    void postSettingValuesSignalE(OAIConfigSettingValuesModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postSettingValuesSignalError(OAIConfigSettingValuesModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use replaceSettingValueSignalError() instead")
    void replaceSettingValueSignalE(OAISettingValueModel_haljson summary, QNetworkReply::NetworkError error_type, QString error_str);
    void replaceSettingValueSignalError(OAISettingValueModel_haljson summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateSettingValueSignalError() instead")
    void updateSettingValueSignalE(OAISettingValueModel_haljson summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateSettingValueSignalError(OAISettingValueModel_haljson summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use getSettingValueSignalErrorFull() instead")
    void getSettingValueSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getSettingValueSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getSettingValuesSignalErrorFull() instead")
    void getSettingValuesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getSettingValuesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postSettingValuesSignalErrorFull() instead")
    void postSettingValuesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postSettingValuesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use replaceSettingValueSignalErrorFull() instead")
    void replaceSettingValueSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void replaceSettingValueSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateSettingValueSignalErrorFull() instead")
    void updateSettingValueSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateSettingValueSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
