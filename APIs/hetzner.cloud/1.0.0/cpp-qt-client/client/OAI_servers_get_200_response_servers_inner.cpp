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

#include "OAI_servers_get_200_response_servers_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAI_servers_get_200_response_servers_inner::OAI_servers_get_200_response_servers_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAI_servers_get_200_response_servers_inner::OAI_servers_get_200_response_servers_inner() {
    this->initializeModel();
}

OAI_servers_get_200_response_servers_inner::~OAI_servers_get_200_response_servers_inner() {}

void OAI_servers_get_200_response_servers_inner::initializeModel() {

    m_backup_window_isSet = false;
    m_backup_window_isValid = false;

    m_created_isSet = false;
    m_created_isValid = false;

    m_datacenter_isSet = false;
    m_datacenter_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_image_isSet = false;
    m_image_isValid = false;

    m_included_traffic_isSet = false;
    m_included_traffic_isValid = false;

    m_ingoing_traffic_isSet = false;
    m_ingoing_traffic_isValid = false;

    m_iso_isSet = false;
    m_iso_isValid = false;

    m_labels_isSet = false;
    m_labels_isValid = false;

    m_load_balancers_isSet = false;
    m_load_balancers_isValid = false;

    m_locked_isSet = false;
    m_locked_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_outgoing_traffic_isSet = false;
    m_outgoing_traffic_isValid = false;

    m_placement_group_isSet = false;
    m_placement_group_isValid = false;

    m_primary_disk_size_isSet = false;
    m_primary_disk_size_isValid = false;

    m_private_net_isSet = false;
    m_private_net_isValid = false;

    m_protection_isSet = false;
    m_protection_isValid = false;

    m_public_net_isSet = false;
    m_public_net_isValid = false;

    m_rescue_enabled_isSet = false;
    m_rescue_enabled_isValid = false;

    m_server_type_isSet = false;
    m_server_type_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_volumes_isSet = false;
    m_volumes_isValid = false;
}

void OAI_servers_get_200_response_servers_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAI_servers_get_200_response_servers_inner::fromJsonObject(QJsonObject json) {

    m_backup_window_isValid = ::OpenAPI::fromJsonValue(m_backup_window, json[QString("backup_window")]);
    m_backup_window_isSet = !json[QString("backup_window")].isNull() && m_backup_window_isValid;

    m_created_isValid = ::OpenAPI::fromJsonValue(m_created, json[QString("created")]);
    m_created_isSet = !json[QString("created")].isNull() && m_created_isValid;

    m_datacenter_isValid = ::OpenAPI::fromJsonValue(m_datacenter, json[QString("datacenter")]);
    m_datacenter_isSet = !json[QString("datacenter")].isNull() && m_datacenter_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_image_isValid = ::OpenAPI::fromJsonValue(m_image, json[QString("image")]);
    m_image_isSet = !json[QString("image")].isNull() && m_image_isValid;

    m_included_traffic_isValid = ::OpenAPI::fromJsonValue(m_included_traffic, json[QString("included_traffic")]);
    m_included_traffic_isSet = !json[QString("included_traffic")].isNull() && m_included_traffic_isValid;

    m_ingoing_traffic_isValid = ::OpenAPI::fromJsonValue(m_ingoing_traffic, json[QString("ingoing_traffic")]);
    m_ingoing_traffic_isSet = !json[QString("ingoing_traffic")].isNull() && m_ingoing_traffic_isValid;

    m_iso_isValid = ::OpenAPI::fromJsonValue(m_iso, json[QString("iso")]);
    m_iso_isSet = !json[QString("iso")].isNull() && m_iso_isValid;

    m_labels_isValid = ::OpenAPI::fromJsonValue(m_labels, json[QString("labels")]);
    m_labels_isSet = !json[QString("labels")].isNull() && m_labels_isValid;

    m_load_balancers_isValid = ::OpenAPI::fromJsonValue(m_load_balancers, json[QString("load_balancers")]);
    m_load_balancers_isSet = !json[QString("load_balancers")].isNull() && m_load_balancers_isValid;

    m_locked_isValid = ::OpenAPI::fromJsonValue(m_locked, json[QString("locked")]);
    m_locked_isSet = !json[QString("locked")].isNull() && m_locked_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_outgoing_traffic_isValid = ::OpenAPI::fromJsonValue(m_outgoing_traffic, json[QString("outgoing_traffic")]);
    m_outgoing_traffic_isSet = !json[QString("outgoing_traffic")].isNull() && m_outgoing_traffic_isValid;

    m_placement_group_isValid = ::OpenAPI::fromJsonValue(m_placement_group, json[QString("placement_group")]);
    m_placement_group_isSet = !json[QString("placement_group")].isNull() && m_placement_group_isValid;

    m_primary_disk_size_isValid = ::OpenAPI::fromJsonValue(m_primary_disk_size, json[QString("primary_disk_size")]);
    m_primary_disk_size_isSet = !json[QString("primary_disk_size")].isNull() && m_primary_disk_size_isValid;

    m_private_net_isValid = ::OpenAPI::fromJsonValue(m_private_net, json[QString("private_net")]);
    m_private_net_isSet = !json[QString("private_net")].isNull() && m_private_net_isValid;

    m_protection_isValid = ::OpenAPI::fromJsonValue(m_protection, json[QString("protection")]);
    m_protection_isSet = !json[QString("protection")].isNull() && m_protection_isValid;

    m_public_net_isValid = ::OpenAPI::fromJsonValue(m_public_net, json[QString("public_net")]);
    m_public_net_isSet = !json[QString("public_net")].isNull() && m_public_net_isValid;

    m_rescue_enabled_isValid = ::OpenAPI::fromJsonValue(m_rescue_enabled, json[QString("rescue_enabled")]);
    m_rescue_enabled_isSet = !json[QString("rescue_enabled")].isNull() && m_rescue_enabled_isValid;

    m_server_type_isValid = ::OpenAPI::fromJsonValue(m_server_type, json[QString("server_type")]);
    m_server_type_isSet = !json[QString("server_type")].isNull() && m_server_type_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_volumes_isValid = ::OpenAPI::fromJsonValue(m_volumes, json[QString("volumes")]);
    m_volumes_isSet = !json[QString("volumes")].isNull() && m_volumes_isValid;
}

