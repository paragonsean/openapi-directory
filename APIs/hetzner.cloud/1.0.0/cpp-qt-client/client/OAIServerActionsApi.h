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

#ifndef OAI_OAIServerActionsApi_H
#define OAI_OAIServerActionsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIActionResponse.h"
#include "OAIActionsResponse.h"
#include "OAIAddToPlacementGroupRequest.h"
#include "OAIAttachToNetworkRequest.h"
#include "OAICreateImageRequest.h"
#include "OAIDetachFromNetworkRequest.h"
#include "OAIRebuildServerRequest.h"
#include "OAI_servers__id__actions_attach_iso_post_request.h"
#include "OAI_servers__id__actions_change_alias_ips_post_request.h"
#include "OAI_servers__id__actions_change_dns_ptr_post_request.h"
#include "OAI_servers__id__actions_change_protection_post_request.h"
#include "OAI_servers__id__actions_change_type_post_request.h"
#include "OAI_servers__id__actions_create_image_post_201_response.h"
#include "OAI_servers__id__actions_enable_rescue_post_201_response.h"
#include "OAI_servers__id__actions_enable_rescue_post_request.h"
#include "OAI_servers__id__actions_rebuild_post_201_response.h"
#include "OAI_servers__id__actions_request_console_post_201_response.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIServerActionsApi : public QObject {
    Q_OBJECT

