/**
 * OnSched Setup API
 * Build secure and scalable custom apps for onboarding and setup. Our flexible API provides many options for configuration.  <br><br>  Take the API for a test drive. Just click on the Authorize button below and authenticate.   You can access our demo company profile if you are not a customer, or your own profile by using your assigned ClientId and Secret.  <br><br>  The API has two interfaces, consumer and setup.   <ul>  <li>  The consumer interface provides all the endpoints required for implementing consumer booking flows.  </li>  <li>  The setup interface provides endpoints for profile configuration and setup.  </li>  </ul>  Toggle freely between the two interfaces using the swagger tool bar option labelled 'Select a definition'.  
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIBusinessUsersApi_H
#define OAI_OAIBusinessUsersApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIAuthorizedCompanyListViewModel.h"
#include "OAIBusinessPermissionListViewModel.h"
#include "OAIBusinessUserInputModel.h"
#include "OAIBusinessUserListViewModel.h"
#include "OAIBusinessUserUpdateModel.h"
#include "OAIBusinessUserViewModel.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIBusinessUsersApi : public QObject {
    Q_OBJECT

public:
    OAIBusinessUsersApi(const int timeOut = 0);
    ~OAIBusinessUsersApi();

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
    * @param[in]  email QString [required]
    * @param[in]  search_text QString [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  limit qint32 [optional]
    */
    virtual void setupV1BusinessusersEmailCompaniesGet(const QString &email, const ::OpenAPI::OptionalParam<QString> &search_text = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  location_id QString [optional]
    * @param[in]  email QString [optional]
    * @param[in]  role QString [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  limit qint32 [optional]
    */
    virtual void setupV1BusinessusersGet(const ::OpenAPI::OptionalParam<QString> &location_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &email = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &role = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    */
    virtual void setupV1BusinessusersIdDelete(const QString &id);

    /**
    * @param[in]  id QString [required]
    */
    virtual void setupV1BusinessusersIdGet(const QString &id);

    /**
    * @param[in]  id QString [required]
    * @param[in]  oai_business_user_update_model OAIBusinessUserUpdateModel [optional]
    */
    virtual void setupV1BusinessusersIdPut(const QString &id, const ::OpenAPI::OptionalParam<OAIBusinessUserUpdateModel> &oai_business_user_update_model = ::OpenAPI::OptionalParam<OAIBusinessUserUpdateModel>());

    /**
    * @param[in]  role QString [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  limit qint32 [optional]
    */
    virtual void setupV1BusinessusersPermissionsGet(const ::OpenAPI::OptionalParam<QString> &role = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  oai_business_user_input_model OAIBusinessUserInputModel [optional]
    */
    virtual void setupV1BusinessusersPost(const ::OpenAPI::OptionalParam<OAIBusinessUserInputModel> &oai_business_user_input_model = ::OpenAPI::OptionalParam<OAIBusinessUserInputModel>());


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

    void setupV1BusinessusersEmailCompaniesGetCallback(OAIHttpRequestWorker *worker);
    void setupV1BusinessusersGetCallback(OAIHttpRequestWorker *worker);
    void setupV1BusinessusersIdDeleteCallback(OAIHttpRequestWorker *worker);
    void setupV1BusinessusersIdGetCallback(OAIHttpRequestWorker *worker);
    void setupV1BusinessusersIdPutCallback(OAIHttpRequestWorker *worker);
    void setupV1BusinessusersPermissionsGetCallback(OAIHttpRequestWorker *worker);
    void setupV1BusinessusersPostCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void setupV1BusinessusersEmailCompaniesGetSignal(OAIAuthorizedCompanyListViewModel summary);
    void setupV1BusinessusersGetSignal(OAIBusinessUserListViewModel summary);
    void setupV1BusinessusersIdDeleteSignal();
    void setupV1BusinessusersIdGetSignal(OAIBusinessUserViewModel summary);
    void setupV1BusinessusersIdPutSignal(OAIBusinessUserViewModel summary);
    void setupV1BusinessusersPermissionsGetSignal(OAIBusinessPermissionListViewModel summary);
    void setupV1BusinessusersPostSignal(OAIBusinessUserViewModel summary);


    void setupV1BusinessusersEmailCompaniesGetSignalFull(OAIHttpRequestWorker *worker, OAIAuthorizedCompanyListViewModel summary);
    void setupV1BusinessusersGetSignalFull(OAIHttpRequestWorker *worker, OAIBusinessUserListViewModel summary);
    void setupV1BusinessusersIdDeleteSignalFull(OAIHttpRequestWorker *worker);
    void setupV1BusinessusersIdGetSignalFull(OAIHttpRequestWorker *worker, OAIBusinessUserViewModel summary);
    void setupV1BusinessusersIdPutSignalFull(OAIHttpRequestWorker *worker, OAIBusinessUserViewModel summary);
    void setupV1BusinessusersPermissionsGetSignalFull(OAIHttpRequestWorker *worker, OAIBusinessPermissionListViewModel summary);
    void setupV1BusinessusersPostSignalFull(OAIHttpRequestWorker *worker, OAIBusinessUserViewModel summary);

    Q_DECL_DEPRECATED_X("Use setupV1BusinessusersEmailCompaniesGetSignalError() instead")
    void setupV1BusinessusersEmailCompaniesGetSignalE(OAIAuthorizedCompanyListViewModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1BusinessusersEmailCompaniesGetSignalError(OAIAuthorizedCompanyListViewModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1BusinessusersGetSignalError() instead")
    void setupV1BusinessusersGetSignalE(OAIBusinessUserListViewModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1BusinessusersGetSignalError(OAIBusinessUserListViewModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1BusinessusersIdDeleteSignalError() instead")
    void setupV1BusinessusersIdDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1BusinessusersIdDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1BusinessusersIdGetSignalError() instead")
    void setupV1BusinessusersIdGetSignalE(OAIBusinessUserViewModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1BusinessusersIdGetSignalError(OAIBusinessUserViewModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1BusinessusersIdPutSignalError() instead")
    void setupV1BusinessusersIdPutSignalE(OAIBusinessUserViewModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1BusinessusersIdPutSignalError(OAIBusinessUserViewModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1BusinessusersPermissionsGetSignalError() instead")
    void setupV1BusinessusersPermissionsGetSignalE(OAIBusinessPermissionListViewModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1BusinessusersPermissionsGetSignalError(OAIBusinessPermissionListViewModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1BusinessusersPostSignalError() instead")
    void setupV1BusinessusersPostSignalE(OAIBusinessUserViewModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1BusinessusersPostSignalError(OAIBusinessUserViewModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use setupV1BusinessusersEmailCompaniesGetSignalErrorFull() instead")
    void setupV1BusinessusersEmailCompaniesGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1BusinessusersEmailCompaniesGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1BusinessusersGetSignalErrorFull() instead")
    void setupV1BusinessusersGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1BusinessusersGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1BusinessusersIdDeleteSignalErrorFull() instead")
    void setupV1BusinessusersIdDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1BusinessusersIdDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1BusinessusersIdGetSignalErrorFull() instead")
    void setupV1BusinessusersIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1BusinessusersIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1BusinessusersIdPutSignalErrorFull() instead")
    void setupV1BusinessusersIdPutSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1BusinessusersIdPutSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1BusinessusersPermissionsGetSignalErrorFull() instead")
    void setupV1BusinessusersPermissionsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1BusinessusersPermissionsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1BusinessusersPostSignalErrorFull() instead")
    void setupV1BusinessusersPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1BusinessusersPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
