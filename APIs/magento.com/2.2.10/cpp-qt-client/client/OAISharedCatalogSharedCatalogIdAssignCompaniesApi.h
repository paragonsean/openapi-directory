/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAISharedCatalogSharedCatalogIdAssignCompaniesApi_H
#define OAI_OAISharedCatalogSharedCatalogIdAssignCompaniesApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIError_response.h"
#include "OAISharedCatalogCompanyManagementV1AssignCompaniesPost_request.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAISharedCatalogSharedCatalogIdAssignCompaniesApi : public QObject {
    Q_OBJECT

public:
    OAISharedCatalogSharedCatalogIdAssignCompaniesApi(const int timeOut = 0);
    ~OAISharedCatalogSharedCatalogIdAssignCompaniesApi();

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
    * @param[in]  shared_catalog_id qint32 [required]
    * @param[in]  oai_shared_catalog_company_management_v1_assign_companies_post_request OAISharedCatalogCompanyManagementV1AssignCompaniesPost_request [optional]
    */
    virtual void sharedCatalogCompanyManagementV1AssignCompaniesPost(const qint32 &shared_catalog_id, const ::OpenAPI::OptionalParam<OAISharedCatalogCompanyManagementV1AssignCompaniesPost_request> &oai_shared_catalog_company_management_v1_assign_companies_post_request = ::OpenAPI::OptionalParam<OAISharedCatalogCompanyManagementV1AssignCompaniesPost_request>());


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

    void sharedCatalogCompanyManagementV1AssignCompaniesPostCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void sharedCatalogCompanyManagementV1AssignCompaniesPostSignal(bool summary);


    void sharedCatalogCompanyManagementV1AssignCompaniesPostSignalFull(OAIHttpRequestWorker *worker, bool summary);

    Q_DECL_DEPRECATED_X("Use sharedCatalogCompanyManagementV1AssignCompaniesPostSignalError() instead")
    void sharedCatalogCompanyManagementV1AssignCompaniesPostSignalE(bool summary, QNetworkReply::NetworkError error_type, QString error_str);
    void sharedCatalogCompanyManagementV1AssignCompaniesPostSignalError(bool summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use sharedCatalogCompanyManagementV1AssignCompaniesPostSignalErrorFull() instead")
    void sharedCatalogCompanyManagementV1AssignCompaniesPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void sharedCatalogCompanyManagementV1AssignCompaniesPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
