/**
 * Highways England API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIReportsApi_H
#define OAI_OAIReportsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIObject.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIReportsApi : public QObject {
    Q_OBJECT

public:
    OAIReportsApi(const int timeOut = 0);
    ~OAIReportsApi();

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
    * @param[in]  report_type QString [required]
    * @param[in]  sites QString [required]
    * @param[in]  start_date QString [required]
    * @param[in]  end_date QString [required]
    * @param[in]  page qint32 [required]
    * @param[in]  page_size qint32 [required]
    * @param[in]  version QString [required]
    * @param[in]  report_sub_type_id qint32 [optional]
    */
    virtual void reportsIndex(const QString &report_type, const QString &sites, const QString &start_date, const QString &end_date, const qint32 &page, const qint32 &page_size, const QString &version, const ::OpenAPI::OptionalParam<qint32> &report_sub_type_id = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  report_type QString [required]
    * @param[in]  sites QString [required]
    * @param[in]  start_date QString [required]
    * @param[in]  end_date QString [required]
    * @param[in]  page qint32 [required]
    * @param[in]  page_size qint32 [required]
    * @param[in]  version QString [required]
    * @param[in]  report_sub_type_id qint32 [optional]
    */
    virtual void vversionReportsStartDateToEndDateReportTypeGet(const QString &report_type, const QString &sites, const QString &start_date, const QString &end_date, const qint32 &page, const qint32 &page_size, const QString &version, const ::OpenAPI::OptionalParam<qint32> &report_sub_type_id = ::OpenAPI::OptionalParam<qint32>());


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

    void reportsIndexCallback(OAIHttpRequestWorker *worker);
    void vversionReportsStartDateToEndDateReportTypeGetCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void reportsIndexSignal(OAIObject summary);
    void vversionReportsStartDateToEndDateReportTypeGetSignal(OAIObject summary);


    void reportsIndexSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void vversionReportsStartDateToEndDateReportTypeGetSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);

    Q_DECL_DEPRECATED_X("Use reportsIndexSignalError() instead")
    void reportsIndexSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void reportsIndexSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use vversionReportsStartDateToEndDateReportTypeGetSignalError() instead")
    void vversionReportsStartDateToEndDateReportTypeGetSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void vversionReportsStartDateToEndDateReportTypeGetSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use reportsIndexSignalErrorFull() instead")
    void reportsIndexSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void reportsIndexSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use vversionReportsStartDateToEndDateReportTypeGetSignalErrorFull() instead")
    void vversionReportsStartDateToEndDateReportTypeGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void vversionReportsStartDateToEndDateReportTypeGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
