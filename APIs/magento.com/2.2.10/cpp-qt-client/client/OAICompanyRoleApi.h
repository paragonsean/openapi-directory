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

#ifndef OAI_OAICompanyRoleApi_H
#define OAI_OAICompanyRoleApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAICompanyRoleRepositoryV1SavePost_request.h"
#include "OAICompany_data_role_interface.h"
#include "OAICompany_data_role_search_results_interface.h"
#include "OAIError_response.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAICompanyRoleApi : public QObject {
    Q_OBJECT

public:
    OAICompanyRoleApi(const int timeOut = 0);
    ~OAICompanyRoleApi();

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
    * @param[in]  search_criteria_filter_groups_0_filters_0_field QString [optional]
    * @param[in]  search_criteria_filter_groups_0_filters_0_value QString [optional]
    * @param[in]  search_criteria_filter_groups_0_filters_0_condition_type QString [optional]
    * @param[in]  search_criteria_sort_orders_0_field QString [optional]
    * @param[in]  search_criteria_sort_orders_0_direction QString [optional]
    * @param[in]  search_criteria_page_size qint32 [optional]
    * @param[in]  search_criteria_current_page qint32 [optional]
    */
    virtual void companyRoleRepositoryV1GetListGet(const ::OpenAPI::OptionalParam<QString> &search_criteria_filter_groups_0_filters_0_field = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &search_criteria_filter_groups_0_filters_0_value = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &search_criteria_filter_groups_0_filters_0_condition_type = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &search_criteria_sort_orders_0_field = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &search_criteria_sort_orders_0_direction = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &search_criteria_page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &search_criteria_current_page = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  oai_company_role_repository_v1_save_post_request OAICompanyRoleRepositoryV1SavePost_request [optional]
    */
    virtual void companyRoleRepositoryV1SavePost(const ::OpenAPI::OptionalParam<OAICompanyRoleRepositoryV1SavePost_request> &oai_company_role_repository_v1_save_post_request = ::OpenAPI::OptionalParam<OAICompanyRoleRepositoryV1SavePost_request>());


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

    void companyRoleRepositoryV1GetListGetCallback(OAIHttpRequestWorker *worker);
    void companyRoleRepositoryV1SavePostCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void companyRoleRepositoryV1GetListGetSignal(OAICompany_data_role_search_results_interface summary);
    void companyRoleRepositoryV1SavePostSignal(OAICompany_data_role_interface summary);


    void companyRoleRepositoryV1GetListGetSignalFull(OAIHttpRequestWorker *worker, OAICompany_data_role_search_results_interface summary);
    void companyRoleRepositoryV1SavePostSignalFull(OAIHttpRequestWorker *worker, OAICompany_data_role_interface summary);

    Q_DECL_DEPRECATED_X("Use companyRoleRepositoryV1GetListGetSignalError() instead")
    void companyRoleRepositoryV1GetListGetSignalE(OAICompany_data_role_search_results_interface summary, QNetworkReply::NetworkError error_type, QString error_str);
    void companyRoleRepositoryV1GetListGetSignalError(OAICompany_data_role_search_results_interface summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companyRoleRepositoryV1SavePostSignalError() instead")
    void companyRoleRepositoryV1SavePostSignalE(OAICompany_data_role_interface summary, QNetworkReply::NetworkError error_type, QString error_str);
    void companyRoleRepositoryV1SavePostSignalError(OAICompany_data_role_interface summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use companyRoleRepositoryV1GetListGetSignalErrorFull() instead")
    void companyRoleRepositoryV1GetListGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void companyRoleRepositoryV1GetListGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companyRoleRepositoryV1SavePostSignalErrorFull() instead")
    void companyRoleRepositoryV1SavePostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void companyRoleRepositoryV1SavePostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
