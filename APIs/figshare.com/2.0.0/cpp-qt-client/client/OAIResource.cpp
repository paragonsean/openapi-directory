/**
 * Figshare API
 * Figshare apiv2. Using Swagger 2.0
 *
 * The version of the OpenAPI document: 2.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIResource.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIResource::OAIResource(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIResource::OAIResource() {
    this->initializeModel();
}

OAIResource::~OAIResource() {}

void OAIResource::initializeModel() {

    m_doi_isSet = false;
    m_doi_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_link_isSet = false;
    m_link_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;

    m_version_isSet = false;
    m_version_isValid = false;
}

void OAIResource::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIResource::fromJsonObject(QJsonObject json) {

    m_doi_isValid = ::OpenAPI::fromJsonValue(m_doi, json[QString("doi")]);
    m_doi_isSet = !json[QString("doi")].isNull() && m_doi_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_link_isValid = ::OpenAPI::fromJsonValue(m_link, json[QString("link")]);
    m_link_isSet = !json[QString("link")].isNull() && m_link_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("title")]);
    m_title_isSet = !json[QString("title")].isNull() && m_title_isValid;

    m_version_isValid = ::OpenAPI::fromJsonValue(m_version, json[QString("version")]);
    m_version_isSet = !json[QString("version")].isNull() && m_version_isValid;
}

QString OAIResource::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIResource::asJsonObject() const {
    QJsonObject obj;
    if (m_doi_isSet) {
        obj.insert(QString("doi"), ::OpenAPI::toJsonValue(m_doi));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_link_isSet) {
        obj.insert(QString("link"), ::OpenAPI::toJsonValue(m_link));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_title_isSet) {
        obj.insert(QString("title"), ::OpenAPI::toJsonValue(m_title));
    }
    if (m_version_isSet) {
        obj.insert(QString("version"), ::OpenAPI::toJsonValue(m_version));
    }
    return obj;
}

QString OAIResource::getDoi() const {
    return m_doi;
}
void OAIResource::setDoi(const QString &doi) {
    m_doi = doi;
    m_doi_isSet = true;
}

bool OAIResource::is_doi_Set() const{
    return m_doi_isSet;
}

bool OAIResource::is_doi_Valid() const{
    return m_doi_isValid;
}

QString OAIResource::getId() const {
    return m_id;
}
void OAIResource::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIResource::is_id_Set() const{
    return m_id_isSet;
}

bool OAIResource::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIResource::getLink() const {
    return m_link;
}
void OAIResource::setLink(const QString &link) {
    m_link = link;
    m_link_isSet = true;
}

bool OAIResource::is_link_Set() const{
    return m_link_isSet;
}

bool OAIResource::is_link_Valid() const{
    return m_link_isValid;
}

QString OAIResource::getStatus() const {
    return m_status;
}
void OAIResource::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIResource::is_status_Set() const{
    return m_status_isSet;
}

bool OAIResource::is_status_Valid() const{
    return m_status_isValid;
}

QString OAIResource::getTitle() const {
    return m_title;
}
void OAIResource::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAIResource::is_title_Set() const{
    return m_title_isSet;
}

bool OAIResource::is_title_Valid() const{
    return m_title_isValid;
}

qint64 OAIResource::getVersion() const {
    return m_version;
}
void OAIResource::setVersion(const qint64 &version) {
    m_version = version;
    m_version_isSet = true;
}

bool OAIResource::is_version_Set() const{
    return m_version_isSet;
}

bool OAIResource::is_version_Valid() const{
    return m_version_isValid;
}

bool OAIResource::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_doi_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_link_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_title_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_version_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIResource::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
