/**
 * DaniWeb Connect API
 * User Recommendation Engine and Chat Network
 *
 * The version of the OpenAPI document: 4
 * Contact: dani@daniwebmail.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIBubble.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBubble::OAIBubble(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBubble::OAIBubble() {
    this->initializeModel();
}

OAIBubble::~OAIBubble() {}

void OAIBubble::initializeModel() {

    m_about_isSet = false;
    m_about_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;
}

void OAIBubble::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBubble::fromJsonObject(QJsonObject json) {

    m_about_isValid = ::OpenAPI::fromJsonValue(m_about, json[QString("about")]);
    m_about_isSet = !json[QString("about")].isNull() && m_about_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;
}

QString OAIBubble::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBubble::asJsonObject() const {
    QJsonObject obj;
    if (m_about.isSet()) {
        obj.insert(QString("about"), ::OpenAPI::toJsonValue(m_about));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    return obj;
}

OAIBubble_about OAIBubble::getAbout() const {
    return m_about;
}
void OAIBubble::setAbout(const OAIBubble_about &about) {
    m_about = about;
    m_about_isSet = true;
}

bool OAIBubble::is_about_Set() const{
    return m_about_isSet;
}

bool OAIBubble::is_about_Valid() const{
    return m_about_isValid;
}

double OAIBubble::getId() const {
    return m_id;
}
void OAIBubble::setId(const double &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIBubble::is_id_Set() const{
    return m_id_isSet;
}

bool OAIBubble::is_id_Valid() const{
    return m_id_isValid;
}

bool OAIBubble::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_about.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBubble::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_id_isValid && true;
}

} // namespace OpenAPI
