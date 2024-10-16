/**
 * CallFire API Documentation
 * CallFire
 *
 * The version of the OpenAPI document: V2
 * Contact: support@callfire.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICallRecipient.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICallRecipient::OAICallRecipient(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICallRecipient::OAICallRecipient() {
    this->initializeModel();
}

OAICallRecipient::~OAICallRecipient() {}

void OAICallRecipient::initializeModel() {

    m_attributes_isSet = false;
    m_attributes_isValid = false;

    m_contact_id_isSet = false;
    m_contact_id_isValid = false;

    m_dialplan_xml_isSet = false;
    m_dialplan_xml_isValid = false;

    m_from_number_isSet = false;
    m_from_number_isValid = false;

    m_live_message_isSet = false;
    m_live_message_isValid = false;

    m_live_message_sound_id_isSet = false;
    m_live_message_sound_id_isValid = false;

    m_machine_message_isSet = false;
    m_machine_message_isValid = false;

    m_machine_message_sound_id_isSet = false;
    m_machine_message_sound_id_isValid = false;

    m_phone_number_isSet = false;
    m_phone_number_isValid = false;

    m_transfer_digit_isSet = false;
    m_transfer_digit_isValid = false;

    m_transfer_message_isSet = false;
    m_transfer_message_isValid = false;

    m_transfer_message_sound_id_isSet = false;
    m_transfer_message_sound_id_isValid = false;

    m_transfer_number_isSet = false;
    m_transfer_number_isValid = false;

    m_voice_isSet = false;
    m_voice_isValid = false;
}

void OAICallRecipient::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICallRecipient::fromJsonObject(QJsonObject json) {

    m_attributes_isValid = ::OpenAPI::fromJsonValue(m_attributes, json[QString("attributes")]);
    m_attributes_isSet = !json[QString("attributes")].isNull() && m_attributes_isValid;

    m_contact_id_isValid = ::OpenAPI::fromJsonValue(m_contact_id, json[QString("contactId")]);
    m_contact_id_isSet = !json[QString("contactId")].isNull() && m_contact_id_isValid;

    m_dialplan_xml_isValid = ::OpenAPI::fromJsonValue(m_dialplan_xml, json[QString("dialplanXml")]);
    m_dialplan_xml_isSet = !json[QString("dialplanXml")].isNull() && m_dialplan_xml_isValid;

    m_from_number_isValid = ::OpenAPI::fromJsonValue(m_from_number, json[QString("fromNumber")]);
    m_from_number_isSet = !json[QString("fromNumber")].isNull() && m_from_number_isValid;

    m_live_message_isValid = ::OpenAPI::fromJsonValue(m_live_message, json[QString("liveMessage")]);
    m_live_message_isSet = !json[QString("liveMessage")].isNull() && m_live_message_isValid;

    m_live_message_sound_id_isValid = ::OpenAPI::fromJsonValue(m_live_message_sound_id, json[QString("liveMessageSoundId")]);
    m_live_message_sound_id_isSet = !json[QString("liveMessageSoundId")].isNull() && m_live_message_sound_id_isValid;

    m_machine_message_isValid = ::OpenAPI::fromJsonValue(m_machine_message, json[QString("machineMessage")]);
    m_machine_message_isSet = !json[QString("machineMessage")].isNull() && m_machine_message_isValid;

    m_machine_message_sound_id_isValid = ::OpenAPI::fromJsonValue(m_machine_message_sound_id, json[QString("machineMessageSoundId")]);
    m_machine_message_sound_id_isSet = !json[QString("machineMessageSoundId")].isNull() && m_machine_message_sound_id_isValid;

    m_phone_number_isValid = ::OpenAPI::fromJsonValue(m_phone_number, json[QString("phoneNumber")]);
    m_phone_number_isSet = !json[QString("phoneNumber")].isNull() && m_phone_number_isValid;

    m_transfer_digit_isValid = ::OpenAPI::fromJsonValue(m_transfer_digit, json[QString("transferDigit")]);
    m_transfer_digit_isSet = !json[QString("transferDigit")].isNull() && m_transfer_digit_isValid;

    m_transfer_message_isValid = ::OpenAPI::fromJsonValue(m_transfer_message, json[QString("transferMessage")]);
    m_transfer_message_isSet = !json[QString("transferMessage")].isNull() && m_transfer_message_isValid;

    m_transfer_message_sound_id_isValid = ::OpenAPI::fromJsonValue(m_transfer_message_sound_id, json[QString("transferMessageSoundId")]);
    m_transfer_message_sound_id_isSet = !json[QString("transferMessageSoundId")].isNull() && m_transfer_message_sound_id_isValid;

    m_transfer_number_isValid = ::OpenAPI::fromJsonValue(m_transfer_number, json[QString("transferNumber")]);
    m_transfer_number_isSet = !json[QString("transferNumber")].isNull() && m_transfer_number_isValid;

    m_voice_isValid = ::OpenAPI::fromJsonValue(m_voice, json[QString("voice")]);
    m_voice_isSet = !json[QString("voice")].isNull() && m_voice_isValid;
}

QString OAICallRecipient::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICallRecipient::asJsonObject() const {
    QJsonObject obj;
    if (m_attributes.size() > 0) {
        obj.insert(QString("attributes"), ::OpenAPI::toJsonValue(m_attributes));
    }
    if (m_contact_id_isSet) {
        obj.insert(QString("contactId"), ::OpenAPI::toJsonValue(m_contact_id));
    }
    if (m_dialplan_xml_isSet) {
        obj.insert(QString("dialplanXml"), ::OpenAPI::toJsonValue(m_dialplan_xml));
    }
    if (m_from_number_isSet) {
        obj.insert(QString("fromNumber"), ::OpenAPI::toJsonValue(m_from_number));
    }
    if (m_live_message_isSet) {
        obj.insert(QString("liveMessage"), ::OpenAPI::toJsonValue(m_live_message));
    }
    if (m_live_message_sound_id_isSet) {
        obj.insert(QString("liveMessageSoundId"), ::OpenAPI::toJsonValue(m_live_message_sound_id));
    }
    if (m_machine_message_isSet) {
        obj.insert(QString("machineMessage"), ::OpenAPI::toJsonValue(m_machine_message));
    }
    if (m_machine_message_sound_id_isSet) {
        obj.insert(QString("machineMessageSoundId"), ::OpenAPI::toJsonValue(m_machine_message_sound_id));
    }
    if (m_phone_number_isSet) {
        obj.insert(QString("phoneNumber"), ::OpenAPI::toJsonValue(m_phone_number));
    }
    if (m_transfer_digit_isSet) {
        obj.insert(QString("transferDigit"), ::OpenAPI::toJsonValue(m_transfer_digit));
    }
    if (m_transfer_message_isSet) {
        obj.insert(QString("transferMessage"), ::OpenAPI::toJsonValue(m_transfer_message));
    }
    if (m_transfer_message_sound_id_isSet) {
        obj.insert(QString("transferMessageSoundId"), ::OpenAPI::toJsonValue(m_transfer_message_sound_id));
    }
    if (m_transfer_number_isSet) {
        obj.insert(QString("transferNumber"), ::OpenAPI::toJsonValue(m_transfer_number));
    }
    if (m_voice_isSet) {
        obj.insert(QString("voice"), ::OpenAPI::toJsonValue(m_voice));
    }
    return obj;
}

QMap<QString, QString> OAICallRecipient::getAttributes() const {
    return m_attributes;
}
void OAICallRecipient::setAttributes(const QMap<QString, QString> &attributes) {
    m_attributes = attributes;
    m_attributes_isSet = true;
}

bool OAICallRecipient::is_attributes_Set() const{
    return m_attributes_isSet;
}

bool OAICallRecipient::is_attributes_Valid() const{
    return m_attributes_isValid;
}

qint64 OAICallRecipient::getContactId() const {
    return m_contact_id;
}
void OAICallRecipient::setContactId(const qint64 &contact_id) {
    m_contact_id = contact_id;
    m_contact_id_isSet = true;
}

bool OAICallRecipient::is_contact_id_Set() const{
    return m_contact_id_isSet;
}

bool OAICallRecipient::is_contact_id_Valid() const{
    return m_contact_id_isValid;
}

QString OAICallRecipient::getDialplanXml() const {
    return m_dialplan_xml;
}
void OAICallRecipient::setDialplanXml(const QString &dialplan_xml) {
    m_dialplan_xml = dialplan_xml;
    m_dialplan_xml_isSet = true;
}

bool OAICallRecipient::is_dialplan_xml_Set() const{
    return m_dialplan_xml_isSet;
}

bool OAICallRecipient::is_dialplan_xml_Valid() const{
    return m_dialplan_xml_isValid;
}

QString OAICallRecipient::getFromNumber() const {
    return m_from_number;
}
void OAICallRecipient::setFromNumber(const QString &from_number) {
    m_from_number = from_number;
    m_from_number_isSet = true;
}

bool OAICallRecipient::is_from_number_Set() const{
    return m_from_number_isSet;
}

bool OAICallRecipient::is_from_number_Valid() const{
    return m_from_number_isValid;
}

QString OAICallRecipient::getLiveMessage() const {
    return m_live_message;
}
void OAICallRecipient::setLiveMessage(const QString &live_message) {
    m_live_message = live_message;
    m_live_message_isSet = true;
}

bool OAICallRecipient::is_live_message_Set() const{
    return m_live_message_isSet;
}

bool OAICallRecipient::is_live_message_Valid() const{
    return m_live_message_isValid;
}

qint64 OAICallRecipient::getLiveMessageSoundId() const {
    return m_live_message_sound_id;
}
void OAICallRecipient::setLiveMessageSoundId(const qint64 &live_message_sound_id) {
    m_live_message_sound_id = live_message_sound_id;
    m_live_message_sound_id_isSet = true;
}

bool OAICallRecipient::is_live_message_sound_id_Set() const{
    return m_live_message_sound_id_isSet;
}

bool OAICallRecipient::is_live_message_sound_id_Valid() const{
    return m_live_message_sound_id_isValid;
}

QString OAICallRecipient::getMachineMessage() const {
    return m_machine_message;
}
void OAICallRecipient::setMachineMessage(const QString &machine_message) {
    m_machine_message = machine_message;
    m_machine_message_isSet = true;
}

bool OAICallRecipient::is_machine_message_Set() const{
    return m_machine_message_isSet;
}

bool OAICallRecipient::is_machine_message_Valid() const{
    return m_machine_message_isValid;
}

qint64 OAICallRecipient::getMachineMessageSoundId() const {
    return m_machine_message_sound_id;
}
void OAICallRecipient::setMachineMessageSoundId(const qint64 &machine_message_sound_id) {
    m_machine_message_sound_id = machine_message_sound_id;
    m_machine_message_sound_id_isSet = true;
}

bool OAICallRecipient::is_machine_message_sound_id_Set() const{
    return m_machine_message_sound_id_isSet;
}

bool OAICallRecipient::is_machine_message_sound_id_Valid() const{
    return m_machine_message_sound_id_isValid;
}

QString OAICallRecipient::getPhoneNumber() const {
    return m_phone_number;
}
void OAICallRecipient::setPhoneNumber(const QString &phone_number) {
    m_phone_number = phone_number;
    m_phone_number_isSet = true;
}

bool OAICallRecipient::is_phone_number_Set() const{
    return m_phone_number_isSet;
}

bool OAICallRecipient::is_phone_number_Valid() const{
    return m_phone_number_isValid;
}

QString OAICallRecipient::getTransferDigit() const {
    return m_transfer_digit;
}
void OAICallRecipient::setTransferDigit(const QString &transfer_digit) {
    m_transfer_digit = transfer_digit;
    m_transfer_digit_isSet = true;
}

bool OAICallRecipient::is_transfer_digit_Set() const{
    return m_transfer_digit_isSet;
}

bool OAICallRecipient::is_transfer_digit_Valid() const{
    return m_transfer_digit_isValid;
}

QString OAICallRecipient::getTransferMessage() const {
    return m_transfer_message;
}
void OAICallRecipient::setTransferMessage(const QString &transfer_message) {
    m_transfer_message = transfer_message;
    m_transfer_message_isSet = true;
}

bool OAICallRecipient::is_transfer_message_Set() const{
    return m_transfer_message_isSet;
}

bool OAICallRecipient::is_transfer_message_Valid() const{
    return m_transfer_message_isValid;
}

qint64 OAICallRecipient::getTransferMessageSoundId() const {
    return m_transfer_message_sound_id;
}
void OAICallRecipient::setTransferMessageSoundId(const qint64 &transfer_message_sound_id) {
    m_transfer_message_sound_id = transfer_message_sound_id;
    m_transfer_message_sound_id_isSet = true;
}

bool OAICallRecipient::is_transfer_message_sound_id_Set() const{
    return m_transfer_message_sound_id_isSet;
}

bool OAICallRecipient::is_transfer_message_sound_id_Valid() const{
    return m_transfer_message_sound_id_isValid;
}

QString OAICallRecipient::getTransferNumber() const {
    return m_transfer_number;
}
void OAICallRecipient::setTransferNumber(const QString &transfer_number) {
    m_transfer_number = transfer_number;
    m_transfer_number_isSet = true;
}

bool OAICallRecipient::is_transfer_number_Set() const{
    return m_transfer_number_isSet;
}

bool OAICallRecipient::is_transfer_number_Valid() const{
    return m_transfer_number_isValid;
}

QString OAICallRecipient::getVoice() const {
    return m_voice;
}
void OAICallRecipient::setVoice(const QString &voice) {
    m_voice = voice;
    m_voice_isSet = true;
}

bool OAICallRecipient::is_voice_Set() const{
    return m_voice_isSet;
}

bool OAICallRecipient::is_voice_Valid() const{
    return m_voice_isValid;
}

bool OAICallRecipient::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_attributes.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_contact_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dialplan_xml_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_from_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_live_message_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_live_message_sound_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_machine_message_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_machine_message_sound_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_phone_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_transfer_digit_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_transfer_message_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_transfer_message_sound_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_transfer_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_voice_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICallRecipient::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
