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

#ifndef OAI_OAILoadBalancerActionsApi_H
#define OAI_OAILoadBalancerActionsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIActionResponse.h"
#include "OAIActionsResponse.h"
#include "OAIAddTargetRequest.h"
#include "OAIChangeLoadbalancerDnsPtrRequest.h"
#include "OAIChangeTypeRequest.h"
#include "OAILoadBalancerService.h"
#include "OAIRemoveTargetRequest.h"
#include "OAI_load_balancers__id__actions_attach_to_network_post_request.h"
#include "OAI_load_balancers__id__actions_change_algorithm_post_request.h"
#include "OAI_load_balancers__id__actions_change_protection_post_request.h"
#include "OAI_load_balancers__id__actions_delete_service_post_request.h"
#include "OAI_load_balancers__id__actions_detach_from_network_post_request.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAILoadBalancerActionsApi : public QObject {
    Q_OBJECT

public:
    OAILoadBalancerActionsApi(const int timeOut = 0);
    ~OAILoadBalancerActionsApi();

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
    virtual void loadBalancersIdActionsActionIdGet(const qint32 &id, const qint32 &action_id);

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  oai_load_balancer_service OAILoadBalancerService [optional]
    */
    virtual void loadBalancersIdActionsAddServicePost(const qint32 &id, const ::OpenAPI::OptionalParam<OAILoadBalancerService> &oai_load_balancer_service = ::OpenAPI::OptionalParam<OAILoadBalancerService>());

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  oai_add_target_request OAIAddTargetRequest [optional]
    */
    virtual void loadBalancersIdActionsAddTargetPost(const qint32 &id, const ::OpenAPI::OptionalParam<OAIAddTargetRequest> &oai_add_target_request = ::OpenAPI::OptionalParam<OAIAddTargetRequest>());

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  oai_load_balancers__id__actions_attach_to_network_post_request OAI_load_balancers__id__actions_attach_to_network_post_request [optional]
    */
    virtual void loadBalancersIdActionsAttachToNetworkPost(const qint32 &id, const ::OpenAPI::OptionalParam<OAI_load_balancers__id__actions_attach_to_network_post_request> &oai_load_balancers__id__actions_attach_to_network_post_request = ::OpenAPI::OptionalParam<OAI_load_balancers__id__actions_attach_to_network_post_request>());

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  oai_load_balancers__id__actions_change_algorithm_post_request OAI_load_balancers__id__actions_change_algorithm_post_request [optional]
    */
    virtual void loadBalancersIdActionsChangeAlgorithmPost(const qint32 &id, const ::OpenAPI::OptionalParam<OAI_load_balancers__id__actions_change_algorithm_post_request> &oai_load_balancers__id__actions_change_algorithm_post_request = ::OpenAPI::OptionalParam<OAI_load_balancers__id__actions_change_algorithm_post_request>());

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  oai_change_loadbalancer_dns_ptr_request OAIChangeLoadbalancerDnsPtrRequest [optional]
    */
    virtual void loadBalancersIdActionsChangeDnsPtrPost(const qint32 &id, const ::OpenAPI::OptionalParam<OAIChangeLoadbalancerDnsPtrRequest> &oai_change_loadbalancer_dns_ptr_request = ::OpenAPI::OptionalParam<OAIChangeLoadbalancerDnsPtrRequest>());

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  oai_load_balancers__id__actions_change_protection_post_request OAI_load_balancers__id__actions_change_protection_post_request [optional]
    */
    virtual void loadBalancersIdActionsChangeProtectionPost(const qint32 &id, const ::OpenAPI::OptionalParam<OAI_load_balancers__id__actions_change_protection_post_request> &oai_load_balancers__id__actions_change_protection_post_request = ::OpenAPI::OptionalParam<OAI_load_balancers__id__actions_change_protection_post_request>());

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  oai_change_type_request OAIChangeTypeRequest [optional]
    */
    virtual void loadBalancersIdActionsChangeTypePost(const qint32 &id, const ::OpenAPI::OptionalParam<OAIChangeTypeRequest> &oai_change_type_request = ::OpenAPI::OptionalParam<OAIChangeTypeRequest>());

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  oai_load_balancers__id__actions_delete_service_post_request OAI_load_balancers__id__actions_delete_service_post_request [optional]
    */
    virtual void loadBalancersIdActionsDeleteServicePost(const qint32 &id, const ::OpenAPI::OptionalParam<OAI_load_balancers__id__actions_delete_service_post_request> &oai_load_balancers__id__actions_delete_service_post_request = ::OpenAPI::OptionalParam<OAI_load_balancers__id__actions_delete_service_post_request>());

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  oai_load_balancers__id__actions_detach_from_network_post_request OAI_load_balancers__id__actions_detach_from_network_post_request [optional]
    */
    virtual void loadBalancersIdActionsDetachFromNetworkPost(const qint32 &id, const ::OpenAPI::OptionalParam<OAI_load_balancers__id__actions_detach_from_network_post_request> &oai_load_balancers__id__actions_detach_from_network_post_request = ::OpenAPI::OptionalParam<OAI_load_balancers__id__actions_detach_from_network_post_request>());

    /**
    * @param[in]  id qint32 [required]
    */
    virtual void loadBalancersIdActionsDisablePublicInterfacePost(const qint32 &id);

    /**
    * @param[in]  id qint32 [required]
    */
    virtual void loadBalancersIdActionsEnablePublicInterfacePost(const qint32 &id);

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  sort QString [optional]
    * @param[in]  status QString [optional]
    */
    virtual void loadBalancersIdActionsGet(const qint32 &id, const ::OpenAPI::OptionalParam<QString> &sort = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &status = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  oai_remove_target_request OAIRemoveTargetRequest [optional]
    */
    virtual void loadBalancersIdActionsRemoveTargetPost(const qint32 &id, const ::OpenAPI::OptionalParam<OAIRemoveTargetRequest> &oai_remove_target_request = ::OpenAPI::OptionalParam<OAIRemoveTargetRequest>());

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  oai_load_balancer_service OAILoadBalancerService [optional]
    */
    virtual void loadBalancersIdActionsUpdateServicePost(const qint32 &id, const ::OpenAPI::OptionalParam<OAILoadBalancerService> &oai_load_balancer_service = ::OpenAPI::OptionalParam<OAILoadBalancerService>());


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

    void loadBalancersIdActionsActionIdGetCallback(OAIHttpRequestWorker *worker);
    void loadBalancersIdActionsAddServicePostCallback(OAIHttpRequestWorker *worker);
    void loadBalancersIdActionsAddTargetPostCallback(OAIHttpRequestWorker *worker);
    void loadBalancersIdActionsAttachToNetworkPostCallback(OAIHttpRequestWorker *worker);
    void loadBalancersIdActionsChangeAlgorithmPostCallback(OAIHttpRequestWorker *worker);
    void loadBalancersIdActionsChangeDnsPtrPostCallback(OAIHttpRequestWorker *worker);
    void loadBalancersIdActionsChangeProtectionPostCallback(OAIHttpRequestWorker *worker);
    void loadBalancersIdActionsChangeTypePostCallback(OAIHttpRequestWorker *worker);
    void loadBalancersIdActionsDeleteServicePostCallback(OAIHttpRequestWorker *worker);
    void loadBalancersIdActionsDetachFromNetworkPostCallback(OAIHttpRequestWorker *worker);
    void loadBalancersIdActionsDisablePublicInterfacePostCallback(OAIHttpRequestWorker *worker);
    void loadBalancersIdActionsEnablePublicInterfacePostCallback(OAIHttpRequestWorker *worker);
    void loadBalancersIdActionsGetCallback(OAIHttpRequestWorker *worker);
    void loadBalancersIdActionsRemoveTargetPostCallback(OAIHttpRequestWorker *worker);
    void loadBalancersIdActionsUpdateServicePostCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void loadBalancersIdActionsActionIdGetSignal(OAIActionResponse summary);
    void loadBalancersIdActionsAddServicePostSignal(OAIActionResponse summary);
    void loadBalancersIdActionsAddTargetPostSignal(OAIActionResponse summary);
    void loadBalancersIdActionsAttachToNetworkPostSignal(OAIActionResponse summary);
    void loadBalancersIdActionsChangeAlgorithmPostSignal(OAIActionResponse summary);
    void loadBalancersIdActionsChangeDnsPtrPostSignal(OAIActionResponse summary);
    void loadBalancersIdActionsChangeProtectionPostSignal(OAIActionResponse summary);
    void loadBalancersIdActionsChangeTypePostSignal(OAIActionResponse summary);
    void loadBalancersIdActionsDeleteServicePostSignal(OAIActionResponse summary);
    void loadBalancersIdActionsDetachFromNetworkPostSignal(OAIActionResponse summary);
    void loadBalancersIdActionsDisablePublicInterfacePostSignal(OAIActionResponse summary);
    void loadBalancersIdActionsEnablePublicInterfacePostSignal(OAIActionResponse summary);
    void loadBalancersIdActionsGetSignal(OAIActionsResponse summary);
    void loadBalancersIdActionsRemoveTargetPostSignal(OAIActionResponse summary);
    void loadBalancersIdActionsUpdateServicePostSignal(OAIActionResponse summary);


    void loadBalancersIdActionsActionIdGetSignalFull(OAIHttpRequestWorker *worker, OAIActionResponse summary);
    void loadBalancersIdActionsAddServicePostSignalFull(OAIHttpRequestWorker *worker, OAIActionResponse summary);
    void loadBalancersIdActionsAddTargetPostSignalFull(OAIHttpRequestWorker *worker, OAIActionResponse summary);
    void loadBalancersIdActionsAttachToNetworkPostSignalFull(OAIHttpRequestWorker *worker, OAIActionResponse summary);
    void loadBalancersIdActionsChangeAlgorithmPostSignalFull(OAIHttpRequestWorker *worker, OAIActionResponse summary);
    void loadBalancersIdActionsChangeDnsPtrPostSignalFull(OAIHttpRequestWorker *worker, OAIActionResponse summary);
    void loadBalancersIdActionsChangeProtectionPostSignalFull(OAIHttpRequestWorker *worker, OAIActionResponse summary);
    void loadBalancersIdActionsChangeTypePostSignalFull(OAIHttpRequestWorker *worker, OAIActionResponse summary);
    void loadBalancersIdActionsDeleteServicePostSignalFull(OAIHttpRequestWorker *worker, OAIActionResponse summary);
    void loadBalancersIdActionsDetachFromNetworkPostSignalFull(OAIHttpRequestWorker *worker, OAIActionResponse summary);
    void loadBalancersIdActionsDisablePublicInterfacePostSignalFull(OAIHttpRequestWorker *worker, OAIActionResponse summary);
    void loadBalancersIdActionsEnablePublicInterfacePostSignalFull(OAIHttpRequestWorker *worker, OAIActionResponse summary);
    void loadBalancersIdActionsGetSignalFull(OAIHttpRequestWorker *worker, OAIActionsResponse summary);
    void loadBalancersIdActionsRemoveTargetPostSignalFull(OAIHttpRequestWorker *worker, OAIActionResponse summary);
    void loadBalancersIdActionsUpdateServicePostSignalFull(OAIHttpRequestWorker *worker, OAIActionResponse summary);

    Q_DECL_DEPRECATED_X("Use loadBalancersIdActionsActionIdGetSignalError() instead")
    void loadBalancersIdActionsActionIdGetSignalE(OAIActionResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void loadBalancersIdActionsActionIdGetSignalError(OAIActionResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use loadBalancersIdActionsAddServicePostSignalError() instead")
    void loadBalancersIdActionsAddServicePostSignalE(OAIActionResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void loadBalancersIdActionsAddServicePostSignalError(OAIActionResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use loadBalancersIdActionsAddTargetPostSignalError() instead")
    void loadBalancersIdActionsAddTargetPostSignalE(OAIActionResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void loadBalancersIdActionsAddTargetPostSignalError(OAIActionResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use loadBalancersIdActionsAttachToNetworkPostSignalError() instead")
    void loadBalancersIdActionsAttachToNetworkPostSignalE(OAIActionResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void loadBalancersIdActionsAttachToNetworkPostSignalError(OAIActionResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use loadBalancersIdActionsChangeAlgorithmPostSignalError() instead")
    void loadBalancersIdActionsChangeAlgorithmPostSignalE(OAIActionResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void loadBalancersIdActionsChangeAlgorithmPostSignalError(OAIActionResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use loadBalancersIdActionsChangeDnsPtrPostSignalError() instead")
    void loadBalancersIdActionsChangeDnsPtrPostSignalE(OAIActionResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void loadBalancersIdActionsChangeDnsPtrPostSignalError(OAIActionResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use loadBalancersIdActionsChangeProtectionPostSignalError() instead")
    void loadBalancersIdActionsChangeProtectionPostSignalE(OAIActionResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void loadBalancersIdActionsChangeProtectionPostSignalError(OAIActionResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use loadBalancersIdActionsChangeTypePostSignalError() instead")
    void loadBalancersIdActionsChangeTypePostSignalE(OAIActionResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void loadBalancersIdActionsChangeTypePostSignalError(OAIActionResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use loadBalancersIdActionsDeleteServicePostSignalError() instead")
    void loadBalancersIdActionsDeleteServicePostSignalE(OAIActionResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void loadBalancersIdActionsDeleteServicePostSignalError(OAIActionResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use loadBalancersIdActionsDetachFromNetworkPostSignalError() instead")
    void loadBalancersIdActionsDetachFromNetworkPostSignalE(OAIActionResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void loadBalancersIdActionsDetachFromNetworkPostSignalError(OAIActionResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use loadBalancersIdActionsDisablePublicInterfacePostSignalError() instead")
    void loadBalancersIdActionsDisablePublicInterfacePostSignalE(OAIActionResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void loadBalancersIdActionsDisablePublicInterfacePostSignalError(OAIActionResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use loadBalancersIdActionsEnablePublicInterfacePostSignalError() instead")
    void loadBalancersIdActionsEnablePublicInterfacePostSignalE(OAIActionResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void loadBalancersIdActionsEnablePublicInterfacePostSignalError(OAIActionResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use loadBalancersIdActionsGetSignalError() instead")
    void loadBalancersIdActionsGetSignalE(OAIActionsResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void loadBalancersIdActionsGetSignalError(OAIActionsResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use loadBalancersIdActionsRemoveTargetPostSignalError() instead")
    void loadBalancersIdActionsRemoveTargetPostSignalE(OAIActionResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void loadBalancersIdActionsRemoveTargetPostSignalError(OAIActionResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use loadBalancersIdActionsUpdateServicePostSignalError() instead")
    void loadBalancersIdActionsUpdateServicePostSignalE(OAIActionResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void loadBalancersIdActionsUpdateServicePostSignalError(OAIActionResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use loadBalancersIdActionsActionIdGetSignalErrorFull() instead")
    void loadBalancersIdActionsActionIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void loadBalancersIdActionsActionIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use loadBalancersIdActionsAddServicePostSignalErrorFull() instead")
    void loadBalancersIdActionsAddServicePostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void loadBalancersIdActionsAddServicePostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use loadBalancersIdActionsAddTargetPostSignalErrorFull() instead")
    void loadBalancersIdActionsAddTargetPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void loadBalancersIdActionsAddTargetPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use loadBalancersIdActionsAttachToNetworkPostSignalErrorFull() instead")
    void loadBalancersIdActionsAttachToNetworkPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void loadBalancersIdActionsAttachToNetworkPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use loadBalancersIdActionsChangeAlgorithmPostSignalErrorFull() instead")
    void loadBalancersIdActionsChangeAlgorithmPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void loadBalancersIdActionsChangeAlgorithmPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use loadBalancersIdActionsChangeDnsPtrPostSignalErrorFull() instead")
    void loadBalancersIdActionsChangeDnsPtrPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void loadBalancersIdActionsChangeDnsPtrPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use loadBalancersIdActionsChangeProtectionPostSignalErrorFull() instead")
    void loadBalancersIdActionsChangeProtectionPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void loadBalancersIdActionsChangeProtectionPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use loadBalancersIdActionsChangeTypePostSignalErrorFull() instead")
    void loadBalancersIdActionsChangeTypePostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void loadBalancersIdActionsChangeTypePostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use loadBalancersIdActionsDeleteServicePostSignalErrorFull() instead")
    void loadBalancersIdActionsDeleteServicePostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void loadBalancersIdActionsDeleteServicePostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use loadBalancersIdActionsDetachFromNetworkPostSignalErrorFull() instead")
    void loadBalancersIdActionsDetachFromNetworkPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void loadBalancersIdActionsDetachFromNetworkPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use loadBalancersIdActionsDisablePublicInterfacePostSignalErrorFull() instead")
    void loadBalancersIdActionsDisablePublicInterfacePostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void loadBalancersIdActionsDisablePublicInterfacePostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use loadBalancersIdActionsEnablePublicInterfacePostSignalErrorFull() instead")
    void loadBalancersIdActionsEnablePublicInterfacePostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void loadBalancersIdActionsEnablePublicInterfacePostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use loadBalancersIdActionsGetSignalErrorFull() instead")
    void loadBalancersIdActionsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void loadBalancersIdActionsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use loadBalancersIdActionsRemoveTargetPostSignalErrorFull() instead")
    void loadBalancersIdActionsRemoveTargetPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void loadBalancersIdActionsRemoveTargetPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use loadBalancersIdActionsUpdateServicePostSignalErrorFull() instead")
    void loadBalancersIdActionsUpdateServicePostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void loadBalancersIdActionsUpdateServicePostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
