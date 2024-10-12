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

#include "OAICreateServerRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICreateServerRequest::OAICreateServerRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICreateServerRequest::OAICreateServerRequest() {
    this->initializeModel();
}

OAICreateServerRequest::~OAICreateServerRequest() {}

void OAICreateServerRequest::initializeModel() {

    m_automount_isSet = false;
    m_automount_isValid = false;

    m_datacenter_isSet = false;
    m_datacenter_isValid = false;

    m_firewalls_isSet = false;
    m_firewalls_isValid = false;

    m_image_isSet = false;
    m_image_isValid = false;

    m_labels_isSet = false;
    m_labels_isValid = false;

    m_location_isSet = false;
    m_location_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_networks_isSet = false;
    m_networks_isValid = false;

    m_placement_group_isSet = false;
    m_placement_group_isValid = false;

    m_public_net_isSet = false;
    m_public_net_isValid = false;

    m_server_type_isSet = false;
    m_server_type_isValid = false;

    m_ssh_keys_isSet = false;
    m_ssh_keys_isValid = false;

    m_start_after_create_isSet = false;
    m_start_after_create_isValid = false;

    m_user_data_isSet = false;
    m_user_data_isValid = false;

    m_volumes_isSet = false;
    m_volumes_isValid = false;
}

void OAICreateServerRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICreateServerRequest::fromJsonObject(QJsonObject json) {

    m_automount_isValid = ::OpenAPI::fromJsonValue(m_automount, json[QString("automount")]);
    m_automount_isSet = !json[QString("automount")].isNull() && m_automount_isValid;

    m_datacenter_isValid = ::OpenAPI::fromJsonValue(m_datacenter, json[QString("datacenter")]);
    m_datacenter_isSet = !json[QString("datacenter")].isNull() && m_datacenter_isValid;

    m_firewalls_isValid = ::OpenAPI::fromJsonValue(m_firewalls, json[QString("firewalls")]);
    m_firewalls_isSet = !json[QString("firewalls")].isNull() && m_firewalls_isValid;

    m_image_isValid = ::OpenAPI::fromJsonValue(m_image, json[QString("image")]);
    m_image_isSet = !json[QString("image")].isNull() && m_image_isValid;

    m_labels_isValid = ::OpenAPI::fromJsonValue(m_labels, json[QString("labels")]);
    m_labels_isSet = !json[QString("labels")].isNull() && m_labels_isValid;

    m_location_isValid = ::OpenAPI::fromJsonValue(m_location, json[QString("location")]);
    m_location_isSet = !json[QString("location")].isNull() && m_location_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_networks_isValid = ::OpenAPI::fromJsonValue(m_networks, json[QString("networks")]);
    m_networks_isSet = !json[QString("networks")].isNull() && m_networks_isValid;

    m_placement_group_isValid = ::OpenAPI::fromJsonValue(m_placement_group, json[QString("placement_group")]);
    m_placement_group_isSet = !json[QString("placement_group")].isNull() && m_placement_group_isValid;

    m_public_net_isValid = ::OpenAPI::fromJsonValue(m_public_net, json[QString("public_net")]);
    m_public_net_isSet = !json[QString("public_net")].isNull() && m_public_net_isValid;

    m_server_type_isValid = ::OpenAPI::fromJsonValue(m_server_type, json[QString("server_type")]);
    m_server_type_isSet = !json[QString("server_type")].isNull() && m_server_type_isValid;

    m_ssh_keys_isValid = ::OpenAPI::fromJsonValue(m_ssh_keys, json[QString("ssh_keys")]);
    m_ssh_keys_isSet = !json[QString("ssh_keys")].isNull() && m_ssh_keys_isValid;

    m_start_after_create_isValid = ::OpenAPI::fromJsonValue(m_start_after_create, json[QString("start_after_create")]);
    m_start_after_create_isSet = !json[QString("start_after_create")].isNull() && m_start_after_create_isValid;

    m_user_data_isValid = ::OpenAPI::fromJsonValue(m_user_data, json[QString("user_data")]);
    m_user_data_isSet = !json[QString("user_data")].isNull() && m_user_data_isValid;

    m_volumes_isValid = ::OpenAPI::fromJsonValue(m_volumes, json[QString("volumes")]);
    m_volumes_isSet = !json[QString("volumes")].isNull() && m_volumes_isValid;
}

