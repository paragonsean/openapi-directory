/**
 * VocaDbWeb
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIVenueApiApi_H
#define OAI_OAIVenueApiApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIContentLanguagePreference.h"
#include "OAIDistanceUnit.h"
#include "OAINameMatchMode.h"
#include "OAIVenueForApiContractPartialFindResult.h"
#include "OAIVenueOptionalFields.h"
#include "OAIVenueReportType.h"
#include "OAIVenueSortRule.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIVenueApiApi : public QObject {
    Q_OBJECT

public:
    OAIVenueApiApi(const int timeOut = 0);
    ~OAIVenueApiApi();

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
    * @param[in]  query QString [optional]
    * @param[in]  fields OAIVenueOptionalFields [optional]
    * @param[in]  start qint32 [optional]
    * @param[in]  max_results qint32 [optional]
    * @param[in]  get_total_count bool [optional]
    * @param[in]  name_match_mode OAINameMatchMode [optional]
    * @param[in]  lang OAIContentLanguagePreference [optional]
    * @param[in]  sort_rule OAIVenueSortRule [optional]
    * @param[in]  latitude double [optional]
    * @param[in]  longitude double [optional]
    * @param[in]  radius double [optional]
    * @param[in]  distance_unit OAIDistanceUnit [optional]
    */
    virtual void apiVenuesGet(const ::OpenAPI::OptionalParam<QString> &query = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<OAIVenueOptionalFields> &fields = ::OpenAPI::OptionalParam<OAIVenueOptionalFields>(), const ::OpenAPI::OptionalParam<qint32> &start = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &max_results = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<bool> &get_total_count = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<OAINameMatchMode> &name_match_mode = ::OpenAPI::OptionalParam<OAINameMatchMode>(), const ::OpenAPI::OptionalParam<OAIContentLanguagePreference> &lang = ::OpenAPI::OptionalParam<OAIContentLanguagePreference>(), const ::OpenAPI::OptionalParam<OAIVenueSortRule> &sort_rule = ::OpenAPI::OptionalParam<OAIVenueSortRule>(), const ::OpenAPI::OptionalParam<double> &latitude = ::OpenAPI::OptionalParam<double>(), const ::OpenAPI::OptionalParam<double> &longitude = ::OpenAPI::OptionalParam<double>(), const ::OpenAPI::OptionalParam<double> &radius = ::OpenAPI::OptionalParam<double>(), const ::OpenAPI::OptionalParam<OAIDistanceUnit> &distance_unit = ::OpenAPI::OptionalParam<OAIDistanceUnit>());

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  notes QString [optional]
    * @param[in]  hard_delete bool [optional]
    */
    virtual void apiVenuesIdDelete(const qint32 &id, const ::OpenAPI::OptionalParam<QString> &notes = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &hard_delete = ::OpenAPI::OptionalParam<bool>());

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  report_type OAIVenueReportType [optional]
    * @param[in]  notes QString [optional]
    * @param[in]  version_number qint32 [optional]
    */
    virtual void apiVenuesIdReportsPost(const qint32 &id, const ::OpenAPI::OptionalParam<OAIVenueReportType> &report_type = ::OpenAPI::OptionalParam<OAIVenueReportType>(), const ::OpenAPI::OptionalParam<QString> &notes = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &version_number = ::OpenAPI::OptionalParam<qint32>());


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

    void apiVenuesGetCallback(OAIHttpRequestWorker *worker);
    void apiVenuesIdDeleteCallback(OAIHttpRequestWorker *worker);
    void apiVenuesIdReportsPostCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void apiVenuesGetSignal(OAIVenueForApiContractPartialFindResult summary);
    void apiVenuesIdDeleteSignal();
    void apiVenuesIdReportsPostSignal();


    void apiVenuesGetSignalFull(OAIHttpRequestWorker *worker, OAIVenueForApiContractPartialFindResult summary);
    void apiVenuesIdDeleteSignalFull(OAIHttpRequestWorker *worker);
    void apiVenuesIdReportsPostSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use apiVenuesGetSignalError() instead")
    void apiVenuesGetSignalE(OAIVenueForApiContractPartialFindResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void apiVenuesGetSignalError(OAIVenueForApiContractPartialFindResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiVenuesIdDeleteSignalError() instead")
    void apiVenuesIdDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void apiVenuesIdDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiVenuesIdReportsPostSignalError() instead")
    void apiVenuesIdReportsPostSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void apiVenuesIdReportsPostSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use apiVenuesGetSignalErrorFull() instead")
    void apiVenuesGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiVenuesGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiVenuesIdDeleteSignalErrorFull() instead")
    void apiVenuesIdDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiVenuesIdDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiVenuesIdReportsPostSignalErrorFull() instead")
    void apiVenuesIdReportsPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiVenuesIdReportsPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
