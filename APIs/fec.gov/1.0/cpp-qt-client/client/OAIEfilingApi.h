/**
 * OpenFEC
 * This application programming interface (API) allows you to explore the way candidates and committees fund their campaigns.    The Federal Election Commission (FEC) API is a RESTful web service supporting full-text and field-specific searches on FEC data. [Bulk downloads](https://www.fec.gov/data/advanced/?tab=bulk-data) are available on the current site. Information is tied to the underlying forms by file ID and image ID. Data is updated nightly.    There are a lot of data, and a good place to start is to use search to find interesting candidates and committees. Then, you can use their IDs to find report or line item details with the other endpoints. If you are interested in individual donors, check out contributor information in the `/schedule_a/` endpoints.    <b class=\"body\" id=\"getting_started_head\">Getting started with the openFEC API</b><br>    If you would like to use the FEC's API programmatically, you can sign up for your own API key using our form. Alternatively, you can still try out our API without an API key by using the web interface and using DEMO_KEY. Note that when you use the openFEC API you are subject to the [Terms of Service](https://github.com/fecgov/FEC/blob/master/TERMS-OF-SERVICE.md) and [Acceptable Use policy](https://github.com/fecgov/FEC/blob/master/ACCEPTABLE-USE-POLICY.md).    Signing up for an API key will enable you to place up to 1,000 calls an hour. Each call is limited to 100 results per page. You can email questions, comments or a request to get a key for 7,200 calls an hour (120 calls per minute) to <a href=\"mailto:APIinfo@fec.gov\">APIinfo@fec.gov</a>. You can also ask questions and discuss the data in a community led [group](https://groups.google.com/forum/#!forum/fec-data).    The model definitions and schema are available at [/swagger](/swagger/). This is useful for making wrappers and exploring the data.    A few restrictions limit the way you can use FEC data. For example, you can’t use contributor lists for commercial purposes or to solicit donations. [Learn more here](https://www.fec.gov/updates/sale-or-use-contributor-information/).    [Inspect our source code](https://github.com/fecgov/openFEC). We welcome issues and pull requests!    <p><br></p> <h2 class=\"title\" id=\"signup_head\">Sign up for an API key</h2> <div id=\"apidatagov_signup\">Loading signup form...</div>
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIEfilingApi_H
#define OAI_OAIEfilingApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIBaseF3FilingPage.h"
#include "OAIBaseF3PFilingPage.h"
#include "OAIBaseF3XFilingPage.h"
#include "OAIEFilingsPage.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIEfilingApi : public QObject {
    Q_OBJECT

public:
    OAIEfilingApi(const int timeOut = 0);
    ~OAIEfilingApi();

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
    * @param[in]  api_key QString [required]
    * @param[in]  min_receipt_date QDate [optional]
    * @param[in]  sort_nulls_last bool [optional]
    * @param[in]  page qint32 [optional]
    * @param[in]  committee_id QList<QString> [optional]
    * @param[in]  sort_null_only bool [optional]
    * @param[in]  max_receipt_date QDate [optional]
    * @param[in]  sort_hide_null bool [optional]
    * @param[in]  file_number QList<qint32> [optional]
    * @param[in]  per_page qint32 [optional]
    * @param[in]  sort QString [optional]
    * @param[in]  q_filer QList<QString> [optional]
    */
    virtual void efileFilingsGet(const QString &api_key, const ::OpenAPI::OptionalParam<QDate> &min_receipt_date = ::OpenAPI::OptionalParam<QDate>(), const ::OpenAPI::OptionalParam<bool> &sort_nulls_last = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QList<QString>> &committee_id = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<bool> &sort_null_only = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QDate> &max_receipt_date = ::OpenAPI::OptionalParam<QDate>(), const ::OpenAPI::OptionalParam<bool> &sort_hide_null = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QList<qint32>> &file_number = ::OpenAPI::OptionalParam<QList<qint32>>(), const ::OpenAPI::OptionalParam<qint32> &per_page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &sort = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QList<QString>> &q_filer = ::OpenAPI::OptionalParam<QList<QString>>());

    /**
    * @param[in]  api_key QString [required]
    * @param[in]  min_receipt_date QDate [optional]
    * @param[in]  sort_nulls_last bool [optional]
    * @param[in]  page qint32 [optional]
    * @param[in]  committee_id QList<QString> [optional]
    * @param[in]  sort_null_only bool [optional]
    * @param[in]  max_receipt_date QDate [optional]
    * @param[in]  sort_hide_null bool [optional]
    * @param[in]  file_number QList<qint32> [optional]
    * @param[in]  per_page qint32 [optional]
    * @param[in]  sort QString [optional]
    * @param[in]  q_filer QList<QString> [optional]
    */
    virtual void efileReportsHouseSenateGet(const QString &api_key, const ::OpenAPI::OptionalParam<QDate> &min_receipt_date = ::OpenAPI::OptionalParam<QDate>(), const ::OpenAPI::OptionalParam<bool> &sort_nulls_last = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QList<QString>> &committee_id = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<bool> &sort_null_only = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QDate> &max_receipt_date = ::OpenAPI::OptionalParam<QDate>(), const ::OpenAPI::OptionalParam<bool> &sort_hide_null = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QList<qint32>> &file_number = ::OpenAPI::OptionalParam<QList<qint32>>(), const ::OpenAPI::OptionalParam<qint32> &per_page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &sort = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QList<QString>> &q_filer = ::OpenAPI::OptionalParam<QList<QString>>());

    /**
    * @param[in]  api_key QString [required]
    * @param[in]  min_receipt_date QDate [optional]
    * @param[in]  sort_nulls_last bool [optional]
    * @param[in]  page qint32 [optional]
    * @param[in]  committee_id QList<QString> [optional]
    * @param[in]  sort_null_only bool [optional]
    * @param[in]  max_receipt_date QDate [optional]
    * @param[in]  sort_hide_null bool [optional]
    * @param[in]  file_number QList<qint32> [optional]
    * @param[in]  per_page qint32 [optional]
    * @param[in]  sort QString [optional]
    * @param[in]  q_filer QList<QString> [optional]
    */
    virtual void efileReportsPacPartyGet(const QString &api_key, const ::OpenAPI::OptionalParam<QDate> &min_receipt_date = ::OpenAPI::OptionalParam<QDate>(), const ::OpenAPI::OptionalParam<bool> &sort_nulls_last = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QList<QString>> &committee_id = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<bool> &sort_null_only = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QDate> &max_receipt_date = ::OpenAPI::OptionalParam<QDate>(), const ::OpenAPI::OptionalParam<bool> &sort_hide_null = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QList<qint32>> &file_number = ::OpenAPI::OptionalParam<QList<qint32>>(), const ::OpenAPI::OptionalParam<qint32> &per_page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &sort = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QList<QString>> &q_filer = ::OpenAPI::OptionalParam<QList<QString>>());

    /**
    * @param[in]  api_key QString [required]
    * @param[in]  min_receipt_date QDate [optional]
    * @param[in]  sort_nulls_last bool [optional]
    * @param[in]  page qint32 [optional]
    * @param[in]  committee_id QList<QString> [optional]
    * @param[in]  sort_null_only bool [optional]
    * @param[in]  max_receipt_date QDate [optional]
    * @param[in]  sort_hide_null bool [optional]
    * @param[in]  file_number QList<qint32> [optional]
    * @param[in]  per_page qint32 [optional]
    * @param[in]  sort QString [optional]
    * @param[in]  q_filer QList<QString> [optional]
    */
    virtual void efileReportsPresidentialGet(const QString &api_key, const ::OpenAPI::OptionalParam<QDate> &min_receipt_date = ::OpenAPI::OptionalParam<QDate>(), const ::OpenAPI::OptionalParam<bool> &sort_nulls_last = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QList<QString>> &committee_id = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<bool> &sort_null_only = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QDate> &max_receipt_date = ::OpenAPI::OptionalParam<QDate>(), const ::OpenAPI::OptionalParam<bool> &sort_hide_null = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QList<qint32>> &file_number = ::OpenAPI::OptionalParam<QList<qint32>>(), const ::OpenAPI::OptionalParam<qint32> &per_page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &sort = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QList<QString>> &q_filer = ::OpenAPI::OptionalParam<QList<QString>>());


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

    void efileFilingsGetCallback(OAIHttpRequestWorker *worker);
    void efileReportsHouseSenateGetCallback(OAIHttpRequestWorker *worker);
    void efileReportsPacPartyGetCallback(OAIHttpRequestWorker *worker);
    void efileReportsPresidentialGetCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void efileFilingsGetSignal(OAIEFilingsPage summary);
    void efileReportsHouseSenateGetSignal(OAIBaseF3FilingPage summary);
    void efileReportsPacPartyGetSignal(OAIBaseF3XFilingPage summary);
    void efileReportsPresidentialGetSignal(OAIBaseF3PFilingPage summary);


    void efileFilingsGetSignalFull(OAIHttpRequestWorker *worker, OAIEFilingsPage summary);
    void efileReportsHouseSenateGetSignalFull(OAIHttpRequestWorker *worker, OAIBaseF3FilingPage summary);
    void efileReportsPacPartyGetSignalFull(OAIHttpRequestWorker *worker, OAIBaseF3XFilingPage summary);
    void efileReportsPresidentialGetSignalFull(OAIHttpRequestWorker *worker, OAIBaseF3PFilingPage summary);

    Q_DECL_DEPRECATED_X("Use efileFilingsGetSignalError() instead")
    void efileFilingsGetSignalE(OAIEFilingsPage summary, QNetworkReply::NetworkError error_type, QString error_str);
    void efileFilingsGetSignalError(OAIEFilingsPage summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use efileReportsHouseSenateGetSignalError() instead")
    void efileReportsHouseSenateGetSignalE(OAIBaseF3FilingPage summary, QNetworkReply::NetworkError error_type, QString error_str);
    void efileReportsHouseSenateGetSignalError(OAIBaseF3FilingPage summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use efileReportsPacPartyGetSignalError() instead")
    void efileReportsPacPartyGetSignalE(OAIBaseF3XFilingPage summary, QNetworkReply::NetworkError error_type, QString error_str);
    void efileReportsPacPartyGetSignalError(OAIBaseF3XFilingPage summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use efileReportsPresidentialGetSignalError() instead")
    void efileReportsPresidentialGetSignalE(OAIBaseF3PFilingPage summary, QNetworkReply::NetworkError error_type, QString error_str);
    void efileReportsPresidentialGetSignalError(OAIBaseF3PFilingPage summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use efileFilingsGetSignalErrorFull() instead")
    void efileFilingsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void efileFilingsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use efileReportsHouseSenateGetSignalErrorFull() instead")
    void efileReportsHouseSenateGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void efileReportsHouseSenateGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use efileReportsPacPartyGetSignalErrorFull() instead")
    void efileReportsPacPartyGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void efileReportsPacPartyGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use efileReportsPresidentialGetSignalErrorFull() instead")
    void efileReportsPresidentialGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void efileReportsPresidentialGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
