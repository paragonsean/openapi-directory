/**
 * Checks API
 * **NOTE:** This is a preview of the API and it is not considered stable since refinements are still being made.  # Introduction  Welcome to the  **Truora Check** [**RESTful API**](https://en.wikipedia.org/wiki/Representational_state_transfer) reference. You may also want to check out our [**Validations API docs**](https://docs.validations.truora.com/) or our [**Signals API docs**](https://docs.signals.truora.com/).  Truora Check API allows performing full background checks on people, vehicles and companies. There are three main types of background checks:  - **Personal background check**: Verifies national IDs in multiple databases of public and legal entities in the LATAM region. For every national ID, returns information on: personal identity, criminal records, international background check, and professional background.  - **Vehicle background check**: Verifies the vehicle documents and the owner identity in multiple databases of public and legal entities in the LATAM region. For every vehicle and owner type, returns information on: personal identity, driving records, criminal records, and vehicle information.    - **Company background check**: Verifies the tax ID or a company name in multiple databases of public and legal entities in the LATAM region. For every company, returns the associated: business status, legal and criminal records, and media reports.  # API Key V1 is live!  API key version 1 is now live. Users with version 0 API keys are not immediately required to upgrade to V1 but should plan to do so at their earliest convenience. The changes for integration with API keys v1 are as follows:  - The field ``user_authorized`` is now required to perform person checks. This field indicates the API user has authorization to perform the check in compliance with data protection law. - The field ``homonym_scores`` is no longer included in our person check response as its results are already included in the body of the check and keeping them duplicated is generating unnecessary confusion.   # API composition  ## Endpoints  - **Check endpoints**: Provide an easy way to create and search for a background check. They also allow inserting groups of checks into reports. Each check contains scores, datasets and databases.   ```plain https://api.truora.com/v1/checks ```  - **Report endpoints**: Support batch uploads and grouping multiple checks together. Excel and .csv files are supported for batch uploads.   ```plain https://api.truora.com/v1/reports ```  - **Configuration endpoints**: Allows personalizing data sets and scores for customized background checks.  ```plain https://api.truora.com/v1/config ```  - **Continuous check endpoints**: Allows creating recurring checks and get notified whenever a change in the check score occurs.  ```plain https://api.truora.com/v1/continuous_checks ```  - **Behavior endpoints**: Allows sharing anonymous feedback about a person behavior when interacting with the company.  ```plain https://api.truora.com/v1/behaviour ```  - **Hooks endpoints**: Allows sending notifications via requests to your service or another third-party service whenever certain events occur.  ```plain https://api.truora.com/v1/hooks ```  ## Datasets  Categories that group the resulting information for background checks from databases are called datasets. Datasets are divided in:  - **Personal identity**: Corroborates the existence and validates personal identity documents.   - **Criminal record**: Checks for crimes according to each country penal code or criminal code. Keep in mind that data aged less than 10 years is usually more consistent.  - **Legal background**: Checks for lawsuits filed. Keep in mind that data aged less than 10 years is usually more consistent.  - **International background**: Checks international lists for crimes related to identity theft, money laundering, terrorist financing, and high crimes.  - **Professional background**: Checks professional regulatory entities for relevant information.  - **Affiliations and insurances**: Checks the history and status of social security affiliations.  - **Alert in media**: Checks major media agencies for relevant news related to violent actions.      - **Vehicle information**: Checks for the physical characteristics of the vehicle, technical status, insurance history, and other relevant information.  - **Traffic fines**: Checks for outstanding traffic fines.  - **Driving licenses**: Shows information relevant to the driver. Such as license status and driver certificates.  - **Business background**: Checks for business status, legal and criminal history, and other relevant information.  - **Taxes and Finances**: Checks for the information related to personal finances, liabilities, and taxes.  ## Requests Format  The POST requests receive a body that must be encoded in `www-x-form-urlencoded`, for instance:  ```plain type=person&national_id=123456&country=CO ```  The responses are always encoded in `JSON` format.  ## Errors  Whenever there is an error, a JSON with the following format is returned:  ```json {     \"code\": <Truora error code>,     \"http_code\": <The HTTP status of the response>,     \"message\": <The error message> } ```  for instance:  ```json {     \"code\": 10404,     \"http_code\": 404,     \"message\": \"The Check was not found\" } ```  ## SDKs  If your favorite language was not on the next list, You can use our [OpenAPI 3 spec](https://docs.truora.com/openapi.json) to generate it using the [Open API Generator](https://openapi-generator.tech/docs/installation).  To download the SDK click on the desired programming language:  - [C# .Net Core](https://truora-sdk.s3.amazonaws.com/checks/checks_csharp-netcore_latest.zip)  - [Elixir](https://truora-sdk.s3.amazonaws.com/checks/checks_elixir_latest.zip)  - [Go](https://truora-sdk.s3.amazonaws.com/checks/checks_go_latest.zip)  - [Java](https://truora-sdk.s3.amazonaws.com/checks/checks_java_latest.zip)  - [JavaScript](https://truora-sdk.s3.amazonaws.com/checks/checks_javascript_latest.zip)  - [Objc](https://truora-sdk.s3.amazonaws.com/checks/checks_objc_latest.zip)  - [Php](https://truora-sdk.s3.amazonaws.com/checks/checks_php_latest.zip)  - [Python](https://truora-sdk.s3.amazonaws.com/checks/checks_python_latest.zip)  - [Ruby](https://truora-sdk.s3.amazonaws.com/checks/checks_ruby_latest.zip)  You can see the full list of supported platforms here:  https://openapi-generator.tech/docs/generators   
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: api@truora.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIChecksApi_H
#define OAI_OAIChecksApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAICheckDetailsOutput.h"
#include "OAICheckOutput.h"
#include "OAIChecksOutput.h"
#include "OAIDatabase.h"
#include "OAIError.h"
#include <QString>
#include <QDate>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIChecksApi : public QObject {
    Q_OBJECT

public:
    OAIChecksApi(const int timeOut = 0);
    ~OAIChecksApi();

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
    * @param[in]  country QString [required]
    * @param[in]  type QString [required]
    * @param[in]  truora_priority QString [optional]
    * @param[in]  birth_certificate QString [optional]
    * @param[in]  company_name QString [optional]
    * @param[in]  date_of_birth QDate [optional]
    * @param[in]  diplomatic_id QString [optional]
    * @param[in]  driver_license QString [optional]
    * @param[in]  escrow QString [optional]
    * @param[in]  first_name QString [optional]
    * @param[in]  force_creation bool [optional]
    * @param[in]  foreign_id QString [optional]
    * @param[in]  issue_date QDate [optional]
    * @param[in]  last_name QString [optional]
    * @param[in]  license_plate QString [optional]
    * @param[in]  national_id QString [optional]
    * @param[in]  native_country QString [optional]
    * @param[in]  owner_document_id QString [optional]
    * @param[in]  owner_document_type QString [optional]
    * @param[in]  passport QString [optional]
    * @param[in]  payment_date QDate [optional]
    * @param[in]  pep QString [optional]
    * @param[in]  phone_number QString [optional]
    * @param[in]  professional_card QString [optional]
    * @param[in]  ptp QString [optional]
    * @param[in]  region QString [optional]
    * @param[in]  report_id QString [optional]
    * @param[in]  state_id QString [optional]
    * @param[in]  tax_id QString [optional]
    * @param[in]  user_authorized bool [optional]
    * @param[in]  vehicle_id QString [optional]
    * @param[in]  verification_code QString [optional]
    * @param[in]  watch QString [optional]
    */
    virtual void createCheck(const QString &country, const QString &type, const ::OpenAPI::OptionalParam<QString> &truora_priority = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &birth_certificate = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &company_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QDate> &date_of_birth = ::OpenAPI::OptionalParam<QDate>(), const ::OpenAPI::OptionalParam<QString> &diplomatic_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &driver_license = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &escrow = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &first_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &force_creation = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &foreign_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QDate> &issue_date = ::OpenAPI::OptionalParam<QDate>(), const ::OpenAPI::OptionalParam<QString> &last_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &license_plate = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &national_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &native_country = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &owner_document_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &owner_document_type = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &passport = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QDate> &payment_date = ::OpenAPI::OptionalParam<QDate>(), const ::OpenAPI::OptionalParam<QString> &pep = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &phone_number = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &professional_card = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &ptp = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &region = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &report_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &state_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &tax_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &user_authorized = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &vehicle_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &verification_code = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &watch = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  check_id QString [required]
    */
    virtual void getCheck(const QString &check_id);

    /**
    * @param[in]  country QString [optional]
    * @param[in]  unix_timestamp_seconds QString [optional]
    * @param[in]  unixtimezone_offset_seconds QString [optional]
    */
    virtual void getHealthDashboard(const ::OpenAPI::OptionalParam<QString> &country = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &unix_timestamp_seconds = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &unixtimezone_offset_seconds = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  check_id QString [required]
    * @param[in]  start_key QString [optional]
    * @param[in]  lang QString [optional]
    */
    virtual void listCheckDetails(const QString &check_id, const ::OpenAPI::OptionalParam<QString> &start_key = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &lang = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  start_key QString [optional]
    * @param[in]  report_id QString [optional]
    */
    virtual void listChecks(const ::OpenAPI::OptionalParam<QString> &start_key = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &report_id = ::OpenAPI::OptionalParam<QString>());


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

    void createCheckCallback(OAIHttpRequestWorker *worker);
    void getCheckCallback(OAIHttpRequestWorker *worker);
    void getHealthDashboardCallback(OAIHttpRequestWorker *worker);
    void listCheckDetailsCallback(OAIHttpRequestWorker *worker);
    void listChecksCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void createCheckSignal(OAICheckOutput summary);
    void getCheckSignal(OAICheckOutput summary);
    void getHealthDashboardSignal(QList<OAIDatabase> summary);
    void listCheckDetailsSignal(OAICheckDetailsOutput summary);
    void listChecksSignal(OAIChecksOutput summary);


    void createCheckSignalFull(OAIHttpRequestWorker *worker, OAICheckOutput summary);
    void getCheckSignalFull(OAIHttpRequestWorker *worker, OAICheckOutput summary);
    void getHealthDashboardSignalFull(OAIHttpRequestWorker *worker, QList<OAIDatabase> summary);
    void listCheckDetailsSignalFull(OAIHttpRequestWorker *worker, OAICheckDetailsOutput summary);
    void listChecksSignalFull(OAIHttpRequestWorker *worker, OAIChecksOutput summary);

    Q_DECL_DEPRECATED_X("Use createCheckSignalError() instead")
    void createCheckSignalE(OAICheckOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createCheckSignalError(OAICheckOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getCheckSignalError() instead")
    void getCheckSignalE(OAICheckOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getCheckSignalError(OAICheckOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getHealthDashboardSignalError() instead")
    void getHealthDashboardSignalE(QList<OAIDatabase> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getHealthDashboardSignalError(QList<OAIDatabase> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listCheckDetailsSignalError() instead")
    void listCheckDetailsSignalE(OAICheckDetailsOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listCheckDetailsSignalError(OAICheckDetailsOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listChecksSignalError() instead")
    void listChecksSignalE(OAIChecksOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listChecksSignalError(OAIChecksOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use createCheckSignalErrorFull() instead")
    void createCheckSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createCheckSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getCheckSignalErrorFull() instead")
    void getCheckSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getCheckSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getHealthDashboardSignalErrorFull() instead")
    void getHealthDashboardSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getHealthDashboardSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listCheckDetailsSignalErrorFull() instead")
    void listCheckDetailsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listCheckDetailsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listChecksSignalErrorFull() instead")
    void listChecksSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listChecksSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
