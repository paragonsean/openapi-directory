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

#include "OAIIntuneGroups.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIIntuneGroups::OAIIntuneGroups(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIIntuneGroups::OAIIntuneGroups() {
    this->initializeModel();
}

OAIIntuneGroups::~OAIIntuneGroups() {}

void OAIIntuneGroups::initializeModel() {

    m_odata_context_isSet = false;
    m_odata_context_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIIntuneGroups::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIIntuneGroups::fromJsonObject(QJsonObject json) {

    m_odata_context_isValid = ::OpenAPI::fromJsonValue(m_odata_context, json[QString("odata.context")]);
    m_odata_context_isSet = !json[QString("odata.context")].isNull() && m_odata_context_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIIntuneGroups::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIIntuneGroups::asJsonObject() const {
    QJsonObject obj;
    if (m_odata_context_isSet) {
        obj.insert(QString("odata.context"), ::OpenAPI::toJsonValue(m_odata_context));
    }
    if (m_value.size() > 0) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

QString OAIIntuneGroups::getOdataContext() const {
    return m_odata_context;
}
void OAIIntuneGroups::setOdataContext(const QString &odata_context) {
    m_odata_context = odata_context;
    m_odata_context_isSet = true;
}

bool OAIIntuneGroups::is_odata_context_Set() const{
    return m_odata_context_isSet;
}

bool OAIIntuneGroups::is_odata_context_Valid() const{
    return m_odata_context_isValid;
}

QList<OAIIntuneGroups_value_inner> OAIIntuneGroups::getValue() const {
    return m_value;
}
void OAIIntuneGroups::setValue(const QList<OAIIntuneGroups_value_inner> &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIIntuneGroups::is_value_Set() const{
    return m_value_isSet;
}

bool OAIIntuneGroups::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIIntuneGroups::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_odata_context_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_value.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIIntuneGroups::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