QString OAI_servers_get_200_response_servers_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAI_servers_get_200_response_servers_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_backup_window_isSet) {
        obj.insert(QString("backup_window"), ::OpenAPI::toJsonValue(m_backup_window));
    }
    if (m_created_isSet) {
        obj.insert(QString("created"), ::OpenAPI::toJsonValue(m_created));
    }
    if (m_datacenter.isSet()) {
        obj.insert(QString("datacenter"), ::OpenAPI::toJsonValue(m_datacenter));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_image.isSet()) {
        obj.insert(QString("image"), ::OpenAPI::toJsonValue(m_image));
    }
    if (m_included_traffic_isSet) {
        obj.insert(QString("included_traffic"), ::OpenAPI::toJsonValue(m_included_traffic));
    }
    if (m_ingoing_traffic_isSet) {
        obj.insert(QString("ingoing_traffic"), ::OpenAPI::toJsonValue(m_ingoing_traffic));
    }
    if (m_iso.isSet()) {
        obj.insert(QString("iso"), ::OpenAPI::toJsonValue(m_iso));
    }
    if (m_labels.size() > 0) {
        obj.insert(QString("labels"), ::OpenAPI::toJsonValue(m_labels));
    }
    if (m_load_balancers.size() > 0) {
        obj.insert(QString("load_balancers"), ::OpenAPI::toJsonValue(m_load_balancers));
    }
    if (m_locked_isSet) {
        obj.insert(QString("locked"), ::OpenAPI::toJsonValue(m_locked));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_outgoing_traffic_isSet) {
        obj.insert(QString("outgoing_traffic"), ::OpenAPI::toJsonValue(m_outgoing_traffic));
    }
    if (m_placement_group.isSet()) {
        obj.insert(QString("placement_group"), ::OpenAPI::toJsonValue(m_placement_group));
    }
    if (m_primary_disk_size_isSet) {
        obj.insert(QString("primary_disk_size"), ::OpenAPI::toJsonValue(m_primary_disk_size));
    }
    if (m_private_net.size() > 0) {
        obj.insert(QString("private_net"), ::OpenAPI::toJsonValue(m_private_net));
    }
    if (m_protection.isSet()) {
        obj.insert(QString("protection"), ::OpenAPI::toJsonValue(m_protection));
    }
    if (m_public_net.isSet()) {
        obj.insert(QString("public_net"), ::OpenAPI::toJsonValue(m_public_net));
    }
    if (m_rescue_enabled_isSet) {
        obj.insert(QString("rescue_enabled"), ::OpenAPI::toJsonValue(m_rescue_enabled));
    }
    if (m_server_type.isSet()) {
        obj.insert(QString("server_type"), ::OpenAPI::toJsonValue(m_server_type));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_volumes.size() > 0) {
        obj.insert(QString("volumes"), ::OpenAPI::toJsonValue(m_volumes));
    }
    return obj;
}

