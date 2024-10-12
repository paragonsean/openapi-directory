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

#ifndef OAI_OAISharedCatalogIdAssignCategoriesApi_H
#define OAI_OAISharedCatalogIdAssignCategoriesApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIError_response.h"
#include "OAISharedCatalogCategoryManagementV1AssignCategoriesPost_request.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAISharedCatalogIdAssignCategoriesApi : public QObject {
    Q_OBJECT

public:
    OAISharedCatalogIdAssignCategoriesApi(const int timeOut = 0);
    ~OAISharedCatalogIdAssignCategoriesApi();

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
    * @param[in]  id qint32 [required]
    * @param[in]  oai_shared_catalog_category_management_v1_assign_categories_post_request OAISharedCatalogCategoryManagementV1AssignCategoriesPost_request [optional]
    */
    virtual void sharedCatalogCategoryManagementV1AssignCategoriesPost(const qint32 &id, const ::OpenAPI::OptionalParam<OAISharedCatalogCategoryManagementV1AssignCategoriesPost_request> &oai_shared_catalog_category_management_v1_assign_categories_post_request = ::OpenAPI::OptionalParam<OAISharedCatalogCategoryManagementV1AssignCategoriesPost_request>());


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

    void sharedCatalogCategoryManagementV1AssignCategoriesPostCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void sharedCatalogCategoryManagementV1AssignCategoriesPostSignal(bool summary);


    void sharedCatalogCategoryManagementV1AssignCategoriesPostSignalFull(OAIHttpRequestWorker *worker, bool summary);

    Q_DECL_DEPRECATED_X("Use sharedCatalogCategoryManagementV1AssignCategoriesPostSignalError() instead")
    void sharedCatalogCategoryManagementV1AssignCategoriesPostSignalE(bool summary, QNetworkReply::NetworkError error_type, QString error_str);
    void sharedCatalogCategoryManagementV1AssignCategoriesPostSignalError(bool summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use sharedCatalogCategoryManagementV1AssignCategoriesPostSignalErrorFull() instead")
    void sharedCatalogCategoryManagementV1AssignCategoriesPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void sharedCatalogCategoryManagementV1AssignCategoriesPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
