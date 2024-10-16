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

#ifndef OAI_OAIStatisticsApi_H
#define OAI_OAIStatisticsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIGetDailySettlementStatsOut.h"
#include "OAIGetSettlementStatsByCountryOut.h"
#include "OAIGetSettlementStatsByTaxationTypeOut.h"
#include "OAIGetTransactionsStatsByCountryOut.h"
#include "OAIGetTransactionsStatsOut.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIStatisticsApi : public QObject {
    Q_OBJECT

public:
    OAIStatisticsApi(const int timeOut = 0);
    ~OAIStatisticsApi();

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
    * @param[in]  interval QString [required]
    * @param[in]  date_from QString [required]
    * @param[in]  date_to QString [required]
    */
    virtual void getDailySettlementStats(const QString &interval, const QString &date_from, const QString &date_to);

    /**
    * @param[in]  date_from QString [required]
    * @param[in]  date_to QString [required]
    */
    virtual void getSettlementStatsByCountry(const QString &date_from, const QString &date_to);

    /**
    * @param[in]  date_from QString [required]
    * @param[in]  date_to QString [required]
    */
    virtual void getSettlementStatsByTaxationType(const QString &date_from, const QString &date_to);

    /**
    * @param[in]  date_from QString [required]
    * @param[in]  date_to QString [required]
    * @param[in]  interval QString [optional]
    */
    virtual void getTransactionsStats(const QString &date_from, const QString &date_to, const ::OpenAPI::OptionalParam<QString> &interval = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  date_from QString [required]
    * @param[in]  date_to QString [required]
    * @param[in]  global_currency_code QString [optional]
    */
    virtual void getTransactionsStatsByCountry(const QString &date_from, const QString &date_to, const ::OpenAPI::OptionalParam<QString> &global_currency_code = ::OpenAPI::OptionalParam<QString>());


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

    void getDailySettlementStatsCallback(OAIHttpRequestWorker *worker);
    void getSettlementStatsByCountryCallback(OAIHttpRequestWorker *worker);
    void getSettlementStatsByTaxationTypeCallback(OAIHttpRequestWorker *worker);
    void getTransactionsStatsCallback(OAIHttpRequestWorker *worker);
    void getTransactionsStatsByCountryCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void getDailySettlementStatsSignal(OAIGetDailySettlementStatsOut summary);
    void getSettlementStatsByCountrySignal(OAIGetSettlementStatsByCountryOut summary);
    void getSettlementStatsByTaxationTypeSignal(OAIGetSettlementStatsByTaxationTypeOut summary);
    void getTransactionsStatsSignal(OAIGetTransactionsStatsOut summary);
    void getTransactionsStatsByCountrySignal(OAIGetTransactionsStatsByCountryOut summary);


    void getDailySettlementStatsSignalFull(OAIHttpRequestWorker *worker, OAIGetDailySettlementStatsOut summary);
    void getSettlementStatsByCountrySignalFull(OAIHttpRequestWorker *worker, OAIGetSettlementStatsByCountryOut summary);
    void getSettlementStatsByTaxationTypeSignalFull(OAIHttpRequestWorker *worker, OAIGetSettlementStatsByTaxationTypeOut summary);
    void getTransactionsStatsSignalFull(OAIHttpRequestWorker *worker, OAIGetTransactionsStatsOut summary);
    void getTransactionsStatsByCountrySignalFull(OAIHttpRequestWorker *worker, OAIGetTransactionsStatsByCountryOut summary);

    Q_DECL_DEPRECATED_X("Use getDailySettlementStatsSignalError() instead")
    void getDailySettlementStatsSignalE(OAIGetDailySettlementStatsOut summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getDailySettlementStatsSignalError(OAIGetDailySettlementStatsOut summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getSettlementStatsByCountrySignalError() instead")
    void getSettlementStatsByCountrySignalE(OAIGetSettlementStatsByCountryOut summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getSettlementStatsByCountrySignalError(OAIGetSettlementStatsByCountryOut summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getSettlementStatsByTaxationTypeSignalError() instead")
    void getSettlementStatsByTaxationTypeSignalE(OAIGetSettlementStatsByTaxationTypeOut summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getSettlementStatsByTaxationTypeSignalError(OAIGetSettlementStatsByTaxationTypeOut summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getTransactionsStatsSignalError() instead")
    void getTransactionsStatsSignalE(OAIGetTransactionsStatsOut summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getTransactionsStatsSignalError(OAIGetTransactionsStatsOut summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getTransactionsStatsByCountrySignalError() instead")
    void getTransactionsStatsByCountrySignalE(OAIGetTransactionsStatsByCountryOut summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getTransactionsStatsByCountrySignalError(OAIGetTransactionsStatsByCountryOut summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use getDailySettlementStatsSignalErrorFull() instead")
    void getDailySettlementStatsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getDailySettlementStatsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getSettlementStatsByCountrySignalErrorFull() instead")
    void getSettlementStatsByCountrySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getSettlementStatsByCountrySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getSettlementStatsByTaxationTypeSignalErrorFull() instead")
    void getSettlementStatsByTaxationTypeSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getSettlementStatsByTaxationTypeSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getTransactionsStatsSignalErrorFull() instead")
    void getTransactionsStatsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getTransactionsStatsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getTransactionsStatsByCountrySignalErrorFull() instead")
    void getTransactionsStatsByCountrySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getTransactionsStatsByCountrySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