QString OAI_servers_get_200_response_servers_inner::getBackupWindow() const {
    return m_backup_window;
}
void OAI_servers_get_200_response_servers_inner::setBackupWindow(const QString &backup_window) {
    m_backup_window = backup_window;
    m_backup_window_isSet = true;
}

bool OAI_servers_get_200_response_servers_inner::is_backup_window_Set() const{
    return m_backup_window_isSet;
}

bool OAI_servers_get_200_response_servers_inner::is_backup_window_Valid() const{
    return m_backup_window_isValid;
}

QString OAI_servers_get_200_response_servers_inner::getCreated() const {
    return m_created;
}
void OAI_servers_get_200_response_servers_inner::setCreated(const QString &created) {
    m_created = created;
    m_created_isSet = true;
}

bool OAI_servers_get_200_response_servers_inner::is_created_Set() const{
    return m_created_isSet;
}

bool OAI_servers_get_200_response_servers_inner::is_created_Valid() const{
    return m_created_isValid;
}

OAI_servers_get_200_response_servers_inner_datacenter OAI_servers_get_200_response_servers_inner::getDatacenter() const {
    return m_datacenter;
}
void OAI_servers_get_200_response_servers_inner::setDatacenter(const OAI_servers_get_200_response_servers_inner_datacenter &datacenter) {
    m_datacenter = datacenter;
    m_datacenter_isSet = true;
}

bool OAI_servers_get_200_response_servers_inner::is_datacenter_Set() const{
    return m_datacenter_isSet;
}

bool OAI_servers_get_200_response_servers_inner::is_datacenter_Valid() const{
    return m_datacenter_isValid;
}

qint32 OAI_servers_get_200_response_servers_inner::getId() const {
    return m_id;
}
void OAI_servers_get_200_response_servers_inner::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAI_servers_get_200_response_servers_inner::is_id_Set() const{
    return m_id_isSet;
}

bool OAI_servers_get_200_response_servers_inner::is_id_Valid() const{
    return m_id_isValid;
}

OAI_servers_get_200_response_servers_inner_image OAI_servers_get_200_response_servers_inner::getImage() const {
    return m_image;
}
void OAI_servers_get_200_response_servers_inner::setImage(const OAI_servers_get_200_response_servers_inner_image &image) {
    m_image = image;
    m_image_isSet = true;
}

bool OAI_servers_get_200_response_servers_inner::is_image_Set() const{
    return m_image_isSet;
}

bool OAI_servers_get_200_response_servers_inner::is_image_Valid() const{
    return m_image_isValid;
}

double OAI_servers_get_200_response_servers_inner::getIncludedTraffic() const {
    return m_included_traffic;
}
void OAI_servers_get_200_response_servers_inner::setIncludedTraffic(const double &included_traffic) {
    m_included_traffic = included_traffic;
    m_included_traffic_isSet = true;
}

bool OAI_servers_get_200_response_servers_inner::is_included_traffic_Set() const{
    return m_included_traffic_isSet;
}

bool OAI_servers_get_200_response_servers_inner::is_included_traffic_Valid() const{
    return m_included_traffic_isValid;
}

double OAI_servers_get_200_response_servers_inner::getIngoingTraffic() const {
    return m_ingoing_traffic;
}
void OAI_servers_get_200_response_servers_inner::setIngoingTraffic(const double &ingoing_traffic) {
    m_ingoing_traffic = ingoing_traffic;
    m_ingoing_traffic_isSet = true;
}

bool OAI_servers_get_200_response_servers_inner::is_ingoing_traffic_Set() const{
    return m_ingoing_traffic_isSet;
}

bool OAI_servers_get_200_response_servers_inner::is_ingoing_traffic_Valid() const{
    return m_ingoing_traffic_isValid;
}

OAI_servers_get_200_response_servers_inner_iso OAI_servers_get_200_response_servers_inner::getIso() const {
    return m_iso;
}
void OAI_servers_get_200_response_servers_inner::setIso(const OAI_servers_get_200_response_servers_inner_iso &iso) {
    m_iso = iso;
    m_iso_isSet = true;
}

