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

#include "OAI_pricing_get_200_response_pricing.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAI_pricing_get_200_response_pricing::OAI_pricing_get_200_response_pricing(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAI_pricing_get_200_response_pricing::OAI_pricing_get_200_response_pricing() {
    this->initializeModel();
}

OAI_pricing_get_200_response_pricing::~OAI_pricing_get_200_response_pricing() {}

void OAI_pricing_get_200_response_pricing::initializeModel() {

    m_currency_isSet = false;
    m_currency_isValid = false;

    m_floating_ip_isSet = false;
    m_floating_ip_isValid = false;

    m_floating_ips_isSet = false;
    m_floating_ips_isValid = false;

    m_image_isSet = false;
    m_image_isValid = false;

    m_load_balancer_types_isSet = false;
    m_load_balancer_types_isValid = false;

    m_primary_ips_isSet = false;
    m_primary_ips_isValid = false;

    m_server_backup_isSet = false;
    m_server_backup_isValid = false;

    m_server_types_isSet = false;
    m_server_types_isValid = false;

    m_traffic_isSet = false;
    m_traffic_isValid = false;

    m_vat_rate_isSet = false;
    m_vat_rate_isValid = false;

    m_volume_isSet = false;
    m_volume_isValid = false;
}

void OAI_pricing_get_200_response_pricing::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAI_pricing_get_200_response_pricing::fromJsonObject(QJsonObject json) {

    m_currency_isValid = ::OpenAPI::fromJsonValue(m_currency, json[QString("currency")]);
    m_currency_isSet = !json[QString("currency")].isNull() && m_currency_isValid;

    m_floating_ip_isValid = ::OpenAPI::fromJsonValue(m_floating_ip, json[QString("floating_ip")]);
    m_floating_ip_isSet = !json[QString("floating_ip")].isNull() && m_floating_ip_isValid;

    m_floating_ips_isValid = ::OpenAPI::fromJsonValue(m_floating_ips, json[QString("floating_ips")]);
    m_floating_ips_isSet = !json[QString("floating_ips")].isNull() && m_floating_ips_isValid;

    m_image_isValid = ::OpenAPI::fromJsonValue(m_image, json[QString("image")]);
    m_image_isSet = !json[QString("image")].isNull() && m_image_isValid;

    m_load_balancer_types_isValid = ::OpenAPI::fromJsonValue(m_load_balancer_types, json[QString("load_balancer_types")]);
    m_load_balancer_types_isSet = !json[QString("load_balancer_types")].isNull() && m_load_balancer_types_isValid;

    m_primary_ips_isValid = ::OpenAPI::fromJsonValue(m_primary_ips, json[QString("primary_ips")]);
    m_primary_ips_isSet = !json[QString("primary_ips")].isNull() && m_primary_ips_isValid;

    m_server_backup_isValid = ::OpenAPI::fromJsonValue(m_server_backup, json[QString("server_backup")]);
    m_server_backup_isSet = !json[QString("server_backup")].isNull() && m_server_backup_isValid;

    m_server_types_isValid = ::OpenAPI::fromJsonValue(m_server_types, json[QString("server_types")]);
    m_server_types_isSet = !json[QString("server_types")].isNull() && m_server_types_isValid;

    m_traffic_isValid = ::OpenAPI::fromJsonValue(m_traffic, json[QString("traffic")]);
    m_traffic_isSet = !json[QString("traffic")].isNull() && m_traffic_isValid;

    m_vat_rate_isValid = ::OpenAPI::fromJsonValue(m_vat_rate, json[QString("vat_rate")]);
    m_vat_rate_isSet = !json[QString("vat_rate")].isNull() && m_vat_rate_isValid;

    m_volume_isValid = ::OpenAPI::fromJsonValue(m_volume, json[QString("volume")]);
    m_volume_isSet = !json[QString("volume")].isNull() && m_volume_isValid;
}

