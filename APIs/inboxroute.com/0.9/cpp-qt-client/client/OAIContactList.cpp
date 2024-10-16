/**
 * Mailsquad
 * MailSquad offers an affordable and super easy way to create, send and track delightful emails.
 *
 * The version of the OpenAPI document: 0.9
 * Contact: support@mailsquad.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIContactList.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIContactList::OAIContactList(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIContactList::OAIContactList() {
    this->initializeModel();
}

OAIContactList::~OAIContactList() {}

void OAIContactList::initializeModel() {

    m__id_isSet = false;
    m__id_isValid = false;

    m_clientid_isSet = false;
    m_clientid_isValid = false;

    m_created_isSet = false;
    m_created_isValid = false;

    m_customfields_isSet = false;
    m_customfields_isValid = false;

    m_eventcustomizations_isSet = false;
    m_eventcustomizations_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;
}

void OAIContactList::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIContactList::fromJsonObject(QJsonObject json) {

    m__id_isValid = ::OpenAPI::fromJsonValue(m__id, json[QString("_id")]);
    m__id_isSet = !json[QString("_id")].isNull() && m__id_isValid;

    m_clientid_isValid = ::OpenAPI::fromJsonValue(m_clientid, json[QString("clientid")]);
    m_clientid_isSet = !json[QString("clientid")].isNull() && m_clientid_isValid;

    m_created_isValid = ::OpenAPI::fromJsonValue(m_created, json[QString("created")]);
    m_created_isSet = !json[QString("created")].isNull() && m_created_isValid;

    m_customfields_isValid = ::OpenAPI::fromJsonValue(m_customfields, json[QString("customfields")]);
    m_customfields_isSet = !json[QString("customfields")].isNull() && m_customfields_isValid;

    m_eventcustomizations_isValid = ::OpenAPI::fromJsonValue(m_eventcustomizations, json[QString("eventcustomizations")]);
    m_eventcustomizations_isSet = !json[QString("eventcustomizations")].isNull() && m_eventcustomizations_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;
}

QString OAIContactList::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIContactList::asJsonObject() const {
    QJsonObject obj;
    if (m__id_isSet) {
        obj.insert(QString("_id"), ::OpenAPI::toJsonValue(m__id));
    }
    if (m_clientid_isSet) {
        obj.insert(QString("clientid"), ::OpenAPI::toJsonValue(m_clientid));
    }
    if (m_created_isSet) {
        obj.insert(QString("created"), ::OpenAPI::toJsonValue(m_created));
    }
    if (m_customfields.size() > 0) {
        obj.insert(QString("customfields"), ::OpenAPI::toJsonValue(m_customfields));
    }
    if (m_eventcustomizations.size() > 0) {
        obj.insert(QString("eventcustomizations"), ::OpenAPI::toJsonValue(m_eventcustomizations));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    return obj;
}

QString OAIContactList::getId() const {
    return m__id;
}
void OAIContactList::setId(const QString &_id) {
    m__id = _id;
    m__id_isSet = true;
}

bool OAIContactList::is__id_Set() const{
    return m__id_isSet;
}

bool OAIContactList::is__id_Valid() const{
    return m__id_isValid;
}

QString OAIContactList::getClientid() const {
    return m_clientid;
}
void OAIContactList::setClientid(const QString &clientid) {
    m_clientid = clientid;
    m_clientid_isSet = true;
}

bool OAIContactList::is_clientid_Set() const{
    return m_clientid_isSet;
}

bool OAIContactList::is_clientid_Valid() const{
    return m_clientid_isValid;
}

QDateTime OAIContactList::getCreated() const {
    return m_created;
}
void OAIContactList::setCreated(const QDateTime &created) {
    m_created = created;
    m_created_isSet = true;
}

bool OAIContactList::is_created_Set() const{
    return m_created_isSet;
}

bool OAIContactList::is_created_Valid() const{
    return m_created_isValid;
}

QList<OAIContactCustomFieldSchema> OAIContactList::getCustomfields() const {
    return m_customfields;
}
void OAIContactList::setCustomfields(const QList<OAIContactCustomFieldSchema> &customfields) {
    m_customfields = customfields;
    m_customfields_isSet = true;
}

bool OAIContactList::is_customfields_Set() const{
    return m_customfields_isSet;
}

bool OAIContactList::is_customfields_Valid() const{
    return m_customfields_isValid;
}

QList<OAIContactListEventCustomization> OAIContactList::getEventcustomizations() const {
    return m_eventcustomizations;
}
void OAIContactList::setEventcustomizations(const QList<OAIContactListEventCustomization> &eventcustomizations) {
    m_eventcustomizations = eventcustomizations;
    m_eventcustomizations_isSet = true;
}

bool OAIContactList::is_eventcustomizations_Set() const{
    return m_eventcustomizations_isSet;
}

bool OAIContactList::is_eventcustomizations_Valid() const{
    return m_eventcustomizations_isValid;
}

QString OAIContactList::getName() const {
    return m_name;
}
void OAIContactList::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIContactList::is_name_Set() const{
    return m_name_isSet;
}

bool OAIContactList::is_name_Valid() const{
    return m_name_isValid;
}

bool OAIContactList::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m__id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_clientid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_customfields.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_eventcustomizations.size() > 0) {
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

bool OAIContactList::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
