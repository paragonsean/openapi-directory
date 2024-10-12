/**
 * obono RKSV API
 * Provides a RESTful API for interacting with virtual cash registers and creating receipts that are conform with the Registrierkassensicherheitsverordnung (RKSV).  You may find our [automatically generated clients](./clients) for various programming languages and environments helpful... 
 *
 * The version of the OpenAPI document: 1.4.0.0
 * Contact: info@obono.at
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIBelegdaten.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBelegdaten::OAIBelegdaten(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBelegdaten::OAIBelegdaten() {
    this->initializeModel();
}

OAIBelegdaten::~OAIBelegdaten() {}

void OAIBelegdaten::initializeModel() {

    m_externer_beleg_belegkreis_isSet = false;
    m_externer_beleg_belegkreis_isValid = false;

    m_externer_beleg_bezeichnung_isSet = false;
    m_externer_beleg_bezeichnung_isValid = false;

    m_externer_beleg_referenz_isSet = false;
    m_externer_beleg_referenz_isValid = false;

    m_kunde_isSet = false;
    m_kunde_isValid = false;

    m_notizen_isSet = false;
    m_notizen_isValid = false;

    m_posten_isSet = false;
    m_posten_isValid = false;

    m_rabatte_isSet = false;
    m_rabatte_isValid = false;

    m_storno_isSet = false;
    m_storno_isValid = false;

    m_storno_beleg_uuid_isSet = false;
    m_storno_beleg_uuid_isValid = false;

    m_storno_text_isSet = false;
    m_storno_text_isValid = false;

    m_training_isSet = false;
    m_training_isValid = false;

    m_unternehmen_adresse1_isSet = false;
    m_unternehmen_adresse1_isValid = false;

    m_unternehmen_adresse2_isSet = false;
    m_unternehmen_adresse2_isValid = false;

    m_unternehmen_fusszeile_isSet = false;
    m_unternehmen_fusszeile_isValid = false;

    m_unternehmen_id_isSet = false;
    m_unternehmen_id_isValid = false;

    m_unternehmen_id_typ_isSet = false;
    m_unternehmen_id_typ_isValid = false;

    m_unternehmen_kopfzeile_isSet = false;
    m_unternehmen_kopfzeile_isValid = false;

    m_unternehmen_name_isSet = false;
    m_unternehmen_name_isValid = false;

    m_unternehmen_ort_isSet = false;
    m_unternehmen_ort_isValid = false;

    m_unternehmen_plz_isSet = false;
    m_unternehmen_plz_isValid = false;

    m_zahlungen_isSet = false;
    m_zahlungen_isValid = false;
}

void OAIBelegdaten::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBelegdaten::fromJsonObject(QJsonObject json) {

    m_externer_beleg_belegkreis_isValid = ::OpenAPI::fromJsonValue(m_externer_beleg_belegkreis, json[QString("Externer-Beleg-Belegkreis")]);
    m_externer_beleg_belegkreis_isSet = !json[QString("Externer-Beleg-Belegkreis")].isNull() && m_externer_beleg_belegkreis_isValid;

    m_externer_beleg_bezeichnung_isValid = ::OpenAPI::fromJsonValue(m_externer_beleg_bezeichnung, json[QString("Externer-Beleg-Bezeichnung")]);
    m_externer_beleg_bezeichnung_isSet = !json[QString("Externer-Beleg-Bezeichnung")].isNull() && m_externer_beleg_bezeichnung_isValid;

    m_externer_beleg_referenz_isValid = ::OpenAPI::fromJsonValue(m_externer_beleg_referenz, json[QString("Externer-Beleg-Referenz")]);
    m_externer_beleg_referenz_isSet = !json[QString("Externer-Beleg-Referenz")].isNull() && m_externer_beleg_referenz_isValid;

    m_kunde_isValid = ::OpenAPI::fromJsonValue(m_kunde, json[QString("Kunde")]);
    m_kunde_isSet = !json[QString("Kunde")].isNull() && m_kunde_isValid;

    m_notizen_isValid = ::OpenAPI::fromJsonValue(m_notizen, json[QString("Notizen")]);
    m_notizen_isSet = !json[QString("Notizen")].isNull() && m_notizen_isValid;

    m_posten_isValid = ::OpenAPI::fromJsonValue(m_posten, json[QString("Posten")]);
    m_posten_isSet = !json[QString("Posten")].isNull() && m_posten_isValid;

    m_rabatte_isValid = ::OpenAPI::fromJsonValue(m_rabatte, json[QString("Rabatte")]);
    m_rabatte_isSet = !json[QString("Rabatte")].isNull() && m_rabatte_isValid;

    m_storno_isValid = ::OpenAPI::fromJsonValue(m_storno, json[QString("Storno")]);
    m_storno_isSet = !json[QString("Storno")].isNull() && m_storno_isValid;

    m_storno_beleg_uuid_isValid = ::OpenAPI::fromJsonValue(m_storno_beleg_uuid, json[QString("Storno-Beleg-UUID")]);
    m_storno_beleg_uuid_isSet = !json[QString("Storno-Beleg-UUID")].isNull() && m_storno_beleg_uuid_isValid;

    m_storno_text_isValid = ::OpenAPI::fromJsonValue(m_storno_text, json[QString("Storno-Text")]);
    m_storno_text_isSet = !json[QString("Storno-Text")].isNull() && m_storno_text_isValid;

    m_training_isValid = ::OpenAPI::fromJsonValue(m_training, json[QString("Training")]);
    m_training_isSet = !json[QString("Training")].isNull() && m_training_isValid;

    m_unternehmen_adresse1_isValid = ::OpenAPI::fromJsonValue(m_unternehmen_adresse1, json[QString("Unternehmen-Adresse1")]);
    m_unternehmen_adresse1_isSet = !json[QString("Unternehmen-Adresse1")].isNull() && m_unternehmen_adresse1_isValid;

    m_unternehmen_adresse2_isValid = ::OpenAPI::fromJsonValue(m_unternehmen_adresse2, json[QString("Unternehmen-Adresse2")]);
    m_unternehmen_adresse2_isSet = !json[QString("Unternehmen-Adresse2")].isNull() && m_unternehmen_adresse2_isValid;

    m_unternehmen_fusszeile_isValid = ::OpenAPI::fromJsonValue(m_unternehmen_fusszeile, json[QString("Unternehmen-Fusszeile")]);
    m_unternehmen_fusszeile_isSet = !json[QString("Unternehmen-Fusszeile")].isNull() && m_unternehmen_fusszeile_isValid;

    m_unternehmen_id_isValid = ::OpenAPI::fromJsonValue(m_unternehmen_id, json[QString("Unternehmen-ID")]);
    m_unternehmen_id_isSet = !json[QString("Unternehmen-ID")].isNull() && m_unternehmen_id_isValid;

    m_unternehmen_id_typ_isValid = ::OpenAPI::fromJsonValue(m_unternehmen_id_typ, json[QString("Unternehmen-ID-Typ")]);
    m_unternehmen_id_typ_isSet = !json[QString("Unternehmen-ID-Typ")].isNull() && m_unternehmen_id_typ_isValid;

    m_unternehmen_kopfzeile_isValid = ::OpenAPI::fromJsonValue(m_unternehmen_kopfzeile, json[QString("Unternehmen-Kopfzeile")]);
    m_unternehmen_kopfzeile_isSet = !json[QString("Unternehmen-Kopfzeile")].isNull() && m_unternehmen_kopfzeile_isValid;

    m_unternehmen_name_isValid = ::OpenAPI::fromJsonValue(m_unternehmen_name, json[QString("Unternehmen-Name")]);
    m_unternehmen_name_isSet = !json[QString("Unternehmen-Name")].isNull() && m_unternehmen_name_isValid;

    m_unternehmen_ort_isValid = ::OpenAPI::fromJsonValue(m_unternehmen_ort, json[QString("Unternehmen-Ort")]);
    m_unternehmen_ort_isSet = !json[QString("Unternehmen-Ort")].isNull() && m_unternehmen_ort_isValid;

    m_unternehmen_plz_isValid = ::OpenAPI::fromJsonValue(m_unternehmen_plz, json[QString("Unternehmen-PLZ")]);
    m_unternehmen_plz_isSet = !json[QString("Unternehmen-PLZ")].isNull() && m_unternehmen_plz_isValid;

    m_zahlungen_isValid = ::OpenAPI::fromJsonValue(m_zahlungen, json[QString("Zahlungen")]);
    m_zahlungen_isSet = !json[QString("Zahlungen")].isNull() && m_zahlungen_isValid;
}

QString OAIBelegdaten::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBelegdaten::asJsonObject() const {
    QJsonObject obj;
    if (m_externer_beleg_belegkreis_isSet) {
        obj.insert(QString("Externer-Beleg-Belegkreis"), ::OpenAPI::toJsonValue(m_externer_beleg_belegkreis));
    }
    if (m_externer_beleg_bezeichnung_isSet) {
        obj.insert(QString("Externer-Beleg-Bezeichnung"), ::OpenAPI::toJsonValue(m_externer_beleg_bezeichnung));
    }
    if (m_externer_beleg_referenz_isSet) {
        obj.insert(QString("Externer-Beleg-Referenz"), ::OpenAPI::toJsonValue(m_externer_beleg_referenz));
    }
    if (m_kunde_isSet) {
        obj.insert(QString("Kunde"), ::OpenAPI::toJsonValue(m_kunde));
    }
    if (m_notizen.size() > 0) {
        obj.insert(QString("Notizen"), ::OpenAPI::toJsonValue(m_notizen));
    }
    if (m_posten.size() > 0) {
        obj.insert(QString("Posten"), ::OpenAPI::toJsonValue(m_posten));
    }
    if (m_rabatte.size() > 0) {
        obj.insert(QString("Rabatte"), ::OpenAPI::toJsonValue(m_rabatte));
    }
    if (m_storno_isSet) {
        obj.insert(QString("Storno"), ::OpenAPI::toJsonValue(m_storno));
    }
    if (m_storno_beleg_uuid_isSet) {
        obj.insert(QString("Storno-Beleg-UUID"), ::OpenAPI::toJsonValue(m_storno_beleg_uuid));
    }
    if (m_storno_text_isSet) {
        obj.insert(QString("Storno-Text"), ::OpenAPI::toJsonValue(m_storno_text));
    }
    if (m_training_isSet) {
        obj.insert(QString("Training"), ::OpenAPI::toJsonValue(m_training));
    }
    if (m_unternehmen_adresse1_isSet) {
        obj.insert(QString("Unternehmen-Adresse1"), ::OpenAPI::toJsonValue(m_unternehmen_adresse1));
    }
    if (m_unternehmen_adresse2_isSet) {
        obj.insert(QString("Unternehmen-Adresse2"), ::OpenAPI::toJsonValue(m_unternehmen_adresse2));
    }
    if (m_unternehmen_fusszeile_isSet) {
        obj.insert(QString("Unternehmen-Fusszeile"), ::OpenAPI::toJsonValue(m_unternehmen_fusszeile));
    }
    if (m_unternehmen_id_isSet) {
        obj.insert(QString("Unternehmen-ID"), ::OpenAPI::toJsonValue(m_unternehmen_id));
    }
    if (m_unternehmen_id_typ_isSet) {
        obj.insert(QString("Unternehmen-ID-Typ"), ::OpenAPI::toJsonValue(m_unternehmen_id_typ));
    }
    if (m_unternehmen_kopfzeile_isSet) {
        obj.insert(QString("Unternehmen-Kopfzeile"), ::OpenAPI::toJsonValue(m_unternehmen_kopfzeile));
    }
    if (m_unternehmen_name_isSet) {
        obj.insert(QString("Unternehmen-Name"), ::OpenAPI::toJsonValue(m_unternehmen_name));
    }
    if (m_unternehmen_ort_isSet) {
        obj.insert(QString("Unternehmen-Ort"), ::OpenAPI::toJsonValue(m_unternehmen_ort));
    }
    if (m_unternehmen_plz_isSet) {
        obj.insert(QString("Unternehmen-PLZ"), ::OpenAPI::toJsonValue(m_unternehmen_plz));
    }
    if (m_zahlungen.size() > 0) {
        obj.insert(QString("Zahlungen"), ::OpenAPI::toJsonValue(m_zahlungen));
    }
    return obj;
}

QString OAIBelegdaten::getExternerBelegBelegkreis() const {
    return m_externer_beleg_belegkreis;
}
void OAIBelegdaten::setExternerBelegBelegkreis(const QString &externer_beleg_belegkreis) {
    m_externer_beleg_belegkreis = externer_beleg_belegkreis;
    m_externer_beleg_belegkreis_isSet = true;
}

bool OAIBelegdaten::is_externer_beleg_belegkreis_Set() const{
    return m_externer_beleg_belegkreis_isSet;
}

bool OAIBelegdaten::is_externer_beleg_belegkreis_Valid() const{
    return m_externer_beleg_belegkreis_isValid;
}

QString OAIBelegdaten::getExternerBelegBezeichnung() const {
    return m_externer_beleg_bezeichnung;
}
void OAIBelegdaten::setExternerBelegBezeichnung(const QString &externer_beleg_bezeichnung) {
    m_externer_beleg_bezeichnung = externer_beleg_bezeichnung;
    m_externer_beleg_bezeichnung_isSet = true;
}

bool OAIBelegdaten::is_externer_beleg_bezeichnung_Set() const{
    return m_externer_beleg_bezeichnung_isSet;
}

bool OAIBelegdaten::is_externer_beleg_bezeichnung_Valid() const{
    return m_externer_beleg_bezeichnung_isValid;
}

QString OAIBelegdaten::getExternerBelegReferenz() const {
    return m_externer_beleg_referenz;
}
void OAIBelegdaten::setExternerBelegReferenz(const QString &externer_beleg_referenz) {
    m_externer_beleg_referenz = externer_beleg_referenz;
    m_externer_beleg_referenz_isSet = true;
}

bool OAIBelegdaten::is_externer_beleg_referenz_Set() const{
    return m_externer_beleg_referenz_isSet;
}

bool OAIBelegdaten::is_externer_beleg_referenz_Valid() const{
    return m_externer_beleg_referenz_isValid;
}

QString OAIBelegdaten::getKunde() const {
    return m_kunde;
}
void OAIBelegdaten::setKunde(const QString &kunde) {
    m_kunde = kunde;
    m_kunde_isSet = true;
}

bool OAIBelegdaten::is_kunde_Set() const{
    return m_kunde_isSet;
}

bool OAIBelegdaten::is_kunde_Valid() const{
    return m_kunde_isValid;
}

QList<QString> OAIBelegdaten::getNotizen() const {
    return m_notizen;
}
void OAIBelegdaten::setNotizen(const QList<QString> &notizen) {
    m_notizen = notizen;
    m_notizen_isSet = true;
}

bool OAIBelegdaten::is_notizen_Set() const{
    return m_notizen_isSet;
}

bool OAIBelegdaten::is_notizen_Valid() const{
    return m_notizen_isValid;
}

QList<OAIPosten> OAIBelegdaten::getPosten() const {
    return m_posten;
}
void OAIBelegdaten::setPosten(const QList<OAIPosten> &posten) {
    m_posten = posten;
    m_posten_isSet = true;
}

bool OAIBelegdaten::is_posten_Set() const{
    return m_posten_isSet;
}

bool OAIBelegdaten::is_posten_Valid() const{
    return m_posten_isValid;
}

QList<OAIRabatt> OAIBelegdaten::getRabatte() const {
    return m_rabatte;
}
void OAIBelegdaten::setRabatte(const QList<OAIRabatt> &rabatte) {
    m_rabatte = rabatte;
    m_rabatte_isSet = true;
}

bool OAIBelegdaten::is_rabatte_Set() const{
    return m_rabatte_isSet;
}

bool OAIBelegdaten::is_rabatte_Valid() const{
    return m_rabatte_isValid;
}

bool OAIBelegdaten::isStorno() const {
    return m_storno;
}
void OAIBelegdaten::setStorno(const bool &storno) {
    m_storno = storno;
    m_storno_isSet = true;
}

bool OAIBelegdaten::is_storno_Set() const{
    return m_storno_isSet;
}

bool OAIBelegdaten::is_storno_Valid() const{
    return m_storno_isValid;
}

QString OAIBelegdaten::getStornoBelegUuid() const {
    return m_storno_beleg_uuid;
}
void OAIBelegdaten::setStornoBelegUuid(const QString &storno_beleg_uuid) {
    m_storno_beleg_uuid = storno_beleg_uuid;
    m_storno_beleg_uuid_isSet = true;
}

bool OAIBelegdaten::is_storno_beleg_uuid_Set() const{
    return m_storno_beleg_uuid_isSet;
}

bool OAIBelegdaten::is_storno_beleg_uuid_Valid() const{
    return m_storno_beleg_uuid_isValid;
}

QString OAIBelegdaten::getStornoText() const {
    return m_storno_text;
}
void OAIBelegdaten::setStornoText(const QString &storno_text) {
    m_storno_text = storno_text;
    m_storno_text_isSet = true;
}

bool OAIBelegdaten::is_storno_text_Set() const{
    return m_storno_text_isSet;
}

bool OAIBelegdaten::is_storno_text_Valid() const{
    return m_storno_text_isValid;
}

bool OAIBelegdaten::isTraining() const {
    return m_training;
}
void OAIBelegdaten::setTraining(const bool &training) {
    m_training = training;
    m_training_isSet = true;
}

bool OAIBelegdaten::is_training_Set() const{
    return m_training_isSet;
}

bool OAIBelegdaten::is_training_Valid() const{
    return m_training_isValid;
}

QString OAIBelegdaten::getUnternehmenAdresse1() const {
    return m_unternehmen_adresse1;
}
void OAIBelegdaten::setUnternehmenAdresse1(const QString &unternehmen_adresse1) {
    m_unternehmen_adresse1 = unternehmen_adresse1;
    m_unternehmen_adresse1_isSet = true;
}

bool OAIBelegdaten::is_unternehmen_adresse1_Set() const{
    return m_unternehmen_adresse1_isSet;
}

bool OAIBelegdaten::is_unternehmen_adresse1_Valid() const{
    return m_unternehmen_adresse1_isValid;
}

QString OAIBelegdaten::getUnternehmenAdresse2() const {
    return m_unternehmen_adresse2;
}
void OAIBelegdaten::setUnternehmenAdresse2(const QString &unternehmen_adresse2) {
    m_unternehmen_adresse2 = unternehmen_adresse2;
    m_unternehmen_adresse2_isSet = true;
}

bool OAIBelegdaten::is_unternehmen_adresse2_Set() const{
    return m_unternehmen_adresse2_isSet;
}

bool OAIBelegdaten::is_unternehmen_adresse2_Valid() const{
    return m_unternehmen_adresse2_isValid;
}

QString OAIBelegdaten::getUnternehmenFusszeile() const {
    return m_unternehmen_fusszeile;
}
void OAIBelegdaten::setUnternehmenFusszeile(const QString &unternehmen_fusszeile) {
    m_unternehmen_fusszeile = unternehmen_fusszeile;
    m_unternehmen_fusszeile_isSet = true;
}

bool OAIBelegdaten::is_unternehmen_fusszeile_Set() const{
    return m_unternehmen_fusszeile_isSet;
}

bool OAIBelegdaten::is_unternehmen_fusszeile_Valid() const{
    return m_unternehmen_fusszeile_isValid;
}

QString OAIBelegdaten::getUnternehmenId() const {
    return m_unternehmen_id;
}
void OAIBelegdaten::setUnternehmenId(const QString &unternehmen_id) {
    m_unternehmen_id = unternehmen_id;
    m_unternehmen_id_isSet = true;
}

bool OAIBelegdaten::is_unternehmen_id_Set() const{
    return m_unternehmen_id_isSet;
}

bool OAIBelegdaten::is_unternehmen_id_Valid() const{
    return m_unternehmen_id_isValid;
}

QString OAIBelegdaten::getUnternehmenIdTyp() const {
    return m_unternehmen_id_typ;
}
void OAIBelegdaten::setUnternehmenIdTyp(const QString &unternehmen_id_typ) {
    m_unternehmen_id_typ = unternehmen_id_typ;
    m_unternehmen_id_typ_isSet = true;
}

bool OAIBelegdaten::is_unternehmen_id_typ_Set() const{
    return m_unternehmen_id_typ_isSet;
}

bool OAIBelegdaten::is_unternehmen_id_typ_Valid() const{
    return m_unternehmen_id_typ_isValid;
}

QString OAIBelegdaten::getUnternehmenKopfzeile() const {
    return m_unternehmen_kopfzeile;
}
void OAIBelegdaten::setUnternehmenKopfzeile(const QString &unternehmen_kopfzeile) {
    m_unternehmen_kopfzeile = unternehmen_kopfzeile;
    m_unternehmen_kopfzeile_isSet = true;
}

bool OAIBelegdaten::is_unternehmen_kopfzeile_Set() const{
    return m_unternehmen_kopfzeile_isSet;
}

bool OAIBelegdaten::is_unternehmen_kopfzeile_Valid() const{
    return m_unternehmen_kopfzeile_isValid;
}

QString OAIBelegdaten::getUnternehmenName() const {
    return m_unternehmen_name;
}
void OAIBelegdaten::setUnternehmenName(const QString &unternehmen_name) {
    m_unternehmen_name = unternehmen_name;
    m_unternehmen_name_isSet = true;
}

bool OAIBelegdaten::is_unternehmen_name_Set() const{
    return m_unternehmen_name_isSet;
}

bool OAIBelegdaten::is_unternehmen_name_Valid() const{
    return m_unternehmen_name_isValid;
}

QString OAIBelegdaten::getUnternehmenOrt() const {
    return m_unternehmen_ort;
}
void OAIBelegdaten::setUnternehmenOrt(const QString &unternehmen_ort) {
    m_unternehmen_ort = unternehmen_ort;
    m_unternehmen_ort_isSet = true;
}

bool OAIBelegdaten::is_unternehmen_ort_Set() const{
    return m_unternehmen_ort_isSet;
}

bool OAIBelegdaten::is_unternehmen_ort_Valid() const{
    return m_unternehmen_ort_isValid;
}

QString OAIBelegdaten::getUnternehmenPlz() const {
    return m_unternehmen_plz;
}
void OAIBelegdaten::setUnternehmenPlz(const QString &unternehmen_plz) {
    m_unternehmen_plz = unternehmen_plz;
    m_unternehmen_plz_isSet = true;
}

bool OAIBelegdaten::is_unternehmen_plz_Set() const{
    return m_unternehmen_plz_isSet;
}

bool OAIBelegdaten::is_unternehmen_plz_Valid() const{
    return m_unternehmen_plz_isValid;
}

QList<OAIZahlung> OAIBelegdaten::getZahlungen() const {
    return m_zahlungen;
}
void OAIBelegdaten::setZahlungen(const QList<OAIZahlung> &zahlungen) {
    m_zahlungen = zahlungen;
    m_zahlungen_isSet = true;
}

bool OAIBelegdaten::is_zahlungen_Set() const{
    return m_zahlungen_isSet;
}

bool OAIBelegdaten::is_zahlungen_Valid() const{
    return m_zahlungen_isValid;
}

bool OAIBelegdaten::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_externer_beleg_belegkreis_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_externer_beleg_bezeichnung_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_externer_beleg_referenz_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_kunde_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_notizen.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_posten.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_rabatte.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_storno_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_storno_beleg_uuid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_storno_text_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_training_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unternehmen_adresse1_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unternehmen_adresse2_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unternehmen_fusszeile_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unternehmen_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unternehmen_id_typ_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unternehmen_kopfzeile_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unternehmen_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unternehmen_ort_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unternehmen_plz_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_zahlungen.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBelegdaten::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