public:
    OAIServerActionsApi(const int timeOut = 0);
    ~OAIServerActionsApi();

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
    virtual void serversIdActionsActionIdGet(const qint32 &id, const qint32 &action_id);

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  oai_add_to_placement_group_request OAIAddToPlacementGroupRequest [optional]
    */
    virtual void serversIdActionsAddToPlacementGroupPost(const qint32 &id, const ::OpenAPI::OptionalParam<OAIAddToPlacementGroupRequest> &oai_add_to_placement_group_request = ::OpenAPI::OptionalParam<OAIAddToPlacementGroupRequest>());

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  oai_servers__id__actions_attach_iso_post_request OAI_servers__id__actions_attach_iso_post_request [optional]
    */
    virtual void serversIdActionsAttachIsoPost(const qint32 &id, const ::OpenAPI::OptionalParam<OAI_servers__id__actions_attach_iso_post_request> &oai_servers__id__actions_attach_iso_post_request = ::OpenAPI::OptionalParam<OAI_servers__id__actions_attach_iso_post_request>());

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  oai_attach_to_network_request OAIAttachToNetworkRequest [optional]
    */
    virtual void serversIdActionsAttachToNetworkPost(const qint32 &id, const ::OpenAPI::OptionalParam<OAIAttachToNetworkRequest> &oai_attach_to_network_request = ::OpenAPI::OptionalParam<OAIAttachToNetworkRequest>());

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  oai_servers__id__actions_change_alias_ips_post_request OAI_servers__id__actions_change_alias_ips_post_request [optional]
    */
    virtual void serversIdActionsChangeAliasIpsPost(const qint32 &id, const ::OpenAPI::OptionalParam<OAI_servers__id__actions_change_alias_ips_post_request> &oai_servers__id__actions_change_alias_ips_post_request = ::OpenAPI::OptionalParam<OAI_servers__id__actions_change_alias_ips_post_request>());

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  oai_servers__id__actions_change_dns_ptr_post_request OAI_servers__id__actions_change_dns_ptr_post_request [optional]
    */
    virtual void serversIdActionsChangeDnsPtrPost(const qint32 &id, const ::OpenAPI::OptionalParam<OAI_servers__id__actions_change_dns_ptr_post_request> &oai_servers__id__actions_change_dns_ptr_post_request = ::OpenAPI::OptionalParam<OAI_servers__id__actions_change_dns_ptr_post_request>());

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  oai_servers__id__actions_change_protection_post_request OAI_servers__id__actions_change_protection_post_request [optional]
    */
    virtual void serversIdActionsChangeProtectionPost(const qint32 &id, const ::OpenAPI::OptionalParam<OAI_servers__id__actions_change_protection_post_request> &oai_servers__id__actions_change_protection_post_request = ::OpenAPI::OptionalParam<OAI_servers__id__actions_change_protection_post_request>());

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  oai_servers__id__actions_change_type_post_request OAI_servers__id__actions_change_type_post_request [optional]
    */
    virtual void serversIdActionsChangeTypePost(const qint32 &id, const ::OpenAPI::OptionalParam<OAI_servers__id__actions_change_type_post_request> &oai_servers__id__actions_change_type_post_request = ::OpenAPI::OptionalParam<OAI_servers__id__actions_change_type_post_request>());

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  oai_create_image_request OAICreateImageRequest [optional]
    */
    virtual void serversIdActionsCreateImagePost(const qint32 &id, const ::OpenAPI::OptionalParam<OAICreateImageRequest> &oai_create_image_request = ::OpenAPI::OptionalParam<OAICreateImageRequest>());

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  oai_detach_from_network_request OAIDetachFromNetworkRequest [optional]
    */
    virtual void serversIdActionsDetachFromNetworkPost(const qint32 &id, const ::OpenAPI::OptionalParam<OAIDetachFromNetworkRequest> &oai_detach_from_network_request = ::OpenAPI::OptionalParam<OAIDetachFromNetworkRequest>());

    /**
    * @param[in]  id qint32 [required]
    */
    virtual void serversIdActionsDetachIsoPost(const qint32 &id);

    /**
    * @param[in]  id qint32 [required]
    */
    virtual void serversIdActionsDisableBackupPost(const qint32 &id);

    /**
    * @param[in]  id qint32 [required]
    */
    virtual void serversIdActionsDisableRescuePost(const qint32 &id);

    /**
    * @param[in]  id qint32 [required]
    */
    virtual void serversIdActionsEnableBackupPost(const qint32 &id);

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  oai_servers__id__actions_enable_rescue_post_request OAI_servers__id__actions_enable_rescue_post_request [optional]
    */
    virtual void serversIdActionsEnableRescuePost(const qint32 &id, const ::OpenAPI::OptionalParam<OAI_servers__id__actions_enable_rescue_post_request> &oai_servers__id__actions_enable_rescue_post_request = ::OpenAPI::OptionalParam<OAI_servers__id__actions_enable_rescue_post_request>());

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  sort QString [optional]
    * @param[in]  status QString [optional]
    */
    virtual void serversIdActionsGet(const qint32 &id, const ::OpenAPI::OptionalParam<QString> &sort = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &status = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id qint32 [required]
    */
    virtual void serversIdActionsPoweroffPost(const qint32 &id);

    /**
    * @param[in]  id qint32 [required]
    */
    virtual void serversIdActionsPoweronPost(const qint32 &id);

    /**
    * @param[in]  id qint32 [required]
    */
    virtual void serversIdActionsRebootPost(const qint32 &id);

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  oai_rebuild_server_request OAIRebuildServerRequest [optional]
    */
    virtual void serversIdActionsRebuildPost(const qint32 &id, const ::OpenAPI::OptionalParam<OAIRebuildServerRequest> &oai_rebuild_server_request = ::OpenAPI::OptionalParam<OAIRebuildServerRequest>());

    /**
    * @param[in]  id qint32 [required]
    */
    virtual void serversIdActionsRemoveFromPlacementGroupPost(const qint32 &id);

    /**
    * @param[in]  id qint32 [required]
    */
    virtual void serversIdActionsRequestConsolePost(const qint32 &id);

    /**
    * @param[in]  id qint32 [required]
    */
    virtual void serversIdActionsResetPasswordPost(const qint32 &id);

    /**
    * @param[in]  id qint32 [required]
    */
    virtual void serversIdActionsResetPost(const qint32 &id);

    /**
    * @param[in]  id qint32 [required]
    */
    virtual void serversIdActionsShutdownPost(const qint32 &id);


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

    void serversIdActionsActionIdGetCallback(OAIHttpRequestWorker *worker);
    void serversIdActionsAddToPlacementGroupPostCallback(OAIHttpRequestWorker *worker);
    void serversIdActionsAttachIsoPostCallback(OAIHttpRequestWorker *worker);
    void serversIdActionsAttachToNetworkPostCallback(OAIHttpRequestWorker *worker);
    void serversIdActionsChangeAliasIpsPostCallback(OAIHttpRequestWorker *worker);
    void serversIdActionsChangeDnsPtrPostCallback(OAIHttpRequestWorker *worker);
    void serversIdActionsChangeProtectionPostCallback(OAIHttpRequestWorker *worker);
    void serversIdActionsChangeTypePostCallback(OAIHttpRequestWorker *worker);
    void serversIdActionsCreateImagePostCallback(OAIHttpRequestWorker *worker);
    void serversIdActionsDetachFromNetworkPostCallback(OAIHttpRequestWorker *worker);
    void serversIdActionsDetachIsoPostCallback(OAIHttpRequestWorker *worker);
    void serversIdActionsDisableBackupPostCallback(OAIHttpRequestWorker *worker);
    void serversIdActionsDisableRescuePostCallback(OAIHttpRequestWorker *worker);
    void serversIdActionsEnableBackupPostCallback(OAIHttpRequestWorker *worker);
    void serversIdActionsEnableRescuePostCallback(OAIHttpRequestWorker *worker);
    void serversIdActionsGetCallback(OAIHttpRequestWorker *worker);
    void serversIdActionsPoweroffPostCallback(OAIHttpRequestWorker *worker);
    void serversIdActionsPoweronPostCallback(OAIHttpRequestWorker *worker);
    void serversIdActionsRebootPostCallback(OAIHttpRequestWorker *worker);
    void serversIdActionsRebuildPostCallback(OAIHttpRequestWorker *worker);
    void serversIdActionsRemoveFromPlacementGroupPostCallback(OAIHttpRequestWorker *worker);
    void serversIdActionsRequestConsolePostCallback(OAIHttpRequestWorker *worker);
    void serversIdActionsResetPasswordPostCallback(OAIHttpRequestWorker *worker);
    void serversIdActionsResetPostCallback(OAIHttpRequestWorker *worker);
    void serversIdActionsShutdownPostCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void serversIdActionsActionIdGetSignal(OAIActionResponse summary);
    void serversIdActionsAddToPlacementGroupPostSignal(OAIActionResponse summary);
    void serversIdActionsAttachIsoPostSignal(OAIActionResponse summary);
    void serversIdActionsAttachToNetworkPostSignal(OAIActionResponse summary);
    void serversIdActionsChangeAliasIpsPostSignal(OAIActionResponse summary);
    void serversIdActionsChangeDnsPtrPostSignal(OAIActionResponse summary);
    void serversIdActionsChangeProtectionPostSignal(OAIActionResponse summary);
    void serversIdActionsChangeTypePostSignal(OAIActionResponse summary);
    void serversIdActionsCreateImagePostSignal(OAI_servers__id__actions_create_image_post_201_response summary);
    void serversIdActionsDetachFromNetworkPostSignal(OAIActionResponse summary);
    void serversIdActionsDetachIsoPostSignal(OAIActionResponse summary);
    void serversIdActionsDisableBackupPostSignal(OAIActionResponse summary);
    void serversIdActionsDisableRescuePostSignal(OAIActionResponse summary);
    void serversIdActionsEnableBackupPostSignal(OAIActionResponse summary);
    void serversIdActionsEnableRescuePostSignal(OAI_servers__id__actions_enable_rescue_post_201_response summary);
    void serversIdActionsGetSignal(OAIActionsResponse summary);
    void serversIdActionsPoweroffPostSignal(OAIActionResponse summary);
    void serversIdActionsPoweronPostSignal(OAIActionResponse summary);
    void serversIdActionsRebootPostSignal(OAIActionResponse summary);
    void serversIdActionsRebuildPostSignal(OAI_servers__id__actions_rebuild_post_201_response summary);
    void serversIdActionsRemoveFromPlacementGroupPostSignal(OAIActionResponse summary);
    void serversIdActionsRequestConsolePostSignal(OAI_servers__id__actions_request_console_post_201_response summary);
    void serversIdActionsResetPasswordPostSignal(OAI_servers__id__actions_enable_rescue_post_201_response summary);
    void serversIdActionsResetPostSignal(OAIActionResponse summary);
    void serversIdActionsShutdownPostSignal(OAIActionResponse summary);


    void serversIdActionsActionIdGetSignalFull(OAIHttpRequestWorker *worker, OAIActionResponse summary);
    void serversIdActionsAddToPlacementGroupPostSignalFull(OAIHttpRequestWorker *worker, OAIActionResponse summary);
    void serversIdActionsAttachIsoPostSignalFull(OAIHttpRequestWorker *worker, OAIActionResponse summary);
    void serversIdActionsAttachToNetworkPostSignalFull(OAIHttpRequestWorker *worker, OAIActionResponse summary);
    void serversIdActionsChangeAliasIpsPostSignalFull(OAIHttpRequestWorker *worker, OAIActionResponse summary);
    void serversIdActionsChangeDnsPtrPostSignalFull(OAIHttpRequestWorker *worker, OAIActionResponse summary);
    void serversIdActionsChangeProtectionPostSignalFull(OAIHttpRequestWorker *worker, OAIActionResponse summary);
    void serversIdActionsChangeTypePostSignalFull(OAIHttpRequestWorker *worker, OAIActionResponse summary);
    void serversIdActionsCreateImagePostSignalFull(OAIHttpRequestWorker *worker, OAI_servers__id__actions_create_image_post_201_response summary);
    void serversIdActionsDetachFromNetworkPostSignalFull(OAIHttpRequestWorker *worker, OAIActionResponse summary);
    void serversIdActionsDetachIsoPostSignalFull(OAIHttpRequestWorker *worker, OAIActionResponse summary);
    void serversIdActionsDisableBackupPostSignalFull(OAIHttpRequestWorker *worker, OAIActionResponse summary);
    void serversIdActionsDisableRescuePostSignalFull(OAIHttpRequestWorker *worker, OAIActionResponse summary);
    void serversIdActionsEnableBackupPostSignalFull(OAIHttpRequestWorker *worker, OAIActionResponse summary);
    void serversIdActionsEnableRescuePostSignalFull(OAIHttpRequestWorker *worker, OAI_servers__id__actions_enable_rescue_post_201_response summary);
    void serversIdActionsGetSignalFull(OAIHttpRequestWorker *worker, OAIActionsResponse summary);
    void serversIdActionsPoweroffPostSignalFull(OAIHttpRequestWorker *worker, OAIActionResponse summary);
    void serversIdActionsPoweronPostSignalFull(OAIHttpRequestWorker *worker, OAIActionResponse summary);
    void serversIdActionsRebootPostSignalFull(OAIHttpRequestWorker *worker, OAIActionResponse summary);
    void serversIdActionsRebuildPostSignalFull(OAIHttpRequestWorker *worker, OAI_servers__id__actions_rebuild_post_201_response summary);
    void serversIdActionsRemoveFromPlacementGroupPostSignalFull(OAIHttpRequestWorker *worker, OAIActionResponse summary);
    void serversIdActionsRequestConsolePostSignalFull(OAIHttpRequestWorker *worker, OAI_servers__id__actions_request_console_post_201_response summary);
    void serversIdActionsResetPasswordPostSignalFull(OAIHttpRequestWorker *worker, OAI_servers__id__actions_enable_rescue_post_201_response summary);
    void serversIdActionsResetPostSignalFull(OAIHttpRequestWorker *worker, OAIActionResponse summary);
    void serversIdActionsShutdownPostSignalFull(OAIHttpRequestWorker *worker, OAIActionResponse summary);

    Q_DECL_DEPRECATED_X("Use serversIdActionsActionIdGetSignalError() instead")
    void serversIdActionsActionIdGetSignalE(OAIActionResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsActionIdGetSignalError(OAIActionResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsAddToPlacementGroupPostSignalError() instead")
    void serversIdActionsAddToPlacementGroupPostSignalE(OAIActionResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsAddToPlacementGroupPostSignalError(OAIActionResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsAttachIsoPostSignalError() instead")
    void serversIdActionsAttachIsoPostSignalE(OAIActionResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsAttachIsoPostSignalError(OAIActionResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsAttachToNetworkPostSignalError() instead")
    void serversIdActionsAttachToNetworkPostSignalE(OAIActionResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsAttachToNetworkPostSignalError(OAIActionResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsChangeAliasIpsPostSignalError() instead")
    void serversIdActionsChangeAliasIpsPostSignalE(OAIActionResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsChangeAliasIpsPostSignalError(OAIActionResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsChangeDnsPtrPostSignalError() instead")
    void serversIdActionsChangeDnsPtrPostSignalE(OAIActionResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsChangeDnsPtrPostSignalError(OAIActionResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsChangeProtectionPostSignalError() instead")
    void serversIdActionsChangeProtectionPostSignalE(OAIActionResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsChangeProtectionPostSignalError(OAIActionResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsChangeTypePostSignalError() instead")
    void serversIdActionsChangeTypePostSignalE(OAIActionResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsChangeTypePostSignalError(OAIActionResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsCreateImagePostSignalError() instead")
    void serversIdActionsCreateImagePostSignalE(OAI_servers__id__actions_create_image_post_201_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsCreateImagePostSignalError(OAI_servers__id__actions_create_image_post_201_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsDetachFromNetworkPostSignalError() instead")
    void serversIdActionsDetachFromNetworkPostSignalE(OAIActionResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsDetachFromNetworkPostSignalError(OAIActionResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsDetachIsoPostSignalError() instead")
    void serversIdActionsDetachIsoPostSignalE(OAIActionResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsDetachIsoPostSignalError(OAIActionResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsDisableBackupPostSignalError() instead")
    void serversIdActionsDisableBackupPostSignalE(OAIActionResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsDisableBackupPostSignalError(OAIActionResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsDisableRescuePostSignalError() instead")
    void serversIdActionsDisableRescuePostSignalE(OAIActionResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsDisableRescuePostSignalError(OAIActionResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsEnableBackupPostSignalError() instead")
    void serversIdActionsEnableBackupPostSignalE(OAIActionResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsEnableBackupPostSignalError(OAIActionResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsEnableRescuePostSignalError() instead")
    void serversIdActionsEnableRescuePostSignalE(OAI_servers__id__actions_enable_rescue_post_201_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsEnableRescuePostSignalError(OAI_servers__id__actions_enable_rescue_post_201_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsGetSignalError() instead")
    void serversIdActionsGetSignalE(OAIActionsResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsGetSignalError(OAIActionsResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsPoweroffPostSignalError() instead")
    void serversIdActionsPoweroffPostSignalE(OAIActionResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsPoweroffPostSignalError(OAIActionResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsPoweronPostSignalError() instead")
    void serversIdActionsPoweronPostSignalE(OAIActionResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsPoweronPostSignalError(OAIActionResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsRebootPostSignalError() instead")
    void serversIdActionsRebootPostSignalE(OAIActionResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsRebootPostSignalError(OAIActionResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsRebuildPostSignalError() instead")
    void serversIdActionsRebuildPostSignalE(OAI_servers__id__actions_rebuild_post_201_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsRebuildPostSignalError(OAI_servers__id__actions_rebuild_post_201_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsRemoveFromPlacementGroupPostSignalError() instead")
    void serversIdActionsRemoveFromPlacementGroupPostSignalE(OAIActionResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsRemoveFromPlacementGroupPostSignalError(OAIActionResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsRequestConsolePostSignalError() instead")
    void serversIdActionsRequestConsolePostSignalE(OAI_servers__id__actions_request_console_post_201_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsRequestConsolePostSignalError(OAI_servers__id__actions_request_console_post_201_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsResetPasswordPostSignalError() instead")
    void serversIdActionsResetPasswordPostSignalE(OAI_servers__id__actions_enable_rescue_post_201_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsResetPasswordPostSignalError(OAI_servers__id__actions_enable_rescue_post_201_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsResetPostSignalError() instead")
    void serversIdActionsResetPostSignalE(OAIActionResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsResetPostSignalError(OAIActionResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsShutdownPostSignalError() instead")
    void serversIdActionsShutdownPostSignalE(OAIActionResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsShutdownPostSignalError(OAIActionResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use serversIdActionsActionIdGetSignalErrorFull() instead")
    void serversIdActionsActionIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsActionIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsAddToPlacementGroupPostSignalErrorFull() instead")
    void serversIdActionsAddToPlacementGroupPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsAddToPlacementGroupPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsAttachIsoPostSignalErrorFull() instead")
    void serversIdActionsAttachIsoPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsAttachIsoPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsAttachToNetworkPostSignalErrorFull() instead")
    void serversIdActionsAttachToNetworkPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsAttachToNetworkPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsChangeAliasIpsPostSignalErrorFull() instead")
    void serversIdActionsChangeAliasIpsPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsChangeAliasIpsPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsChangeDnsPtrPostSignalErrorFull() instead")
    void serversIdActionsChangeDnsPtrPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsChangeDnsPtrPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsChangeProtectionPostSignalErrorFull() instead")
    void serversIdActionsChangeProtectionPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsChangeProtectionPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsChangeTypePostSignalErrorFull() instead")
    void serversIdActionsChangeTypePostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsChangeTypePostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsCreateImagePostSignalErrorFull() instead")
    void serversIdActionsCreateImagePostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsCreateImagePostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsDetachFromNetworkPostSignalErrorFull() instead")
    void serversIdActionsDetachFromNetworkPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsDetachFromNetworkPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsDetachIsoPostSignalErrorFull() instead")
    void serversIdActionsDetachIsoPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsDetachIsoPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsDisableBackupPostSignalErrorFull() instead")
    void serversIdActionsDisableBackupPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsDisableBackupPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsDisableRescuePostSignalErrorFull() instead")
    void serversIdActionsDisableRescuePostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsDisableRescuePostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsEnableBackupPostSignalErrorFull() instead")
    void serversIdActionsEnableBackupPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsEnableBackupPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsEnableRescuePostSignalErrorFull() instead")
    void serversIdActionsEnableRescuePostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsEnableRescuePostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsGetSignalErrorFull() instead")
    void serversIdActionsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsPoweroffPostSignalErrorFull() instead")
    void serversIdActionsPoweroffPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsPoweroffPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsPoweronPostSignalErrorFull() instead")
    void serversIdActionsPoweronPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsPoweronPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsRebootPostSignalErrorFull() instead")
    void serversIdActionsRebootPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsRebootPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsRebuildPostSignalErrorFull() instead")
    void serversIdActionsRebuildPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsRebuildPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsRemoveFromPlacementGroupPostSignalErrorFull() instead")
    void serversIdActionsRemoveFromPlacementGroupPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsRemoveFromPlacementGroupPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsRequestConsolePostSignalErrorFull() instead")
    void serversIdActionsRequestConsolePostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsRequestConsolePostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsResetPasswordPostSignalErrorFull() instead")
    void serversIdActionsResetPasswordPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsResetPasswordPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsResetPostSignalErrorFull() instead")
    void serversIdActionsResetPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsResetPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use serversIdActionsShutdownPostSignalErrorFull() instead")
    void serversIdActionsShutdownPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void serversIdActionsShutdownPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