QString OAICreateServerRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICreateServerRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_automount_isSet) {
        obj.insert(QString("automount"), ::OpenAPI::toJsonValue(m_automount));
    }
    if (m_datacenter_isSet) {
        obj.insert(QString("datacenter"), ::OpenAPI::toJsonValue(m_datacenter));
    }
    if (m_firewalls.size() > 0) {
        obj.insert(QString("firewalls"), ::OpenAPI::toJsonValue(m_firewalls));
    }
    if (m_image_isSet) {
        obj.insert(QString("image"), ::OpenAPI::toJsonValue(m_image));
    }
    if (m_labels_isSet) {
        obj.insert(QString("labels"), ::OpenAPI::toJsonValue(m_labels));
    }
    if (m_location_isSet) {
        obj.insert(QString("location"), ::OpenAPI::toJsonValue(m_location));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_networks.size() > 0) {
        obj.insert(QString("networks"), ::OpenAPI::toJsonValue(m_networks));
    }
    if (m_placement_group_isSet) {
        obj.insert(QString("placement_group"), ::OpenAPI::toJsonValue(m_placement_group));
    }
    if (m_public_net.isSet()) {
        obj.insert(QString("public_net"), ::OpenAPI::toJsonValue(m_public_net));
    }
    if (m_server_type_isSet) {
        obj.insert(QString("server_type"), ::OpenAPI::toJsonValue(m_server_type));
    }
    if (m_ssh_keys.size() > 0) {
        obj.insert(QString("ssh_keys"), ::OpenAPI::toJsonValue(m_ssh_keys));
    }
    if (m_start_after_create_isSet) {
        obj.insert(QString("start_after_create"), ::OpenAPI::toJsonValue(m_start_after_create));
    }
    if (m_user_data_isSet) {
        obj.insert(QString("user_data"), ::OpenAPI::toJsonValue(m_user_data));
    }
    if (m_volumes.size() > 0) {
        obj.insert(QString("volumes"), ::OpenAPI::toJsonValue(m_volumes));
    }
    return obj;
}

bool OAICreateServerRequest::isAutomount() const {
    return m_automount;
}
void OAICreateServerRequest::setAutomount(const bool &automount) {
    m_automount = automount;
    m_automount_isSet = true;
}

bool OAICreateServerRequest::is_automount_Set() const{
    return m_automount_isSet;
}

bool OAICreateServerRequest::is_automount_Valid() const{
    return m_automount_isValid;
}

QString OAICreateServerRequest::getDatacenter() const {
    return m_datacenter;
}
void OAICreateServerRequest::setDatacenter(const QString &datacenter) {
    m_datacenter = datacenter;
    m_datacenter_isSet = true;
}

bool OAICreateServerRequest::is_datacenter_Set() const{
    return m_datacenter_isSet;
}

bool OAICreateServerRequest::is_datacenter_Valid() const{
    return m_datacenter_isValid;
}

QList<OAICreateServerRequest_firewalls_inner> OAICreateServerRequest::getFirewalls() const {
    return m_firewalls;
}
void OAICreateServerRequest::setFirewalls(const QList<OAICreateServerRequest_firewalls_inner> &firewalls) {
    m_firewalls = firewalls;
    m_firewalls_isSet = true;
}

bool OAICreateServerRequest::is_firewalls_Set() const{
    return m_firewalls_isSet;
}

bool OAICreateServerRequest::is_firewalls_Valid() const{
    return m_firewalls_isValid;
}

QString OAICreateServerRequest::getImage() const {
    return m_image;
}
void OAICreateServerRequest::setImage(const QString &image) {
    m_image = image;
    m_image_isSet = true;
}

bool OAICreateServerRequest::is_image_Set() const{
    return m_image_isSet;
}

bool OAICreateServerRequest::is_image_Valid() const{
    return m_image_isValid;
}

OAIObject OAICreateServerRequest::getLabels() const {
    return m_labels;
}
void OAICreateServerRequest::setLabels(const OAIObject &labels) {
    m_labels = labels;
    m_labels_isSet = true;
}

bool OAICreateServerRequest::is_labels_Set() const{
    return m_labels_isSet;
}

bool OAICreateServerRequest::is_labels_Valid() const{
    return m_labels_isValid;
}

QString OAICreateServerRequest::getLocation() const {
    return m_location;
}
void OAICreateServerRequest::setLocation(const QString &location) {
    m_location = location;
    m_location_isSet = true;
}

bool OAICreateServerRequest::is_location_Set() const{
    return m_location_isSet;
}

