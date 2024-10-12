/**
 * Open States API v3
 *  * [More documentation](https://docs.openstates.org/en/latest/api/v3/index.html) * [Register for an account](https://openstates.org/accounts/signup/)   **We are currently working to restore experimental support for committees & events.**  During this period please note that data is not yet available for all states and the exact format of the new endpoints may change slightly depending on user feedback.  If you have any issues or questions use our [GitHub Issues](https://github.com/openstates/issues/issues) to give feedback. 
 *
 * The version of the OpenAPI document: 2021.11.12
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIOrganization.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIOrganization::OAIOrganization(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIOrganization::OAIOrganization() {
    this->initializeModel();
}

OAIOrganization::~OAIOrganization() {}

void OAIOrganization::initializeModel() {

    m_classification_isSet = false;
    m_classification_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;
}

void OAIOrganization::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIOrganization::fromJsonObject(QJsonObject json) {

    m_classification_isValid = ::OpenAPI::fromJsonValue(m_classification, json[QString("classification")]);
    m_classification_isSet = !json[QString("classification")].isNull() && m_classification_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;
}

QString OAIOrganization::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIOrganization::asJsonObject() const {
    QJsonObject obj;
    if (m_classification_isSet) {
        obj.insert(QString("classification"), ::OpenAPI::toJsonValue(m_classification));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    return obj;
}

QString OAIOrganization::getClassification() const {
    return m_classification;
}
void OAIOrganization::setClassification(const QString &classification) {
    m_classification = classification;
    m_classification_isSet = true;
}

bool OAIOrganization::is_classification_Set() const{
    return m_classification_isSet;
}

bool OAIOrganization::is_classification_Valid() const{
    return m_classification_isValid;
}

QString OAIOrganization::getId() const {
    return m_id;
}
void OAIOrganization::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIOrganization::is_id_Set() const{
    return m_id_isSet;
}

bool OAIOrganization::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIOrganization::getName() const {
    return m_name;
}
void OAIOrganization::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIOrganization::is_name_Set() const{
    return m_name_isSet;
}

bool OAIOrganization::is_name_Valid() const{
    return m_name_isValid;
}

bool OAIOrganization::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_classification_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
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

bool OAIOrganization::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_classification_isValid && m_id_isValid && m_name_isValid && true;
}

} // namespace OpenAPI