QString OAI_pricing_get_200_response_pricing::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAI_pricing_get_200_response_pricing::asJsonObject() const {
    QJsonObject obj;
    if (m_currency_isSet) {
        obj.insert(QString("currency"), ::OpenAPI::toJsonValue(m_currency));
    }
    if (m_floating_ip.isSet()) {
        obj.insert(QString("floating_ip"), ::OpenAPI::toJsonValue(m_floating_ip));
    }
    if (m_floating_ips.size() > 0) {
        obj.insert(QString("floating_ips"), ::OpenAPI::toJsonValue(m_floating_ips));
    }
    if (m_image.isSet()) {
        obj.insert(QString("image"), ::OpenAPI::toJsonValue(m_image));
    }
    if (m_load_balancer_types.size() > 0) {
        obj.insert(QString("load_balancer_types"), ::OpenAPI::toJsonValue(m_load_balancer_types));
    }
    if (m_primary_ips.size() > 0) {
        obj.insert(QString("primary_ips"), ::OpenAPI::toJsonValue(m_primary_ips));
    }
    if (m_server_backup.isSet()) {
        obj.insert(QString("server_backup"), ::OpenAPI::toJsonValue(m_server_backup));
    }
    if (m_server_types.size() > 0) {
        obj.insert(QString("server_types"), ::OpenAPI::toJsonValue(m_server_types));
    }
    if (m_traffic.isSet()) {
        obj.insert(QString("traffic"), ::OpenAPI::toJsonValue(m_traffic));
    }
    if (m_vat_rate_isSet) {
        obj.insert(QString("vat_rate"), ::OpenAPI::toJsonValue(m_vat_rate));
    }
    if (m_volume.isSet()) {
        obj.insert(QString("volume"), ::OpenAPI::toJsonValue(m_volume));
    }
    return obj;
}

QString OAI_pricing_get_200_response_pricing::getCurrency() const {
    return m_currency;
}
void OAI_pricing_get_200_response_pricing::setCurrency(const QString &currency) {
    m_currency = currency;
    m_currency_isSet = true;
}

bool OAI_pricing_get_200_response_pricing::is_currency_Set() const{
    return m_currency_isSet;
}

bool OAI_pricing_get_200_response_pricing::is_currency_Valid() const{
    return m_currency_isValid;
}

OAI_pricing_get_200_response_pricing_floating_ip OAI_pricing_get_200_response_pricing::getFloatingIp() const {
    return m_floating_ip;
}
void OAI_pricing_get_200_response_pricing::setFloatingIp(const OAI_pricing_get_200_response_pricing_floating_ip &floating_ip) {
    m_floating_ip = floating_ip;
    m_floating_ip_isSet = true;
}

bool OAI_pricing_get_200_response_pricing::is_floating_ip_Set() const{
    return m_floating_ip_isSet;
}

bool OAI_pricing_get_200_response_pricing::is_floating_ip_Valid() const{
    return m_floating_ip_isValid;
}

QList<OAI_pricing_get_200_response_pricing_floating_ips_inner> OAI_pricing_get_200_response_pricing::getFloatingIps() const {
    return m_floating_ips;
}
void OAI_pricing_get_200_response_pricing::setFloatingIps(const QList<OAI_pricing_get_200_response_pricing_floating_ips_inner> &floating_ips) {
    m_floating_ips = floating_ips;
    m_floating_ips_isSet = true;
}

bool OAI_pricing_get_200_response_pricing::is_floating_ips_Set() const{
    return m_floating_ips_isSet;
}

bool OAI_pricing_get_200_response_pricing::is_floating_ips_Valid() const{
    return m_floating_ips_isValid;
}

OAI_pricing_get_200_response_pricing_image OAI_pricing_get_200_response_pricing::getImage() const {
    return m_image;
}
void OAI_pricing_get_200_response_pricing::setImage(const OAI_pricing_get_200_response_pricing_image &image) {
    m_image = image;
    m_image_isSet = true;
}

bool OAI_pricing_get_200_response_pricing::is_image_Set() const{
    return m_image_isSet;
}

bool OAI_pricing_get_200_response_pricing::is_image_Valid() const{
    return m_image_isValid;
}

QList<OAI_pricing_get_200_response_pricing_load_balancer_types_inner> OAI_pricing_get_200_response_pricing::getLoadBalancerTypes() const {
    return m_load_balancer_types;
}
void OAI_pricing_get_200_response_pricing::setLoadBalancerTypes(const QList<OAI_pricing_get_200_response_pricing_load_balancer_types_inner> &load_balancer_types) {
    m_load_balancer_types = load_balancer_types;
    m_load_balancer_types_isSet = true;
}

bool OAI_pricing_get_200_response_pricing::is_load_balancer_types_Set() const{
    return m_load_balancer_types_isSet;
}

