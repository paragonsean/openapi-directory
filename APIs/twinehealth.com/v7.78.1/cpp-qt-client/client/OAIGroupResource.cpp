/**
 * Fitbit Plus API
 * # Overview The Fitbit Plus API is a RESTful API. The requests and responses are formated according to the [JSON API](http://jsonapi.org/format/1.0/) specification.  In addition to this documentation, we also provide an [OpenAPI](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md) \"yaml\" file describing the API: [Fitbit Plus API Specification](swagger.yaml).  # Authentication Authentication for the Fitbit Plus API is based on the [OAuth 2.0 Authorization Framework](https://tools.ietf.org/html/rfc6749). Fitbit Plus currently supports grant types of **client_credentials** and **refresh_token**.  See [POST /oauth/token](#operation/createToken) for details on the request and response formats. <!-- ReDoc-Inject: <security-definitions> -->  ## Building Integrations We will provide customers with unique client credentials for each application/integration they build, allowing us to enforce appropriate access controls and monitor API usage. The client credentials will be scoped to the organization, and allow full access to all patients and related data within that organization.  These credentials are appropriate for creating an integration that does one of the following:  - background reporting/analysis  - synchronizing data with another system (such as an EMR)  The API credentials and oauth flows we currently support are **not** well suited for creating a user-facing application that allows a user (patient, coach, or admin) to login and have access to data which is appropriate to that specific user. It is possible to build such an application, but it is not possible to use Fitbit Plus as a federated identity provider. You would need to have a separate means of verifying a user's identity. We do not currently support the required password-based oauth flow to make this possible.  # Paging The Fitbit Plus API supports two different pagination strategies for GET collection endpoints.  #### Skip-based paging  Skip-based paging uses the query parameters `page[size]` and `page[number]` to specify the max number of resources returned and the page number. We default to skip-based paging if there are no page parameters. The response will include a `links` object containing links to the first, last, prev, and next pages of data.  If the contents of the collection change while you are iterating through the collection, you will see duplicate or missing documents. For example, if you are iterating through the `calender_event` resource via `GET /pub/calendar_event?sort=start_at&page[size]=50&page[number]=1`, and a new `calendar_event` is created that has a `start_at` value before the first `calendar_event`, when you fetch the next page at `GET /pub/calendar_event?sort=start_at&page[size]=50&page[number]=2`, the first entry in the second response will be a duplicate of the last entry in the first response.  #### Cursor-based paging Cursor-based paging uses the query parameters `page[limit]` and `page[after]` to specify the max number of entries returned and identify where to begin the next page. Add `page[limit]` to the parameters to use cursor-based paging. The response will include a `links` object containing a link to the next page of data, if the next page exists.  Cursor-based paging is not subject to duplication if new resources are added to the collection. For example, if you are iterating through the `calender_event` resource via `GET /pub/calendar_event?sort=start_at&page[limit]=50`, and a new `calendar_event` is created that has a `start_at` value before the first `calendar_event`, you will not see a duplicate entry when you fetch the next page at `GET /pub/calendar_event?sort=start_at&page[limit]=50&page[after]=<cursor>`.  We encourage the use of cursor-based paging for performance reasons.  In either form of paging, you can determine whether any resources were missed by comparing the number of fetched resources against `meta.count`. Set `page[size]` or `page[limit]` to 0 to get only the count.  It is not valid to mix the two strategies. 
 *
 * The version of the OpenAPI document: v7.78.1
 * Contact: apiteam@twinehealth.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGroupResource.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGroupResource::OAIGroupResource(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGroupResource::OAIGroupResource() {
    this->initializeModel();
}

OAIGroupResource::~OAIGroupResource() {}

void OAIGroupResource::initializeModel() {

    m_attributes_isSet = false;
    m_attributes_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_links_isSet = false;
    m_links_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIGroupResource::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGroupResource::fromJsonObject(QJsonObject json) {

    m_attributes_isValid = ::OpenAPI::fromJsonValue(m_attributes, json[QString("attributes")]);
    m_attributes_isSet = !json[QString("attributes")].isNull() && m_attributes_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_links_isValid = ::OpenAPI::fromJsonValue(m_links, json[QString("links")]);
    m_links_isSet = !json[QString("links")].isNull() && m_links_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIGroupResource::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGroupResource::asJsonObject() const {
    QJsonObject obj;
    if (m_attributes.isSet()) {
        obj.insert(QString("attributes"), ::OpenAPI::toJsonValue(m_attributes));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_links.isSet()) {
        obj.insert(QString("links"), ::OpenAPI::toJsonValue(m_links));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

OAIGroupResource_attributes OAIGroupResource::getAttributes() const {
    return m_attributes;
}
void OAIGroupResource::setAttributes(const OAIGroupResource_attributes &attributes) {
    m_attributes = attributes;
    m_attributes_isSet = true;
}

bool OAIGroupResource::is_attributes_Set() const{
    return m_attributes_isSet;
}

bool OAIGroupResource::is_attributes_Valid() const{
    return m_attributes_isValid;
}

QString OAIGroupResource::getId() const {
    return m_id;
}
void OAIGroupResource::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIGroupResource::is_id_Set() const{
    return m_id_isSet;
}

bool OAIGroupResource::is_id_Valid() const{
    return m_id_isValid;
}

OAIGroupResource_links OAIGroupResource::getLinks() const {
    return m_links;
}
void OAIGroupResource::setLinks(const OAIGroupResource_links &links) {
    m_links = links;
    m_links_isSet = true;
}

bool OAIGroupResource::is_links_Set() const{
    return m_links_isSet;
}

bool OAIGroupResource::is_links_Valid() const{
    return m_links_isValid;
}

QString OAIGroupResource::getType() const {
    return m_type;
}
void OAIGroupResource::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIGroupResource::is_type_Set() const{
    return m_type_isSet;
}

bool OAIGroupResource::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIGroupResource::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_attributes.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_links.isSet()) {
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

bool OAIGroupResource::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_attributes_isValid && m_id_isValid && m_type_isValid && true;
}

} // namespace OpenAPI
