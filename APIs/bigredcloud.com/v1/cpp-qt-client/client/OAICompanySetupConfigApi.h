/**
 * Big Red Cloud API
 *   <div style='line-height: 30px;'>      <strong>Welcome to the Big Red Cloud API</strong><br/>      This API enables programmatic access to Big Red Cloud data.<br/>      We have used Swagger to auto generate the API documentation on this page, and it also enables direct interaction with the API in this page. <br/>      To get started, you will require an API Key - check out our guide at <a target='_blank' href='https://www.bigredcloud.com/support/generating-api-key-guide/'>https://www.bigredcloud.com/support/generating-api-key-guide/</a> for information on how to get one. <br/>      Use the  'Enter API Key' button below to enter your API key and start interacting with your Big Red Cloud data right on this page. <br/>      The API key will be stored in your browsers local storage for convenience, but you will be able to delete it at any time if you wish. <br/>      For additional information on the API, check out our support article at <a target='_blank' href='https://www.bigredcloud.com/support/api/'>https://www.bigredcloud.com/support/api/</a><br/>  </div>
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAICompanySetupConfigApi_H
#define OAI_OAICompanySetupConfigApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAICompanyOptionDto.h"
#include "OAICompanySetupConfigViewModel.h"
#include "OAIFinancialYearDto.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAICompanySetupConfigApi : public QObject {
    Q_OBJECT

public:
    OAICompanySetupConfigApi(const int timeOut = 0);
    ~OAICompanySetupConfigApi();

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


    virtual void companySetupConfigGet();


    virtual void companySetupConfigGetCompanyOptions();


    virtual void companySetupConfigGetFinancialYear();


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

    void companySetupConfigGetCallback(OAIHttpRequestWorker *worker);
    void companySetupConfigGetCompanyOptionsCallback(OAIHttpRequestWorker *worker);
    void companySetupConfigGetFinancialYearCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void companySetupConfigGetSignal(OAICompanySetupConfigViewModel summary);
    void companySetupConfigGetCompanyOptionsSignal(OAICompanyOptionDto summary);
    void companySetupConfigGetFinancialYearSignal(OAIFinancialYearDto summary);


    void companySetupConfigGetSignalFull(OAIHttpRequestWorker *worker, OAICompanySetupConfigViewModel summary);
    void companySetupConfigGetCompanyOptionsSignalFull(OAIHttpRequestWorker *worker, OAICompanyOptionDto summary);
    void companySetupConfigGetFinancialYearSignalFull(OAIHttpRequestWorker *worker, OAIFinancialYearDto summary);

    Q_DECL_DEPRECATED_X("Use companySetupConfigGetSignalError() instead")
    void companySetupConfigGetSignalE(OAICompanySetupConfigViewModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void companySetupConfigGetSignalError(OAICompanySetupConfigViewModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companySetupConfigGetCompanyOptionsSignalError() instead")
    void companySetupConfigGetCompanyOptionsSignalE(OAICompanyOptionDto summary, QNetworkReply::NetworkError error_type, QString error_str);
    void companySetupConfigGetCompanyOptionsSignalError(OAICompanyOptionDto summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companySetupConfigGetFinancialYearSignalError() instead")
    void companySetupConfigGetFinancialYearSignalE(OAIFinancialYearDto summary, QNetworkReply::NetworkError error_type, QString error_str);
    void companySetupConfigGetFinancialYearSignalError(OAIFinancialYearDto summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use companySetupConfigGetSignalErrorFull() instead")
    void companySetupConfigGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void companySetupConfigGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companySetupConfigGetCompanyOptionsSignalErrorFull() instead")
    void companySetupConfigGetCompanyOptionsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void companySetupConfigGetCompanyOptionsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companySetupConfigGetFinancialYearSignalErrorFull() instead")
    void companySetupConfigGetFinancialYearSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void companySetupConfigGetFinancialYearSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
