/**
 * Hetzner Cloud API
 * This is the official API documentation for the Public Hetzner Cloud.  ## Introduction  The Hetzner Cloud API operates over HTTPS and uses JSON as its data format. The API is a RESTful API and utilizes HTTP methods and HTTP status codes to specify requests and responses.  As an alternative to working directly with our API you may also consider to use: * Our CLI program [hcloud](https://github.com/hetznercloud/cli) * Our [library for Go](https://github.com/hetznercloud/hcloud-go) * Our [library for Python](https://github.com/hetznercloud/hcloud-python)  Also you can find a [list of libraries, tools, and integrations on GitHub](https://github.com/hetznercloud/awesome-hcloud).  If you are developing integrations based on our API and your product is Open Source you may be eligible for a free one time €50 (excl. VAT) credit on your account. Please contact us via the the support page on your Cloud Console and let us know the following: * The type of integration you would like to develop * Link to the GitHub repo you will use for the Project * Link to some other Open Source work you have already done (if you have done so)  ## Getting Started To get started using the API you first need an API token. Sign in into the [Hetzner Cloud Console](https://console.hetzner.cloud/) choose a Project, go to `Security` → `API Tokens`, and generate a new token. Make sure to copy the token because it won’t be shown to you again. A token is bound to a Project, to interact with the API of another Project you have to create a new token inside the Project. Let’s say your new token is `jEheVytlAoFl7F8MqUQ7jAo2hOXASztX`.  You’re now ready to do your first request against the API. To get a list of all Servers in your Project, issue the example request on the right side using [curl](https://curl.haxx.se/).  Make sure to replace the token in the example command with the token you have just created. Since your Project probably does not contain any Servers yet, the example response will look like the response on the right side. We will almost always provide a resource root like `servers` inside the example response. A response can also contain a `meta` object with information like [Pagination](https://docs.hetzner.cloud/#overview-pagination).  **Example Request** ```bash curl -H \"Authorization: Bearer jEheVytlAoFl7F8MqUQ7jAo2hOXASztX\" \\     https://api.hetzner.cloud/v1/servers ```  **Example Response** ```json {     \"servers\": [],     \"meta\": {         \"pagination\": {             \"page\": 1,             \"per_page\": 25,             \"previous_page\": null,             \"next_page\": null,             \"last_page\": 1,             \"total_entries\": 0         }     } } ```  ## Authentication All requests to the Hetzner Cloud API must be authenticated via a API token. Include your secret API token in every request you send to the API with the `Authorization` HTTP header.  To create a new API token for your Project, switch into the [Hetzner Cloud Console](https://console.hetzner.cloud/) choose a Project, go to `Security` → `API Tokens`, and generate a new token.  **Example Authorization header** ```html Authorization: Bearer LRK9DAWQ1ZAEFSrCNEEzLCUwhYX1U3g7wMg4dTlkkDC96fyDuyJ39nVbVjCKSDfj ```  ## Errors Errors are indicated by HTTP status codes. Further, the response of the request which generated the error contains an error code, an error message, and, optionally, error details. The schema of the error details object depends on the error code.  The error response contains the following keys:  | Keys      | Meaning                                                               | |-----------|-----------------------------------------------------------------------| | `code`    | Short string indicating the type of error (machine-parsable)          | | `message` | Textual description on what has gone wrong                            | | `details` | An object providing for details on the error (schema depends on code) |  **Example response** ```json {   \"error\": {     \"code\": \"invalid_input\",     \"message\": \"invalid input in field 'broken_field': is too long\",     \"details\": {       \"fields\": [         {           \"name\": \"broken_field\",           \"messages\": [\"is too long\"]         }       ]     }   } } ```  ### Error Codes  | Code                      | Description                                                                      | |---------------------------|----------------------------------------------------------------------------------| | `forbidden`               | Insufficient permissions for this request                                        | | `invalid_input`           | Error while parsing or processing the input                                      | | `json_error`              | Invalid JSON input in your request                                               | | `locked`                  | The item you are trying to access is locked (there is already an Action running) | | `not_found`               | Entity not found                                                                 | | `rate_limit_exceeded`     | Error when sending too many requests                                             | | `resource_limit_exceeded` | Error when exceeding the maximum quantity of a resource for an account           | | `resource_unavailable`    | The requested resource is currently unavailable                                  | | `service_error`           | Error within a service                                                           | | `uniqueness_error`        | One or more of the objects fields must be unique                                 | | `protected`               | The Action you are trying to start is protected for this resource                | | `maintenance`             | Cannot perform operation due to maintenance                                      | | `conflict`                | The resource has changed during the request, please retry                        | | `unsupported_error`       | The corresponding resource does not support the Action                           | | `token_readonly`          | The token is only allowed to perform GET requests                                | | `unavailable`             | A service or product is currently not available                                  |  **invalid_input** ```json {   \"error\": {     \"code\": \"invalid_input\",     \"message\": \"invalid input in field 'broken_field': is too long\",     \"details\": {       \"fields\": [         {           \"name\": \"broken_field\",           \"messages\": [\"is too long\"]         }       ]     }   } } ```  **uniqueness_error** ```json {   \"error\": {     \"code\": \"uniqueness_error\",     \"message\": \"SSH key with the same fingerprint already exists\",     \"details\": {       \"fields\": [         {           \"name\": \"public_key\"         }       ]     }   } } ```  **resource_limit_exceeded** ```json {   \"error\": {     \"code\": \"resource_limit_exceeded\",     \"message\": \"project limit exceeded\",     \"details\": {       \"limits\": [         {           \"name\": \"project_limit\"         }       ]     }   } } ```  ## Labels Labels are `key/value` pairs that can be attached to all resources.  Valid label keys have two segments: an optional prefix and name, separated by a slash (`/`). The name segment is required and must be a string of 63 characters or less, beginning and ending with an alphanumeric character (`[a-z0-9A-Z]`) with dashes (`-`), underscores (`_`), dots (`.`), and alphanumerics between. The prefix is optional. If specified, the prefix must be a DNS subdomain: a series of DNS labels separated by dots (`.`), not longer than 253 characters in total, followed by a slash (`/`).  Valid label values must be a string of 63 characters or less and must be empty or begin and end with an alphanumeric character (`[a-z0-9A-Z]`) with dashes (`-`), underscores (`_`), dots (`.`), and alphanumerics between.  The `hetzner.cloud/` prefix is reserved and cannot be used.  **Example Labels** ```json {   \"labels\": {     \"environment\":\"development\",     \"service\":\"backend\",     \"example.com/my\":\"label\",     \"just-a-key\":\"\"   } } ```  ## Label Selector For resources with labels, you can filter resources by their labels using the label selector query language.  | Expression           | Meaning                                                             | |----------------------|---------------------------------------------------------------------| | `k==v` / `k=v`       | Value of key `k` does equal value `v`                               | | `k!=v`               | Value of key `k` does not equal value `v`                           | | `k`                  | Key `k` is present                                                  | | `!k`                 | Key `k` is not present                                              | | `k in (v1,v2,v3)`    | Value of key `k` is `v1`, `v2`, or `v3`                             | | `k notin (v1,v2,v3)` | Value of key `k` is neither `v1`, nor `v2`, nor `v3`                | | `k1==v,!k2`          | Value of key `k1` is `v` and key `k2` is not present                |  ### Examples * Returns all resources that have a `env=production` label and that don't have a `type=database` label:    `env=production,type!=database` * Returns all resources that have a `env=testing` or `env=staging` label:      `env in (testing,staging)` * Returns all resources that don't have a `type` label:      `!type`  ## Pagination Responses which return multiple items support pagination. If they do support pagination, it can be controlled with following query string parameters:  * A `page` parameter specifies the page to fetch. The number of the first page is 1. * A `per_page` parameter specifies the number of items returned per page. The default value is 25, the maximum value is 50 except otherwise specified in the documentation.  Responses contain a `Link` header with pagination information.  Additionally, if the response body is JSON and the root object is an object, that object has a `pagination` object inside the `meta` object with pagination information:  **Example Pagination** ```json {     \"servers\": [...],     \"meta\": {         \"pagination\": {             \"page\": 2,             \"per_page\": 25,             \"previous_page\": 1,             \"next_page\": 3,             \"last_page\": 4,             \"total_entries\": 100         }     } } ```  The keys `previous_page`, `next_page`, `last_page`, and `total_entries` may be `null` when on the first page, last page, or when the total number of entries is unknown.  **Example Pagination Link header** ```bash Link: <https://api.hetzner.cloud/v1/actions?page=2&per_page=5>; rel=\"prev\",       <https://api.hetzner.cloud/v1/actions?page=4&per_page=5>; rel=\"next\",       <https://api.hetzner.cloud/v1/actions?page=6&per_page=5>; rel=\"last\" ```  Line breaks have been added for display purposes only and responses may only contain some of the above `rel` values.  ## Rate Limiting All requests, whether they are authenticated or not, are subject to rate limiting. If you have reached your limit, your requests will be handled with a `429 Too Many Requests` error. Burst requests are allowed. Responses contain serveral headers which provide information about your current rate limit status.  * The `RateLimit-Limit` header contains the total number of requests you can perform per hour. * The `RateLimit-Remaining` header contains the number of requests remaining in the current rate limit time frame. * The `RateLimit-Reset` header contains a UNIX timestamp of the point in time when your rate limit will have recovered and you will have the full number of requests available again.  The default limit is 3600 requests per hour and per Project. The number of remaining requests increases gradually. For example, when your limit is 3600 requests per hour, the number of remaining requests will increase by 1 every second.  ## Server Metadata Your Server can discover metadata about itself by doing a HTTP request to specific URLs. The following data is available:  | Data              | Format | Contents                                                     | |-------------------|--------|--------------------------------------------------------------| | hostname          | text   | Name of the Server as set in the api                         | | instance-id       | number | ID of the server                                             | | public-ipv4       | text   | Primary public IPv4 address                                  | | private-networks  | yaml   | Details about the private networks the Server is attached to | | availability-zone | text   | Name of the availability zone that Server runs in            | | region            | text   | Network zone, e.g. eu-central                                |  **Example: Summary** ```bash $ curl http://169.254.169.254/hetzner/v1/metadata ```  ```yaml availability-zone: hel1-dc2 hostname: my-server instance-id: 42 public-ipv4: 1.2.3.4 region: eu-central ```  **Example: Hostname** ```bash $ curl http://169.254.169.254/hetzner/v1/metadata/hostname my-server ```  **Example: Instance ID** ```bash $ curl http://169.254.169.254/hetzner/v1/metadata/instance-id 42 ```  **Example: Public IPv4** ```bash $ curl http://169.254.169.254/hetzner/v1/metadata/public-ipv4 1.2.3.4 ```  **Example: Private Networks** ```bash $ curl http://169.254.169.254/hetzner/v1/metadata/private-networks ```  ```json - ip: 10.0.0.2   alias_ips: [10.0.0.3, 10.0.0.4]   interface_num: 1   mac_address: 86:00:00:2a:7d:e0   network_id: 1234   network_name: nw-test1   network: 10.0.0.0/8   subnet: 10.0.0.0/24   gateway: 10.0.0.1 - ip: 192.168.0.2   alias_ips: []   interface_num: 2   mac_address: 86:00:00:2a:7d:e1   network_id: 4321   network_name: nw-test2   network: 192.168.0.0/16   subnet: 192.168.0.0/24   gateway: 192.168.0.1 ```  **Example: Availability Zone** ```bash $ curl http://169.254.169.254/hetzner/v1/metadata/availability-zone hel1-dc2 ```  **Example: Region** ```bash $ curl http://169.254.169.254/hetzner/v1/metadata/region eu-central ```  ## Sorting Some responses which return multiple items support sorting. If they do support sorting the documentation states which fields can be used for sorting. You specify sorting with the `sort` query string parameter. You can sort by multiple fields. You can set the sort direction by appending `:asc` or `:desc` to the field name. By default, ascending sorting is used.  **Example: Sorting** ```bash https://api.hetzner.cloud/v1/actions?sort=status https://api.hetzner.cloud/v1/actions?sort=status:asc https://api.hetzner.cloud/v1/actions?sort=status:desc https://api.hetzner.cloud/v1/actions?sort=status:asc&sort=command:desc ``` 
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAINetworkActionsApi_H
#define OAI_OAINetworkActionsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIActionResponse.h"
#include "OAIActionsResponse.h"
#include "OAIAddDeleteRouteRequest.h"
#include "OAIAddSubnetRequest.h"
#include "OAIChangeIPRangeRequest.h"
#include "OAIChangeProtectionRequest_1.h"
#include "OAIDeleteSubnetRequest.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAINetworkActionsApi : public QObject {
    Q_OBJECT

public:
    OAINetworkActionsApi(const int timeOut = 0);
    ~OAINetworkActionsApi();

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
    * @param[in]  id qint32 [required]
    * @param[in]  action_id qint32 [required]
    */
    virtual void networksIdActionsActionIdGet(const qint32 &id, const qint32 &action_id);

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  oai_add_delete_route_request OAIAddDeleteRouteRequest [optional]
    */
    virtual void networksIdActionsAddRoutePost(const qint32 &id, const ::OpenAPI::OptionalParam<OAIAddDeleteRouteRequest> &oai_add_delete_route_request = ::OpenAPI::OptionalParam<OAIAddDeleteRouteRequest>());

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  oai_add_subnet_request OAIAddSubnetRequest [optional]
    */
    virtual void networksIdActionsAddSubnetPost(const qint32 &id, const ::OpenAPI::OptionalParam<OAIAddSubnetRequest> &oai_add_subnet_request = ::OpenAPI::OptionalParam<OAIAddSubnetRequest>());

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  oai_change_ip_range_request OAIChangeIPRangeRequest [optional]
    */
    virtual void networksIdActionsChangeIpRangePost(const qint32 &id, const ::OpenAPI::OptionalParam<OAIChangeIPRangeRequest> &oai_change_ip_range_request = ::OpenAPI::OptionalParam<OAIChangeIPRangeRequest>());

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  oai_change_protection_request_1 OAIChangeProtectionRequest_1 [optional]
    */
    virtual void networksIdActionsChangeProtectionPost(const qint32 &id, const ::OpenAPI::OptionalParam<OAIChangeProtectionRequest_1> &oai_change_protection_request_1 = ::OpenAPI::OptionalParam<OAIChangeProtectionRequest_1>());

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  oai_add_delete_route_request OAIAddDeleteRouteRequest [optional]
    */
    virtual void networksIdActionsDeleteRoutePost(const qint32 &id, const ::OpenAPI::OptionalParam<OAIAddDeleteRouteRequest> &oai_add_delete_route_request = ::OpenAPI::OptionalParam<OAIAddDeleteRouteRequest>());

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  oai_delete_subnet_request OAIDeleteSubnetRequest [optional]
    */
    virtual void networksIdActionsDeleteSubnetPost(const qint32 &id, const ::OpenAPI::OptionalParam<OAIDeleteSubnetRequest> &oai_delete_subnet_request = ::OpenAPI::OptionalParam<OAIDeleteSubnetRequest>());

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  sort QString [optional]
    * @param[in]  status QString [optional]
    */
    virtual void networksIdActionsGet(const qint32 &id, const ::OpenAPI::OptionalParam<QString> &sort = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &status = ::OpenAPI::OptionalParam<QString>());


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

    void networksIdActionsActionIdGetCallback(OAIHttpRequestWorker *worker);
    void networksIdActionsAddRoutePostCallback(OAIHttpRequestWorker *worker);
    void networksIdActionsAddSubnetPostCallback(OAIHttpRequestWorker *worker);
    void networksIdActionsChangeIpRangePostCallback(OAIHttpRequestWorker *worker);
    void networksIdActionsChangeProtectionPostCallback(OAIHttpRequestWorker *worker);
    void networksIdActionsDeleteRoutePostCallback(OAIHttpRequestWorker *worker);
    void networksIdActionsDeleteSubnetPostCallback(OAIHttpRequestWorker *worker);
    void networksIdActionsGetCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void networksIdActionsActionIdGetSignal(OAIActionResponse summary);
    void networksIdActionsAddRoutePostSignal(OAIActionResponse summary);
    void networksIdActionsAddSubnetPostSignal(OAIActionResponse summary);
    void networksIdActionsChangeIpRangePostSignal(OAIActionResponse summary);
    void networksIdActionsChangeProtectionPostSignal(OAIActionResponse summary);
    void networksIdActionsDeleteRoutePostSignal(OAIActionResponse summary);
    void networksIdActionsDeleteSubnetPostSignal(OAIActionResponse summary);
    void networksIdActionsGetSignal(OAIActionsResponse summary);


    void networksIdActionsActionIdGetSignalFull(OAIHttpRequestWorker *worker, OAIActionResponse summary);
    void networksIdActionsAddRoutePostSignalFull(OAIHttpRequestWorker *worker, OAIActionResponse summary);
    void networksIdActionsAddSubnetPostSignalFull(OAIHttpRequestWorker *worker, OAIActionResponse summary);
    void networksIdActionsChangeIpRangePostSignalFull(OAIHttpRequestWorker *worker, OAIActionResponse summary);
    void networksIdActionsChangeProtectionPostSignalFull(OAIHttpRequestWorker *worker, OAIActionResponse summary);
    void networksIdActionsDeleteRoutePostSignalFull(OAIHttpRequestWorker *worker, OAIActionResponse summary);
    void networksIdActionsDeleteSubnetPostSignalFull(OAIHttpRequestWorker *worker, OAIActionResponse summary);
    void networksIdActionsGetSignalFull(OAIHttpRequestWorker *worker, OAIActionsResponse summary);

    Q_DECL_DEPRECATED_X("Use networksIdActionsActionIdGetSignalError() instead")
    void networksIdActionsActionIdGetSignalE(OAIActionResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void networksIdActionsActionIdGetSignalError(OAIActionResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use networksIdActionsAddRoutePostSignalError() instead")
    void networksIdActionsAddRoutePostSignalE(OAIActionResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void networksIdActionsAddRoutePostSignalError(OAIActionResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use networksIdActionsAddSubnetPostSignalError() instead")
    void networksIdActionsAddSubnetPostSignalE(OAIActionResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void networksIdActionsAddSubnetPostSignalError(OAIActionResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use networksIdActionsChangeIpRangePostSignalError() instead")
    void networksIdActionsChangeIpRangePostSignalE(OAIActionResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void networksIdActionsChangeIpRangePostSignalError(OAIActionResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use networksIdActionsChangeProtectionPostSignalError() instead")
    void networksIdActionsChangeProtectionPostSignalE(OAIActionResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void networksIdActionsChangeProtectionPostSignalError(OAIActionResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use networksIdActionsDeleteRoutePostSignalError() instead")
    void networksIdActionsDeleteRoutePostSignalE(OAIActionResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void networksIdActionsDeleteRoutePostSignalError(OAIActionResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use networksIdActionsDeleteSubnetPostSignalError() instead")
    void networksIdActionsDeleteSubnetPostSignalE(OAIActionResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void networksIdActionsDeleteSubnetPostSignalError(OAIActionResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use networksIdActionsGetSignalError() instead")
    void networksIdActionsGetSignalE(OAIActionsResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void networksIdActionsGetSignalError(OAIActionsResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use networksIdActionsActionIdGetSignalErrorFull() instead")
    void networksIdActionsActionIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void networksIdActionsActionIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use networksIdActionsAddRoutePostSignalErrorFull() instead")
    void networksIdActionsAddRoutePostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void networksIdActionsAddRoutePostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use networksIdActionsAddSubnetPostSignalErrorFull() instead")
    void networksIdActionsAddSubnetPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void networksIdActionsAddSubnetPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use networksIdActionsChangeIpRangePostSignalErrorFull() instead")
    void networksIdActionsChangeIpRangePostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void networksIdActionsChangeIpRangePostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use networksIdActionsChangeProtectionPostSignalErrorFull() instead")
    void networksIdActionsChangeProtectionPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void networksIdActionsChangeProtectionPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use networksIdActionsDeleteRoutePostSignalErrorFull() instead")
    void networksIdActionsDeleteRoutePostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void networksIdActionsDeleteRoutePostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use networksIdActionsDeleteSubnetPostSignalErrorFull() instead")
    void networksIdActionsDeleteSubnetPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void networksIdActionsDeleteSubnetPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use networksIdActionsGetSignalErrorFull() instead")
    void networksIdActionsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void networksIdActionsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
