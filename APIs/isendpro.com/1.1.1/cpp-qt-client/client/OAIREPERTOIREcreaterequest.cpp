/**
 * API iSendPro
 * [1] Liste des fonctionnalités : - envoi de SMS à un ou plusieurs destinataires, - lookup HLR, - récupération des récapitulatifs de campagne, - gestion des répertoires, - ajout en liste noire. - comptage du nombre de caractères des SMS  [2] Pour utiliser cette API vous devez: - Créer un compte iSendPro sur https://isendpro.com/ - Créditer votre compte      - Remarque: obtention d'un crédit de test possible sous conditions - Noter votre clé de compte (keyid)   - Elle vous sera indispensable à l'utilisation de l'API   - Vous pouvez la trouver dans le rubrique mon \"compte\", sous-rubrique \"mon API\" - Configurer le contrôle IP   - Le contrôle IP est configurable dans le rubrique mon \"compte\", sous-rubrique \"mon API\"   - Il s'agit d'un système de liste blanche, vous devez entrer les IP utilisées pour appeler l'API   - Vous pouvez également désactiver totalement le contrôle IP 
 *
 * The version of the OpenAPI document: 1.1.1
 * Contact: support@isendpro.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIREPERTOIREcreaterequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIREPERTOIREcreaterequest::OAIREPERTOIREcreaterequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIREPERTOIREcreaterequest::OAIREPERTOIREcreaterequest() {
    this->initializeModel();
}

OAIREPERTOIREcreaterequest::~OAIREPERTOIREcreaterequest() {}

void OAIREPERTOIREcreaterequest::initializeModel() {

    m_keyid_isSet = false;
    m_keyid_isValid = false;

    m_repertoire_edit_isSet = false;
    m_repertoire_edit_isValid = false;

    m_repertoire_nom_isSet = false;
    m_repertoire_nom_isValid = false;
}

void OAIREPERTOIREcreaterequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIREPERTOIREcreaterequest::fromJsonObject(QJsonObject json) {

    m_keyid_isValid = ::OpenAPI::fromJsonValue(m_keyid, json[QString("keyid")]);
    m_keyid_isSet = !json[QString("keyid")].isNull() && m_keyid_isValid;

    m_repertoire_edit_isValid = ::OpenAPI::fromJsonValue(m_repertoire_edit, json[QString("repertoireEdit")]);
    m_repertoire_edit_isSet = !json[QString("repertoireEdit")].isNull() && m_repertoire_edit_isValid;

    m_repertoire_nom_isValid = ::OpenAPI::fromJsonValue(m_repertoire_nom, json[QString("repertoireNom")]);
    m_repertoire_nom_isSet = !json[QString("repertoireNom")].isNull() && m_repertoire_nom_isValid;
}

QString OAIREPERTOIREcreaterequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIREPERTOIREcreaterequest::asJsonObject() const {
    QJsonObject obj;
    if (m_keyid_isSet) {
        obj.insert(QString("keyid"), ::OpenAPI::toJsonValue(m_keyid));
    }
    if (m_repertoire_edit_isSet) {
        obj.insert(QString("repertoireEdit"), ::OpenAPI::toJsonValue(m_repertoire_edit));
    }
    if (m_repertoire_nom_isSet) {
        obj.insert(QString("repertoireNom"), ::OpenAPI::toJsonValue(m_repertoire_nom));
    }
    return obj;
}

QString OAIREPERTOIREcreaterequest::getKeyid() const {
    return m_keyid;
}
void OAIREPERTOIREcreaterequest::setKeyid(const QString &keyid) {
    m_keyid = keyid;
    m_keyid_isSet = true;
}

bool OAIREPERTOIREcreaterequest::is_keyid_Set() const{
    return m_keyid_isSet;
}

bool OAIREPERTOIREcreaterequest::is_keyid_Valid() const{
    return m_keyid_isValid;
}

QString OAIREPERTOIREcreaterequest::getRepertoireEdit() const {
    return m_repertoire_edit;
}
void OAIREPERTOIREcreaterequest::setRepertoireEdit(const QString &repertoire_edit) {
    m_repertoire_edit = repertoire_edit;
    m_repertoire_edit_isSet = true;
}

bool OAIREPERTOIREcreaterequest::is_repertoire_edit_Set() const{
    return m_repertoire_edit_isSet;
}

bool OAIREPERTOIREcreaterequest::is_repertoire_edit_Valid() const{
    return m_repertoire_edit_isValid;
}

QString OAIREPERTOIREcreaterequest::getRepertoireNom() const {
    return m_repertoire_nom;
}
void OAIREPERTOIREcreaterequest::setRepertoireNom(const QString &repertoire_nom) {
    m_repertoire_nom = repertoire_nom;
    m_repertoire_nom_isSet = true;
}

bool OAIREPERTOIREcreaterequest::is_repertoire_nom_Set() const{
    return m_repertoire_nom_isSet;
}

bool OAIREPERTOIREcreaterequest::is_repertoire_nom_Valid() const{
    return m_repertoire_nom_isValid;
}

bool OAIREPERTOIREcreaterequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_keyid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_repertoire_edit_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_repertoire_nom_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIREPERTOIREcreaterequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_keyid_isValid && m_repertoire_edit_isValid && m_repertoire_nom_isValid && true;
}

} // namespace OpenAPI
