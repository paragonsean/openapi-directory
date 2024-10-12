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

#include "OAI_images_get_200_response_images_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAI_images_get_200_response_images_inner::OAI_images_get_200_response_images_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAI_images_get_200_response_images_inner::OAI_images_get_200_response_images_inner() {
    this->initializeModel();
}

OAI_images_get_200_response_images_inner::~OAI_images_get_200_response_images_inner() {}

void OAI_images_get_200_response_images_inner::initializeModel() {

    m_bound_to_isSet = false;
    m_bound_to_isValid = false;

    m_created_isSet = false;
    m_created_isValid = false;

    m_created_from_isSet = false;
    m_created_from_isValid = false;

    m_deleted_isSet = false;
    m_deleted_isValid = false;

    m_deprecated_isSet = false;
    m_deprecated_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_disk_size_isSet = false;
    m_disk_size_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_image_size_isSet = false;
    m_image_size_isValid = false;

    m_labels_isSet = false;
    m_labels_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_os_flavor_isSet = false;
    m_os_flavor_isValid = false;

    m_os_version_isSet = false;
    m_os_version_isValid = false;

    m_protection_isSet = false;
    m_protection_isValid = false;

    m_rapid_deploy_isSet = false;
    m_rapid_deploy_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAI_images_get_200_response_images_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAI_images_get_200_response_images_inner::fromJsonObject(QJsonObject json) {

    m_bound_to_isValid = ::OpenAPI::fromJsonValue(m_bound_to, json[QString("bound_to")]);
    m_bound_to_isSet = !json[QString("bound_to")].isNull() && m_bound_to_isValid;

    m_created_isValid = ::OpenAPI::fromJsonValue(m_created, json[QString("created")]);
    m_created_isSet = !json[QString("created")].isNull() && m_created_isValid;

    m_created_from_isValid = ::OpenAPI::fromJsonValue(m_created_from, json[QString("created_from")]);
    m_created_from_isSet = !json[QString("created_from")].isNull() && m_created_from_isValid;

    m_deleted_isValid = ::OpenAPI::fromJsonValue(m_deleted, json[QString("deleted")]);
    m_deleted_isSet = !json[QString("deleted")].isNull() && m_deleted_isValid;

    m_deprecated_isValid = ::OpenAPI::fromJsonValue(m_deprecated, json[QString("deprecated")]);
    m_deprecated_isSet = !json[QString("deprecated")].isNull() && m_deprecated_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_disk_size_isValid = ::OpenAPI::fromJsonValue(m_disk_size, json[QString("disk_size")]);
    m_disk_size_isSet = !json[QString("disk_size")].isNull() && m_disk_size_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_image_size_isValid = ::OpenAPI::fromJsonValue(m_image_size, json[QString("image_size")]);
    m_image_size_isSet = !json[QString("image_size")].isNull() && m_image_size_isValid;

    m_labels_isValid = ::OpenAPI::fromJsonValue(m_labels, json[QString("labels")]);
    m_labels_isSet = !json[QString("labels")].isNull() && m_labels_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_os_flavor_isValid = ::OpenAPI::fromJsonValue(m_os_flavor, json[QString("os_flavor")]);
    m_os_flavor_isSet = !json[QString("os_flavor")].isNull() && m_os_flavor_isValid;

    m_os_version_isValid = ::OpenAPI::fromJsonValue(m_os_version, json[QString("os_version")]);
    m_os_version_isSet = !json[QString("os_version")].isNull() && m_os_version_isValid;

    m_protection_isValid = ::OpenAPI::fromJsonValue(m_protection, json[QString("protection")]);
    m_protection_isSet = !json[QString("protection")].isNull() && m_protection_isValid;

    m_rapid_deploy_isValid = ::OpenAPI::fromJsonValue(m_rapid_deploy, json[QString("rapid_deploy")]);
    m_rapid_deploy_isSet = !json[QString("rapid_deploy")].isNull() && m_rapid_deploy_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAI_images_get_200_response_images_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAI_images_get_200_response_images_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_bound_to_isSet) {
        obj.insert(QString("bound_to"), ::OpenAPI::toJsonValue(m_bound_to));
    }
    if (m_created_isSet) {
        obj.insert(QString("created"), ::OpenAPI::toJsonValue(m_created));
    }
    if (m_created_from.isSet()) {
        obj.insert(QString("created_from"), ::OpenAPI::toJsonValue(m_created_from));
    }
    if (m_deleted_isSet) {
        obj.insert(QString("deleted"), ::OpenAPI::toJsonValue(m_deleted));
    }
    if (m_deprecated_isSet) {
        obj.insert(QString("deprecated"), ::OpenAPI::toJsonValue(m_deprecated));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_disk_size_isSet) {
        obj.insert(QString("disk_size"), ::OpenAPI::toJsonValue(m_disk_size));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_image_size_isSet) {
        obj.insert(QString("image_size"), ::OpenAPI::toJsonValue(m_image_size));
    }
    if (m_labels.size() > 0) {
        obj.insert(QString("labels"), ::OpenAPI::toJsonValue(m_labels));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_os_flavor_isSet) {
        obj.insert(QString("os_flavor"), ::OpenAPI::toJsonValue(m_os_flavor));
    }
    if (m_os_version_isSet) {
        obj.insert(QString("os_version"), ::OpenAPI::toJsonValue(m_os_version));
    }
    if (m_protection.isSet()) {
        obj.insert(QString("protection"), ::OpenAPI::toJsonValue(m_protection));
    }
    if (m_rapid_deploy_isSet) {
        obj.insert(QString("rapid_deploy"), ::OpenAPI::toJsonValue(m_rapid_deploy));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

qint32 OAI_images_get_200_response_images_inner::getBoundTo() const {
    return m_bound_to;
}
void OAI_images_get_200_response_images_inner::setBoundTo(const qint32 &bound_to) {
    m_bound_to = bound_to;
    m_bound_to_isSet = true;
}

bool OAI_images_get_200_response_images_inner::is_bound_to_Set() const{
    return m_bound_to_isSet;
}

bool OAI_images_get_200_response_images_inner::is_bound_to_Valid() const{
    return m_bound_to_isValid;
}

QString OAI_images_get_200_response_images_inner::getCreated() const {
    return m_created;
}
void OAI_images_get_200_response_images_inner::setCreated(const QString &created) {
    m_created = created;
    m_created_isSet = true;
}

bool OAI_images_get_200_response_images_inner::is_created_Set() const{
    return m_created_isSet;
}

bool OAI_images_get_200_response_images_inner::is_created_Valid() const{
    return m_created_isValid;
}

OAI_images_get_200_response_images_inner_created_from OAI_images_get_200_response_images_inner::getCreatedFrom() const {
    return m_created_from;
}
void OAI_images_get_200_response_images_inner::setCreatedFrom(const OAI_images_get_200_response_images_inner_created_from &created_from) {
    m_created_from = created_from;
    m_created_from_isSet = true;
}

bool OAI_images_get_200_response_images_inner::is_created_from_Set() const{
    return m_created_from_isSet;
}

bool OAI_images_get_200_response_images_inner::is_created_from_Valid() const{
    return m_created_from_isValid;
}

QString OAI_images_get_200_response_images_inner::getDeleted() const {
    return m_deleted;
}
void OAI_images_get_200_response_images_inner::setDeleted(const QString &deleted) {
    m_deleted = deleted;
    m_deleted_isSet = true;
}

bool OAI_images_get_200_response_images_inner::is_deleted_Set() const{
    return m_deleted_isSet;
}

bool OAI_images_get_200_response_images_inner::is_deleted_Valid() const{
    return m_deleted_isValid;
}

QString OAI_images_get_200_response_images_inner::getDeprecated() const {
    return m_deprecated;
}
void OAI_images_get_200_response_images_inner::setDeprecated(const QString &deprecated) {
    m_deprecated = deprecated;
    m_deprecated_isSet = true;
}

bool OAI_images_get_200_response_images_inner::is_deprecated_Set() const{
    return m_deprecated_isSet;
}

bool OAI_images_get_200_response_images_inner::is_deprecated_Valid() const{
    return m_deprecated_isValid;
}

QString OAI_images_get_200_response_images_inner::getDescription() const {
    return m_description;
}
void OAI_images_get_200_response_images_inner::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAI_images_get_200_response_images_inner::is_description_Set() const{
    return m_description_isSet;
}

bool OAI_images_get_200_response_images_inner::is_description_Valid() const{
    return m_description_isValid;
}

double OAI_images_get_200_response_images_inner::getDiskSize() const {
    return m_disk_size;
}
void OAI_images_get_200_response_images_inner::setDiskSize(const double &disk_size) {
    m_disk_size = disk_size;
    m_disk_size_isSet = true;
}

bool OAI_images_get_200_response_images_inner::is_disk_size_Set() const{
    return m_disk_size_isSet;
}

bool OAI_images_get_200_response_images_inner::is_disk_size_Valid() const{
    return m_disk_size_isValid;
}

qint32 OAI_images_get_200_response_images_inner::getId() const {
    return m_id;
}
void OAI_images_get_200_response_images_inner::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAI_images_get_200_response_images_inner::is_id_Set() const{
    return m_id_isSet;
}

bool OAI_images_get_200_response_images_inner::is_id_Valid() const{
    return m_id_isValid;
}

double OAI_images_get_200_response_images_inner::getImageSize() const {
    return m_image_size;
}
void OAI_images_get_200_response_images_inner::setImageSize(const double &image_size) {
    m_image_size = image_size;
    m_image_size_isSet = true;
}

bool OAI_images_get_200_response_images_inner::is_image_size_Set() const{
    return m_image_size_isSet;
}

bool OAI_images_get_200_response_images_inner::is_image_size_Valid() const{
    return m_image_size_isValid;
}

QMap<QString, QString> OAI_images_get_200_response_images_inner::getLabels() const {
    return m_labels;
}
void OAI_images_get_200_response_images_inner::setLabels(const QMap<QString, QString> &labels) {
    m_labels = labels;
    m_labels_isSet = true;
}

bool OAI_images_get_200_response_images_inner::is_labels_Set() const{
    return m_labels_isSet;
}

bool OAI_images_get_200_response_images_inner::is_labels_Valid() const{
    return m_labels_isValid;
}

QString OAI_images_get_200_response_images_inner::getName() const {
    return m_name;
}
void OAI_images_get_200_response_images_inner::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAI_images_get_200_response_images_inner::is_name_Set() const{
    return m_name_isSet;
}

bool OAI_images_get_200_response_images_inner::is_name_Valid() const{
    return m_name_isValid;
}

QString OAI_images_get_200_response_images_inner::getOsFlavor() const {
    return m_os_flavor;
}
void OAI_images_get_200_response_images_inner::setOsFlavor(const QString &os_flavor) {
    m_os_flavor = os_flavor;
    m_os_flavor_isSet = true;
}

bool OAI_images_get_200_response_images_inner::is_os_flavor_Set() const{
    return m_os_flavor_isSet;
}

bool OAI_images_get_200_response_images_inner::is_os_flavor_Valid() const{
    return m_os_flavor_isValid;
}

QString OAI_images_get_200_response_images_inner::getOsVersion() const {
    return m_os_version;
}
void OAI_images_get_200_response_images_inner::setOsVersion(const QString &os_version) {
    m_os_version = os_version;
    m_os_version_isSet = true;
}

bool OAI_images_get_200_response_images_inner::is_os_version_Set() const{
    return m_os_version_isSet;
}

bool OAI_images_get_200_response_images_inner::is_os_version_Valid() const{
    return m_os_version_isValid;
}

OAI_floating_ips_get_200_response_floating_ips_inner_protection OAI_images_get_200_response_images_inner::getProtection() const {
    return m_protection;
}
void OAI_images_get_200_response_images_inner::setProtection(const OAI_floating_ips_get_200_response_floating_ips_inner_protection &protection) {
    m_protection = protection;
    m_protection_isSet = true;
}

bool OAI_images_get_200_response_images_inner::is_protection_Set() const{
    return m_protection_isSet;
}

bool OAI_images_get_200_response_images_inner::is_protection_Valid() const{
    return m_protection_isValid;
}

bool OAI_images_get_200_response_images_inner::isRapidDeploy() const {
    return m_rapid_deploy;
}
void OAI_images_get_200_response_images_inner::setRapidDeploy(const bool &rapid_deploy) {
    m_rapid_deploy = rapid_deploy;
    m_rapid_deploy_isSet = true;
}

bool OAI_images_get_200_response_images_inner::is_rapid_deploy_Set() const{
    return m_rapid_deploy_isSet;
}

bool OAI_images_get_200_response_images_inner::is_rapid_deploy_Valid() const{
    return m_rapid_deploy_isValid;
}

QString OAI_images_get_200_response_images_inner::getStatus() const {
    return m_status;
}
void OAI_images_get_200_response_images_inner::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAI_images_get_200_response_images_inner::is_status_Set() const{
    return m_status_isSet;
}

bool OAI_images_get_200_response_images_inner::is_status_Valid() const{
    return m_status_isValid;
}

QString OAI_images_get_200_response_images_inner::getType() const {
    return m_type;
}
void OAI_images_get_200_response_images_inner::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAI_images_get_200_response_images_inner::is_type_Set() const{
    return m_type_isSet;
}

bool OAI_images_get_200_response_images_inner::is_type_Valid() const{
    return m_type_isValid;
}

bool OAI_images_get_200_response_images_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_bound_to_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_from.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_deleted_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_deprecated_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_disk_size_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_image_size_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_labels.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_os_flavor_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_os_version_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_protection.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_rapid_deploy_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAI_images_get_200_response_images_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_bound_to_isValid && m_created_isValid && m_created_from_isValid && m_deleted_isValid && m_deprecated_isValid && m_description_isValid && m_disk_size_isValid && m_id_isValid && m_image_size_isValid && m_labels_isValid && m_name_isValid && m_os_flavor_isValid && m_os_version_isValid && m_protection_isValid && m_status_isValid && m_type_isValid && true;
}

} // namespace OpenAPI