bool OAICreateServerRequest::is_location_Valid() const{
    return m_location_isValid;
}

QString OAICreateServerRequest::getName() const {
    return m_name;
}
void OAICreateServerRequest::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAICreateServerRequest::is_name_Set() const{
    return m_name_isSet;
}

bool OAICreateServerRequest::is_name_Valid() const{
    return m_name_isValid;
}

QList<qint32> OAICreateServerRequest::getNetworks() const {
    return m_networks;
}
void OAICreateServerRequest::setNetworks(const QList<qint32> &networks) {
    m_networks = networks;
    m_networks_isSet = true;
}

bool OAICreateServerRequest::is_networks_Set() const{
    return m_networks_isSet;
}

bool OAICreateServerRequest::is_networks_Valid() const{
    return m_networks_isValid;
}

qint32 OAICreateServerRequest::getPlacementGroup() const {
    return m_placement_group;
}
void OAICreateServerRequest::setPlacementGroup(const qint32 &placement_group) {
    m_placement_group = placement_group;
    m_placement_group_isSet = true;
}

bool OAICreateServerRequest::is_placement_group_Set() const{
    return m_placement_group_isSet;
}

bool OAICreateServerRequest::is_placement_group_Valid() const{
    return m_placement_group_isValid;
}

OAICreateServerRequest_public_net OAICreateServerRequest::getPublicNet() const {
    return m_public_net;
}
void OAICreateServerRequest::setPublicNet(const OAICreateServerRequest_public_net &public_net) {
    m_public_net = public_net;
    m_public_net_isSet = true;
}

bool OAICreateServerRequest::is_public_net_Set() const{
    return m_public_net_isSet;
}

bool OAICreateServerRequest::is_public_net_Valid() const{
    return m_public_net_isValid;
}

QString OAICreateServerRequest::getServerType() const {
    return m_server_type;
}
void OAICreateServerRequest::setServerType(const QString &server_type) {
    m_server_type = server_type;
    m_server_type_isSet = true;
}

bool OAICreateServerRequest::is_server_type_Set() const{
    return m_server_type_isSet;
}

bool OAICreateServerRequest::is_server_type_Valid() const{
    return m_server_type_isValid;
}

QList<QString> OAICreateServerRequest::getSshKeys() const {
    return m_ssh_keys;
}
void OAICreateServerRequest::setSshKeys(const QList<QString> &ssh_keys) {
    m_ssh_keys = ssh_keys;
    m_ssh_keys_isSet = true;
}

bool OAICreateServerRequest::is_ssh_keys_Set() const{
    return m_ssh_keys_isSet;
}

bool OAICreateServerRequest::is_ssh_keys_Valid() const{
    return m_ssh_keys_isValid;
}

bool OAICreateServerRequest::isStartAfterCreate() const {
    return m_start_after_create;
}
void OAICreateServerRequest::setStartAfterCreate(const bool &start_after_create) {
    m_start_after_create = start_after_create;
    m_start_after_create_isSet = true;
}

bool OAICreateServerRequest::is_start_after_create_Set() const{
    return m_start_after_create_isSet;
}

bool OAICreateServerRequest::is_start_after_create_Valid() const{
    return m_start_after_create_isValid;
}

QString OAICreateServerRequest::getUserData() const {
    return m_user_data;
}
void OAICreateServerRequest::setUserData(const QString &user_data) {
    m_user_data = user_data;
    m_user_data_isSet = true;
}

bool OAICreateServerRequest::is_user_data_Set() const{
    return m_user_data_isSet;
}

bool OAICreateServerRequest::is_user_data_Valid() const{
    return m_user_data_isValid;
}

QList<qint32> OAICreateServerRequest::getVolumes() const {
    return m_volumes;
}
void OAICreateServerRequest::setVolumes(const QList<qint32> &volumes) {
    m_volumes = volumes;
    m_volumes_isSet = true;
}

bool OAICreateServerRequest::is_volumes_Set() const{
    return m_volumes_isSet;
}

bool OAICreateServerRequest::is_volumes_Valid() const{
    return m_volumes_isValid;
}

bool OAICreateServerRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_automount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_datacenter_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_firewalls.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_image_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_labels_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_location_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_networks.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_placement_group_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_public_net.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_server_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ssh_keys.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_start_after_create_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_data_isSet) {
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

bool OAICreateServerRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_image_isValid && m_name_isValid && m_server_type_isValid && true;
}

} // namespace OpenAPI
