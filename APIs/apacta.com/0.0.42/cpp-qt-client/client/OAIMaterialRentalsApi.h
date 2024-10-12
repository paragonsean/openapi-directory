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

#ifndef OAI_OAIMaterialRentalsApi_H
#define OAI_OAIMaterialRentalsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIErrorNotFound.h"
#include "OAIErrorValidation.h"
#include "OAI_clocking_records_post_201_response.h"
#include "OAI_expense_files__expense_file_id__put_200_response.h"
#include "OAI_materials__material_id__rentals__get_200_response.h"
#include "OAI_materials__material_id__rentals__material_rental_id___get_200_response.h"
#include "OAI_materials__material_id__rentals__post_request.h"
#include "OAI_materials__material_id__rentals_checkout__post_request.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIMaterialRentalsApi : public QObject {
    Q_OBJECT

public:
    OAIMaterialRentalsApi(const int timeOut = 0);
    ~OAIMaterialRentalsApi();

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
    * @param[in]  material_id QString [required]
    * @param[in]  oai_materials__material_id__rentals_checkout__post_request OAI_materials__material_id__rentals_checkout__post_request [optional]
    */
    virtual void materialsMaterialIdRentalsCheckoutPost(const QString &material_id, const ::OpenAPI::OptionalParam<OAI_materials__material_id__rentals_checkout__post_request> &oai_materials__material_id__rentals_checkout__post_request = ::OpenAPI::OptionalParam<OAI_materials__material_id__rentals_checkout__post_request>());

    /**
    * @param[in]  material_id QString [required]
    */
    virtual void materialsMaterialIdRentalsGet(const QString &material_id);

    /**
    * @param[in]  material_id QString [required]
    * @param[in]  material_rental_id QString [required]
    */
    virtual void materialsMaterialIdRentalsMaterialRentalIdDelete(const QString &material_id, const QString &material_rental_id);

    /**
    * @param[in]  material_id QString [required]
    * @param[in]  material_rental_id QString [required]
    */
    virtual void materialsMaterialIdRentalsMaterialRentalIdGet(const QString &material_id, const QString &material_rental_id);

    /**
    * @param[in]  material_id QString [required]
    * @param[in]  material_rental_id QString [required]
    */
    virtual void materialsMaterialIdRentalsMaterialRentalIdPut(const QString &material_id, const QString &material_rental_id);

    /**
    * @param[in]  material_id QString [required]
    * @param[in]  oai_materials__material_id__rentals__post_request OAI_materials__material_id__rentals__post_request [optional]
    */
    virtual void materialsMaterialIdRentalsPost(const QString &material_id, const ::OpenAPI::OptionalParam<OAI_materials__material_id__rentals__post_request> &oai_materials__material_id__rentals__post_request = ::OpenAPI::OptionalParam<OAI_materials__material_id__rentals__post_request>());


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

    void materialsMaterialIdRentalsCheckoutPostCallback(OAIHttpRequestWorker *worker);
    void materialsMaterialIdRentalsGetCallback(OAIHttpRequestWorker *worker);
    void materialsMaterialIdRentalsMaterialRentalIdDeleteCallback(OAIHttpRequestWorker *worker);
    void materialsMaterialIdRentalsMaterialRentalIdGetCallback(OAIHttpRequestWorker *worker);
    void materialsMaterialIdRentalsMaterialRentalIdPutCallback(OAIHttpRequestWorker *worker);
    void materialsMaterialIdRentalsPostCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void materialsMaterialIdRentalsCheckoutPostSignal(OAI_clocking_records_post_201_response summary);
    void materialsMaterialIdRentalsGetSignal(OAI_materials__material_id__rentals__get_200_response summary);
    void materialsMaterialIdRentalsMaterialRentalIdDeleteSignal(OAI_expense_files__expense_file_id__put_200_response summary);
    void materialsMaterialIdRentalsMaterialRentalIdGetSignal(OAI_materials__material_id__rentals__material_rental_id___get_200_response summary);
    void materialsMaterialIdRentalsMaterialRentalIdPutSignal(OAI_expense_files__expense_file_id__put_200_response summary);
    void materialsMaterialIdRentalsPostSignal(OAI_clocking_records_post_201_response summary);


    void materialsMaterialIdRentalsCheckoutPostSignalFull(OAIHttpRequestWorker *worker, OAI_clocking_records_post_201_response summary);
    void materialsMaterialIdRentalsGetSignalFull(OAIHttpRequestWorker *worker, OAI_materials__material_id__rentals__get_200_response summary);
    void materialsMaterialIdRentalsMaterialRentalIdDeleteSignalFull(OAIHttpRequestWorker *worker, OAI_expense_files__expense_file_id__put_200_response summary);
    void materialsMaterialIdRentalsMaterialRentalIdGetSignalFull(OAIHttpRequestWorker *worker, OAI_materials__material_id__rentals__material_rental_id___get_200_response summary);
    void materialsMaterialIdRentalsMaterialRentalIdPutSignalFull(OAIHttpRequestWorker *worker, OAI_expense_files__expense_file_id__put_200_response summary);
    void materialsMaterialIdRentalsPostSignalFull(OAIHttpRequestWorker *worker, OAI_clocking_records_post_201_response summary);

    Q_DECL_DEPRECATED_X("Use materialsMaterialIdRentalsCheckoutPostSignalError() instead")
    void materialsMaterialIdRentalsCheckoutPostSignalE(OAI_clocking_records_post_201_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void materialsMaterialIdRentalsCheckoutPostSignalError(OAI_clocking_records_post_201_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use materialsMaterialIdRentalsGetSignalError() instead")
    void materialsMaterialIdRentalsGetSignalE(OAI_materials__material_id__rentals__get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void materialsMaterialIdRentalsGetSignalError(OAI_materials__material_id__rentals__get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use materialsMaterialIdRentalsMaterialRentalIdDeleteSignalError() instead")
    void materialsMaterialIdRentalsMaterialRentalIdDeleteSignalE(OAI_expense_files__expense_file_id__put_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void materialsMaterialIdRentalsMaterialRentalIdDeleteSignalError(OAI_expense_files__expense_file_id__put_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use materialsMaterialIdRentalsMaterialRentalIdGetSignalError() instead")
    void materialsMaterialIdRentalsMaterialRentalIdGetSignalE(OAI_materials__material_id__rentals__material_rental_id___get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void materialsMaterialIdRentalsMaterialRentalIdGetSignalError(OAI_materials__material_id__rentals__material_rental_id___get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use materialsMaterialIdRentalsMaterialRentalIdPutSignalError() instead")
    void materialsMaterialIdRentalsMaterialRentalIdPutSignalE(OAI_expense_files__expense_file_id__put_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void materialsMaterialIdRentalsMaterialRentalIdPutSignalError(OAI_expense_files__expense_file_id__put_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use materialsMaterialIdRentalsPostSignalError() instead")
    void materialsMaterialIdRentalsPostSignalE(OAI_clocking_records_post_201_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void materialsMaterialIdRentalsPostSignalError(OAI_clocking_records_post_201_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use materialsMaterialIdRentalsCheckoutPostSignalErrorFull() instead")
    void materialsMaterialIdRentalsCheckoutPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void materialsMaterialIdRentalsCheckoutPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use materialsMaterialIdRentalsGetSignalErrorFull() instead")
    void materialsMaterialIdRentalsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void materialsMaterialIdRentalsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use materialsMaterialIdRentalsMaterialRentalIdDeleteSignalErrorFull() instead")
    void materialsMaterialIdRentalsMaterialRentalIdDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void materialsMaterialIdRentalsMaterialRentalIdDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use materialsMaterialIdRentalsMaterialRentalIdGetSignalErrorFull() instead")
    void materialsMaterialIdRentalsMaterialRentalIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void materialsMaterialIdRentalsMaterialRentalIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use materialsMaterialIdRentalsMaterialRentalIdPutSignalErrorFull() instead")
    void materialsMaterialIdRentalsMaterialRentalIdPutSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void materialsMaterialIdRentalsMaterialRentalIdPutSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use materialsMaterialIdRentalsPostSignalErrorFull() instead")
    void materialsMaterialIdRentalsPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void materialsMaterialIdRentalsPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