bool OAI_servers_get_200_response_servers_inner::is_iso_Set() const{
    return m_iso_isSet;
}

bool OAI_servers_get_200_response_servers_inner::is_iso_Valid() const{
    return m_iso_isValid;
}

QMap<QString, QString> OAI_servers_get_200_response_servers_inner::getLabels() const {
    return m_labels;
}
void OAI_servers_get_200_response_servers_inner::setLabels(const QMap<QString, QString> &labels) {
    m_labels = labels;
    m_labels_isSet = true;
}

bool OAI_servers_get_200_response_servers_inner::is_labels_Set() const{
    return m_labels_isSet;
}

bool OAI_servers_get_200_response_servers_inner::is_labels_Valid() const{
    return m_labels_isValid;
}

QList<qint32> OAI_servers_get_200_response_servers_inner::getLoadBalancers() const {
    return m_load_balancers;
}
void OAI_servers_get_200_response_servers_inner::setLoadBalancers(const QList<qint32> &load_balancers) {
    m_load_balancers = load_balancers;
    m_load_balancers_isSet = true;
}

bool OAI_servers_get_200_response_servers_inner::is_load_balancers_Set() const{
    return m_load_balancers_isSet;
}

bool OAI_servers_get_200_response_servers_inner::is_load_balancers_Valid() const{
    return m_load_balancers_isValid;
}

bool OAI_servers_get_200_response_servers_inner::isLocked() const {
    return m_locked;
}
void OAI_servers_get_200_response_servers_inner::setLocked(const bool &locked) {
    m_locked = locked;
    m_locked_isSet = true;
}

bool OAI_servers_get_200_response_servers_inner::is_locked_Set() const{
    return m_locked_isSet;
}

bool OAI_servers_get_200_response_servers_inner::is_locked_Valid() const{
    return m_locked_isValid;
}

QString OAI_servers_get_200_response_servers_inner::getName() const {
    return m_name;
}
void OAI_servers_get_200_response_servers_inner::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAI_servers_get_200_response_servers_inner::is_name_Set() const{
    return m_name_isSet;
}

bool OAI_servers_get_200_response_servers_inner::is_name_Valid() const{
    return m_name_isValid;
}

double OAI_servers_get_200_response_servers_inner::getOutgoingTraffic() const {
    return m_outgoing_traffic;
}
void OAI_servers_get_200_response_servers_inner::setOutgoingTraffic(const double &outgoing_traffic) {
    m_outgoing_traffic = outgoing_traffic;
    m_outgoing_traffic_isSet = true;
}

bool OAI_servers_get_200_response_servers_inner::is_outgoing_traffic_Set() const{
    return m_outgoing_traffic_isSet;
}

bool OAI_servers_get_200_response_servers_inner::is_outgoing_traffic_Valid() const{
    return m_outgoing_traffic_isValid;
}

OAIPlacementGroupNullable OAI_servers_get_200_response_servers_inner::getPlacementGroup() const {
    return m_placement_group;
}
void OAI_servers_get_200_response_servers_inner::setPlacementGroup(const OAIPlacementGroupNullable &placement_group) {
    m_placement_group = placement_group;
    m_placement_group_isSet = true;
}

bool OAI_servers_get_200_response_servers_inner::is_placement_group_Set() const{
    return m_placement_group_isSet;
}

bool OAI_servers_get_200_response_servers_inner::is_placement_group_Valid() const{
    return m_placement_group_isValid;
}

double OAI_servers_get_200_response_servers_inner::getPrimaryDiskSize() const {
    return m_primary_disk_size;
}
void OAI_servers_get_200_response_servers_inner::setPrimaryDiskSize(const double &primary_disk_size) {
    m_primary_disk_size = primary_disk_size;
    m_primary_disk_size_isSet = true;
}

bool OAI_servers_get_200_response_servers_inner::is_primary_disk_size_Set() const{
    return m_primary_disk_size_isSet;
}

bool OAI_servers_get_200_response_servers_inner::is_primary_disk_size_Valid() const{
    return m_primary_disk_size_isValid;
}

QList<OAI_servers_get_200_response_servers_inner_private_net_inner> OAI_servers_get_200_response_servers_inner::getPrivateNet() const {
    return m_private_net;
}
void OAI_servers_get_200_response_servers_inner::setPrivateNet(const QList<OAI_servers_get_200_response_servers_inner_private_net_inner> &private_net) {
    m_private_net = private_net;
    m_private_net_isSet = true;
}

