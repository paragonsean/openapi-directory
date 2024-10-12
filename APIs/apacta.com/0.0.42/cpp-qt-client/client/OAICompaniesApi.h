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

#ifndef OAI_OAICompaniesApi_H
#define OAI_OAICompaniesApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAICreateSuccessResponse.h"
#include "OAIEmptySuccessResponse.h"
#include "OAIErrorNotFound.h"
#include "OAIErrorValidation.h"
#include "OAIForbiddenError.h"
#include "OAI_companies__company_id__companies_integration_feature_settings_get_200_response.h"
#include "OAI_companies__company_id__companies_integration_feature_settings_post_request.h"
#include "OAI_companies__company_id__form_templates__get_200_response.h"
#include "OAI_companies__company_id__get_200_response.h"
#include "OAI_companies__company_id__integration_feature_settings__integration_feature_setting_id__get_200_response.h"
#include "OAI_companies__company_id__integration_feature_settings_get_200_response.h"
#include "OAI_companies__company_id__integration_settings__companies_integration_setting_id__get_200_response.h"
#include "OAI_companies__company_id__integration_settings_get_200_response.h"
#include "OAI_companies__company_id__integration_settings_post_request.h"
#include "OAI_companies__company_id__price_margins__price_margins_id__get_200_response.h"
#include "OAI_companies__company_id__price_margins__price_margins_id__post_request.h"
#include "OAI_companies_get_200_response.h"
#include "OAI_companies_subscription_self_service_get_200_response.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAICompaniesApi : public QObject {
    Q_OBJECT

