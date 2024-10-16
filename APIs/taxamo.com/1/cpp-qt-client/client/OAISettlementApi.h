/**
 * Taxamo
 * Taxamo’s elegant suite of APIs and comprehensive reporting dashboard enables digital merchants to easily comply with EU regulatory requirements on tax calculation, evidence collection, tax return creation and data storage.
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAISettlementApi_H
#define OAI_OAISettlementApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIGetDetailedRefundsOut.h"
#include "OAIGetRefundsOut.h"
#include "OAIGetSettlementOut.h"
#include "OAIGetSettlementSummaryOut.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAISettlementApi : public QObject {
    Q_OBJECT

public:
    OAISettlementApi(const int timeOut = 0);
    ~OAISettlementApi();

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
    * @param[in]  format QString [optional]
    * @param[in]  country_codes QString [optional]
    * @param[in]  date_from QString [optional]
    * @param[in]  date_to QString [optional]
    * @param[in]  limit double [optional]
    * @param[in]  offset double [optional]
    */
    virtual void getDetailedRefunds(const ::OpenAPI::OptionalParam<QString> &format = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &country_codes = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &date_from = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &date_to = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<double> &limit = ::OpenAPI::OptionalParam<double>(), const ::OpenAPI::OptionalParam<double> &offset = ::OpenAPI::OptionalParam<double>());

    /**
    * @param[in]  date_from QString [required]
    * @param[in]  format QString [optional]
    * @param[in]  moss_country_code QString [optional]
    * @param[in]  tax_region QString [optional]
    */
    virtual void getRefunds(const QString &date_from, const ::OpenAPI::OptionalParam<QString> &format = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &moss_country_code = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &tax_region = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  quarter QString [required]
    * @param[in]  moss_tax_id QString [optional]
    * @param[in]  currency_code QString [optional]
    * @param[in]  end_month QString [optional]
    * @param[in]  tax_id QString [optional]
    * @param[in]  refund_date_kind_override QString [optional]
    * @param[in]  start_month QString [optional]
    * @param[in]  moss_country_code QString [optional]
    * @param[in]  format QString [optional]
    * @param[in]  tax_country_code QString [optional]
    */
    virtual void getSettlement(const QString &quarter, const ::OpenAPI::OptionalParam<QString> &moss_tax_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &currency_code = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &end_month = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &tax_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &refund_date_kind_override = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &start_month = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &moss_country_code = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &format = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &tax_country_code = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  quarter QString [required]
    * @param[in]  moss_country_code QString [optional]
    * @param[in]  tax_region QString [optional]
    * @param[in]  start_month QString [optional]
    * @param[in]  end_month QString [optional]
    */
    virtual void getSettlementSummary(const QString &quarter, const ::OpenAPI::OptionalParam<QString> &moss_country_code = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &tax_region = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &start_month = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &end_month = ::OpenAPI::OptionalParam<QString>());


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

    void getDetailedRefundsCallback(OAIHttpRequestWorker *worker);
    void getRefundsCallback(OAIHttpRequestWorker *worker);
    void getSettlementCallback(OAIHttpRequestWorker *worker);
    void getSettlementSummaryCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void getDetailedRefundsSignal(OAIGetDetailedRefundsOut summary);
    void getRefundsSignal(OAIGetRefundsOut summary);
    void getSettlementSignal(OAIGetSettlementOut summary);
    void getSettlementSummarySignal(OAIGetSettlementSummaryOut summary);


    void getDetailedRefundsSignalFull(OAIHttpRequestWorker *worker, OAIGetDetailedRefundsOut summary);
    void getRefundsSignalFull(OAIHttpRequestWorker *worker, OAIGetRefundsOut summary);
    void getSettlementSignalFull(OAIHttpRequestWorker *worker, OAIGetSettlementOut summary);
    void getSettlementSummarySignalFull(OAIHttpRequestWorker *worker, OAIGetSettlementSummaryOut summary);

    Q_DECL_DEPRECATED_X("Use getDetailedRefundsSignalError() instead")
    void getDetailedRefundsSignalE(OAIGetDetailedRefundsOut summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getDetailedRefundsSignalError(OAIGetDetailedRefundsOut summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getRefundsSignalError() instead")
    void getRefundsSignalE(OAIGetRefundsOut summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getRefundsSignalError(OAIGetRefundsOut summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getSettlementSignalError() instead")
    void getSettlementSignalE(OAIGetSettlementOut summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getSettlementSignalError(OAIGetSettlementOut summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getSettlementSummarySignalError() instead")
    void getSettlementSummarySignalE(OAIGetSettlementSummaryOut summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getSettlementSummarySignalError(OAIGetSettlementSummaryOut summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use getDetailedRefundsSignalErrorFull() instead")
    void getDetailedRefundsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getDetailedRefundsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getRefundsSignalErrorFull() instead")
    void getRefundsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getRefundsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getSettlementSignalErrorFull() instead")
    void getSettlementSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getSettlementSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getSettlementSummarySignalErrorFull() instead")
    void getSettlementSummarySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getSettlementSummarySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