bool OAI_pricing_get_200_response_pricing::is_load_balancer_types_Valid() const{
    return m_load_balancer_types_isValid;
}

QList<OAI_pricing_get_200_response_pricing_primary_ips_inner> OAI_pricing_get_200_response_pricing::getPrimaryIps() const {
    return m_primary_ips;
}
void OAI_pricing_get_200_response_pricing::setPrimaryIps(const QList<OAI_pricing_get_200_response_pricing_primary_ips_inner> &primary_ips) {
    m_primary_ips = primary_ips;
    m_primary_ips_isSet = true;
}

bool OAI_pricing_get_200_response_pricing::is_primary_ips_Set() const{
    return m_primary_ips_isSet;
}

bool OAI_pricing_get_200_response_pricing::is_primary_ips_Valid() const{
    return m_primary_ips_isValid;
}

OAI_pricing_get_200_response_pricing_server_backup OAI_pricing_get_200_response_pricing::getServerBackup() const {
    return m_server_backup;
}
void OAI_pricing_get_200_response_pricing::setServerBackup(const OAI_pricing_get_200_response_pricing_server_backup &server_backup) {
    m_server_backup = server_backup;
    m_server_backup_isSet = true;
}

bool OAI_pricing_get_200_response_pricing::is_server_backup_Set() const{
    return m_server_backup_isSet;
}

bool OAI_pricing_get_200_response_pricing::is_server_backup_Valid() const{
    return m_server_backup_isValid;
}

QList<OAI_pricing_get_200_response_pricing_server_types_inner> OAI_pricing_get_200_response_pricing::getServerTypes() const {
    return m_server_types;
}
void OAI_pricing_get_200_response_pricing::setServerTypes(const QList<OAI_pricing_get_200_response_pricing_server_types_inner> &server_types) {
    m_server_types = server_types;
    m_server_types_isSet = true;
}

bool OAI_pricing_get_200_response_pricing::is_server_types_Set() const{
    return m_server_types_isSet;
}

bool OAI_pricing_get_200_response_pricing::is_server_types_Valid() const{
    return m_server_types_isValid;
}

OAI_pricing_get_200_response_pricing_traffic OAI_pricing_get_200_response_pricing::getTraffic() const {
    return m_traffic;
}
void OAI_pricing_get_200_response_pricing::setTraffic(const OAI_pricing_get_200_response_pricing_traffic &traffic) {
    m_traffic = traffic;
    m_traffic_isSet = true;
}

bool OAI_pricing_get_200_response_pricing::is_traffic_Set() const{
    return m_traffic_isSet;
}

bool OAI_pricing_get_200_response_pricing::is_traffic_Valid() const{
    return m_traffic_isValid;
}

QString OAI_pricing_get_200_response_pricing::getVatRate() const {
    return m_vat_rate;
}
void OAI_pricing_get_200_response_pricing::setVatRate(const QString &vat_rate) {
    m_vat_rate = vat_rate;
    m_vat_rate_isSet = true;
}

bool OAI_pricing_get_200_response_pricing::is_vat_rate_Set() const{
    return m_vat_rate_isSet;
}

bool OAI_pricing_get_200_response_pricing::is_vat_rate_Valid() const{
    return m_vat_rate_isValid;
}

OAI_pricing_get_200_response_pricing_volume OAI_pricing_get_200_response_pricing::getVolume() const {
    return m_volume;
}
void OAI_pricing_get_200_response_pricing::setVolume(const OAI_pricing_get_200_response_pricing_volume &volume) {
    m_volume = volume;
    m_volume_isSet = true;
}

bool OAI_pricing_get_200_response_pricing::is_volume_Set() const{
    return m_volume_isSet;
}

bool OAI_pricing_get_200_response_pricing::is_volume_Valid() const{
    return m_volume_isValid;
}

bool OAI_pricing_get_200_response_pricing::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_currency_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_floating_ip.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_floating_ips.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_image.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_load_balancer_types.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_primary_ips.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_server_backup.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_server_types.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_traffic.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_vat_rate_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_volume.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAI_pricing_get_200_response_pricing::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_currency_isValid && m_floating_ip_isValid && m_floating_ips_isValid && m_image_isValid && m_load_balancer_types_isValid && m_primary_ips_isValid && m_server_backup_isValid && m_server_types_isValid && m_traffic_isValid && m_vat_rate_isValid && m_volume_isValid && true;
}

} // namespace OpenAPI