public:
    OAICompaniesApi(const int timeOut = 0);
    ~OAICompaniesApi();

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
    * @param[in]  company_id QString [required]
    * @param[in]  c_integration_feature_setting_id QString [required]
    */
    virtual void companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGet(const QString &company_id, const QString &c_integration_feature_setting_id);

    /**
    * @param[in]  company_id QString [required]
    * @param[in]  c_integration_feature_setting_id QString [required]
    */
    virtual void companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPut(const QString &company_id, const QString &c_integration_feature_setting_id);

    /**
    * @param[in]  company_id QString [required]
    */
    virtual void companiesCompanyIdCompaniesIntegrationFeatureSettingsGet(const QString &company_id);

    /**
    * @param[in]  company_id QString [required]
    * @param[in]  oai_companies__company_id__companies_integration_feature_settings_post_request OAI_companies__company_id__companies_integration_feature_settings_post_request [optional]
    */
    virtual void companiesCompanyIdCompaniesIntegrationFeatureSettingsPost(const QString &company_id, const ::OpenAPI::OptionalParam<OAI_companies__company_id__companies_integration_feature_settings_post_request> &oai_companies__company_id__companies_integration_feature_settings_post_request = ::OpenAPI::OptionalParam<OAI_companies__company_id__companies_integration_feature_settings_post_request>());

    /**
    * @param[in]  company_id QString [required]
    * @param[in]  form_template_id QString [required]
    */
    virtual void companiesCompanyIdFormTemplatesFormTemplateIdDelete(const QString &company_id, const QString &form_template_id);

    /**
    * @param[in]  company_id QString [required]
    * @param[in]  id QString [required]
    * @param[in]  form_template_id QString [required]
    */
    virtual void companiesCompanyIdFormTemplatesFormTemplateIdGet(const QString &company_id, const QString &id, const QString &form_template_id);

    /**
    * @param[in]  company_id QString [required]
    * @param[in]  form_template_id QString [required]
    */
    virtual void companiesCompanyIdFormTemplatesGet(const QString &company_id, const QString &form_template_id);

    /**
    * @param[in]  company_id QString [required]
    */
    virtual void companiesCompanyIdGet(const QString &company_id);

    /**
    * @param[in]  company_id QString [required]
    */
    virtual void companiesCompanyIdIntegrationFeatureSettingsGet(const QString &company_id);

    /**
    * @param[in]  company_id QString [required]
    * @param[in]  integration_feature_setting_id QString [required]
    */
    virtual void companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet(const QString &company_id, const QString &integration_feature_setting_id);

    /**
    * @param[in]  company_id QString [required]
    * @param[in]  companies_integration_setting_id QString [required]
    */
    virtual void companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDelete(const QString &company_id, const QString &companies_integration_setting_id);

    /**
    * @param[in]  company_id QString [required]
    * @param[in]  companies_integration_setting_id QString [required]
    */
    virtual void companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet(const QString &company_id, const QString &companies_integration_setting_id);

    /**
    * @param[in]  company_id QString [required]
    * @param[in]  companies_integration_setting_id QString [required]
    */
    virtual void companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPut(const QString &company_id, const QString &companies_integration_setting_id);

    /**
    * @param[in]  company_id QString [required]
    * @param[in]  identifier QString [optional]
    */
    virtual void companiesCompanyIdIntegrationSettingsGet(const QString &company_id, const ::OpenAPI::OptionalParam<QString> &identifier = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  company_id QString [required]
    * @param[in]  oai_companies__company_id__integration_settings_post_request OAI_companies__company_id__integration_settings_post_request [optional]
    */
    virtual void companiesCompanyIdIntegrationSettingsPost(const QString &company_id, const ::OpenAPI::OptionalParam<OAI_companies__company_id__integration_settings_post_request> &oai_companies__company_id__integration_settings_post_request = ::OpenAPI::OptionalParam<OAI_companies__company_id__integration_settings_post_request>());

    /**
    * @param[in]  company_id QString [required]
    * @param[in]  price_margin_id QString [required]
    * @param[in]  price_margins_id QString [required]
    */
    virtual void companiesCompanyIdPriceMarginsPriceMarginsIdDelete(const QString &company_id, const QString &price_margin_id, const QString &price_margins_id);

    /**
    * @param[in]  company_id QString [required]
    * @param[in]  price_margins_id QString [required]
    */
    virtual void companiesCompanyIdPriceMarginsPriceMarginsIdGet(const QString &company_id, const QString &price_margins_id);

    /**
    * @param[in]  company_id QString [required]
    * @param[in]  price_margins_id QString [required]
    * @param[in]  oai_companies__company_id__price_margins__price_margins_id__post_request OAI_companies__company_id__price_margins__price_margins_id__post_request [optional]
    */
    virtual void companiesCompanyIdPriceMarginsPriceMarginsIdPost(const QString &company_id, const QString &price_margins_id, const ::OpenAPI::OptionalParam<OAI_companies__company_id__price_margins__price_margins_id__post_request> &oai_companies__company_id__price_margins__price_margins_id__post_request = ::OpenAPI::OptionalParam<OAI_companies__company_id__price_margins__price_margins_id__post_request>());


    virtual void companiesGet();


    virtual void companiesSubscriptionSelfServiceGet();


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

    void companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGetCallback(OAIHttpRequestWorker *worker);
    void companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPutCallback(OAIHttpRequestWorker *worker);
    void companiesCompanyIdCompaniesIntegrationFeatureSettingsGetCallback(OAIHttpRequestWorker *worker);
    void companiesCompanyIdCompaniesIntegrationFeatureSettingsPostCallback(OAIHttpRequestWorker *worker);
    void companiesCompanyIdFormTemplatesFormTemplateIdDeleteCallback(OAIHttpRequestWorker *worker);
    void companiesCompanyIdFormTemplatesFormTemplateIdGetCallback(OAIHttpRequestWorker *worker);
    void companiesCompanyIdFormTemplatesGetCallback(OAIHttpRequestWorker *worker);
    void companiesCompanyIdGetCallback(OAIHttpRequestWorker *worker);
    void companiesCompanyIdIntegrationFeatureSettingsGetCallback(OAIHttpRequestWorker *worker);
    void companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGetCallback(OAIHttpRequestWorker *worker);
    void companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDeleteCallback(OAIHttpRequestWorker *worker);
    void companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGetCallback(OAIHttpRequestWorker *worker);
    void companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPutCallback(OAIHttpRequestWorker *worker);
    void companiesCompanyIdIntegrationSettingsGetCallback(OAIHttpRequestWorker *worker);
    void companiesCompanyIdIntegrationSettingsPostCallback(OAIHttpRequestWorker *worker);
    void companiesCompanyIdPriceMarginsPriceMarginsIdDeleteCallback(OAIHttpRequestWorker *worker);
    void companiesCompanyIdPriceMarginsPriceMarginsIdGetCallback(OAIHttpRequestWorker *worker);
    void companiesCompanyIdPriceMarginsPriceMarginsIdPostCallback(OAIHttpRequestWorker *worker);
    void companiesGetCallback(OAIHttpRequestWorker *worker);
    void companiesSubscriptionSelfServiceGetCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGetSignal(OAI_companies__company_id__companies_integration_feature_settings_get_200_response summary);
    void companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPutSignal(OAI_companies__company_id__companies_integration_feature_settings_get_200_response summary);
    void companiesCompanyIdCompaniesIntegrationFeatureSettingsGetSignal(OAI_companies__company_id__companies_integration_feature_settings_get_200_response summary);
    void companiesCompanyIdCompaniesIntegrationFeatureSettingsPostSignal(OAICreateSuccessResponse summary);
    void companiesCompanyIdFormTemplatesFormTemplateIdDeleteSignal(OAIEmptySuccessResponse summary);
    void companiesCompanyIdFormTemplatesFormTemplateIdGetSignal(OAI_companies__company_id__form_templates__get_200_response summary);
    void companiesCompanyIdFormTemplatesGetSignal(OAI_companies__company_id__form_templates__get_200_response summary);
    void companiesCompanyIdGetSignal(OAI_companies__company_id__get_200_response summary);
    void companiesCompanyIdIntegrationFeatureSettingsGetSignal(OAI_companies__company_id__integration_feature_settings_get_200_response summary);
    void companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGetSignal(OAI_companies__company_id__integration_feature_settings__integration_feature_setting_id__get_200_response summary);
    void companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDeleteSignal(OAIEmptySuccessResponse summary);
    void companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGetSignal(OAI_companies__company_id__integration_settings__companies_integration_setting_id__get_200_response summary);
    void companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPutSignal(OAIEmptySuccessResponse summary);
    void companiesCompanyIdIntegrationSettingsGetSignal(OAI_companies__company_id__integration_settings_get_200_response summary);
    void companiesCompanyIdIntegrationSettingsPostSignal(OAICreateSuccessResponse summary);
    void companiesCompanyIdPriceMarginsPriceMarginsIdDeleteSignal(OAIEmptySuccessResponse summary);
    void companiesCompanyIdPriceMarginsPriceMarginsIdGetSignal(OAI_companies__company_id__price_margins__price_margins_id__get_200_response summary);
    void companiesCompanyIdPriceMarginsPriceMarginsIdPostSignal(OAICreateSuccessResponse summary);
    void companiesGetSignal(OAI_companies_get_200_response summary);
    void companiesSubscriptionSelfServiceGetSignal(OAI_companies_subscription_self_service_get_200_response summary);


    void companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGetSignalFull(OAIHttpRequestWorker *worker, OAI_companies__company_id__companies_integration_feature_settings_get_200_response summary);
    void companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPutSignalFull(OAIHttpRequestWorker *worker, OAI_companies__company_id__companies_integration_feature_settings_get_200_response summary);
    void companiesCompanyIdCompaniesIntegrationFeatureSettingsGetSignalFull(OAIHttpRequestWorker *worker, OAI_companies__company_id__companies_integration_feature_settings_get_200_response summary);
    void companiesCompanyIdCompaniesIntegrationFeatureSettingsPostSignalFull(OAIHttpRequestWorker *worker, OAICreateSuccessResponse summary);
    void companiesCompanyIdFormTemplatesFormTemplateIdDeleteSignalFull(OAIHttpRequestWorker *worker, OAIEmptySuccessResponse summary);
    void companiesCompanyIdFormTemplatesFormTemplateIdGetSignalFull(OAIHttpRequestWorker *worker, OAI_companies__company_id__form_templates__get_200_response summary);
    void companiesCompanyIdFormTemplatesGetSignalFull(OAIHttpRequestWorker *worker, OAI_companies__company_id__form_templates__get_200_response summary);
    void companiesCompanyIdGetSignalFull(OAIHttpRequestWorker *worker, OAI_companies__company_id__get_200_response summary);
    void companiesCompanyIdIntegrationFeatureSettingsGetSignalFull(OAIHttpRequestWorker *worker, OAI_companies__company_id__integration_feature_settings_get_200_response summary);
    void companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGetSignalFull(OAIHttpRequestWorker *worker, OAI_companies__company_id__integration_feature_settings__integration_feature_setting_id__get_200_response summary);
    void companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDeleteSignalFull(OAIHttpRequestWorker *worker, OAIEmptySuccessResponse summary);
    void companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGetSignalFull(OAIHttpRequestWorker *worker, OAI_companies__company_id__integration_settings__companies_integration_setting_id__get_200_response summary);
    void companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPutSignalFull(OAIHttpRequestWorker *worker, OAIEmptySuccessResponse summary);
    void companiesCompanyIdIntegrationSettingsGetSignalFull(OAIHttpRequestWorker *worker, OAI_companies__company_id__integration_settings_get_200_response summary);
    void companiesCompanyIdIntegrationSettingsPostSignalFull(OAIHttpRequestWorker *worker, OAICreateSuccessResponse summary);
    void companiesCompanyIdPriceMarginsPriceMarginsIdDeleteSignalFull(OAIHttpRequestWorker *worker, OAIEmptySuccessResponse summary);
    void companiesCompanyIdPriceMarginsPriceMarginsIdGetSignalFull(OAIHttpRequestWorker *worker, OAI_companies__company_id__price_margins__price_margins_id__get_200_response summary);
    void companiesCompanyIdPriceMarginsPriceMarginsIdPostSignalFull(OAIHttpRequestWorker *worker, OAICreateSuccessResponse summary);
    void companiesGetSignalFull(OAIHttpRequestWorker *worker, OAI_companies_get_200_response summary);
    void companiesSubscriptionSelfServiceGetSignalFull(OAIHttpRequestWorker *worker, OAI_companies_subscription_self_service_get_200_response summary);

    Q_DECL_DEPRECATED_X("Use companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGetSignalError() instead")
    void companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGetSignalE(OAI_companies__company_id__companies_integration_feature_settings_get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGetSignalError(OAI_companies__company_id__companies_integration_feature_settings_get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPutSignalError() instead")
    void companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPutSignalE(OAI_companies__company_id__companies_integration_feature_settings_get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPutSignalError(OAI_companies__company_id__companies_integration_feature_settings_get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companiesCompanyIdCompaniesIntegrationFeatureSettingsGetSignalError() instead")
    void companiesCompanyIdCompaniesIntegrationFeatureSettingsGetSignalE(OAI_companies__company_id__companies_integration_feature_settings_get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void companiesCompanyIdCompaniesIntegrationFeatureSettingsGetSignalError(OAI_companies__company_id__companies_integration_feature_settings_get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companiesCompanyIdCompaniesIntegrationFeatureSettingsPostSignalError() instead")
    void companiesCompanyIdCompaniesIntegrationFeatureSettingsPostSignalE(OAICreateSuccessResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void companiesCompanyIdCompaniesIntegrationFeatureSettingsPostSignalError(OAICreateSuccessResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companiesCompanyIdFormTemplatesFormTemplateIdDeleteSignalError() instead")
    void companiesCompanyIdFormTemplatesFormTemplateIdDeleteSignalE(OAIEmptySuccessResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void companiesCompanyIdFormTemplatesFormTemplateIdDeleteSignalError(OAIEmptySuccessResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companiesCompanyIdFormTemplatesFormTemplateIdGetSignalError() instead")
    void companiesCompanyIdFormTemplatesFormTemplateIdGetSignalE(OAI_companies__company_id__form_templates__get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void companiesCompanyIdFormTemplatesFormTemplateIdGetSignalError(OAI_companies__company_id__form_templates__get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companiesCompanyIdFormTemplatesGetSignalError() instead")
    void companiesCompanyIdFormTemplatesGetSignalE(OAI_companies__company_id__form_templates__get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void companiesCompanyIdFormTemplatesGetSignalError(OAI_companies__company_id__form_templates__get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companiesCompanyIdGetSignalError() instead")
    void companiesCompanyIdGetSignalE(OAI_companies__company_id__get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void companiesCompanyIdGetSignalError(OAI_companies__company_id__get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companiesCompanyIdIntegrationFeatureSettingsGetSignalError() instead")
    void companiesCompanyIdIntegrationFeatureSettingsGetSignalE(OAI_companies__company_id__integration_feature_settings_get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void companiesCompanyIdIntegrationFeatureSettingsGetSignalError(OAI_companies__company_id__integration_feature_settings_get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGetSignalError() instead")
    void companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGetSignalE(OAI_companies__company_id__integration_feature_settings__integration_feature_setting_id__get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGetSignalError(OAI_companies__company_id__integration_feature_settings__integration_feature_setting_id__get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDeleteSignalError() instead")
    void companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDeleteSignalE(OAIEmptySuccessResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDeleteSignalError(OAIEmptySuccessResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGetSignalError() instead")
    void companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGetSignalE(OAI_companies__company_id__integration_settings__companies_integration_setting_id__get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGetSignalError(OAI_companies__company_id__integration_settings__companies_integration_setting_id__get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPutSignalError() instead")
    void companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPutSignalE(OAIEmptySuccessResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPutSignalError(OAIEmptySuccessResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companiesCompanyIdIntegrationSettingsGetSignalError() instead")
    void companiesCompanyIdIntegrationSettingsGetSignalE(OAI_companies__company_id__integration_settings_get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void companiesCompanyIdIntegrationSettingsGetSignalError(OAI_companies__company_id__integration_settings_get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companiesCompanyIdIntegrationSettingsPostSignalError() instead")
    void companiesCompanyIdIntegrationSettingsPostSignalE(OAICreateSuccessResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void companiesCompanyIdIntegrationSettingsPostSignalError(OAICreateSuccessResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companiesCompanyIdPriceMarginsPriceMarginsIdDeleteSignalError() instead")
    void companiesCompanyIdPriceMarginsPriceMarginsIdDeleteSignalE(OAIEmptySuccessResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void companiesCompanyIdPriceMarginsPriceMarginsIdDeleteSignalError(OAIEmptySuccessResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companiesCompanyIdPriceMarginsPriceMarginsIdGetSignalError() instead")
    void companiesCompanyIdPriceMarginsPriceMarginsIdGetSignalE(OAI_companies__company_id__price_margins__price_margins_id__get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void companiesCompanyIdPriceMarginsPriceMarginsIdGetSignalError(OAI_companies__company_id__price_margins__price_margins_id__get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companiesCompanyIdPriceMarginsPriceMarginsIdPostSignalError() instead")
    void companiesCompanyIdPriceMarginsPriceMarginsIdPostSignalE(OAICreateSuccessResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void companiesCompanyIdPriceMarginsPriceMarginsIdPostSignalError(OAICreateSuccessResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companiesGetSignalError() instead")
    void companiesGetSignalE(OAI_companies_get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void companiesGetSignalError(OAI_companies_get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companiesSubscriptionSelfServiceGetSignalError() instead")
    void companiesSubscriptionSelfServiceGetSignalE(OAI_companies_subscription_self_service_get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void companiesSubscriptionSelfServiceGetSignalError(OAI_companies_subscription_self_service_get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGetSignalErrorFull() instead")
    void companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPutSignalErrorFull() instead")
    void companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPutSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPutSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companiesCompanyIdCompaniesIntegrationFeatureSettingsGetSignalErrorFull() instead")
    void companiesCompanyIdCompaniesIntegrationFeatureSettingsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void companiesCompanyIdCompaniesIntegrationFeatureSettingsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companiesCompanyIdCompaniesIntegrationFeatureSettingsPostSignalErrorFull() instead")
    void companiesCompanyIdCompaniesIntegrationFeatureSettingsPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void companiesCompanyIdCompaniesIntegrationFeatureSettingsPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companiesCompanyIdFormTemplatesFormTemplateIdDeleteSignalErrorFull() instead")
    void companiesCompanyIdFormTemplatesFormTemplateIdDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void companiesCompanyIdFormTemplatesFormTemplateIdDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companiesCompanyIdFormTemplatesFormTemplateIdGetSignalErrorFull() instead")
    void companiesCompanyIdFormTemplatesFormTemplateIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void companiesCompanyIdFormTemplatesFormTemplateIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companiesCompanyIdFormTemplatesGetSignalErrorFull() instead")
    void companiesCompanyIdFormTemplatesGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void companiesCompanyIdFormTemplatesGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companiesCompanyIdGetSignalErrorFull() instead")
    void companiesCompanyIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void companiesCompanyIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companiesCompanyIdIntegrationFeatureSettingsGetSignalErrorFull() instead")
    void companiesCompanyIdIntegrationFeatureSettingsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void companiesCompanyIdIntegrationFeatureSettingsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGetSignalErrorFull() instead")
    void companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDeleteSignalErrorFull() instead")
    void companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGetSignalErrorFull() instead")
    void companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPutSignalErrorFull() instead")
    void companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPutSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPutSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companiesCompanyIdIntegrationSettingsGetSignalErrorFull() instead")
    void companiesCompanyIdIntegrationSettingsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void companiesCompanyIdIntegrationSettingsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companiesCompanyIdIntegrationSettingsPostSignalErrorFull() instead")
    void companiesCompanyIdIntegrationSettingsPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void companiesCompanyIdIntegrationSettingsPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companiesCompanyIdPriceMarginsPriceMarginsIdDeleteSignalErrorFull() instead")
    void companiesCompanyIdPriceMarginsPriceMarginsIdDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void companiesCompanyIdPriceMarginsPriceMarginsIdDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companiesCompanyIdPriceMarginsPriceMarginsIdGetSignalErrorFull() instead")
    void companiesCompanyIdPriceMarginsPriceMarginsIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void companiesCompanyIdPriceMarginsPriceMarginsIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companiesCompanyIdPriceMarginsPriceMarginsIdPostSignalErrorFull() instead")
    void companiesCompanyIdPriceMarginsPriceMarginsIdPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void companiesCompanyIdPriceMarginsPriceMarginsIdPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companiesGetSignalErrorFull() instead")
    void companiesGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void companiesGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companiesSubscriptionSelfServiceGetSignalErrorFull() instead")
    void companiesSubscriptionSelfServiceGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void companiesSubscriptionSelfServiceGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
