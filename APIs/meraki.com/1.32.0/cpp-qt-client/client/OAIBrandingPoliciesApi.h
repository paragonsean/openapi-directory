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

#ifndef OAI_OAIBrandingPoliciesApi_H
#define OAI_OAIBrandingPoliciesApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAICreateOrganizationBrandingPolicy_201_response.h"
#include "OAICreateOrganizationBrandingPolicy_request.h"
#include "OAIGetOrganizationBrandingPoliciesPriorities_200_response.h"
#include "OAIGetOrganizationBrandingPolicies_200_response_inner.h"
#include "OAIUpdateOrganizationBrandingPoliciesPriorities_request.h"
#include "OAIUpdateOrganizationBrandingPolicy_request.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIBrandingPoliciesApi : public QObject {
    Q_OBJECT

public:
    OAIBrandingPoliciesApi(const int timeOut = 0);
    ~OAIBrandingPoliciesApi();

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
    * @param[in]  organization_id QString [required]
    * @param[in]  oai_create_organization_branding_policy_request OAICreateOrganizationBrandingPolicy_request [optional]
    */
    virtual void createOrganizationBrandingPolicy(const QString &organization_id, const ::OpenAPI::OptionalParam<OAICreateOrganizationBrandingPolicy_request> &oai_create_organization_branding_policy_request = ::OpenAPI::OptionalParam<OAICreateOrganizationBrandingPolicy_request>());

    /**
    * @param[in]  organization_id QString [required]
    * @param[in]  branding_policy_id QString [required]
    */
    virtual void deleteOrganizationBrandingPolicy(const QString &organization_id, const QString &branding_policy_id);

    /**
    * @param[in]  organization_id QString [required]
    */
    virtual void getOrganizationBrandingPoliciesPriorities(const QString &organization_id);

    /**
    * @param[in]  organization_id QString [required]
    */
    virtual void getOrganizationBrandingPolicies(const QString &organization_id);

    /**
    * @param[in]  organization_id QString [required]
    * @param[in]  branding_policy_id QString [required]
    */
    virtual void getOrganizationBrandingPolicy(const QString &organization_id, const QString &branding_policy_id);

    /**
    * @param[in]  organization_id QString [required]
    * @param[in]  oai_update_organization_branding_policies_priorities_request OAIUpdateOrganizationBrandingPoliciesPriorities_request [optional]
    */
    virtual void updateOrganizationBrandingPoliciesPriorities(const QString &organization_id, const ::OpenAPI::OptionalParam<OAIUpdateOrganizationBrandingPoliciesPriorities_request> &oai_update_organization_branding_policies_priorities_request = ::OpenAPI::OptionalParam<OAIUpdateOrganizationBrandingPoliciesPriorities_request>());

    /**
    * @param[in]  organization_id QString [required]
    * @param[in]  branding_policy_id QString [required]
    * @param[in]  oai_update_organization_branding_policy_request OAIUpdateOrganizationBrandingPolicy_request [optional]
    */
    virtual void updateOrganizationBrandingPolicy(const QString &organization_id, const QString &branding_policy_id, const ::OpenAPI::OptionalParam<OAIUpdateOrganizationBrandingPolicy_request> &oai_update_organization_branding_policy_request = ::OpenAPI::OptionalParam<OAIUpdateOrganizationBrandingPolicy_request>());


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

    void createOrganizationBrandingPolicyCallback(OAIHttpRequestWorker *worker);
    void deleteOrganizationBrandingPolicyCallback(OAIHttpRequestWorker *worker);
    void getOrganizationBrandingPoliciesPrioritiesCallback(OAIHttpRequestWorker *worker);
    void getOrganizationBrandingPoliciesCallback(OAIHttpRequestWorker *worker);
    void getOrganizationBrandingPolicyCallback(OAIHttpRequestWorker *worker);
    void updateOrganizationBrandingPoliciesPrioritiesCallback(OAIHttpRequestWorker *worker);
    void updateOrganizationBrandingPolicyCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void createOrganizationBrandingPolicySignal(OAICreateOrganizationBrandingPolicy_201_response summary);
    void deleteOrganizationBrandingPolicySignal();
    void getOrganizationBrandingPoliciesPrioritiesSignal(OAIGetOrganizationBrandingPoliciesPriorities_200_response summary);
    void getOrganizationBrandingPoliciesSignal(QList<OAIGetOrganizationBrandingPolicies_200_response_inner> summary);
    void getOrganizationBrandingPolicySignal(OAIGetOrganizationBrandingPolicies_200_response_inner summary);
    void updateOrganizationBrandingPoliciesPrioritiesSignal(OAIGetOrganizationBrandingPoliciesPriorities_200_response summary);
    void updateOrganizationBrandingPolicySignal(OAIGetOrganizationBrandingPolicies_200_response_inner summary);


    void createOrganizationBrandingPolicySignalFull(OAIHttpRequestWorker *worker, OAICreateOrganizationBrandingPolicy_201_response summary);
    void deleteOrganizationBrandingPolicySignalFull(OAIHttpRequestWorker *worker);
    void getOrganizationBrandingPoliciesPrioritiesSignalFull(OAIHttpRequestWorker *worker, OAIGetOrganizationBrandingPoliciesPriorities_200_response summary);
    void getOrganizationBrandingPoliciesSignalFull(OAIHttpRequestWorker *worker, QList<OAIGetOrganizationBrandingPolicies_200_response_inner> summary);
    void getOrganizationBrandingPolicySignalFull(OAIHttpRequestWorker *worker, OAIGetOrganizationBrandingPolicies_200_response_inner summary);
    void updateOrganizationBrandingPoliciesPrioritiesSignalFull(OAIHttpRequestWorker *worker, OAIGetOrganizationBrandingPoliciesPriorities_200_response summary);
    void updateOrganizationBrandingPolicySignalFull(OAIHttpRequestWorker *worker, OAIGetOrganizationBrandingPolicies_200_response_inner summary);

    Q_DECL_DEPRECATED_X("Use createOrganizationBrandingPolicySignalError() instead")
    void createOrganizationBrandingPolicySignalE(OAICreateOrganizationBrandingPolicy_201_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createOrganizationBrandingPolicySignalError(OAICreateOrganizationBrandingPolicy_201_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteOrganizationBrandingPolicySignalError() instead")
    void deleteOrganizationBrandingPolicySignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void deleteOrganizationBrandingPolicySignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getOrganizationBrandingPoliciesPrioritiesSignalError() instead")
    void getOrganizationBrandingPoliciesPrioritiesSignalE(OAIGetOrganizationBrandingPoliciesPriorities_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getOrganizationBrandingPoliciesPrioritiesSignalError(OAIGetOrganizationBrandingPoliciesPriorities_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getOrganizationBrandingPoliciesSignalError() instead")
    void getOrganizationBrandingPoliciesSignalE(QList<OAIGetOrganizationBrandingPolicies_200_response_inner> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getOrganizationBrandingPoliciesSignalError(QList<OAIGetOrganizationBrandingPolicies_200_response_inner> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getOrganizationBrandingPolicySignalError() instead")
    void getOrganizationBrandingPolicySignalE(OAIGetOrganizationBrandingPolicies_200_response_inner summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getOrganizationBrandingPolicySignalError(OAIGetOrganizationBrandingPolicies_200_response_inner summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateOrganizationBrandingPoliciesPrioritiesSignalError() instead")
    void updateOrganizationBrandingPoliciesPrioritiesSignalE(OAIGetOrganizationBrandingPoliciesPriorities_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateOrganizationBrandingPoliciesPrioritiesSignalError(OAIGetOrganizationBrandingPoliciesPriorities_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateOrganizationBrandingPolicySignalError() instead")
    void updateOrganizationBrandingPolicySignalE(OAIGetOrganizationBrandingPolicies_200_response_inner summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateOrganizationBrandingPolicySignalError(OAIGetOrganizationBrandingPolicies_200_response_inner summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use createOrganizationBrandingPolicySignalErrorFull() instead")
    void createOrganizationBrandingPolicySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createOrganizationBrandingPolicySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteOrganizationBrandingPolicySignalErrorFull() instead")
    void deleteOrganizationBrandingPolicySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteOrganizationBrandingPolicySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getOrganizationBrandingPoliciesPrioritiesSignalErrorFull() instead")
    void getOrganizationBrandingPoliciesPrioritiesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getOrganizationBrandingPoliciesPrioritiesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getOrganizationBrandingPoliciesSignalErrorFull() instead")
    void getOrganizationBrandingPoliciesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getOrganizationBrandingPoliciesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getOrganizationBrandingPolicySignalErrorFull() instead")
    void getOrganizationBrandingPolicySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getOrganizationBrandingPolicySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateOrganizationBrandingPoliciesPrioritiesSignalErrorFull() instead")
    void updateOrganizationBrandingPoliciesPrioritiesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateOrganizationBrandingPoliciesPrioritiesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateOrganizationBrandingPolicySignalErrorFull() instead")
    void updateOrganizationBrandingPolicySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateOrganizationBrandingPolicySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
