/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIWebhooksApi_H
#define OAI_OAIWebhooksApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAICreateNetworkWebhooksHttpServer_request.h"
#include "OAICreateNetworkWebhooksPayloadTemplate_request.h"
#include "OAICreateNetworkWebhooksWebhookTest_201_response.h"
#include "OAICreateNetworkWebhooksWebhookTest_request.h"
#include "OAIGetNetworkWebhooksHttpServers_200_response_inner.h"
#include "OAIGetNetworkWebhooksPayloadTemplates_200_response_inner.h"
#include "OAIGetOrganizationWebhooksLogs_200_response_inner.h"
#include "OAIObject.h"
#include "OAIUpdateNetworkWebhooksHttpServer_request.h"
#include "OAIUpdateNetworkWebhooksPayloadTemplate_request.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIWebhooksApi : public QObject {
    Q_OBJECT

public:
    OAIWebhooksApi(const int timeOut = 0);
    ~OAIWebhooksApi();

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
    * @param[in]  network_id QString [required]
    * @param[in]  oai_create_network_webhooks_http_server_request OAICreateNetworkWebhooksHttpServer_request [required]
    */
    virtual void createNetworkWebhooksHttpServer(const QString &network_id, const OAICreateNetworkWebhooksHttpServer_request &oai_create_network_webhooks_http_server_request);

    /**
    * @param[in]  network_id QString [required]
    * @param[in]  oai_create_network_webhooks_payload_template_request OAICreateNetworkWebhooksPayloadTemplate_request [required]
    */
    virtual void createNetworkWebhooksPayloadTemplate(const QString &network_id, const OAICreateNetworkWebhooksPayloadTemplate_request &oai_create_network_webhooks_payload_template_request);

    /**
    * @param[in]  network_id QString [required]
    * @param[in]  oai_create_network_webhooks_webhook_test_request OAICreateNetworkWebhooksWebhookTest_request [required]
    */
    virtual void createNetworkWebhooksWebhookTest(const QString &network_id, const OAICreateNetworkWebhooksWebhookTest_request &oai_create_network_webhooks_webhook_test_request);

    /**
    * @param[in]  network_id QString [required]
    * @param[in]  http_server_id QString [required]
    */
    virtual void deleteNetworkWebhooksHttpServer(const QString &network_id, const QString &http_server_id);

    /**
    * @param[in]  network_id QString [required]
    * @param[in]  payload_template_id QString [required]
    */
    virtual void deleteNetworkWebhooksPayloadTemplate(const QString &network_id, const QString &payload_template_id);

    /**
    * @param[in]  network_id QString [required]
    * @param[in]  http_server_id QString [required]
    */
    virtual void getNetworkWebhooksHttpServer(const QString &network_id, const QString &http_server_id);

    /**
    * @param[in]  network_id QString [required]
    */
    virtual void getNetworkWebhooksHttpServers(const QString &network_id);

    /**
    * @param[in]  network_id QString [required]
    * @param[in]  payload_template_id QString [required]
    */
    virtual void getNetworkWebhooksPayloadTemplate(const QString &network_id, const QString &payload_template_id);

    /**
    * @param[in]  network_id QString [required]
    */
    virtual void getNetworkWebhooksPayloadTemplates(const QString &network_id);

    /**
    * @param[in]  network_id QString [required]
    * @param[in]  webhook_test_id QString [required]
    */
    virtual void getNetworkWebhooksWebhookTest(const QString &network_id, const QString &webhook_test_id);

    /**
    * @param[in]  organization_id QString [required]
    * @param[in]  product_type QString [optional]
    */
    virtual void getOrganizationWebhooksAlertTypes(const QString &organization_id, const ::OpenAPI::OptionalParam<QString> &product_type = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  organization_id QString [required]
    * @param[in]  t0 QString [optional]
    * @param[in]  t1 QString [optional]
    * @param[in]  timespan float [optional]
    * @param[in]  per_page qint32 [optional]
    * @param[in]  starting_after QString [optional]
    * @param[in]  ending_before QString [optional]
    * @param[in]  url QString [optional]
    */
    virtual void getOrganizationWebhooksLogs(const QString &organization_id, const ::OpenAPI::OptionalParam<QString> &t0 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &t1 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<float> &timespan = ::OpenAPI::OptionalParam<float>(), const ::OpenAPI::OptionalParam<qint32> &per_page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &starting_after = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &ending_before = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &url = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  network_id QString [required]
    * @param[in]  http_server_id QString [required]
    * @param[in]  oai_update_network_webhooks_http_server_request OAIUpdateNetworkWebhooksHttpServer_request [optional]
    */
    virtual void updateNetworkWebhooksHttpServer(const QString &network_id, const QString &http_server_id, const ::OpenAPI::OptionalParam<OAIUpdateNetworkWebhooksHttpServer_request> &oai_update_network_webhooks_http_server_request = ::OpenAPI::OptionalParam<OAIUpdateNetworkWebhooksHttpServer_request>());

    /**
    * @param[in]  network_id QString [required]
    * @param[in]  payload_template_id QString [required]
    * @param[in]  oai_update_network_webhooks_payload_template_request OAIUpdateNetworkWebhooksPayloadTemplate_request [optional]
    */
    virtual void updateNetworkWebhooksPayloadTemplate(const QString &network_id, const QString &payload_template_id, const ::OpenAPI::OptionalParam<OAIUpdateNetworkWebhooksPayloadTemplate_request> &oai_update_network_webhooks_payload_template_request = ::OpenAPI::OptionalParam<OAIUpdateNetworkWebhooksPayloadTemplate_request>());


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

    void createNetworkWebhooksHttpServerCallback(OAIHttpRequestWorker *worker);
    void createNetworkWebhooksPayloadTemplateCallback(OAIHttpRequestWorker *worker);
    void createNetworkWebhooksWebhookTestCallback(OAIHttpRequestWorker *worker);
    void deleteNetworkWebhooksHttpServerCallback(OAIHttpRequestWorker *worker);
    void deleteNetworkWebhooksPayloadTemplateCallback(OAIHttpRequestWorker *worker);
    void getNetworkWebhooksHttpServerCallback(OAIHttpRequestWorker *worker);
    void getNetworkWebhooksHttpServersCallback(OAIHttpRequestWorker *worker);
    void getNetworkWebhooksPayloadTemplateCallback(OAIHttpRequestWorker *worker);
    void getNetworkWebhooksPayloadTemplatesCallback(OAIHttpRequestWorker *worker);
    void getNetworkWebhooksWebhookTestCallback(OAIHttpRequestWorker *worker);
    void getOrganizationWebhooksAlertTypesCallback(OAIHttpRequestWorker *worker);
    void getOrganizationWebhooksLogsCallback(OAIHttpRequestWorker *worker);
    void updateNetworkWebhooksHttpServerCallback(OAIHttpRequestWorker *worker);
    void updateNetworkWebhooksPayloadTemplateCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void createNetworkWebhooksHttpServerSignal(OAIGetNetworkWebhooksHttpServers_200_response_inner summary);
    void createNetworkWebhooksPayloadTemplateSignal(OAIGetNetworkWebhooksPayloadTemplates_200_response_inner summary);
    void createNetworkWebhooksWebhookTestSignal(OAICreateNetworkWebhooksWebhookTest_201_response summary);
    void deleteNetworkWebhooksHttpServerSignal();
    void deleteNetworkWebhooksPayloadTemplateSignal();
    void getNetworkWebhooksHttpServerSignal(OAIGetNetworkWebhooksHttpServers_200_response_inner summary);
    void getNetworkWebhooksHttpServersSignal(QList<OAIGetNetworkWebhooksHttpServers_200_response_inner> summary);
    void getNetworkWebhooksPayloadTemplateSignal(OAIGetNetworkWebhooksPayloadTemplates_200_response_inner summary);
    void getNetworkWebhooksPayloadTemplatesSignal(QList<OAIGetNetworkWebhooksPayloadTemplates_200_response_inner> summary);
    void getNetworkWebhooksWebhookTestSignal(OAICreateNetworkWebhooksWebhookTest_201_response summary);
    void getOrganizationWebhooksAlertTypesSignal(QList<OAIObject> summary);
    void getOrganizationWebhooksLogsSignal(QList<OAIGetOrganizationWebhooksLogs_200_response_inner> summary);
    void updateNetworkWebhooksHttpServerSignal(OAIGetNetworkWebhooksHttpServers_200_response_inner summary);
    void updateNetworkWebhooksPayloadTemplateSignal(OAIGetNetworkWebhooksPayloadTemplates_200_response_inner summary);


    void createNetworkWebhooksHttpServerSignalFull(OAIHttpRequestWorker *worker, OAIGetNetworkWebhooksHttpServers_200_response_inner summary);
    void createNetworkWebhooksPayloadTemplateSignalFull(OAIHttpRequestWorker *worker, OAIGetNetworkWebhooksPayloadTemplates_200_response_inner summary);
    void createNetworkWebhooksWebhookTestSignalFull(OAIHttpRequestWorker *worker, OAICreateNetworkWebhooksWebhookTest_201_response summary);
    void deleteNetworkWebhooksHttpServerSignalFull(OAIHttpRequestWorker *worker);
    void deleteNetworkWebhooksPayloadTemplateSignalFull(OAIHttpRequestWorker *worker);
    void getNetworkWebhooksHttpServerSignalFull(OAIHttpRequestWorker *worker, OAIGetNetworkWebhooksHttpServers_200_response_inner summary);
    void getNetworkWebhooksHttpServersSignalFull(OAIHttpRequestWorker *worker, QList<OAIGetNetworkWebhooksHttpServers_200_response_inner> summary);
    void getNetworkWebhooksPayloadTemplateSignalFull(OAIHttpRequestWorker *worker, OAIGetNetworkWebhooksPayloadTemplates_200_response_inner summary);
    void getNetworkWebhooksPayloadTemplatesSignalFull(OAIHttpRequestWorker *worker, QList<OAIGetNetworkWebhooksPayloadTemplates_200_response_inner> summary);
    void getNetworkWebhooksWebhookTestSignalFull(OAIHttpRequestWorker *worker, OAICreateNetworkWebhooksWebhookTest_201_response summary);
    void getOrganizationWebhooksAlertTypesSignalFull(OAIHttpRequestWorker *worker, QList<OAIObject> summary);
    void getOrganizationWebhooksLogsSignalFull(OAIHttpRequestWorker *worker, QList<OAIGetOrganizationWebhooksLogs_200_response_inner> summary);
    void updateNetworkWebhooksHttpServerSignalFull(OAIHttpRequestWorker *worker, OAIGetNetworkWebhooksHttpServers_200_response_inner summary);
    void updateNetworkWebhooksPayloadTemplateSignalFull(OAIHttpRequestWorker *worker, OAIGetNetworkWebhooksPayloadTemplates_200_response_inner summary);

    Q_DECL_DEPRECATED_X("Use createNetworkWebhooksHttpServerSignalError() instead")
    void createNetworkWebhooksHttpServerSignalE(OAIGetNetworkWebhooksHttpServers_200_response_inner summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createNetworkWebhooksHttpServerSignalError(OAIGetNetworkWebhooksHttpServers_200_response_inner summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createNetworkWebhooksPayloadTemplateSignalError() instead")
    void createNetworkWebhooksPayloadTemplateSignalE(OAIGetNetworkWebhooksPayloadTemplates_200_response_inner summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createNetworkWebhooksPayloadTemplateSignalError(OAIGetNetworkWebhooksPayloadTemplates_200_response_inner summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createNetworkWebhooksWebhookTestSignalError() instead")
    void createNetworkWebhooksWebhookTestSignalE(OAICreateNetworkWebhooksWebhookTest_201_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createNetworkWebhooksWebhookTestSignalError(OAICreateNetworkWebhooksWebhookTest_201_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteNetworkWebhooksHttpServerSignalError() instead")
    void deleteNetworkWebhooksHttpServerSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void deleteNetworkWebhooksHttpServerSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteNetworkWebhooksPayloadTemplateSignalError() instead")
    void deleteNetworkWebhooksPayloadTemplateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void deleteNetworkWebhooksPayloadTemplateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getNetworkWebhooksHttpServerSignalError() instead")
    void getNetworkWebhooksHttpServerSignalE(OAIGetNetworkWebhooksHttpServers_200_response_inner summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkWebhooksHttpServerSignalError(OAIGetNetworkWebhooksHttpServers_200_response_inner summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getNetworkWebhooksHttpServersSignalError() instead")
    void getNetworkWebhooksHttpServersSignalE(QList<OAIGetNetworkWebhooksHttpServers_200_response_inner> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkWebhooksHttpServersSignalError(QList<OAIGetNetworkWebhooksHttpServers_200_response_inner> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getNetworkWebhooksPayloadTemplateSignalError() instead")
    void getNetworkWebhooksPayloadTemplateSignalE(OAIGetNetworkWebhooksPayloadTemplates_200_response_inner summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkWebhooksPayloadTemplateSignalError(OAIGetNetworkWebhooksPayloadTemplates_200_response_inner summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getNetworkWebhooksPayloadTemplatesSignalError() instead")
    void getNetworkWebhooksPayloadTemplatesSignalE(QList<OAIGetNetworkWebhooksPayloadTemplates_200_response_inner> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkWebhooksPayloadTemplatesSignalError(QList<OAIGetNetworkWebhooksPayloadTemplates_200_response_inner> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getNetworkWebhooksWebhookTestSignalError() instead")
    void getNetworkWebhooksWebhookTestSignalE(OAICreateNetworkWebhooksWebhookTest_201_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkWebhooksWebhookTestSignalError(OAICreateNetworkWebhooksWebhookTest_201_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getOrganizationWebhooksAlertTypesSignalError() instead")
    void getOrganizationWebhooksAlertTypesSignalE(QList<OAIObject> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getOrganizationWebhooksAlertTypesSignalError(QList<OAIObject> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getOrganizationWebhooksLogsSignalError() instead")
    void getOrganizationWebhooksLogsSignalE(QList<OAIGetOrganizationWebhooksLogs_200_response_inner> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getOrganizationWebhooksLogsSignalError(QList<OAIGetOrganizationWebhooksLogs_200_response_inner> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateNetworkWebhooksHttpServerSignalError() instead")
    void updateNetworkWebhooksHttpServerSignalE(OAIGetNetworkWebhooksHttpServers_200_response_inner summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateNetworkWebhooksHttpServerSignalError(OAIGetNetworkWebhooksHttpServers_200_response_inner summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateNetworkWebhooksPayloadTemplateSignalError() instead")
    void updateNetworkWebhooksPayloadTemplateSignalE(OAIGetNetworkWebhooksPayloadTemplates_200_response_inner summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateNetworkWebhooksPayloadTemplateSignalError(OAIGetNetworkWebhooksPayloadTemplates_200_response_inner summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use createNetworkWebhooksHttpServerSignalErrorFull() instead")
    void createNetworkWebhooksHttpServerSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createNetworkWebhooksHttpServerSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createNetworkWebhooksPayloadTemplateSignalErrorFull() instead")
    void createNetworkWebhooksPayloadTemplateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createNetworkWebhooksPayloadTemplateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createNetworkWebhooksWebhookTestSignalErrorFull() instead")
    void createNetworkWebhooksWebhookTestSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createNetworkWebhooksWebhookTestSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteNetworkWebhooksHttpServerSignalErrorFull() instead")
    void deleteNetworkWebhooksHttpServerSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteNetworkWebhooksHttpServerSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteNetworkWebhooksPayloadTemplateSignalErrorFull() instead")
    void deleteNetworkWebhooksPayloadTemplateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteNetworkWebhooksPayloadTemplateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getNetworkWebhooksHttpServerSignalErrorFull() instead")
    void getNetworkWebhooksHttpServerSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkWebhooksHttpServerSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getNetworkWebhooksHttpServersSignalErrorFull() instead")
    void getNetworkWebhooksHttpServersSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkWebhooksHttpServersSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getNetworkWebhooksPayloadTemplateSignalErrorFull() instead")
    void getNetworkWebhooksPayloadTemplateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkWebhooksPayloadTemplateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getNetworkWebhooksPayloadTemplatesSignalErrorFull() instead")
    void getNetworkWebhooksPayloadTemplatesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkWebhooksPayloadTemplatesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getNetworkWebhooksWebhookTestSignalErrorFull() instead")
    void getNetworkWebhooksWebhookTestSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkWebhooksWebhookTestSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getOrganizationWebhooksAlertTypesSignalErrorFull() instead")
    void getOrganizationWebhooksAlertTypesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getOrganizationWebhooksAlertTypesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getOrganizationWebhooksLogsSignalErrorFull() instead")
    void getOrganizationWebhooksLogsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getOrganizationWebhooksLogsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateNetworkWebhooksHttpServerSignalErrorFull() instead")
    void updateNetworkWebhooksHttpServerSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateNetworkWebhooksHttpServerSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateNetworkWebhooksPayloadTemplateSignalErrorFull() instead")
    void updateNetworkWebhooksPayloadTemplateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateNetworkWebhooksPayloadTemplateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
