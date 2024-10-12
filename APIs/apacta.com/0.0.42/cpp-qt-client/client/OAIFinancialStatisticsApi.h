/**
 * Apacta
 * API for a tool to craftsmen used to register working hours, material usage and quality assurance. # Endpoint The endpoint `https://app.apacta.com/api/v1` should be used to communicate with the API. API access is only allowed with SSL encrypted connection (https). # Authentication URL query authentication with an API key is used, so appending `?api_key={api_key}` to the URL where `{api_key}` is found within Apacta settings is used for authentication # Pagination If the endpoint returns a `pagination` object it means the endpoint supports pagination - currently it's only possible to change pages with `?page={page_number}` but implementing custom page sizes are on the road map.   # Search/filter Is experimental but implemented in some cases - see the individual endpoints' docs for further explanation. # Ordering Is currently experimental, but on some endpoints it's implemented on URL querys so eg. to order Invoices by `invoice_number` appending `?sort=Invoices.invoice_number&direction=desc` would sort the list descending by the value of `invoice_number`. # Associations Is currently implemented on an experimental basis where you can append eg. `?include=Contacts,Projects`  to the `/api/v1/invoices/` endpoint to embed `Contact` and `Project` objects directly. # Project Files Currently project files can be retrieved from two endpoints. `/projects/{project_id}/files` handles files uploaded from wall posts or forms. `/projects/{project_id}/project_files` allows uploading and showing files, not belonging to specific form or wall post. # Errors/Exceptions ## 422 (Validation) Write something about how the `errors` object contains keys with the properties that failes validation like: ```   {       \"success\": false,       \"data\": {           \"code\": 422,           \"url\": \"/api/v1/contacts?api_key=5523be3b-30ef-425d-8203-04df7caaa93a\",           \"message\": \"A validation error occurred\",           \"errorCount\": 1,           \"errors\": {               \"contact_types\": [ ## Property name that failed validation                   \"Contacts must have at least one contact type\" ## Message with further explanation               ]           }       }   } ``` ## Code examples Running examples of how to retrieve the 5 most recent forms registered and embed the details of the User that made the form, and eventual products contained in the form ### Swift ``` ``` ### Java #### OkHttp ```   OkHttpClient client = new OkHttpClient();    Request request = new Request.Builder()     .url(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\")     .get()     .addHeader(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\")     .addHeader(\"accept\", \"application/json\")     .build();    Response response = client.newCall(request).execute(); ``` #### Unirest ```   HttpResponse<String> response = Unirest.get(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\")     .header(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\")     .header(\"accept\", \"application/json\")     .asString(); ``` ### Javascript #### Native ```   var data = null;    var xhr = new XMLHttpRequest();    xhr.addEventListener(\"readystatechange\", function () {     if (this.readyState === 4) {       console.log(this.responseText);     }   });    xhr.open(\"GET\", \"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\");   xhr.setRequestHeader(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\");   xhr.setRequestHeader(\"accept\", \"application/json\");    xhr.send(data); ``` #### jQuery ```   var settings = {     \"async\": true,     \"crossDomain\": true,     \"url\": \"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\",     \"method\": \"GET\",     \"headers\": {       \"x-auth-token\": \"{INSERT_YOUR_TOKEN}\",       \"accept\": \"application/json\",     }   }    $.ajax(settings).done(function (response) {     console.log(response);   }); ``` #### NodeJS (Request) ```   var request = require(\"request\");    var options = { method: 'GET',     url: 'https://app.apacta.com/api/v1/forms',     qs:      { extended: 'true',        sort: 'Forms.created',        direction: 'DESC',        include: 'Products,CreatedBy',        limit: '5' },     headers:      { accept: 'application/json',        'x-auth-token': '{INSERT_YOUR_TOKEN}' } };    request(options, function (error, response, body) {     if (error) throw new Error(error);      console.log(body);   });  ``` ### Python 3 ```   import http.client    conn = http.client.HTTPSConnection(\"app.apacta.com\")    payload = \"\"    headers = {       'x-auth-token': \"{INSERT_YOUR_TOKEN}\",       'accept': \"application/json\",       }    conn.request(\"GET\", \"/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\", payload, headers)    res = conn.getresponse()   data = res.read()    print(data.decode(\"utf-8\")) ``` ### C# #### RestSharp ```   var client = new RestClient(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\");   var request = new RestRequest(Method.GET);   request.AddHeader(\"accept\", \"application/json\");   request.AddHeader(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\");   IRestResponse response = client.Execute(request); ``` ### Ruby ```   require 'uri'   require 'net/http'    url = URI(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\")    http = Net::HTTP.new(url.host, url.port)   http.use_ssl = true   http.verify_mode = OpenSSL::SSL::VERIFY_NONE    request = Net::HTTP::Get.new(url)   request[\"x-auth-token\"] = '{INSERT_YOUR_TOKEN}'   request[\"accept\"] = 'application/json'    response = http.request(request)   puts response.read_body ``` ### PHP (HttpRequest) ```   <?php    $request = new HttpRequest();   $request->setUrl('https://app.apacta.com/api/v1/forms');   $request->setMethod(HTTP_METH_GET);    $request->setQueryData(array(     'extended' => 'true',     'sort' => 'Forms.created',     'direction' => 'DESC',     'include' => 'Products,CreatedBy',     'limit' => '5'   ));    $request->setHeaders(array(     'accept' => 'application/json',     'x-auth-token' => '{INSERT_YOUR_TOKEN}'   ));    try {     $response = $request->send();      echo $response->getBody();   } catch (HttpException $ex) {     echo $ex;   } ``` ### Shell (cURL) ```    $ curl --request GET --url 'https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5' --header 'accept: application/json' --header 'x-auth-token: {INSERT_YOUR_TOKEN}'  ```
 *
 * The version of the OpenAPI document: 0.0.42
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIFinancialStatisticsApi_H
#define OAI_OAIFinancialStatisticsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIGetExpensesSalesPrice_200_response.h"
#include "OAIGetFinancialStatisticsOverview_200_response.h"
#include "OAIGetFinancialStatistics_200_response.h"
#include "OAIGetInvoicedAmount_200_response.h"
#include "OAIGetMargin_200_response.h"
#include "OAIGetMaterialRentalsCostPrice_200_response.h"
#include "OAIGetProductsCostPrice_200_response.h"
#include "OAI_financial_statistics_workingHours_get_200_response.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIFinancialStatisticsApi : public QObject {
    Q_OBJECT

public:
    OAIFinancialStatisticsApi(const int timeOut = 0);
    ~OAIFinancialStatisticsApi();

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
    * @param[in]  date_from QDate [optional]
    * @param[in]  date_to QDate [optional]
    * @param[in]  project_id QString [optional]
    */
    virtual void financialStatisticsWorkingHoursGet(const ::OpenAPI::OptionalParam<QDate> &date_from = ::OpenAPI::OptionalParam<QDate>(), const ::OpenAPI::OptionalParam<QDate> &date_to = ::OpenAPI::OptionalParam<QDate>(), const ::OpenAPI::OptionalParam<QString> &project_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  date_from QDate [optional]
    * @param[in]  date_to QDate [optional]
    * @param[in]  project_id QString [optional]
    */
    virtual void getExpensesSalesPrice(const ::OpenAPI::OptionalParam<QDate> &date_from = ::OpenAPI::OptionalParam<QDate>(), const ::OpenAPI::OptionalParam<QDate> &date_to = ::OpenAPI::OptionalParam<QDate>(), const ::OpenAPI::OptionalParam<QString> &project_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  date_from QDate [optional]
    * @param[in]  date_to QDate [optional]
    * @param[in]  project_id QString [optional]
    * @param[in]  project_status_ids QString [optional]
    * @param[in]  only_not_invoiced bool [optional]
    * @param[in]  details bool [optional]
    */
    virtual void getFinancialStatistics(const ::OpenAPI::OptionalParam<QDate> &date_from = ::OpenAPI::OptionalParam<QDate>(), const ::OpenAPI::OptionalParam<QDate> &date_to = ::OpenAPI::OptionalParam<QDate>(), const ::OpenAPI::OptionalParam<QString> &project_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &project_status_ids = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &only_not_invoiced = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<bool> &details = ::OpenAPI::OptionalParam<bool>());

    /**
    * @param[in]  date_from QDate [optional]
    * @param[in]  date_to QDate [optional]
    * @param[in]  project_id QString [optional]
    */
    virtual void getFinancialStatisticsOverview(const ::OpenAPI::OptionalParam<QDate> &date_from = ::OpenAPI::OptionalParam<QDate>(), const ::OpenAPI::OptionalParam<QDate> &date_to = ::OpenAPI::OptionalParam<QDate>(), const ::OpenAPI::OptionalParam<QString> &project_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  date_from QDate [optional]
    * @param[in]  date_to QDate [optional]
    * @param[in]  project_id QString [optional]
    */
    virtual void getInvoicedAmount(const ::OpenAPI::OptionalParam<QDate> &date_from = ::OpenAPI::OptionalParam<QDate>(), const ::OpenAPI::OptionalParam<QDate> &date_to = ::OpenAPI::OptionalParam<QDate>(), const ::OpenAPI::OptionalParam<QString> &project_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  date_from QDate [optional]
    * @param[in]  date_to QDate [optional]
    * @param[in]  project_id QString [optional]
    */
    virtual void getMargin(const ::OpenAPI::OptionalParam<QDate> &date_from = ::OpenAPI::OptionalParam<QDate>(), const ::OpenAPI::OptionalParam<QDate> &date_to = ::OpenAPI::OptionalParam<QDate>(), const ::OpenAPI::OptionalParam<QString> &project_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  date_from QDate [optional]
    * @param[in]  date_to QDate [optional]
    * @param[in]  project_id QString [optional]
    */
    virtual void getMaterialRentalsCostPrice(const ::OpenAPI::OptionalParam<QDate> &date_from = ::OpenAPI::OptionalParam<QDate>(), const ::OpenAPI::OptionalParam<QDate> &date_to = ::OpenAPI::OptionalParam<QDate>(), const ::OpenAPI::OptionalParam<QString> &project_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  date_from QDate [optional]
    * @param[in]  date_to QDate [optional]
    * @param[in]  project_id QString [optional]
    */
    virtual void getProductsCostPrice(const ::OpenAPI::OptionalParam<QDate> &date_from = ::OpenAPI::OptionalParam<QDate>(), const ::OpenAPI::OptionalParam<QDate> &date_to = ::OpenAPI::OptionalParam<QDate>(), const ::OpenAPI::OptionalParam<QString> &project_id = ::OpenAPI::OptionalParam<QString>());


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

    void financialStatisticsWorkingHoursGetCallback(OAIHttpRequestWorker *worker);
    void getExpensesSalesPriceCallback(OAIHttpRequestWorker *worker);
    void getFinancialStatisticsCallback(OAIHttpRequestWorker *worker);
    void getFinancialStatisticsOverviewCallback(OAIHttpRequestWorker *worker);
    void getInvoicedAmountCallback(OAIHttpRequestWorker *worker);
    void getMarginCallback(OAIHttpRequestWorker *worker);
    void getMaterialRentalsCostPriceCallback(OAIHttpRequestWorker *worker);
    void getProductsCostPriceCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void financialStatisticsWorkingHoursGetSignal(OAI_financial_statistics_workingHours_get_200_response summary);
    void getExpensesSalesPriceSignal(OAIGetExpensesSalesPrice_200_response summary);
    void getFinancialStatisticsSignal(OAIGetFinancialStatistics_200_response summary);
    void getFinancialStatisticsOverviewSignal(OAIGetFinancialStatisticsOverview_200_response summary);
    void getInvoicedAmountSignal(OAIGetInvoicedAmount_200_response summary);
    void getMarginSignal(OAIGetMargin_200_response summary);
    void getMaterialRentalsCostPriceSignal(OAIGetMaterialRentalsCostPrice_200_response summary);
    void getProductsCostPriceSignal(OAIGetProductsCostPrice_200_response summary);


    void financialStatisticsWorkingHoursGetSignalFull(OAIHttpRequestWorker *worker, OAI_financial_statistics_workingHours_get_200_response summary);
    void getExpensesSalesPriceSignalFull(OAIHttpRequestWorker *worker, OAIGetExpensesSalesPrice_200_response summary);
    void getFinancialStatisticsSignalFull(OAIHttpRequestWorker *worker, OAIGetFinancialStatistics_200_response summary);
    void getFinancialStatisticsOverviewSignalFull(OAIHttpRequestWorker *worker, OAIGetFinancialStatisticsOverview_200_response summary);
    void getInvoicedAmountSignalFull(OAIHttpRequestWorker *worker, OAIGetInvoicedAmount_200_response summary);
    void getMarginSignalFull(OAIHttpRequestWorker *worker, OAIGetMargin_200_response summary);
    void getMaterialRentalsCostPriceSignalFull(OAIHttpRequestWorker *worker, OAIGetMaterialRentalsCostPrice_200_response summary);
    void getProductsCostPriceSignalFull(OAIHttpRequestWorker *worker, OAIGetProductsCostPrice_200_response summary);

    Q_DECL_DEPRECATED_X("Use financialStatisticsWorkingHoursGetSignalError() instead")
    void financialStatisticsWorkingHoursGetSignalE(OAI_financial_statistics_workingHours_get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void financialStatisticsWorkingHoursGetSignalError(OAI_financial_statistics_workingHours_get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getExpensesSalesPriceSignalError() instead")
    void getExpensesSalesPriceSignalE(OAIGetExpensesSalesPrice_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getExpensesSalesPriceSignalError(OAIGetExpensesSalesPrice_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getFinancialStatisticsSignalError() instead")
    void getFinancialStatisticsSignalE(OAIGetFinancialStatistics_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getFinancialStatisticsSignalError(OAIGetFinancialStatistics_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getFinancialStatisticsOverviewSignalError() instead")
    void getFinancialStatisticsOverviewSignalE(OAIGetFinancialStatisticsOverview_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getFinancialStatisticsOverviewSignalError(OAIGetFinancialStatisticsOverview_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getInvoicedAmountSignalError() instead")
    void getInvoicedAmountSignalE(OAIGetInvoicedAmount_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getInvoicedAmountSignalError(OAIGetInvoicedAmount_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getMarginSignalError() instead")
    void getMarginSignalE(OAIGetMargin_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getMarginSignalError(OAIGetMargin_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getMaterialRentalsCostPriceSignalError() instead")
    void getMaterialRentalsCostPriceSignalE(OAIGetMaterialRentalsCostPrice_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getMaterialRentalsCostPriceSignalError(OAIGetMaterialRentalsCostPrice_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getProductsCostPriceSignalError() instead")
    void getProductsCostPriceSignalE(OAIGetProductsCostPrice_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getProductsCostPriceSignalError(OAIGetProductsCostPrice_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use financialStatisticsWorkingHoursGetSignalErrorFull() instead")
    void financialStatisticsWorkingHoursGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void financialStatisticsWorkingHoursGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getExpensesSalesPriceSignalErrorFull() instead")
    void getExpensesSalesPriceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getExpensesSalesPriceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getFinancialStatisticsSignalErrorFull() instead")
    void getFinancialStatisticsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getFinancialStatisticsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getFinancialStatisticsOverviewSignalErrorFull() instead")
    void getFinancialStatisticsOverviewSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getFinancialStatisticsOverviewSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getInvoicedAmountSignalErrorFull() instead")
    void getInvoicedAmountSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getInvoicedAmountSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getMarginSignalErrorFull() instead")
    void getMarginSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getMarginSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getMaterialRentalsCostPriceSignalErrorFull() instead")
    void getMaterialRentalsCostPriceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getMaterialRentalsCostPriceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getProductsCostPriceSignalErrorFull() instead")
    void getProductsCostPriceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getProductsCostPriceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