bool OAI_servers_get_200_response_servers_inner::is_private_net_Set() const{
    return m_private_net_isSet;
}

bool OAI_servers_get_200_response_servers_inner::is_private_net_Valid() const{
    return m_private_net_isValid;
}

OAI_servers_get_200_response_servers_inner_protection OAI_servers_get_200_response_servers_inner::getProtection() const {
    return m_protection;
}
void OAI_servers_get_200_response_servers_inner::setProtection(const OAI_servers_get_200_response_servers_inner_protection &protection) {
    m_protection = protection;
    m_protection_isSet = true;
}

bool OAI_servers_get_200_response_servers_inner::is_protection_Set() const{
    return m_protection_isSet;
}

bool OAI_servers_get_200_response_servers_inner::is_protection_Valid() const{
    return m_protection_isValid;
}

OAI_servers_get_200_response_servers_inner_public_net OAI_servers_get_200_response_servers_inner::getPublicNet() const {
    return m_public_net;
}
void OAI_servers_get_200_response_servers_inner::setPublicNet(const OAI_servers_get_200_response_servers_inner_public_net &public_net) {
    m_public_net = public_net;
    m_public_net_isSet = true;
}

bool OAI_servers_get_200_response_servers_inner::is_public_net_Set() const{
    return m_public_net_isSet;
}

bool OAI_servers_get_200_response_servers_inner::is_public_net_Valid() const{
    return m_public_net_isValid;
}

bool OAI_servers_get_200_response_servers_inner::isRescueEnabled() const {
    return m_rescue_enabled;
}
void OAI_servers_get_200_response_servers_inner::setRescueEnabled(const bool &rescue_enabled) {
    m_rescue_enabled = rescue_enabled;
    m_rescue_enabled_isSet = true;
}

bool OAI_servers_get_200_response_servers_inner::is_rescue_enabled_Set() const{
    return m_rescue_enabled_isSet;
}

bool OAI_servers_get_200_response_servers_inner::is_rescue_enabled_Valid() const{
    return m_rescue_enabled_isValid;
}

OAI_servers_get_200_response_servers_inner_server_type OAI_servers_get_200_response_servers_inner::getServerType() const {
    return m_server_type;
}
void OAI_servers_get_200_response_servers_inner::setServerType(const OAI_servers_get_200_response_servers_inner_server_type &server_type) {
    m_server_type = server_type;
    m_server_type_isSet = true;
}

bool OAI_servers_get_200_response_servers_inner::is_server_type_Set() const{
    return m_server_type_isSet;
}

bool OAI_servers_get_200_response_servers_inner::is_server_type_Valid() const{
    return m_server_type_isValid;
}

QString OAI_servers_get_200_response_servers_inner::getStatus() const {
    return m_status;
}
void OAI_servers_get_200_response_servers_inner::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAI_servers_get_200_response_servers_inner::is_status_Set() const{
    return m_status_isSet;
}

bool OAI_servers_get_200_response_servers_inner::is_status_Valid() const{
    return m_status_isValid;
}

QList<qint32> OAI_servers_get_200_response_servers_inner::getVolumes() const {
    return m_volumes;
}
void OAI_servers_get_200_response_servers_inner::setVolumes(const QList<qint32> &volumes) {
    m_volumes = volumes;
    m_volumes_isSet = true;
}

bool OAI_servers_get_200_response_servers_inner::is_volumes_Set() const{
    return m_volumes_isSet;
}

bool OAI_servers_get_200_response_servers_inner::is_volumes_Valid() const{
    return m_volumes_isValid;
}

bool OAI_servers_get_200_response_servers_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_backup_window_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_datacenter.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_image.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_included_traffic_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ingoing_traffic_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_iso.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_labels.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_load_balancers.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_locked_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_outgoing_traffic_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_placement_group.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_primary_disk_size_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_private_net.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_protection.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_public_net.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_rescue_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_server_type.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_volumes.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAI_servers_get_200_response_servers_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_backup_window_isValid && m_created_isValid && m_datacenter_isValid && m_id_isValid && m_image_isValid && m_included_traffic_isValid && m_ingoing_traffic_isValid && m_iso_isValid && m_labels_isValid && m_locked_isValid && m_name_isValid && m_outgoing_traffic_isValid && m_primary_disk_size_isValid && m_private_net_isValid && m_protection_isValid && m_public_net_isValid && m_rescue_enabled_isValid && m_server_type_isValid && m_status_isValid && true;
}

} // namespace OpenAPI
