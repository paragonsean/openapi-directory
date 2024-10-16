/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIDistributionGroupPatchRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDistributionGroupPatchRequest::OAIDistributionGroupPatchRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDistributionGroupPatchRequest::OAIDistributionGroupPatchRequest() {
    this->initializeModel();
}

OAIDistributionGroupPatchRequest::~OAIDistributionGroupPatchRequest() {}

void OAIDistributionGroupPatchRequest::initializeModel() {

    m_is_public_isSet = false;
    m_is_public_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;
}

void OAIDistributionGroupPatchRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDistributionGroupPatchRequest::fromJsonObject(QJsonObject json) {

    m_is_public_isValid = ::OpenAPI::fromJsonValue(m_is_public, json[QString("is_public")]);
    m_is_public_isSet = !json[QString("is_public")].isNull() && m_is_public_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;
}

QString OAIDistributionGroupPatchRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDistributionGroupPatchRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_is_public_isSet) {
        obj.insert(QString("is_public"), ::OpenAPI::toJsonValue(m_is_public));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    return obj;
}

bool OAIDistributionGroupPatchRequest::isIsPublic() const {
    return m_is_public;
}
void OAIDistributionGroupPatchRequest::setIsPublic(const bool &is_public) {
    m_is_public = is_public;
    m_is_public_isSet = true;
}

bool OAIDistributionGroupPatchRequest::is_is_public_Set() const{
    return m_is_public_isSet;
}

bool OAIDistributionGroupPatchRequest::is_is_public_Valid() const{
    return m_is_public_isValid;
}

QString OAIDistributionGroupPatchRequest::getName() const {
    return m_name;
}
void OAIDistributionGroupPatchRequest::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIDistributionGroupPatchRequest::is_name_Set() const{
    return m_name_isSet;
}

bool OAIDistributionGroupPatchRequest::is_name_Valid() const{
    return m_name_isValid;
}

bool OAIDistributionGroupPatchRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_is_public_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDistributionGroupPatchRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
