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

#include "OAIPatientCreateResource.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPatientCreateResource::OAIPatientCreateResource(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPatientCreateResource::OAIPatientCreateResource() {
    this->initializeModel();
}

OAIPatientCreateResource::~OAIPatientCreateResource() {}

void OAIPatientCreateResource::initializeModel() {

    m_attributes_isSet = false;
    m_attributes_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_links_isSet = false;
    m_links_isValid = false;

    m_relationships_isSet = false;
    m_relationships_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIPatientCreateResource::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPatientCreateResource::fromJsonObject(QJsonObject json) {

    m_attributes_isValid = ::OpenAPI::fromJsonValue(m_attributes, json[QString("attributes")]);
    m_attributes_isSet = !json[QString("attributes")].isNull() && m_attributes_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_links_isValid = ::OpenAPI::fromJsonValue(m_links, json[QString("links")]);
    m_links_isSet = !json[QString("links")].isNull() && m_links_isValid;

    m_relationships_isValid = ::OpenAPI::fromJsonValue(m_relationships, json[QString("relationships")]);
    m_relationships_isSet = !json[QString("relationships")].isNull() && m_relationships_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIPatientCreateResource::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPatientCreateResource::asJsonObject() const {
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
    if (m_relationships.isSet()) {
        obj.insert(QString("relationships"), ::OpenAPI::toJsonValue(m_relationships));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

OAIPatientResource_attributes OAIPatientCreateResource::getAttributes() const {
    return m_attributes;
}
void OAIPatientCreateResource::setAttributes(const OAIPatientResource_attributes &attributes) {
    m_attributes = attributes;
    m_attributes_isSet = true;
}

bool OAIPatientCreateResource::is_attributes_Set() const{
    return m_attributes_isSet;
}

bool OAIPatientCreateResource::is_attributes_Valid() const{
    return m_attributes_isValid;
}

QString OAIPatientCreateResource::getId() const {
    return m_id;
}
void OAIPatientCreateResource::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIPatientCreateResource::is_id_Set() const{
    return m_id_isSet;
}

bool OAIPatientCreateResource::is_id_Valid() const{
    return m_id_isValid;
}

OAIPatientResource_links OAIPatientCreateResource::getLinks() const {
    return m_links;
}
void OAIPatientCreateResource::setLinks(const OAIPatientResource_links &links) {
    m_links = links;
    m_links_isSet = true;
}

bool OAIPatientCreateResource::is_links_Set() const{
    return m_links_isSet;
}

bool OAIPatientCreateResource::is_links_Valid() const{
    return m_links_isValid;
}

OAIPatientCreateResource_allOf_relationships OAIPatientCreateResource::getRelationships() const {
    return m_relationships;
}
void OAIPatientCreateResource::setRelationships(const OAIPatientCreateResource_allOf_relationships &relationships) {
    m_relationships = relationships;
    m_relationships_isSet = true;
}

bool OAIPatientCreateResource::is_relationships_Set() const{
    return m_relationships_isSet;
}

bool OAIPatientCreateResource::is_relationships_Valid() const{
    return m_relationships_isValid;
}

QString OAIPatientCreateResource::getType() const {
    return m_type;
}
void OAIPatientCreateResource::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIPatientCreateResource::is_type_Set() const{
    return m_type_isSet;
}

bool OAIPatientCreateResource::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIPatientCreateResource::isSet() const {
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

        if (m_relationships.isSet()) {
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

bool OAIPatientCreateResource::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_attributes_isValid && m_type_isValid && true;
}

} // namespace OpenAPI
